## fy6-8-L1-01
**Annettu:** lähdejännite $E = 1{,}58\,\text{V}$, sisäinen resistanssi $R_\text{s} = 0{,}25\,\Omega$, virta $I = 0{,}80\,\text{A}$
**Kysytty:** napajännite $U$ voltteina
**Periaate:** Paristo on ideaalinen lähde, jonka kanssa on sarjassa sisäinen resistanssi. Kun paristosta otetaan virta, potentiaali laskee sisäisessä resistanssissa jännitteen $R_\text{s} I$ verran, joten napojen välille jää lähdejännitettä pienempi jännite.
**Kaava:** $U = E - R_\text{s} I$
**Muunnokset:** Ei tarvita: $1\,\Omega \cdot 1\,\text{A} = 1\,\text{V}$.
**Sijoitus:** $U = 1{,}58\,\text{V} - 0{,}25\,\Omega \cdot 0{,}80\,\text{A} = 1{,}58\,\text{V} - 0{,}20\,\text{V} = 1{,}38\,\text{V}$
**Vastaus:** $1{,}38\,\text{V}$, sadasosavoltin tarkkuudella kuten lähdejännite $1{,}58\,\text{V}$.
**Järkevyys:** Napajännite on lähdejännitettä pienempi, kuten virtaa antavalla paristolla kuuluu. Sisäisen resistanssin jännite $0{,}20\,\text{V}$ on noin kahdeksasosa lähdejännitteestä, mikä sopii melko suureen virtaan $0{,}80\,\text{A}$.

## fy6-8-L1-02
**Annettu:** lähdejännite $E = 1{,}30\,\text{V}$, sisäinen resistanssi $R_\text{s} = 0{,}040\,\Omega$; oikosulkujohtimen resistanssi jätetään huomiotta
**Kysytty:** oikosulkuvirta $I_\text{k}$ ampeereina
**Periaate:** Oikosulussa ulkoisen piirin resistanssi on nolla, joten Kirchhoffin jännitelain mukaan koko lähdejännite jää kennon sisäiselle resistanssille. Virtaa rajoittaa vain sisäinen resistanssi.
**Kaava:** $E - R_\text{s} I_\text{k} = 0$, josta $I_\text{k} = \dfrac{E}{R_\text{s}}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Sijoitus:** $I_\text{k} = \dfrac{1{,}30\,\text{V}}{0{,}040\,\Omega} = 32{,}5\,\text{A}$
**Vastaus:** $33\,\text{A}$, kaksi merkitsevää numeroa kuten sisäisessä resistanssissa $0{,}040\,\Omega$.
**Järkevyys:** Arvio $1{,}3\,\text{V} : 0{,}04\,\Omega \approx 30\,\text{A}$. Ladattavan kennon sisäinen resistanssi on pieni, joten oikosulkuvirta on kymmeniä ampeereja: niin suuri virta kuumentaa johtimen ja kennon nopeasti, minkä vuoksi oikosulku on vaarallinen.

## fy6-8-L1-03
**Annettu:** neljä paristoa sarjassa, kunkin lähdejännite $E_1 = 1{,}55\,\text{V}$
**Kysytty:** paristoryhmän lähdejännite $E$ voltteina
**Periaate:** Sarjaankytkennässä varaus kulkee jokaisen pariston läpi peräkkäin, ja jokaisessa potentiaali nousee lähdejännitteen verran. Paristot ovat oikein päin, joten nousut summautuvat.
**Kaava:** $E = E_1 + E_2 + E_3 + E_4$, ja samanlaisille paristoille $E = 4E_1$
**Muunnokset:** Ei tarvita: jännitteet ovat voltteina.
**Sijoitus:** $E = 4 \cdot 1{,}55\,\text{V} = 6{,}20\,\text{V}$
**Vastaus:** $6{,}20\,\text{V}$, kolme merkitsevää numeroa kuten pariston lähdejännitteessä $1{,}55\,\text{V}$.
**Järkevyys:** Neljän $1{,}5\,\text{V}$:n pariston ryhmältä odottaa noin $6\,\text{V}$, ja tulos on sitä hieman suurempi, koska uuden pariston lähdejännite on vähän yli merkinnän $1{,}5\,\text{V}$.

## fy6-8-L1-04
**Annettu:** kolme samanlaista paristoa rinnan, kunkin sisäinen resistanssi $R_{\text{s}1} = 0{,}45\,\Omega$
**Kysytty:** paristoryhmän sisäinen resistanssi $R_\text{s}$ ohmeina
**Periaate:** Rinnan kytkettyjen paristojen sisäiset resistanssit ovat rinnakkaisia haaroja samojen kahden kohdan välissä. Paristot ovat samanlaisia, joten virta jakautuu niille tasan, ja ryhmän sisäinen resistanssi on yhden pariston sisäinen resistanssi jaettuna paristojen määrällä.
**Kaava:** $R_\text{s} = \dfrac{R_{\text{s}1}}{n}$
**Muunnokset:** Ei tarvita: resistanssi on ohmeina.
**Sijoitus:** $R_\text{s} = \dfrac{0{,}45\,\Omega}{3} = 0{,}15\,\Omega$
**Vastaus:** $0{,}15\,\Omega$, kaksi merkitsevää numeroa kuten sisäisessä resistanssissa $0{,}45\,\Omega$; paristojen määrä $3$ on tarkka luku.
**Järkevyys:** Rinnankytkennän resistanssi on pienempi kuin yhdenkään haaran resistanssi, ja $0{,}15\,\Omega < 0{,}45\,\Omega$. Tarkistus vastusten rinnankytkennän yhtälöllä: $\tfrac{1}{R_\text{s}} = \tfrac{3}{0{,}45\,\Omega}$, joten $R_\text{s} = 0{,}15\,\Omega$.

## fy6-8-L1-05
**Annettu:** kuvaajan pisteet ja niiden kautta piirretty suora, jota on jatkettu akseleille
**Kysytty:** oikosulkuvirta $I_\text{k}$ ampeereina
**Periaate:** Oikosulussa napajännite on nolla. Pariston $(I, U)$-kuvaaja on suora $U = E - R_\text{s} I$, joten oikosulkuvirta on se virta, jolla suora leikkaa vaaka-akselin. Oikosulkuvirtaa ei mitattu, vaan se saadaan jatkamalla pisteiden kautta piirrettyä suoraa.
**Kuvaajan lukeminen:** Katkoviivaksi jatkettu suora kohtaa vaaka-akselin $U = 0$ ruudukkoviivalla $3{,}0\,\text{A}$. Pystyakselin se kohtaa kohdassa $4{,}5\,\text{V}$, joka on lähdejännite.
**Kaava:** $U = E - R_\text{s} I_\text{k} = 0$, josta $I_\text{k} = \dfrac{E}{R_\text{s}}$; arvo luetaan suoran ja vaaka-akselin leikkauskohdasta.
**Muunnokset:** Ei tarvita: virta luetaan ampeereina.
**Sijoitus:** Kuvaajasta $I_\text{k} = 3{,}0\,\text{A}$.
**Vastaus:** $3{,}0\,\text{A}$, kahden merkitsevän numeron tarkkuudella, koska arvo luetaan $0{,}5\,\text{A}$:n ruudukolta.
**Järkevyys:** Suoran pisteistä $(0{,}40\,\text{A};\ 3{,}9\,\text{V})$ ja $(1{,}60\,\text{A};\ 2{,}1\,\text{V})$ saadaan $R_\text{s} = 1{,}8\,\text{V} : 1{,}20\,\text{A} = 1{,}5\,\Omega$, ja $I_\text{k} = E : R_\text{s} = 4{,}5\,\text{V} : 1{,}5\,\Omega = 3{,}0\,\text{A}$. Tulos riippuu siitä, että sisäinen resistanssi pysyy samana myös mittausalueen ulkopuolella.

## fy6-8-L2-01
**Annettu:** ensimmäinen kuorma: $I_1 = 0{,}20\,\text{A}$, $U_1 = 4{,}30\,\text{V}$; toinen kuorma: $I_2 = 0{,}80\,\text{A}$, $U_2 = 3{,}70\,\text{V}$
**Kysytty:** sisäinen resistanssi $R_\text{s}$ ohmeina
**Periaate:** Sama paristo on molemmissa mittauksissa, joten sen lähdejännite ja sisäinen resistanssi ovat samat. Napajännite $U = E - R_\text{s} I$ pienenee virran kasvaessa $R_\text{s}$:n verran ampeeria kohti, joten kahden mittauksen erotuksesta lähdejännite häviää.
**Kaava:** $U_1 = E - R_\text{s} I_1$ ja $U_2 = E - R_\text{s} I_2$; vähentämällä $U_1 - U_2 = R_\text{s}(I_2 - I_1)$, josta $R_\text{s} = \dfrac{U_1 - U_2}{I_2 - I_1}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Sijoitus:** $R_\text{s} = \dfrac{4{,}30\,\text{V} - 3{,}70\,\text{V}}{0{,}80\,\text{A} - 0{,}20\,\text{A}} = \dfrac{0{,}60\,\text{V}}{0{,}60\,\text{A}} = 1{,}0\,\Omega$
**Vastaus:** $1{,}0\,\Omega$, kaksi merkitsevää numeroa kuten erotuksissa $0{,}60\,\text{V}$ ja $0{,}60\,\text{A}$.
**Järkevyys:** Lähdejännite on $E = 4{,}30\,\text{V} + 1{,}0\,\Omega \cdot 0{,}20\,\text{A} = 4{,}50\,\text{V}$, ja toinen mittaus antaa saman: $3{,}70\,\text{V} + 1{,}0\,\Omega \cdot 0{,}80\,\text{A} = 4{,}50\,\text{V}$. Kyseessä voi olla litteä $4{,}5\,\text{V}$:n paristo, jonka sisäinen resistanssi on ohmin luokkaa.

## fy6-8-L2-02
**Annettu:** lähdejännite $E = 6{,}0\,\text{V}$, sisäinen resistanssi $R_\text{s} = 0{,}50\,\Omega$, kuormitusvastus $R = 5{,}5\,\Omega$
**Kysytty:** napajännite $U$ voltteina
**Periaate:** Sisäinen resistanssi ja kuormitusvastus ovat samassa silmukassa sarjassa, joten Kirchhoffin jännitelaki $E - R_\text{s} I - RI = 0$ antaa virran. Napajännite on kuormitusvastuksen jännite, koska vastus on kytketty suoraan lähteen napoihin.
**Kaava:** $I = \dfrac{E}{R + R_\text{s}}$ ja $U = RI$, joten $U = \dfrac{R E}{R + R_\text{s}}$
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä.
**Sijoitus:** $I = \dfrac{6{,}0\,\text{V}}{5{,}5\,\Omega + 0{,}50\,\Omega} = 1{,}0\,\text{A}$ ja $U = 5{,}5\,\Omega \cdot 1{,}0\,\text{A} = 5{,}5\,\text{V}$
**Vastaus:** $5{,}5\,\text{V}$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Napajännitteen yhtälö antaa saman: $U = 6{,}0\,\text{V} - 0{,}50\,\Omega \cdot 1{,}0\,\text{A} = 5{,}5\,\text{V}$. Sisäinen resistanssi on vain noin kymmenesosa kuormasta, joten napajännite jää vain vähän lähdejännitettä pienemmäksi.

## fy6-8-L2-03
**Annettu:** lampun resistanssi $R = 3{,}0\,\Omega$, lähdejännite $E = 4{,}5\,\text{V}$, sisäinen resistanssi $R_\text{s} = 1{,}5\,\Omega$
**Kysytty:** lampun teho $P$ watteina
**Periaate:** Lamppu ja pariston sisäinen resistanssi ovat samassa silmukassa sarjassa, joten jännitelaki antaa virran. Lampun jännite on pariston napajännite, ja sähköteho on jännitteen ja virran tulo (luku *Sähköteho ja vastuksen lämpeneminen*).
**Kaava:** $I = \dfrac{E}{R + R_\text{s}}$, $U = E - R_\text{s} I$ ja $P = UI$
**Muunnokset:** Ei tarvita: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Sijoitus:** $I = \dfrac{4{,}5\,\text{V}}{3{,}0\,\Omega + 1{,}5\,\Omega} = 1{,}0\,\text{A}$, $U = 4{,}5\,\text{V} - 1{,}5\,\Omega \cdot 1{,}0\,\text{A} = 3{,}0\,\text{V}$ ja $P = 3{,}0\,\text{V} \cdot 1{,}0\,\text{A} = 3{,}0\,\text{W}$
**Vastaus:** $3{,}0\,\text{W}$, kaksi merkitsevää numeroa kuten resistansseissa.
**Järkevyys:** Lähde antaa tehon $4{,}5\,\text{V} \cdot 1{,}0\,\text{A} = 4{,}5\,\text{W}$, josta $1{,}5\,\Omega \cdot (1{,}0\,\text{A})^2 = 1{,}5\,\text{W}$ muuttuu pariston sisäenergiaksi ja $3{,}0\,\text{W}$ siirtyy lamppuun: $1{,}5\,\text{W} + 3{,}0\,\text{W} = 4{,}5\,\text{W}$. Ilman sisäistä resistanssia lampun teho olisi suurempi.

## fy6-8-L2-04
**Annettu:** kaksi paristoa sarjassa, kummankin $E_1 = 1{,}5\,\text{V}$ ja $R_{\text{s}1} = 0{,}30\,\Omega$; kuormitusvastus $R = 2{,}4\,\Omega$
**Kysytty:** virta $I$ ampeereina
**Periaate:** Sarjaan kytkettyjen paristojen lähdejännitteet summautuvat, ja niiden sisäiset resistanssit ovat kuorman kanssa samassa silmukassa peräkkäin. Kirchhoffin jännitelaki antaa silmukan virran.
**Kaava:** $E = 2E_1$ ja $R_\text{s} = 2R_{\text{s}1}$, joten $I = \dfrac{E}{R + R_\text{s}} = \dfrac{2E_1}{R + 2R_{\text{s}1}}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Sijoitus:** $I = \dfrac{2 \cdot 1{,}5\,\text{V}}{2{,}4\,\Omega + 2 \cdot 0{,}30\,\Omega} = \dfrac{3{,}0\,\text{V}}{3{,}0\,\Omega} = 1{,}0\,\text{A}$
**Vastaus:** $1{,}0\,\text{A}$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Ilman sisäisiä resistansseja virta olisi $3{,}0\,\text{V} : 2{,}4\,\Omega = 1{,}25\,\text{A}$, joten sisäiset resistanssit pienentävät sitä, kuten pitääkin. Napajännite on $2{,}4\,\Omega \cdot 1{,}0\,\text{A} = 2{,}4\,\text{V}$, mikä on vähemmän kuin lähdejännite $3{,}0\,\text{V}$.

## fy6-8-L3-01
**Annettu:** kaksi samanlaista paristoa rinnan, kummankin $E_1 = 1{,}5\,\text{V}$ ja $R_{\text{s}1} = 0{,}40\,\Omega$; lampun resistanssi $R = 0{,}80\,\Omega$
**Kysytty:** kunkin pariston läpi kulkeva virta $I_1$ ampeereina
**Periaate:** Rinnan kytkettyjen samanlaisten paristojen lähdejännite on sama kuin yhden, ja sisäiset resistanssit ovat rinnakkaisia haaroja, joten ryhmän sisäinen resistanssi on puolet yhden pariston sisäisestä resistanssista. Ryhmä ja lamppu muodostavat silmukan, jonka virta saadaan jännitelaista. Paristot ovat samanlaisia, joten virtalain mukaan kokonaisvirta jakautuu niille tasan.
**Kaava:** $R_\text{s} = \dfrac{R_{\text{s}1}}{2}$, $I = \dfrac{E_1}{R + R_\text{s}}$ ja $I_1 = \dfrac{I}{2}$
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä.
**Sijoitus:** $R_\text{s} = \dfrac{0{,}40\,\Omega}{2} = 0{,}20\,\Omega$, $I = \dfrac{1{,}5\,\text{V}}{0{,}80\,\Omega + 0{,}20\,\Omega} = 1{,}5\,\text{A}$ ja $I_1 = \dfrac{1{,}5\,\text{A}}{2} = 0{,}75\,\text{A}$
**Vastaus:** $0{,}75\,\text{A}$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Napajännite on $0{,}80\,\Omega \cdot 1{,}5\,\text{A} = 1{,}2\,\text{V}$. Kunkin pariston yli tämä on $1{,}5\,\text{V} - 0{,}40\,\Omega \cdot 0{,}75\,\text{A} = 1{,}2\,\text{V}$, joten molemmat haarat antavat saman jännitteen. Yksi paristo yksinään antaisi vain $1{,}5\,\text{V} : 1{,}20\,\Omega = 1{,}25\,\text{A}$ ja joutuisi antamaan sen kokonaan itse.

## fy6-8-L3-02
**Annettu:** kolme paristoa sarjassa, yksi väärin päin; kunkin $E_1 = 1{,}5\,\text{V}$ ja $R_{\text{s}1} = 0{,}25\,\Omega$; lampun resistanssi $R = 4{,}0\,\Omega$
**Kysytty:** lampun läpi kulkeva virta $I$ ampeereina
**Periaate:** Sarjaankytkennässä potentiaalin muutokset summautuvat. Oikein päin olevissa paristoissa potentiaali nousee $E_1$:n verran, mutta väärin päin olevassa se laskee saman verran, joten ryhmän lähdejännite on $E_1 + E_1 - E_1$. Kaikkien kolmen sisäinen resistanssi on silti samassa silmukassa peräkkäin.
**Kaava:** $E = E_1 + E_1 - E_1 = E_1$, $R_\text{s} = 3R_{\text{s}1}$ ja $I = \dfrac{E}{R + R_\text{s}} = \dfrac{E_1}{R + 3R_{\text{s}1}}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Sijoitus:** $I = \dfrac{1{,}5\,\text{V}}{4{,}0\,\Omega + 3 \cdot 0{,}25\,\Omega} = \dfrac{1{,}5\,\text{V}}{4{,}75\,\Omega} = 0{,}3158\,\text{A}$
**Vastaus:** $0{,}32\,\text{A}$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Oikein asetettuna ryhmän lähdejännite olisi $4{,}5\,\text{V}$ ja virta $4{,}5\,\text{V} : 4{,}75\,\Omega = 0{,}95\,\text{A}$, kolminkertainen. Lamppu hehkuu siis selvästi himmeämmin, mikä on tavallinen merkki väärin päin asetetusta paristosta.

## fy6-8-L3-03
**Annettu:** kuorma $R_1 = 2{,}0\,\Omega$, napajännite $U_1 = 1{,}20\,\text{V}$; kuorma $R_2 = 6{,}0\,\Omega$, napajännite $U_2 = 1{,}44\,\text{V}$
**Kysytty:** lähdejännite $E$ voltteina
**Periaate:** Napajännite on kuormitusvastuksen jännite, joten Ohmin laki antaa kummankin mittauksen virran. Sama paristo on molemmissa mittauksissa, joten $U = E - R_\text{s} I$ pätee samoilla $E$:llä ja $R_\text{s}$:llä. Kahdesta yhtälöstä ratkaistaan ensin sisäinen resistanssi ja sitten lähdejännite.
**Kaava:** $I_1 = \dfrac{U_1}{R_1}$ ja $I_2 = \dfrac{U_2}{R_2}$; $U_1 = E - R_\text{s} I_1$ ja $U_2 = E - R_\text{s} I_2$, joten $R_\text{s} = \dfrac{U_2 - U_1}{I_1 - I_2}$ ja $E = U_1 + R_\text{s} I_1$
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä.
**Sijoitus:** $I_1 = \dfrac{1{,}20\,\text{V}}{2{,}0\,\Omega} = 0{,}60\,\text{A}$, $I_2 = \dfrac{1{,}44\,\text{V}}{6{,}0\,\Omega} = 0{,}24\,\text{A}$, $R_\text{s} = \dfrac{1{,}44\,\text{V} - 1{,}20\,\text{V}}{0{,}60\,\text{A} - 0{,}24\,\text{A}} = 0{,}667\,\Omega$ ja $E = 1{,}20\,\text{V} + 0{,}667\,\Omega \cdot 0{,}60\,\text{A} = 1{,}60\,\text{V}$
**Vastaus:** $1{,}60\,\text{V}$, sadasosavoltin tarkkuudella kuten mitatut napajännitteet.
**Järkevyys:** Toinen mittaus antaa saman: $1{,}44\,\text{V} + 0{,}667\,\Omega \cdot 0{,}24\,\text{A} = 1{,}60\,\text{V}$. Lähdejännite on suurempi kuin kumpikin napajännite, kuten pitääkin, ja $1{,}60\,\text{V}$ on tyypillinen uuden AA-pariston lähdejännite.

## fy6-8-L1-06
**Kysytty:** milloin pariston napajännite on yhtä suuri kuin sen lähdejännite.
**Periaate:** Napajännite on $U = E - R_\text{s} I$, missä $R_\text{s} I$ on jännitehäviö pariston sisäisessä resistanssissa. Napajännite on lähdejännite vain, kun tämä jännitehäviö on nolla, eli kun paristosta ei oteta virtaa.
**Mallivastaus:** Napajännite on yhtä suuri kuin lähdejännite, kun paristosta ei oteta virtaa, koska silloin sisäisessä resistanssissa ei synny jännitehäviötä. Jos virta on suuri, jännitehäviö on suuri ja navoille jää lähdejännitettä pienempi jännite; suurimmillaan virta on oikosulussa, jolloin napajännite on nolla. Kun kuormitusvastus on yhtä suuri kuin sisäinen resistanssi, napajännite on vain puolet lähdejännitteestä. Väite, jonka mukaan jännitteet ovat aina yhtä suuret, ei pidä: lähdejännite on pariston ominaisuus, mutta napajännite riippuu otettavasta virrasta.

## fy6-8-L1-07
**Kysytty:** mitä pariston oikosulussa tapahtuu.
**Periaate:** Virta on $I = E : (R + R_\text{s})$. Oikosulussa ulkoisen piirin resistanssi on $R \approx 0$, joten virtaa rajoittaa vain pariston sisäinen resistanssi, ja virta on oikosulkuvirta $I_\text{k} = E : R_\text{s}$. Paristoissa $R_\text{s}$ on pieni, joten oikosulkuvirta on suuri.
**Mallivastaus:** Oikosulussa virta kasvaa suureksi, koska sitä rajoittaa vain pariston sisäinen resistanssi. Koko lähdejännite jää sisäisen resistanssin yli, joten napajännite on lähes nolla ja pariston sisällä kehittyy paljon lämpöä. Siksi oikosulku on vaarallinen ja voi vahingoittaa paristoa. Virta ei pienene nollaan eikä pysy ennallaan, koska virta määräytyy koko piirin resistanssista, ja napajännite ei voi ylittää lähdejännitettä.

## fy6-8-L1-08
**Annettu:** lähdejännite $E = 1{,}50\,\text{V}$, napajännite $U = 1{,}31\,\text{V}$, virta $I = 0{,}50\,\text{A}$
**Kysytty:** sisäinen resistanssi $R_\text{s}$ ohmeina
**Periaate:** Napajännite on lähdejännitettä pienempi sisäisen resistanssin jännitehäviön $R_\text{s} I$ verran. Kun lähdejännite, napajännite ja virta tunnetaan, yhtälöstä voidaan ratkaista $R_\text{s}$.
**Kaava:** $U = E - R_\text{s} I$, josta $R_\text{s} = \dfrac{E - U}{I}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Sijoitus:** $R_\text{s} = \dfrac{1{,}50\,\text{V} - 1{,}31\,\text{V}}{0{,}50\,\text{A}} = \dfrac{0{,}19\,\text{V}}{0{,}50\,\text{A}} = 0{,}38\,\Omega$
**Vastaus:** $0{,}38\,\Omega$, kaksi merkitsevää numeroa kuten virrassa $0{,}50\,\text{A}$.
**Järkevyys:** Jännitehäviö on $0{,}38\,\Omega \cdot 0{,}50\,\text{A} = 0{,}19\,\text{V}$, ja $1{,}50\,\text{V} - 0{,}19\,\text{V} = 1{,}31\,\text{V}$ on annettu napajännite. Oikosulkuvirta olisi $1{,}50\,\text{V} : 0{,}38\,\Omega \approx 3{,}9\,\text{A}$, mikä on tavallinen suuruus uudelle pariston kennolle.

## fy6-8-L2-05
**Annettu:** taulukon mittauspisteet $(I;\ U)$: $(0{,}20\,\text{A};\ 1{,}43\,\text{V})$, $(0{,}40\,\text{A};\ 1{,}31\,\text{V})$, $(0{,}60\,\text{A};\ 1{,}20\,\text{V})$, $(0{,}80\,\text{A};\ 1{,}10\,\text{V})$, $(1{,}00\,\text{A};\ 0{,}99\,\text{V})$ ja $(1{,}20\,\text{A};\ 0{,}86\,\text{V})$ (esimerkkiaineisto)
**Kysytty:** a) lähdejännite $E$ suoralta luettuna, b) sisäinen resistanssi $R_\text{s}$ ohmeina
**Periaate:** Pariston napajännite on $U = E - R_\text{s} I$, joten $(I, U)$-pisteet asettuvat laskevalle suoralle. Suora leikkaa pystyakselin kohdassa $U = E$, ja sen kulmakerroin on $-R_\text{s}$. Mittauspisteissä on pientä hajontaa, joten suora piirretään pisteiden joukon keskeltä eikä sitä sidota yksittäisiin pisteisiin.
**Kuvaajan lukeminen:** Sovitettu suora leikkaa pystyakselin kohdassa $1{,}54\,\text{V}$ ja kulkee likimain pisteen $(1{,}20\,\text{A};\ 0{,}87\,\text{V})$ kautta. Pisteet jäävät suoran molemmille puolille. Kaksi suoralta luettua pistettä ovat kaukana toisistaan: $(0\,\text{A};\ 1{,}54\,\text{V})$ ja $(1{,}20\,\text{A};\ 0{,}87\,\text{V})$.
**Kaava:** $R_\text{s} = -\dfrac{\Delta U}{\Delta I} = \dfrac{U_1 - U_2}{I_2 - I_1}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Sijoitus:** $R_\text{s} = \dfrac{1{,}54\,\text{V} - 0{,}87\,\text{V}}{1{,}20\,\text{A} - 0\,\text{A}} = \dfrac{0{,}67\,\text{V}}{1{,}20\,\text{A}} = 0{,}558\,\Omega$
**Vastaus:** a) $E \approx 1{,}54\,\text{V}$; b) $R_\text{s} \approx 0{,}56\,\Omega$, kaksi merkitsevää numeroa, koska suora sovitetaan silmämääräisesti. Silmämääräinen sovitus vaihtelee, joten arvo väliltä $0{,}53\text{–}0{,}59\,\Omega$ on hyvä vastaus.
**Järkevyys:** Mallin mukaan virralla $0{,}60\,\text{A}$ napajännite on $1{,}54\,\text{V} - 0{,}56\,\Omega \cdot 0{,}60\,\text{A} = 1{,}20\,\text{V}$, ja se on taulukon kolmas arvo. Lähdejännite on suurempi kuin yksikään mitattu napajännite, kuten pitää. Oikosulkuvirta olisi $1{,}54\,\text{V} : 0{,}56\,\Omega \approx 2{,}8\,\text{A}$, mutta se on suoran jatke mittausalueen ulkopuolelle eikä sitä mitata.

## fy6-8-L2-06
**Annettu:** taulukon mittauspisteet $(I;\ U_\text{A};\ U_\text{B})$ virroilla $0{,}10\,\text{A}$ … $1{,}00\,\text{A}$: A-pariston napajännite pienenee arvosta $1{,}55\,\text{V}$ arvoon $1{,}10\,\text{V}$ ja B-pariston arvosta $1{,}47\,\text{V}$ arvoon $1{,}27\,\text{V}$ (esimerkkiaineisto)
**Kysytty:** a) virta $I$, jolla napajännitteet ovat yhtä suuret; b) kumpi paristo on parempi suurella virralla ja miksi
**Periaate:** Kumpikin paristo noudattaa mallia $U = E - R_\text{s} I$, joten kummankin pisteet sopivat omalle laskevalle suoralle. Suorien leikkauskohdassa napajännitteet ovat yhtä suuret. Suoran kulmakerroin on $-R_\text{s}$, joten loivempi suora tarkoittaa pienempää sisäistä resistanssia.
**Kuvaajan lukeminen:** A-pariston suora kulkee pisteiden $(0\,\text{A};\ 1{,}60\,\text{V})$ ja $(1{,}00\,\text{A};\ 1{,}10\,\text{V})$ kautta, joten $E_\text{A} = 1{,}60\,\text{V}$ ja $R_\text{A} = 0{,}50\,\Omega$. B-pariston suora kulkee pisteiden $(0\,\text{A};\ 1{,}49\,\text{V})$ ja $(1{,}00\,\text{A};\ 1{,}27\,\text{V})$ kautta, joten $E_\text{B} = 1{,}49\,\text{V}$ ja $R_\text{B} = 0{,}22\,\Omega$. Suorat leikkaavat kuvaajassa noin virralla $0{,}4\,\text{A}$.
**Kaava:** $E_\text{A} - R_\text{A} I = E_\text{B} - R_\text{B} I$, josta $I = \dfrac{E_\text{A} - E_\text{B}}{R_\text{A} - R_\text{B}}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Sijoitus:** $I = \dfrac{1{,}60\,\text{V} - 1{,}49\,\text{V}}{0{,}50\,\Omega - 0{,}22\,\Omega} = \dfrac{0{,}11\,\text{V}}{0{,}28\,\Omega} = 0{,}39\,\text{A}$
**Vastaus:** a) noin $0{,}40\,\text{A}$; graafinen lukema ja laskenta antavat arvon väliltä $0{,}35\text{–}0{,}45\,\text{A}$. b) Suurella virralla parempi on B, koska sen sisäinen resistanssi $0{,}22\,\Omega$ on pienempi kuin A:n $0{,}50\,\Omega$, joten sen napajännite pienenee virran kasvaessa loivemmin. A:n lähdejännite on suurempi, joten pienellä virralla alle $0{,}4\,\text{A}$ A antaa korkeamman napajännitteen. Virralla $1{,}00\,\text{A}$ napajännite on A:lla $1{,}10\,\text{V}$ ja B:llä $1{,}27\,\text{V}$.
**Järkevyys:** Virralla $0{,}40\,\text{A}$ A:n napajännite on $1{,}60\,\text{V} - 0{,}50\,\Omega \cdot 0{,}40\,\text{A} = 1{,}40\,\text{V}$ ja B:n $1{,}49\,\text{V} - 0{,}22\,\Omega \cdot 0{,}40\,\text{A} = 1{,}40\,\text{V}$, mikä vastaa taulukon riviä. Oikosulkuvirta on B:llä $1{,}49\,\text{V} : 0{,}22\,\Omega \approx 6{,}8\,\text{A}$ ja A:lla $1{,}60\,\text{V} : 0{,}50\,\Omega = 3{,}2\,\text{A}$, joten B kestää suuremman virran.

## fy6-8-L2-07
**Kysytty:** mikä väite oppilaan päätelmästä, että sisäinen resistanssi on nolla, on oikein.
**Periaate:** Napajännite on $U = E - R_\text{s} I$. Kun jännitemittari on kytketty ilman kuormaa, sen läpi kulkee häviävän pieni virta, joten $I \approx 0$ ja jännitehäviö sisäisessä resistanssissa on nolla. Silloin $U = E$ riippumatta siitä, kuinka suuri sisäinen resistanssi on.
**Mallivastaus:** Oppilaan päätelmä on virheellinen. Ilman kuormaa mitattu jännite $1{,}58\,\text{V}$ on pariston lähdejännite, koska virta on nolla eikä sisäisessä resistanssissa synny jännitehäviötä. Sama jännite näkyisi, vaikka sisäinen resistanssi olisi suuri, joten yksi virraton mittaus ei kerro siitä mitään. Jännitemittarin virta on hyvin pieni, joten mittari ei itse pienennä jännitettä. Sisäinen resistanssi ei myöskään ole ääretön, vaikka virta on nolla, koska se on pariston vakio-ominaisuus. Sisäinen resistanssi saadaan mittaamalla napajännite ja virta kuormitettuna, mieluiten usealla kuormalla, ja laskemalla $R_\text{s} = (E - U) : I$ tai kuvaajan kulmakertoimesta.

## fy6-8-L3-04
**Annettu:** taulukon mittauspisteet virroilla $0{,}10\,\text{A}$ … $0{,}50\,\text{A}$: uuden pariston napajännite pienenee arvosta $1{,}56\,\text{V}$ arvoon $1{,}46\,\text{V}$ ja ikääntyneen arvosta $1{,}41\,\text{V}$ arvoon $0{,}97\,\text{V}$ (esimerkkiaineisto); kuormitusvastus $R = 2{,}0\,\Omega$
**Kysytty:** a) kummankin pariston $E$ ja $R_\text{s}$; b) osuus ikääntyneen pariston kehittämästä sähkötehosta, joka muuttuu pariston sisäenergiaksi, prosentteina; c) vastukseen siirtyvä teho vastuksilla $0{,}55\,\Omega$, $1{,}1\,\Omega$, $2{,}2\,\Omega$ ja $4{,}4\,\Omega$ sekä suurimman tehon kuorma
**Periaate:** Kummankin pariston napajännite noudattaa mallia $U = E - R_\text{s} I$, joten sovitetun suoran leikkaus pystyakselilla on $E$ ja kulmakerroin on $-R_\text{s}$. Kuormitettuna virta on $I = E : (R + R_\text{s})$. Pariston kehittämä teho on $P = EI$, sisäiseen resistanssiin muuttuu teho $R_\text{s} I^2$ ja kuormaan teho $RI^2$. Tehon lauseke saadaan sähkötehon kaavasta (luku *Sähköteho ja vastuksen lämpeneminen*).
**Kuvaajan lukeminen:** Uuden pariston suora kulkee pisteiden $(0{,}10\,\text{A};\ 1{,}56\,\text{V})$ ja $(0{,}50\,\text{A};\ 1{,}46\,\text{V})$ kautta ja ikääntyneen pisteiden $(0{,}10\,\text{A};\ 1{,}41\,\text{V})$ ja $(0{,}50\,\text{A};\ 0{,}97\,\text{V})$ kautta. Kummankin pisteet jäävät suoran molemmille puolille.
**Kaava:** $R_\text{s} = \dfrac{U_1 - U_2}{I_2 - I_1}$ ja $E = U_1 + R_\text{s} I_1$; $I = \dfrac{E}{R + R_\text{s}}$; osuus $= \dfrac{R_\text{s} I^2}{EI} = \dfrac{R_\text{s}}{R + R_\text{s}}$; kuorman teho $P = RI^2 = \dfrac{E^2 R}{(R + R_\text{s})^2}$
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä.
**Sijoitus:** a) Uusi: $R_\text{s} = \dfrac{0{,}10\,\text{V}}{0{,}40\,\text{A}} = 0{,}25\,\Omega$ ja $E = 1{,}56\,\text{V} + 0{,}25\,\Omega \cdot 0{,}10\,\text{A} = 1{,}58\,\text{V}$. Ikääntynyt: $R_\text{s} = \dfrac{1{,}41\,\text{V} - 0{,}97\,\text{V}}{0{,}40\,\text{A}} = 1{,}10\,\Omega$ ja $E = 1{,}41\,\text{V} + 1{,}10\,\Omega \cdot 0{,}10\,\text{A} = 1{,}52\,\text{V}$.
b) Ikääntynyt: $I = \dfrac{1{,}52\,\text{V}}{2{,}0\,\Omega + 1{,}10\,\Omega} = 0{,}490\,\text{A}$, kehitetty teho $EI = 1{,}52\,\text{V} \cdot 0{,}490\,\text{A} = 0{,}745\,\text{W}$ ja paristoon jäävä teho $R_\text{s} I^2 = 1{,}10\,\Omega \cdot (0{,}490\,\text{A})^2 = 0{,}264\,\text{W}$. Osuus on $\dfrac{0{,}264\,\text{W}}{0{,}745\,\text{W}} = \dfrac{1{,}10\,\Omega}{3{,}10\,\Omega} = 0{,}355$. Uusi paristo: $\dfrac{0{,}25\,\Omega}{2{,}0\,\Omega + 0{,}25\,\Omega} = 0{,}11$.
c) Ikääntyneelle ($E = 1{,}52\,\text{V}$, $R_\text{s} = 1{,}10\,\Omega$): $R = 0{,}55\,\Omega$: $P = \dfrac{(1{,}52\,\text{V})^2 \cdot 0{,}55\,\Omega}{(1{,}65\,\Omega)^2} = 0{,}47\,\text{W}$; $R = 1{,}1\,\Omega$: $P = \dfrac{(1{,}52\,\text{V})^2 \cdot 1{,}1\,\Omega}{(2{,}2\,\Omega)^2} = 0{,}53\,\text{W}$; $R = 2{,}2\,\Omega$: $P = 0{,}47\,\text{W}$; $R = 4{,}4\,\Omega$: $P = 0{,}34\,\text{W}$. Osuus pariston lämmöksi: $R = 1{,}1\,\Omega$: $\dfrac{1{,}10\,\Omega}{2{,}2\,\Omega} = 0{,}50$.
**Vastaus:** b) noin $35\,\%$ ikääntyneen pariston kehittämästä tehosta muuttuu pariston sisäenergiaksi, kaksi merkitsevää numeroa kuten kuorman $2{,}0\,\Omega$ tarkkuus. Uudella paristolla osuus on vain noin $11\,\%$, koska sen sisäinen resistanssi $0{,}25\,\Omega$ on paljon pienempi. a) Uusi: $E = 1{,}58\,\text{V}$, $R_\text{s} = 0{,}25\,\Omega$; ikääntynyt: $E = 1{,}52\,\text{V}$, $R_\text{s} = 1{,}1\,\Omega$. c) Teho on suurin, noin $0{,}53\,\text{W}$, kuormalla $1{,}1\,\Omega$, joka on yhtä suuri kuin sisäinen resistanssi. Silloin puolet kehitetystä tehosta lämmittää paristoa.
**Järkevyys:** Tehot täsmäävät: $0{,}264\,\text{W} + 2{,}0\,\Omega \cdot (0{,}490\,\text{A})^2 = 0{,}264\,\text{W} + 0{,}481\,\text{W} = 0{,}745\,\text{W}$, kuten kehitetty teho. Ikääntyneen pariston lähdejännite on vain hieman pienempi kuin uuden, mutta sisäinen resistanssi on yli nelinkertainen, ja siksi se lämpenee paljon enemmän ja antaa kuormalle vähemmän tehoa. Tehon maksimi on loiva, kuten arvot $0{,}47\,\text{W}$, $0{,}53\,\text{W}$ ja $0{,}47\,\text{W}$ näyttävät, mutta suurimmallakin teholla puolet energiasta menee hukkaan, joten laitteissa kuorma valitaan yleensä suuremmaksi kuin $R_\text{s}$.

## fy6-8-L3-05
**Annettu:** taulukon mittauspisteet $(I;\ U)$ virroilla $0{,}50\,\text{A}$ … $3{,}00\,\text{A}$: jännite pienenee arvosta $5{,}56\,\text{V}$ arvoon $2{,}79\,\text{V}$ (esimerkkiaineisto); johtimien yhteenlaskettu resistanssi $R_\text{j} = 0{,}30\,\Omega$; oppilaan kulmakerroin $1{,}1\,\Omega$ ja oikosulkuvirta $5{,}6\,\text{A}$
**Kysytty:** a) lähdejännite $E$; b) oppilaan virhe ja akun oikea sisäinen resistanssi; c) akun oikea oikosulkuvirta $I_\text{k}$ ampeereina
**Periaate:** Jännitemittari on kuormitusvastuksen napoissa, joten se näyttää akun napajännitteestä vielä johtimien jännitehäviön $R_\text{j} I$ verran pienemmän jännitteen: $U = E - R_\text{s} I - R_\text{j} I = E - (R_\text{s} + R_\text{j}) I$. Kuvaajan kulmakerroin on siis $-(R_\text{s} + R_\text{j})$, ja oppilaan luku sisältää johtimien resistanssin. Akun oma sisäinen resistanssi saadaan vähentämällä $R_\text{j}$, ja oikosulkuvirta lasketaan siitä.
**Kuvaajan lukeminen:** Sovitettu suora kulkee pisteiden $(0{,}50\,\text{A};\ 5{,}56\,\text{V})$ ja $(3{,}00\,\text{A};\ 2{,}80\,\text{V})$ kautta. Pisteet jäävät suoran molemmille puolille. Suora leikkaa pystyakselin kohdassa $6{,}11\,\text{V}$, joka on lähdejännite, koska virran ollessa nolla johtimissa ei ole jännitehäviötä.
**Kaava:** $E = U_1 + (R_\text{s} + R_\text{j}) I_1$; $R_\text{s} + R_\text{j} = \dfrac{U_1 - U_2}{I_2 - I_1}$; $R_\text{s} = (R_\text{s} + R_\text{j}) - R_\text{j}$; $I_\text{k} = \dfrac{E}{R_\text{s}}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Sijoitus:** a) $R_\text{s} + R_\text{j} = \dfrac{5{,}56\,\text{V} - 2{,}80\,\text{V}}{3{,}00\,\text{A} - 0{,}50\,\text{A}} = \dfrac{2{,}76\,\text{V}}{2{,}50\,\text{A}} = 1{,}10\,\Omega$ ja $E = 5{,}56\,\text{V} + 1{,}10\,\Omega \cdot 0{,}50\,\text{A} = 6{,}11\,\text{V}$.
b) $R_\text{s} = 1{,}10\,\Omega - 0{,}30\,\Omega = 0{,}80\,\Omega$.
c) $I_\text{k} = \dfrac{6{,}11\,\text{V}}{0{,}80\,\Omega} = 7{,}64\,\text{A}$
**Vastaus:** c) $7{,}6\,\text{A}$, kaksi merkitsevää numeroa kuten johtimien resistanssissa $0{,}30\,\Omega$. a) $E \approx 6{,}11\,\text{V}$. b) Oppilaan sisäinen resistanssi on liian suuri, koska kulmakerroin sisältää johtimien resistanssin; akun oma sisäinen resistanssi on $0{,}80\,\Omega$. Oppilaan oikosulkuvirta $5{,}6\,\text{A}$ on liian pieni, koska hän jakoi lähdejännitteen liian suurella resistanssilla. Mittaus olisi pitänyt tehdä kytkemällä jännitemittari suoraan akun napoihin, jolloin johtimien jännitehäviö ei sisälly mitattuun jännitteeseen.
**Järkevyys:** Mallin mukaan virralla $2{,}00\,\text{A}$ akun napajännite on $6{,}11\,\text{V} - 0{,}80\,\Omega \cdot 2{,}00\,\text{A} = 4{,}51\,\text{V}$ ja johtimien jälkeen $4{,}51\,\text{V} - 0{,}30\,\Omega \cdot 2{,}00\,\text{A} = 3{,}91\,\text{V}$, mikä on taulukon neljäs arvo. Oikea oikosulkuvirta on suurempi kuin oppilaan, koska akun sisäinen resistanssi on pienempi kuin hänen saamansa $1{,}1\,\Omega$. Jos navat yhdistettäisiin johtimilla, virta olisi pienempi, $6{,}11\,\text{V} : 1{,}10\,\Omega \approx 5{,}6\,\text{A}$ eli oppilaan luku, mutta se on virta johtimien kanssa, ei akun oikosulkuvirta.
