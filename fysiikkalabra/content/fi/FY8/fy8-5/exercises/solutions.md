## fy8-5-L1-01
**Annettu:** kuoren pääkvanttiluku $n = 5$
**Kysytty:** kuorelle mahtuvien elektronien enimmäismäärä $N_\text{max}$
**Periaate:** Kuorella $n$ on $n^2$ orbitaalia, koska sen alikuorilla s, p, d, … on $1$, $3$, $5$, … orbitaalia. Kullakin orbitaalilla voi olla enintään kaksi elektronia, joilla on vastakkainen spin (Paulin kieltosääntö), joten enimmäismäärä on kaksi kertaa orbitaalien määrä.
**Kaava:** $N_\text{max} = 2n^2$
**Muunnokset:** Ei tarvita, koska kysytään lukumäärää.
**Sijoitus:** $N_\text{max} = 2 \cdot 5^2 = 2 \cdot 25 = 50$
**Vastaus:** $50$ elektronia; tulos on tarkka kokonaisluku, koska se on laskettu lukumääristä.
**Järkevyys:** Tulos jatkaa taulukon sarjaa $2, 8, 18, 32$: peräkkäisten kuorten erotukset $6$, $10$ ja $14$ kasvavat neljällä, joten seuraava erotus on $18$ ja $32 + 18 = 50$. Kuorelle $n = 5$ mahtuu siis enemmän elektroneja kuin kuorelle $n = 4$, kuten pitääkin.

## fy8-5-L1-02
**Annettu:** mittauksia $N = 8000$, solmupallon sisäpuolelle osuneita $k = 421$
**Kysytty:** todennäköisyys $P$ havaita $2\text{s}$-elektroni solmupallon sisäpuolella, prosentteina
**Periaate:** Todennäköisyystulkinnan mukaan aallosta voidaan laskea vain todennäköisyyksiä, ja monessa samassa tilassa olevassa atomissa tehdyistä mittauksista todennäköisyys arvioidaan alueeseen osuneiden osuutena. Arvio on sitä tarkempi, mitä enemmän mittauksia on.
**Kaava:** todennäköisyyden arvio on $P = \dfrac{k}{N}$
**Muunnokset:** Osuus muunnetaan prosenteiksi kertomalla sadalla: $1 = 100\,\%$.
**Sijoitus:** $P = \dfrac{421}{8000} = 0{,}052\,625 = 5{,}2625\,\%$
**Vastaus:** $5{,}26\,\%$, kolme merkitsevää numeroa kuten osumien määrässä $421$.
**Järkevyys:** Noin joka kahdeskymmenes mittaus osuu solmupallon sisään, sillä $8000 : 20 = 400$, mikä on lähellä lukua $421$. Osuus on pieni, koska solmupallon säde on vain noin $0{,}11\,\text{nm}$ ja suurin osa $2\text{s}$-elektronin todennäköisyydestä on sen ulkopuolella.

## fy8-5-L1-03
**Annettu:** mittauksia $N = 3000$, orbitaalin raja $90\,\%$
**Kysytty:** rajan ulkopuolelle osuvien mittausten odotettu määrä $k_\text{ulko}$
**Periaate:** Raja on piirretty niin, että sen sisällä elektroni havaitaan todennäköisyydellä $0{,}90$, joten ulkopuolelle osumisen todennäköisyys on $1 - 0{,}90 = 0{,}10$. Monessa mittauksessa ulkopuolelle osuvien osuus on likimain tämä todennäköisyys, $P \approx \tfrac{k}{N}$.
**Kaava:** $k_\text{ulko} = (1 - p)\,N$
**Muunnokset:** $p = 90\,\% = 0{,}90$
**Sijoitus:** $k_\text{ulko} = (1 - 0{,}90) \cdot 3000 = 0{,}10 \cdot 3000 = 300$
**Vastaus:** noin $300$ mittausta; luku on odotusarvo, ja todellinen määrä vaihtelee sarjasta toiseen.
**Järkevyys:** Joka kymmenes mittaus osuu rajan ulkopuolelle, ja $3000$:n kymmenesosa on $300$. Jos raja olisi seinä, ulkopuolella ei olisi yhtään osumaa, mutta orbitaalin raja on vain sovittu todennäköisyysraja.

## fy8-5-L1-04
**Annettu:** elektroni $3\text{p}$-tilassa, joten $n = 3$; vetyatomin energiatasot $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$
**Kysytty:** irrottamiseen tarvittava pienin energia $E_\text{i}$ elektronivoltteina
**Periaate:** Elektroni on irti atomista, kun sen energia on vähintään $0$. Vetyatomissa tilan energia riippuu vain pääkvanttiluvusta, joten $3\text{p}$-tilan energia on kuoren $n = 3$ energia, ja tarvittava energia on erotus $0 - E_3$.
**Kaava:** $E_\text{i} = 0 - E_3 = \dfrac{13{,}6\,\text{eV}}{3^2}$
**Muunnokset:** Ei tarvita, koska energiatasot ja kysytty energia ovat elektronivoltteina.
**Sijoitus:** $E_\text{i} = \dfrac{13{,}6\,\text{eV}}{9} = 1{,}5111\,\text{eV}$
**Vastaus:** $1{,}51\,\text{eV}$, kolme merkitsevää numeroa kuten energiassa $13{,}6\,\text{eV}$.
**Järkevyys:** Kuorella $n = 3$ elektroni on kauempana ytimestä ja heikommin sidottu kuin perustilassa, joten irrottaminen vaatii vain yhdeksäsosan perustilan energiasta $13{,}6\,\text{eV}$. Energia on positiivinen, koska se tuodaan atomiin.

## fy8-5-L1-05
**Annettu:** kuori $n = 5$; vetyatomin energiatasot $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$
**Kysytty:** elektronin energia $E_5$ elektronivoltteina
**Periaate:** Vetyatomissa elektronin tilan energia riippuu vain pääkvanttiluvusta, ja energiatasot saadaan annetusta kaavasta. Energia on negatiivinen, koska sidottu elektroni tarvitsee energiaa irrotakseen.
**Kaava:** $E_5 = -\dfrac{13{,}6\,\text{eV}}{5^2}$
**Muunnokset:** Ei tarvita, koska energia kysytään elektronivoltteina.
**Sijoitus:** $E_5 = -\dfrac{13{,}6\,\text{eV}}{25} = -0{,}544\,\text{eV}$
**Vastaus:** $-0{,}544\,\text{eV}$, kolme merkitsevää numeroa kuten energiassa $13{,}6\,\text{eV}$.
**Järkevyys:** Energia on lähellä nollaa, koska kuoren $n = 5$ elektroni on heikosti sidottu. Se on suurempi kuin $E_4 = -0{,}85\,\text{eV}$, kuten pitääkin, koska energia kasvaa kuoren numeron kasvaessa.

## fy8-5-L2-01
**Annettu:** alkutila $3\text{p}$, joten $n = 3$; lopputila $1\text{s}$, joten $n = 1$; $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$
**Kysytty:** fotonin aallonpituus $\lambda$ nanometreinä
**Periaate:** Energia säilyy: atomin energia pienenee tilojen energioiden erotuksen verran, ja sama energia lähtee fotonina, jonka energia on $hf = \tfrac{hc}{\lambda}$. Vetyatomissa tilan energia riippuu vain pääkvanttiluvusta.
**Kaava:** $\dfrac{hc}{\lambda} = E_3 - E_1$, josta $\lambda = \dfrac{hc}{E_3 - E_1}$
**Muunnokset:** Energiaero elektronivoltteina on $E_3 - E_1 = -\tfrac{13{,}6\,\text{eV}}{9} + 13{,}6\,\text{eV} = 12{,}089\,\text{eV}$. Sijoitetaan $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$: $E_3 - E_1 = 12{,}089 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 1{,}9366 \cdot 10^{-18}\,\text{J}$. Lopuksi $1\,\text{nm} = 10^{-9}\,\text{m}$.
**Sijoitus:** Ensin $hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} = 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}$ ja sitten $\lambda = \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{1{,}9366 \cdot 10^{-18}\,\text{J}} = 1{,}0257 \cdot 10^{-7}\,\text{m} = 102{,}57\,\text{nm}$
**Vastaus:** $103\,\text{nm}$, kolme merkitsevää numeroa kuten energiassa $13{,}6\,\text{eV}$.
**Järkevyys:** Fotonin energia on noin $12\,\text{eV}$, enemmän kuin siirtymän $2\text{p} \to 1\text{s}$ energia $10{,}2\,\text{eV}$, joten aallonpituuden on oltava lyhyempi kuin tämän siirtymän $122\,\text{nm}$. Säteily on ultraviolettia, kuten vedyn kaikki perustilaan päättyvät viivat.

## fy8-5-L2-02
**Annettu:** argonissa $18$ elektronia; täyttöjärjestys $1\text{s}$, $2\text{s}$, $2\text{p}$, $3\text{s}$, $3\text{p}$; orbitaalille enintään kaksi elektronia
**Kysytty:** uloimman kuoren elektronien määrä $N_\text{ulko}$
**Periaate:** Perustilassa elektronit täyttävät orbitaalit alimmasta energiasta alkaen. Kuorelle $n$ mahtuu enintään $2n^2$ elektronia, joten ensin täyttyvät kuoret $n = 1$ ja $n = 2$, ja loput elektronit jäävät kuorelle $n = 3$, joka on argonin uloin kuori.
**Kaava:** $N_\text{ulko} = N - 2 \cdot 1^2 - 2 \cdot 2^2$
**Muunnokset:** Ei tarvita, koska kysytään lukumäärää.
**Sijoitus:** $N_\text{ulko} = 18 - 2 - 8 = 8$
**Vastaus:** $8$ elektronia; tulos on tarkka kokonaisluku.
**Järkevyys:** Kuorella $n = 3$ elektronit ovat $3\text{s}$- ja $3\text{p}$-alikuorilla: $2 + 6 = 8$, eli molemmat alikuoret ovat täynnä. Konfiguraatio $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^2\,3\text{p}^6$ sisältää $18$ elektronia. Täysi uloin s- ja p-alikuori sopii siihen, että argon on jalokaasu, joka ei juuri muodosta sidoksia.

## fy8-5-L2-03
**Annettu:** mittauksia $N = 2400$; $50\,\%$:n raja $0{,}071\,\text{nm}$ ja $90\,\%$:n raja $0{,}14\,\text{nm}$
**Kysytty:** rajojen väliin osuvien mittausten odotettu määrä $k$
**Periaate:** $90\,\%$:n rajan sisällä on $50\,\%$:n raja kokonaan, joten rajojen väliseen kuoreen jää todennäköisyys $0{,}90 - 0{,}50 = 0{,}40$. Monessa mittauksessa alueeseen osuvien osuus on likimain alueen todennäköisyys. Rajojen säteitä ei tarvita.
**Kaava:** $k = (p_{90} - p_{50})\,N$
**Muunnokset:** $p_{90} = 90\,\% = 0{,}90$ ja $p_{50} = 50\,\% = 0{,}50$
**Sijoitus:** $k = (0{,}90 - 0{,}50) \cdot 2400 = 0{,}40 \cdot 2400 = 960$
**Vastaus:** noin $960$ mittausta; luku on odotusarvo, ja todellinen määrä vaihtelee sarjasta toiseen.
**Järkevyys:** Puolet eli $1200$ mittausta osuu $50\,\%$:n rajan sisään ja $2160$ mittausta $90\,\%$:n rajan sisään; niiden erotus on $960$. Rajojen välissä on vähemmän osumia kuin sisemmän rajan sisällä, vaikka kuori on tilavuudeltaan suurempi, koska pilvi harvenee ulospäin.

## fy8-5-L2-04
**Annettu:** elektroni kuorella $n = 2$; $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$
**Kysytty:** suurin aallonpituus $\lambda_\text{max}$, jolla fotoni irrottaa elektronin, nanometreinä
**Periaate:** Fotonin energian on oltava vähintään irrottamiseen tarvittava energia $0 - E_2$. Fotonin energia $\tfrac{hc}{\lambda}$ pienenee aallonpituuden kasvaessa, joten suurin kelpaava aallonpituus vastaa juuri tätä energiaa.
**Kaava:** $\dfrac{hc}{\lambda_\text{max}} = 0 - E_2$, josta $\lambda_\text{max} = \dfrac{hc}{-E_2}$
**Muunnokset:** $-E_2 = \tfrac{13{,}6\,\text{eV}}{4} = 3{,}40\,\text{eV}$. Sijoitetaan $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$: $-E_2 = 3{,}40 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 5{,}4468 \cdot 10^{-19}\,\text{J}$. Lopuksi $1\,\text{nm} = 10^{-9}\,\text{m}$.
**Sijoitus:** Ensin $hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} = 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}$ ja sitten $\lambda_\text{max} = \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{5{,}4468 \cdot 10^{-19}\,\text{J}} = 3{,}6470 \cdot 10^{-7}\,\text{m} = 364{,}70\,\text{nm}$
**Vastaus:** $365\,\text{nm}$, kolme merkitsevää numeroa kuten energiassa $13{,}6\,\text{eV}$.
**Järkevyys:** Energia $3{,}4\,\text{eV}$ on hieman yli violetin valon fotonin energian, joten aallonpituus on juuri näkyvän alueen alapuolella, lähellä ultraviolettia. Tätä pidempiaaltoinen näkyvä valo ei irrota elektronia kuorelta $n = 2$.

## fy8-5-L3-01
**Annettu:** fotonin aallonpituus $\lambda = 97{,}3\,\text{nm}$; atomi perustilassa, $n = 1$; $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$
**Kysytty:** orbitaalien määrä sillä kuorella $n$, jolle elektroni siirtyy
**Periaate:** Atomi voi absorboida fotonin vain, jos fotonin energia on täsmälleen kahden tilan energioiden erotus. Fotonin energiasta saadaan ylemmän tilan energia $E_n = E_1 + \tfrac{hc}{\lambda}$, siitä kuoren numero $n$, ja kuorella $n$ on $n^2$ orbitaalia.
**Kaava:** $E_n = E_1 + \dfrac{hc}{\lambda}$, josta $n = \sqrt{\dfrac{13{,}6\,\text{eV}}{-E_n}}$ ja orbitaalien määrä on $n^2$
**Muunnokset:** $\lambda = 97{,}3\,\text{nm} = 97{,}3 \cdot 10^{-9}\,\text{m}$. Kun $hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} = 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}$, fotonin energia on $\tfrac{hc}{\lambda} = \tfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{97{,}3 \cdot 10^{-9}\,\text{m}} = 2{,}0416 \cdot 10^{-18}\,\text{J}$. Elektronivolteiksi se muunnetaan sijoittamalla $1\,\text{J} = \tfrac{1}{1{,}602 \cdot 10^{-19}}\,\text{eV}$: $\tfrac{2{,}0416 \cdot 10^{-18}}{1{,}602 \cdot 10^{-19}}\,\text{eV} = 12{,}744\,\text{eV}$.
**Sijoitus:** $E_n = -13{,}6\,\text{eV} + 12{,}744\,\text{eV} = -0{,}856\,\text{eV}$ ja $n = \sqrt{\dfrac{13{,}6\,\text{eV}}{0{,}856\,\text{eV}}} = \sqrt{15{,}9} = 3{,}99 \approx 4$, joten orbitaaleja on $4^2 = 16$
**Vastaus:** $16$ orbitaalia (kuori $n = 4$: $4\text{s}$, kolme $4\text{p}$, viisi $4\text{d}$ ja seitsemän $4\text{f}$); $n$ on kokonaisluku, joten pyöristys $3{,}99 \to 4$ on luotettava.
**Järkevyys:** Kuoren $n = 4$ energia $-\tfrac{13{,}6\,\text{eV}}{16} = -0{,}85\,\text{eV}$ on yhtä kuin laskettu $-0{,}856\,\text{eV}$ aallonpituuden kolmen numeron tarkkuudella. Kuorien $n = 3$ ($-1{,}51\,\text{eV}$) ja $n = 5$ ($-0{,}54\,\text{eV}$) energiat ovat selvästi kauempana, joten muu kuori ei sovi.

## fy8-5-L3-02
**Annettu:** täyttöjärjestys $1\text{s}$, $2\text{s}$, $2\text{p}$, $3\text{s}$, $3\text{p}$; orbitaalille enintään kaksi elektronia; $3\text{p}$-alikuori puoliksi täynnä
**Kysytty:** atomin elektronien määrä $N$
**Periaate:** Perustilassa elektronit täyttävät orbitaalit alimmasta energiasta alkaen, joten $3\text{p}$-alikuorelle tulee elektroneja vasta, kun $1\text{s}$, $2\text{s}$, $2\text{p}$ ja $3\text{s}$ ovat täynnä. s-alikuorella on yksi orbitaali ja p-alikuorella kolme, joten niille mahtuu $2$ ja $6$ elektronia. Puoliksi täyteen $3\text{p}$-alikuoreen kuuluu puolet sen enimmäismäärästä.
**Kaava:** $N = N_\text{1s} + N_\text{2s} + N_\text{2p} + N_\text{3s} + \dfrac{N_\text{3p,max}}{2}$
**Muunnokset:** Ei tarvita, koska kysytään lukumäärää.
**Sijoitus:** $N = 2 + 2 + 6 + 2 + \dfrac{6}{2} = 2 + 2 + 6 + 2 + 3 = 15$
**Vastaus:** $15$ elektronia (alkuaine on fosfori, konfiguraatio $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^2\,3\text{p}^3$); tulos on tarkka kokonaisluku.
**Järkevyys:** Täysiin kuoriin $n = 1$ ja $n = 2$ mahtuu $2 + 8 = 10$ elektronia, ja kuorella $n = 3$ on $2 + 3 = 5$ elektronia, yhteensä $15$. Jaksollisessa järjestelmässä järjestysluku $15$ on fosfori, joka on kolmannen jakson keskellä, kuten puolillaan oleva $3\text{p}$-alikuori antaa odottaa.

## fy8-5-L3-03
**Annettu:** mittauksia $N = 5000$; orbitaalin raja $90\,\%$; solmupallon sisäpuolelle osuu $5{,}3\,\%$ mittauksista, ja tämä sisäosa kuuluu käytännössä kokonaan orbitaalin alueeseen
**Kysytty:** orbitaalin alueeseen solmupallon ulkopuolelle osuvien mittausten odotettu määrä $k$
**Periaate:** Orbitaalin alueen todennäköisyys $0{,}90$ jakautuu kahteen osaan: solmupallon sisäosaan ja solmupallon ulkopuoliseen kuoreen. Koska sisäosa kuuluu alueeseen kokonaan, ulkoosan todennäköisyys on erotus $0{,}90 - 0{,}053$. Monessa mittauksessa alueeseen osuvien osuus on likimain alueen todennäköisyys.
**Kaava:** $k = (p - p_\text{sisä})\,N$
**Muunnokset:** $p = 90\,\% = 0{,}90$ ja $p_\text{sisä} = 5{,}3\,\% = 0{,}053$
**Sijoitus:** $k = (0{,}90 - 0{,}053) \cdot 5000 = 0{,}847 \cdot 5000 = 4235$
**Vastaus:** noin $4240$ mittausta; luku on odotusarvo, jonka todellinen sarja toteuttaa vain likimain, ja sisäosan osuus $5{,}3\,\%$ rajaa tarkkuuden noin kahteen tai kolmeen merkitsevään numeroon.
**Järkevyys:** Alueeseen osuu kaikkiaan noin $0{,}90 \cdot 5000 = 4500$ mittausta, ja solmupallon sisään niistä noin $0{,}053 \cdot 5000 = 265$; erotus $4235$ on selvästi suurin osa. Se sopii siihen, että $2\text{s}$-elektronin yleisin etäisyys on solmupallon ulkopuolella.

## fy8-5-L1-06
**Kysytty:** mikä on aaltomekaanisen atomimallin orbitaalin olennainen ero Bohrin malliin radan verrattuna.
**Periaate:** Aaltomallissa elektronin tilaa kuvaa ytimen ympärille levittäytyvä seisova aalto, ja aalto kertoo, kuinka todennäköisesti elektroni havaitaan kussakin kohdassa. Orbitaali piirretään alueena, jonka sisällä elektroni havaitaan valitulla todennäköisyydellä, tavallisesti $90\,\%$.
**Mallivastaus:** Orbitaali ei ole rata vaan alue, jonka sisällä elektroni havaitaan valitulla todennäköisyydellä, eikä elektronille voi piirtää reittiä. Bohrin mallissa elektronilla on tarkka rata, mutta aaltomallissa mittaus antaa aina yhden pisteen ja orbitaali kuvaa vasta monen mittauksen jakaumaa. Väite, että orbitaali olisi epätarkka rata, on väärä, koska rataa ei ole lainkaan. Pallopinta ei kelpaa, koska mittaustulokset hajaantuvat eri etäisyyksille. Pilvi ei myöskään tarkoita, että elektroni olisi levinnyt osiin: jokaisessa mittauksessa havaitaan kokonainen elektroni yhdessä kohdassa.

## fy8-5-L1-07
**Kysytty:** mitä $5000$ mittauksen pistepilvi kuvaa.
**Periaate:** Todennäköisyystulkinnan mukaan aalto ei kerro hiukkasen paikkaa vaan sen, kuinka todennäköisesti hiukkanen havaitaan kussakin kohdassa. Yksittäinen mittaus antaa yhden satunnaisen tuloksen, ja jakauma näkyy vasta monesta mittauksesta.
**Mallivastaus:** Pilvi kuvaa mittaustulosten jakaumaa: pisteitä on eniten siellä, missä elektroni havaitaan todennäköisimmin, joten pilvi on tiheimmillään ytimen lähellä. Jokainen piste on oma, toisista riippumaton mittaustulos, joten pisteet eivät ole elektronin reitti. Sumenemisselitys ei kelpaa, koska jokainen mittaus löytää elektronin tarkasti yhdestä kohdasta, ja pilvi syntyy vasta tulosten kertymisestä. Elektroni ei myöskään hajoa osiin, vaan jokaisessa mittauksessa havaitaan kokonainen elektroni.

## fy8-5-L1-08
**Annettu:** alikuori $4\text{f}$; f-alikuorella on seitsemän orbitaalia; orbitaalilla enintään kaksi elektronia
**Kysytty:** alikuoren $4\text{f}$ elektronien enimmäismäärä $N_\text{max}$
**Periaate:** Alikuoren orbitaalien määrä riippuu aallon muodosta, ja f-alikuorella niitä on seitsemän. Elektronilla on spin, jolla on vain kaksi arvoa, joten kullekin orbitaalille mahtuu enintään kaksi elektronia, joilla on vastakkainen spin (Paulin kieltosääntö). Enimmäismäärä on kaksi kertaa orbitaalien määrä.
**Kaava:** $N_\text{max} = 2 \cdot N_\text{orbitaalit}$
**Muunnokset:** Ei tarvita, koska kysytään lukumäärää.
**Sijoitus:** $N_\text{max} = 2 \cdot 7 = 14$
**Vastaus:** $14$ elektronia; tulos on tarkka kokonaisluku, koska se on laskettu lukumääristä.
**Järkevyys:** Samalla säännöllä s-alikuorelle mahtuu $2 \cdot 1 = 2$, p-alikuorelle $2 \cdot 3 = 6$ ja d-alikuorelle $2 \cdot 5 = 10$ elektronia. Kuoren $n = 4$ alikuorille s, p, d ja f mahtuu yhteensä $2 + 6 + 10 + 14 = 32$ elektronia, ja tämä on yhtä kuin $2n^2 = 2 \cdot 4^2 = 32$.

## fy8-5-L2-05
**Annettu:** mittauksia $N = 400$; luokan leveys $0{,}05\,\text{nm}$; luokkien lukumäärät $k$: $118$, $171$, $79$, $23$, $7$ ja $2$; $90\,\%$:n rajan säde $0{,}14\,\text{nm}$
**Kysytty:** a) yleisin luokka, b) alle $0{,}10\,\text{nm}$:n etäisyydelle osuvien mittausten osuus $P$ prosentteina, c) aineiston sopivuus $90\,\%$:n rajaan
**Periaate:** Todennäköisyys arvioidaan alueeseen osuneiden mittausten osuutena kaikista mittauksista, $P \approx \tfrac{k}{N}$. Alle $0{,}10\,\text{nm}$ kuuluvat kaksi ensimmäistä luokkaa. $90\,\%$:n raja on etäisyys, jonka sisään osuu $90\,\%$ mittauksista.
**Kuvaajan lukeminen:** Taulukosta luetaan lukumäärät luokittain: luokissa $0{,}00$–$0{,}05\,\text{nm}$ ja $0{,}05$–$0{,}10\,\text{nm}$ on $118$ ja $171$ mittausta. Luokka $0{,}05$–$0{,}10\,\text{nm}$ on yleisin, koska siinä on suurin lukumäärä $171$.
**Kaava:** $P = \dfrac{k}{N}$, missä $k$ on alueeseen osuneiden mittausten summa
**Muunnokset:** Osuus muunnetaan prosenteiksi kertomalla sadalla: $1 = 100\,\%$.
**Sijoitus:** Kahden ensimmäisen luokan mittausten summa on $k = 118 + 171 = 289$, joten $P = \dfrac{289}{400} = 0{,}7225 = 72{,}25\,\%$. Kohdassa c) lasketaan vastaavasti kolmen ensimmäisen luokan summa $289 + 79 = 368$ ja osuus $\dfrac{368}{400} = 0{,}920 = 92{,}0\,\%$.
**Vastaus:** Vastauslaatikkoon $72{,}3\,\%$.

a) Yleisin luokka on $0{,}05$–$0{,}10\,\text{nm}$.

b) $72{,}3\,\%$, kolme merkitsevää numeroa kuten lukumäärissä.

c) Alle $0{,}10\,\text{nm}$:n etäisyydelle osuu $72{,}3\,\%$ ja alle $0{,}15\,\text{nm}$:n etäisyydelle $92{,}0\,\%$ mittauksista, joten $90\,\%$ saavutetaan näiden välissä. Lineaarisesti interpoloiden raja on noin $0{,}10\,\text{nm} + \tfrac{90{,}0 - 72{,}3}{92{,}0 - 72{,}3} \cdot 0{,}05\,\text{nm} = 0{,}145\,\text{nm}$, mikä on lähellä arvoa $0{,}14\,\text{nm}$. Aineisto on siis sopusoinnussa rajan kanssa. Rajan ulkopuolellakin on osumia: etäisyydellä yli $0{,}15\,\text{nm}$ on $23 + 7 + 2 = 32$ mittausta, eli $8{,}0\,\%$.
**Järkevyys:** Yleisin luokka $0{,}05$–$0{,}10\,\text{nm}$ sisältää Bohrin säteen $0{,}053\,\text{nm}$, ja ydintä lähinnä oleva luokka on toiseksi yleisin. Lukumäärät pienenevät nopeasti ulospäin, ja yhteensä $118 + 171 + 79 + 23 + 7 + 2 = 400$, kuten pitää.

## fy8-5-L2-06
**Annettu:** kielen pituus $L = 0{,}80\,\text{m}$; aallon nopeus $v = 64\,\text{m/s}$; kielen päät kiinnitetty
**Kysytty:** a) aallonpituus $\lambda$ kussakin tilassa, b) taajuus $f$ kussakin tilassa, c) selitys solmujen ja taajuuden yhteydestä
**Periaate:** Kielen päät pysyvät paikallaan, joten päät ovat solmuja ja kieleen mahtuu kokonainen määrä kupuja. Kun kupuja on $m$, kunkin kuvun pituus on puoli aallonpituutta, joten $L = m \cdot \tfrac{\lambda}{2}$. Aallolle pätee $v = f\lambda$.
**Kuvaajan lukeminen:** Kuvassa ylimmässä tilassa on yksi kupu ja ei solmua päiden välissä, keskimmäisessä kaksi kupua ja yksi solmu ja alimmassa kolme kupua ja kaksi solmua. Kupuja on siis aina yksi enemmän kuin solmuja: $m = 1, 2, 3$. Kuvan aallonpituudet eivät ole luettavissa, joten ne lasketaan kielen pituudesta.
**Kaava:** $\lambda = \dfrac{2L}{m}$ ja $f = \dfrac{v}{\lambda}$
**Muunnokset:** Ei tarvita, koska pituus on metreinä ja nopeus yksikössä $\text{m/s}$.
**Sijoitus:** a) Tilassa $m = 1$ aallonpituus $\lambda = \dfrac{2 \cdot 0{,}80\,\text{m}}{1} = 1{,}60\,\text{m}$, tilassa $m = 2$ aallonpituus $\lambda = \dfrac{2 \cdot 0{,}80\,\text{m}}{2} = 0{,}80\,\text{m}$ ja tilassa $m = 3$ aallonpituus $\lambda = \dfrac{2 \cdot 0{,}80\,\text{m}}{3} = 0{,}533\,\text{m}$. b) Tilassa $m = 1$ taajuus $f_1 = \dfrac{64\,\text{m/s}}{1{,}60\,\text{m}} = 40\,\text{Hz}$, tilassa $m = 2$ taajuus $f_2 = \dfrac{64\,\text{m/s}}{0{,}80\,\text{m}} = 80\,\text{Hz}$ ja tilassa $m = 3$ (kaksi solmua) $f_3 = \dfrac{64\,\text{m/s}}{0{,}5333\,\text{m}} = 120\,\text{Hz}$.
**Vastaus:** kahden solmun tilan taajuus on $120\,\text{Hz}$, kaksi merkitsevää numeroa kuten nopeudessa $64\,\text{m/s}$.

a) Aallonpituudet ovat $1{,}60\,\text{m}$, $0{,}80\,\text{m}$ ja $0{,}533\,\text{m}$.

b) Taajuudet ovat $40\,\text{Hz}$, $80\,\text{Hz}$ ja $120\,\text{Hz}$.

c) Solmujen lisääntyessä kuvuja mahtuu kieleen enemmän, joten aallonpituus lyhenee ja taajuus kasvaa: aallonpituudet $1{,}60\,\text{m}$, $0{,}80\,\text{m}$ ja $0{,}533\,\text{m}$ antavat taajuudet $40\,\text{Hz}$, $80\,\text{Hz}$ ja $120\,\text{Hz}$. Atomin elektronin tilaa kuvaa myös seisova aalto, joten vain tietyt aallon muodot ovat mahdollisia ja energia on kvantittunut. Vetyatomissa mitä enemmän solmuja, sitä suurempi energia, aivan kuten kielellä mitä enemmän solmuja, sitä suurempi taajuus.
**Järkevyys:** Tilassa $m = 2$ aallonpituus $0{,}80\,\text{m}$ on yhtä kuin kielen pituus, ja sen taajuus $\dfrac{64\,\text{m/s}}{0{,}80\,\text{m}} = 80\,\text{Hz}$ on välissä $40\,\text{Hz}$ ja $120\,\text{Hz}$. Taajuudet $40\,\text{Hz}$, $80\,\text{Hz}$ ja $120\,\text{Hz}$ ovat peräkkäisiä perustaajuuden $40\,\text{Hz}$ monikertoja, kuten kuvun lukumäärän mukaan pitääkin.

## fy8-5-L2-07
**Kysytty:** mikä oppilaan päättelyssä on virheellistä.
**Periaate:** Orbitaalin raja on sovittu todennäköisyysraja eikä seinä. $90\,\%$:n rajan sisään osuu keskimäärin $90\,\%$ mittauksista, joten ulkopuolelle osuu $1 - 0{,}90 = 0{,}10$ eli joka kymmenes mittaus. Monessa mittauksessa osuus on likimain tämä todennäköisyys, $P \approx \tfrac{k}{N}$.
**Mallivastaus:** Raja on sovittu todennäköisyysraja: sen sisään osuu noin yhdeksän kymmenesosaa mittauksista, loput osuvat ulkopuolelle. Ulkopuolelle odotetaan $0{,}10 \cdot 2000 = 200$ osumaa, ja havaittu luku $205$ sopii tähän: $\tfrac{205}{2000} = 10{,}25\,\%$. Simulaatio toimii siis oikein, ja osumat rajan ulkopuolella kuuluvat aaltomallin todennäköisyysjakaumaan. Ne eivät johdu elektronin nopeasta kiitämisestä eivätkä mittausvirheestä, koska jokainen mittaus antaa yhden pisteen ja tarkempikin mittaus löytäisi elektronin joka kymmenennellä kerralla rajan ulkopuolelta.

## fy8-5-L3-04
**Annettu:** aallonpituudet $\lambda$: $657{,}1\,\text{nm}$, $485{,}4\,\text{nm}$, $433{,}5\,\text{nm}$ ja $410{,}6\,\text{nm}$; loppukuori $n = 2$; $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$; $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$, $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$
**Kysytty:** a) fotonien energiat $E_\text{f}$, b) alkukuorten numerot $n$, c) kuvaajan suoran kulmakerroin, d) kuoresta $n = 7$ lähtevän viivan aallonpituus
**Periaate:** Atomin energia pienenee tilojen energioiden erotuksen verran, ja sama energia lähtee fotonina: $E_\text{f} = \tfrac{hc}{\lambda} = E_n - E_2$. Sijoittamalla energiatasokaava saadaan $E_\text{f} = 13{,}6\,\text{eV} \cdot \left(\tfrac{1}{4} - \tfrac{1}{n^2}\right)$. Jos pisteet piirretään tämän yhtälön mukaisesti, ne asettuvat suoralle, jonka kulmakerroin on energiatasokaavan vakio.
**Kuvaajan lukeminen:** Vaaka-akselin arvot ovat $\tfrac{1}{4} - \tfrac{1}{n^2} = 0{,}139$, $0{,}188$, $0{,}210$ ja $0{,}222$ kuorille $n = 3, 4, 5, 6$ ja pystyakselin arvot kohdan a) energiat. Pisteet asettuvat likimain suoralle, joka kulkee origon kautta; mittauspisteet vaihtelevat hieman suoran ympärillä. Tarkistuksena ensimmäisen ja viimeisen mittauspisteen $(0{,}1389;\ 1{,}887\,\text{eV})$ ja $(0{,}2222;\ 3{,}020\,\text{eV})$ kautta laskettu kulmakerroin on $\dfrac{3{,}020\,\text{eV} - 1{,}887\,\text{eV}}{0{,}2222 - 0{,}1389} = 13{,}6\,\text{eV}$, ja kaikkiin pisteisiin sovitettu suora, jonka kulmakerrointa käytetään vastauksena, antaa $13{,}62\,\text{eV}$ ja vakiotermiksi $-0{,}003\,\text{eV}$.
**Kaava:** $E_\text{f} = \dfrac{hc}{\lambda}$, $\ \dfrac{1}{n^2} = \dfrac{1}{4} - \dfrac{E_\text{f}}{13{,}6\,\text{eV}}$ ja kulmakerroin $k = \dfrac{\Delta E_\text{f}}{\Delta\left(\tfrac{1}{4} - \tfrac{1}{n^2}\right)}$
**Muunnokset:** Aallonpituus $657{,}1\,\text{nm} = 657{,}1 \cdot 10^{-9}\,\text{m}$ ja samoin muut. Tulo $hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} = 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}$. Joulet muunnetaan elektronivolteiksi jakamalla luvulla $1{,}602 \cdot 10^{-19}$.
**Sijoitus:** a) Ensimmäiselle viivalle $E_\text{f} = \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{657{,}1 \cdot 10^{-9}\,\text{m}} = 3{,}0231 \cdot 10^{-19}\,\text{J} = 1{,}887\,\text{eV}$. Samoin muille viivoille: $2{,}555\,\text{eV}$, $2{,}860\,\text{eV}$ ja $3{,}020\,\text{eV}$. b) Ensimmäiselle viivalle $\dfrac{1}{n^2} = \dfrac{1}{4} - \dfrac{1{,}887\,\text{eV}}{13{,}6\,\text{eV}} = 0{,}2500 - 0{,}1388 = 0{,}1112$, joten $n = \sqrt{\dfrac{1}{0{,}1112}} = 3{,}00$. Samoin muille viivoille $n = 4{,}01$, $5{,}02$ ja $5{,}98$. d) Kuoresta $n = 7$ lähtevän fotonin energia on $13{,}6\,\text{eV} \cdot \left(\tfrac{1}{4} - \tfrac{1}{49}\right) = 3{,}122\,\text{eV} = 5{,}002 \cdot 10^{-19}\,\text{J}$ ja aallonpituus $\lambda = \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{5{,}002 \cdot 10^{-19}\,\text{J}} = 3{,}971 \cdot 10^{-7}\,\text{m} = 397{,}1\,\text{nm}$.
**Vastaus:** a) $1{,}887\,\text{eV}$, $2{,}555\,\text{eV}$, $2{,}860\,\text{eV}$ ja $3{,}020\,\text{eV}$; b) alkukuoret ovat $n = 3, 4, 5$ ja $6$, koska $n$ on kuoren numero ja siksi kokonaisluku, ja lasketut arvot $3{,}00$, $4{,}01$, $5{,}02$ ja $5{,}98$ poikkeavat kokonaisluvuista vain mittausepävarmuuden verran; c) kulmakerroin on $13{,}6\,\text{eV}$, ja se on energiatasokaavan vakio eli vetyatomin perustilan energian itseisarvo; d) noin $397\,\text{nm}$.
**Järkevyys:** Kulmakerroin $13{,}6\,\text{eV}$ on sama kuin energiatasokaavan vakio, ja suora kulkee origon kautta, kuten $E_\text{f} = 13{,}6\,\text{eV} \cdot \left(\tfrac{1}{4} - \tfrac{1}{n^2}\right)$ edellyttää. Ennustettu aallonpituus $397\,\text{nm}$ on lyhyempi kuin neljännen viivan $410{,}6\,\text{nm}$, ja viivat tihenevät kohti rajaa, jossa $n \to \infty$: tällöin $E_\text{f} = \tfrac{13{,}6\,\text{eV}}{4} = 3{,}40\,\text{eV}$ ja $\lambda = 365\,\text{nm}$. Viivat ovat erillisiä, koska elektronin sallitut tilat ovat seisovia aaltoja ja energia on kvantittunut.

## fy8-5-L3-05
**Annettu:** $Z = 11$; ionisaatioenergiat $E_\text{i}$ (NIST Atomic Spectra Database): Li $5{,}39\,\text{eV}$ ($n = 2$), Na $5{,}14\,\text{eV}$ ($n = 3$), K $4{,}34\,\text{eV}$ ($n = 4$); siirtymän $3\text{s} \to 3\text{p}$ energia $\Delta E = 2{,}10\,\text{eV}$; $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$, $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$
**Kysytty:** a) natriumin elektronikonfiguraatio, b) ionisaatioenergian pieneneminen, c) viritysfotonin aallonpituus $\lambda$, d) ionisoivan fotonin pisin aallonpituus $\lambda_\text{max}$
**Periaate:** Perustilassa elektronit täyttävät orbitaalit alimmasta energiasta alkaen, kullekin orbitaalille enintään kaksi. Atomin energia muuttuu fotonin absorptiossa fotonin energian verran, joten fotonin energia on tilojen energioiden erotus, $\tfrac{hc}{\lambda} = \Delta E$. Elektronin irrottamiseen tarvitaan vähintään ionisaatioenergia, joten pisin kelpaava aallonpituus vastaa energiaa $E_\text{i}$.
**Kaava:** $\lambda = \dfrac{hc}{\Delta E}$ ja $\lambda_\text{max} = \dfrac{hc}{E_\text{i}}$
**Muunnokset:** $\Delta E = 2{,}10\,\text{eV} = 2{,}10 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 3{,}3642 \cdot 10^{-19}\,\text{J}$ ja $E_\text{i} = 5{,}14\,\text{eV} = 5{,}14 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 8{,}2343 \cdot 10^{-19}\,\text{J}$. Lopuksi $1\,\text{nm} = 10^{-9}\,\text{m}$.
**Sijoitus:** Ensin $hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} = 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}$. Kohdassa c) $\lambda = \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{3{,}3642 \cdot 10^{-19}\,\text{J}} = 5{,}905 \cdot 10^{-7}\,\text{m} = 590{,}5\,\text{nm}$ ja kohdassa d) $\lambda_\text{max} = \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{8{,}2343 \cdot 10^{-19}\,\text{J}} = 2{,}412 \cdot 10^{-7}\,\text{m} = 241{,}2\,\text{nm}$.
**Vastaus:** a) Atomissa on $11$ elektronia, ja konfiguraatio on $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^1$: kuoret $n = 1$ ja $n = 2$ täyttyvät ($2 + 8 = 10$ elektronia), ja yhdestoista elektroni on seuraavassa alimmassa orbitaalissa $3\text{s}$, joten uloimmalla kuorella on vain yksi elektroni. b) Valenssielektroni on litiumilla kuorella $n = 2$, natriumilla kuorella $n = 3$ ja kaliumilla kuorella $n = 4$. Se on sitä kauempana ytimestä, mitä korkeampi kuori on, ja sen ja ytimen välissä on yhä useampi täysi kuori, jonka elektronit hylkivät sitä. Ytimen varaus kasvaa lukujen $3$, $11$ ja $19$ mukaan, mutta ionisaatioenergia silti pienenee arvoista $5{,}39\,\text{eV}$ ja $5{,}14\,\text{eV}$ arvoon $4{,}34\,\text{eV}$, joten kuoren kasvun vaikutus on suurempi kuin ytimen varauksen. Vetyatomin kaava $\tfrac{13{,}6\,\text{eV}}{n^2}$ antaisi samalla tavalla pienenevät arvot $3{,}40\,\text{eV}$, $1{,}51\,\text{eV}$ ja $0{,}85\,\text{eV}$; alkalimetalleilla arvot ovat suurempia, koska sisäkuorten elektronit eivät varjosta ytimen varausta täysin, joten valenssielektroniin vaikuttaa suurempi varaus kuin vedyssä. c) Fotonin aallonpituus on $590\,\text{nm}$, kolme merkitsevää numeroa kuten luvussa $2{,}10\,\text{eV}$. d) Ionisaatioon kelpaa fotoni, jonka aallonpituus on enintään $241\,\text{nm}$. Fotonin energia $2{,}10\,\text{eV}$ on pienempi kuin $E_\text{i} = 5{,}14\,\text{eV}$, joten c)-kohdan fotoni ei riitä irrottamaan elektronia; se vain siirtää elektronin tilalle $3\text{p}$.
**Järkevyys:** Aallonpituus $590\,\text{nm}$ on näkyvän valon alueella, keltaisen valon kohdalla, ja natriumlamppu hohtaa keltaisena. Energiat ovat johdonmukaisia: ionisoiva fotoni tarvitsee energian $5{,}14\,\text{eV}$, mikä on $\tfrac{5{,}14}{2{,}10} = 2{,}45$ kertaa viritysfotonin energia, ja aallonpituus on vastaavasti $\tfrac{590{,}5\,\text{nm}}{241{,}2\,\text{nm}} = 2{,}45$ kertaa niin pitkä. Ionisaatioraja $241\,\text{nm}$ on ultraviolettia, kuten pitääkin.
