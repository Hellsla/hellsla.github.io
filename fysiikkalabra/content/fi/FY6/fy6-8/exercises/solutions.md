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
**Annettu:** kuvaajan mittauspisteet ja niiden kautta piirretty suora, jota on jatkettu akseleille
**Kysytty:** oikosulkuvirta $I_\text{k}$ ampeereina
**Periaate:** Oikosulussa napajännite on nolla. Pariston $(I, U)$-kuvaaja on suora $U = E - R_\text{s} I$, joten oikosulkuvirta on se virta, jolla suora leikkaa vaaka-akselin. Oikosulkuvirtaa ei mitattu, vaan se saadaan jatkamalla mittauspisteiden suoraa.
**Kuvaajan lukeminen:** Katkoviivaksi jatkettu suora kohtaa vaaka-akselin $U = 0$ ruudukkoviivalla $3{,}0\,\text{A}$. Pystyakselin se kohtaa kohdassa $4{,}5\,\text{V}$, joka on lähdejännite.
**Kaava:** $U = E - R_\text{s} I_\text{k} = 0$, josta $I_\text{k} = \dfrac{E}{R_\text{s}}$; arvo luetaan suoran ja vaaka-akselin leikkauskohdasta.
**Muunnokset:** Ei tarvita: virta luetaan ampeereina.
**Sijoitus:** Kuvaajasta $I_\text{k} = 3{,}0\,\text{A}$.
**Vastaus:** $3{,}0\,\text{A}$, kahden merkitsevän numeron tarkkuudella, koska arvo luetaan $0{,}5\,\text{A}$:n ruudukolta.
**Järkevyys:** Mittauspisteistä $(0{,}40\,\text{A};\ 3{,}9\,\text{V})$ ja $(1{,}60\,\text{A};\ 2{,}1\,\text{V})$ saadaan $R_\text{s} = 1{,}8\,\text{V} : 1{,}20\,\text{A} = 1{,}5\,\Omega$, ja $I_\text{k} = E : R_\text{s} = 4{,}5\,\text{V} : 1{,}5\,\Omega = 3{,}0\,\text{A}$. Tulos riippuu siitä, että sisäinen resistanssi pysyy samana myös mittausalueen ulkopuolella.

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
