## fy8-5-L1-01
**Annettu:** kuoren pääkvanttiluku $n = 5$
**Kysytty:** kuorelle mahtuvien elektronien enimmäismäärä $N_\text{max}$
**Periaate:** Kuorella $n$ on $n^2$ orbitaalia, koska sen alikuorilla s, p, d, … on $1$, $3$, $5$, … orbitaalia. Kullakin orbitaalilla voi olla enintään kaksi elektronia, joilla on vastakkainen spin (Paulin kieltosääntö). Enimmäismäärä on siis kaksi kertaa orbitaalien määrä.
**Kaava:** $N_\text{max} = 2n^2$
**Muunnokset:** Ei tarvita, koska kysytään lukumäärää.
**Sijoitus:** $N_\text{max} = 2 \cdot 5^2 = 2 \cdot 25 = 50$
**Vastaus:** $50$ elektronia. Tulos on tarkka kokonaisluku, koska se on laskettu lukumääristä.
**Järkevyys:** Tulos jatkaa taulukon sarjaa $2, 8, 18, 32$. Peräkkäisten kuorten erotukset $6$, $10$ ja $14$ kasvavat neljällä, joten seuraava erotus on $18$ ja $32 + 18 = 50$. Kuorelle $n = 5$ mahtuu siis enemmän elektroneja kuin kuorelle $n = 4$, kuten pitääkin.

## fy8-5-L1-02
**Annettu:** mittauksia $N = 8000$, solmupallon sisäpuolelle osuneita $k = 421$
**Kysytty:** todennäköisyys $P$ havaita $2\text{s}$-elektroni solmupallon sisäpuolella, prosentteina
**Periaate:** Todennäköisyystulkinnan mukaan aallosta voidaan laskea vain todennäköisyyksiä. Kun mittauksia on tehty monessa samassa tilassa olevassa atomissa, todennäköisyys arvioidaan alueeseen osuneiden mittausten osuutena. Arvio on sitä tarkempi, mitä enemmän mittauksia on.
**Kaava:** todennäköisyyden arvio on $P = \dfrac{k}{N}$
**Muunnokset:** Osuus muunnetaan prosenteiksi kertomalla sadalla: $1 = 100\,\%$.
**Sijoitus:** $P = \dfrac{421}{8000} = 0{,}052\,625 = 5{,}2625\,\%$
**Vastaus:** $5{,}26\,\%$. Vastauksessa on kolme merkitsevää numeroa, koska osumien määrässä $421$ on kolme.
**Järkevyys:** Noin joka kahdeskymmenes mittaus osuu solmupallon sisään, sillä $8000 : 20 = 400$. Se on lähellä lukua $421$. Osuus on pieni, koska solmupallon säde on vain noin $0{,}11\,\text{nm}$ ja suurin osa $2\text{s}$-elektronin todennäköisyydestä on sen ulkopuolella.

## fy8-5-L1-03
**Annettu:** mittauksia $N = 3000$, orbitaalin raja $90\,\%$
**Kysytty:** rajan ulkopuolelle osuvien mittausten odotettu määrä $k_\text{ulko}$
**Periaate:** Raja on piirretty niin, että sen sisällä elektroni havaitaan todennäköisyydellä $0{,}90$. Ulkopuolelle osumisen todennäköisyys on siis $1 - 0{,}90 = 0{,}10$. Monessa mittauksessa ulkopuolelle osuvien osuus on likimain tämä todennäköisyys, $P \approx \tfrac{k}{N}$.
**Kaava:** $k_\text{ulko} = (1 - p)\,N$
**Muunnokset:** $p = 90\,\% = 0{,}90$
**Sijoitus:** $k_\text{ulko} = (1 - 0{,}90) \cdot 3000 = 0{,}10 \cdot 3000 = 300$
**Vastaus:** noin $300$ mittausta. Luku on odotusarvo, ja todellinen määrä vaihtelee sarjasta toiseen.
**Järkevyys:** Joka kymmenes mittaus osuu rajan ulkopuolelle, ja $3000$:n kymmenesosa on $300$. Jos raja olisi seinä, ulkopuolella ei olisi yhtään osumaa. Orbitaalin raja on kuitenkin vain sovittu todennäköisyysraja.

## fy8-5-L1-04
**Annettu:** elektroni $3\text{p}$-tilassa, joten $n = 3$. Vetyatomin energiatasot ovat $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$.
**Kysytty:** irrottamiseen tarvittava pienin energia $E_\text{i}$ elektronivoltteina
**Periaate:** Elektroni on irti atomista, kun sen energia on vähintään $0$. Vetyatomissa tilan energia riippuu vain pääkvanttiluvusta. Tilan $3\text{p}$ energia on siis kuoren $n = 3$ energia. Tarvittava energia on erotus $0 - E_3$.
**Kaava:** $E_\text{i} = 0 - E_3 = \dfrac{13{,}6\,\text{eV}}{3^2}$
**Muunnokset:** Ei tarvita, koska energiatasot ja kysytty energia ovat elektronivoltteina.
**Sijoitus:** $E_\text{i} = \dfrac{13{,}6\,\text{eV}}{9} = 1{,}5111\,\text{eV}$
**Vastaus:** $1{,}51\,\text{eV}$. Vastauksessa on kolme merkitsevää numeroa, koska energiassa $13{,}6\,\text{eV}$ on kolme.
**Järkevyys:** Kuorella $n = 3$ elektroni on kauempana ytimestä ja heikommin sidottu kuin perustilassa. Irrottaminen vaatii siksi vain yhdeksäsosan perustilan energiasta $13{,}6\,\text{eV}$. Energia on positiivinen, koska se tuodaan atomiin.

## fy8-5-L1-05
**Annettu:** kuori $n = 5$. Vetyatomin energiatasot ovat $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$.
**Kysytty:** elektronin energia $E_5$ elektronivoltteina
**Periaate:** Vetyatomissa elektronin tilan energia riippuu vain pääkvanttiluvusta. Energiatasot saadaan annetusta kaavasta. Energia on negatiivinen, koska sidottu elektroni tarvitsee energiaa irrotakseen.
**Kaava:** $E_5 = -\dfrac{13{,}6\,\text{eV}}{5^2}$
**Muunnokset:** Ei tarvita, koska energia kysytään elektronivoltteina.
**Sijoitus:** $E_5 = -\dfrac{13{,}6\,\text{eV}}{25} = -0{,}544\,\text{eV}$
**Vastaus:** $-0{,}544\,\text{eV}$. Vastauksessa on kolme merkitsevää numeroa, koska energiassa $13{,}6\,\text{eV}$ on kolme.
**Järkevyys:** Energia on lähellä nollaa, koska kuoren $n = 5$ elektroni on heikosti sidottu. Energia on suurempi kuin $E_4 = -0{,}85\,\text{eV}$, kuten pitääkin, koska energia kasvaa kuoren numeron kasvaessa.

## fy8-5-L2-01
**Annettu:** alkutila $3\text{p}$, joten $n = 3$. Lopputila $1\text{s}$, joten $n = 1$. Lisäksi $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ ja $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$.
**Kysytty:** fotonin aallonpituus $\lambda$ nanometreinä
**Periaate:** Energia säilyy. Atomin energia pienenee tilojen energioiden erotuksen verran, ja sama energia lähtee fotonina. Fotonin energia on $hf = \tfrac{hc}{\lambda}$. Vetyatomissa tilan energia riippuu vain pääkvanttiluvusta.
**Kaava:** $\dfrac{hc}{\lambda} = E_3 - E_1$, josta $\lambda = \dfrac{hc}{E_3 - E_1}$
**Muunnokset:** Energiaero elektronivoltteina on $E_3 - E_1 = -\tfrac{13{,}6\,\text{eV}}{9} + 13{,}6\,\text{eV} = 12{,}089\,\text{eV}$. Sijoitetaan $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$: $E_3 - E_1 = 12{,}089 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 1{,}9366 \cdot 10^{-18}\,\text{J}$. Lopuksi tarvitaan vielä $1\,\text{nm} = 10^{-9}\,\text{m}$.
**Sijoitus:** Ensin $hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} = 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}$. Sitten $\lambda = \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{1{,}9366 \cdot 10^{-18}\,\text{J}} = 1{,}0257 \cdot 10^{-7}\,\text{m} = 102{,}57\,\text{nm}$
**Vastaus:** $103\,\text{nm}$. Vastauksessa on kolme merkitsevää numeroa, koska energiassa $13{,}6\,\text{eV}$ on kolme.
**Järkevyys:** Fotonin energia on noin $12\,\text{eV}$. Se on enemmän kuin siirtymän $2\text{p} \to 1\text{s}$ energia $10{,}2\,\text{eV}$. Aallonpituuden on siis oltava lyhyempi kuin tämän siirtymän aallonpituus $122\,\text{nm}$. Säteily on ultraviolettia, kuten vedyn kaikki perustilaan päättyvät viivat.

## fy8-5-L2-02
**Annettu:** argonissa on $18$ elektronia. Täyttöjärjestys on $1\text{s}$, $2\text{s}$, $2\text{p}$, $3\text{s}$, $3\text{p}$. Orbitaalille mahtuu enintään kaksi elektronia.
**Kysytty:** uloimman kuoren elektronien määrä $N_\text{ulko}$
**Periaate:** Perustilassa elektronit täyttävät orbitaalit alimmasta energiasta alkaen. Kuorelle $n$ mahtuu enintään $2n^2$ elektronia. Ensin täyttyvät kuoret $n = 1$ ja $n = 2$. Loput elektronit jäävät kuorelle $n = 3$, joka on argonin uloin kuori.
**Kaava:** $N_\text{ulko} = N - 2 \cdot 1^2 - 2 \cdot 2^2$
**Muunnokset:** Ei tarvita, koska kysytään lukumäärää.
**Sijoitus:** $N_\text{ulko} = 18 - 2 - 8 = 8$
**Vastaus:** $8$ elektronia. Tulos on tarkka kokonaisluku.
**Järkevyys:** Kuorella $n = 3$ elektronit ovat alikuorilla $3\text{s}$ ja $3\text{p}$: $2 + 6 = 8$. Molemmat alikuoret ovat siis täynnä. Konfiguraatio $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^2\,3\text{p}^6$ sisältää $18$ elektronia. Täysi uloin s- ja p-alikuori sopii siihen, että argon on jalokaasu, joka ei juuri muodosta sidoksia.

## fy8-5-L2-03
**Annettu:** mittauksia $N = 2400$. Rajat ovat $50\,\%$:n raja $0{,}071\,\text{nm}$ ja $90\,\%$:n raja $0{,}14\,\text{nm}$.
**Kysytty:** rajojen väliin osuvien mittausten odotettu määrä $k$
**Periaate:** Rajan $90\,\%$ sisällä on raja $50\,\%$ kokonaan. Rajojen väliseen kuoreen jää siis todennäköisyys $0{,}90 - 0{,}50 = 0{,}40$. Monessa mittauksessa alueeseen osuvien osuus on likimain alueen todennäköisyys. Rajojen säteitä ei tarvita.
**Kaava:** $k = (p_{90} - p_{50})\,N$
**Muunnokset:** $p_{90} = 90\,\% = 0{,}90$ ja $p_{50} = 50\,\% = 0{,}50$
**Sijoitus:** $k = (0{,}90 - 0{,}50) \cdot 2400 = 0{,}40 \cdot 2400 = 960$
**Vastaus:** noin $960$ mittausta. Luku on odotusarvo, ja todellinen määrä vaihtelee sarjasta toiseen.
**Järkevyys:** Puolet eli $1200$ mittausta osuu $50\,\%$:n rajan sisään. Rajan $90\,\%$ sisään osuu $2160$ mittausta. Niiden erotus on $960$. Rajojen välissä on vähemmän osumia kuin sisemmän rajan sisällä, vaikka kuori on tilavuudeltaan suurempi. Syy on se, että pilvi harvenee ulospäin.

## fy8-5-L2-04
**Annettu:** elektroni kuorella $n = 2$. Lisäksi $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ ja $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$.
**Kysytty:** suurin aallonpituus $\lambda_\text{max}$, jolla fotoni irrottaa elektronin, nanometreinä
**Periaate:** Fotonin energian on oltava vähintään irrottamiseen tarvittava energia $0 - E_2$. Fotonin energia $\tfrac{hc}{\lambda}$ pienenee, kun aallonpituus kasvaa. Suurin kelpaava aallonpituus vastaa siis juuri tätä energiaa.
**Kaava:** $\dfrac{hc}{\lambda_\text{max}} = 0 - E_2$, josta $\lambda_\text{max} = \dfrac{hc}{-E_2}$
**Muunnokset:** $-E_2 = \tfrac{13{,}6\,\text{eV}}{4} = 3{,}40\,\text{eV}$. Sijoitetaan $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$: $-E_2 = 3{,}40 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 5{,}4468 \cdot 10^{-19}\,\text{J}$. Lopuksi tarvitaan vielä $1\,\text{nm} = 10^{-9}\,\text{m}$.
**Sijoitus:** Ensin $hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} = 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}$. Sitten $\lambda_\text{max} = \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{5{,}4468 \cdot 10^{-19}\,\text{J}} = 3{,}6470 \cdot 10^{-7}\,\text{m} = 364{,}70\,\text{nm}$
**Vastaus:** $365\,\text{nm}$. Vastauksessa on kolme merkitsevää numeroa, koska energiassa $13{,}6\,\text{eV}$ on kolme.
**Järkevyys:** Energia $3{,}4\,\text{eV}$ on hieman yli violetin valon fotonin energian. Aallonpituus on siis juuri näkyvän alueen alapuolella, lähellä ultraviolettia. Tätä pidempiaaltoinen näkyvä valo ei irrota elektronia kuorelta $n = 2$.

## fy8-5-L3-01
**Annettu:** fotonin aallonpituus $\lambda = 97{,}3\,\text{nm}$. Atomi on perustilassa, $n = 1$. Lisäksi $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ ja $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$.
**Kysytty:** orbitaalien määrä sillä kuorella $n$, jolle elektroni siirtyy
**Periaate:** Atomi voi absorboida fotonin vain, jos fotonin energia on täsmälleen kahden tilan energioiden erotus. Fotonin energiasta saadaan ylemmän tilan energia $E_n = E_1 + \tfrac{hc}{\lambda}$. Siitä saadaan kuoren numero $n$. Kuorella $n$ on $n^2$ orbitaalia.
**Kaava:** $E_n = E_1 + \dfrac{hc}{\lambda}$, josta $n = \sqrt{\dfrac{13{,}6\,\text{eV}}{-E_n}}$. Orbitaalien määrä on $n^2$.
**Muunnokset:** $\lambda = 97{,}3\,\text{nm} = 97{,}3 \cdot 10^{-9}\,\text{m}$. Kun $hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} = 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}$, fotonin energia on $\tfrac{hc}{\lambda} = \tfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{97{,}3 \cdot 10^{-9}\,\text{m}} = 2{,}0416 \cdot 10^{-18}\,\text{J}$. Elektronivolteiksi energia muunnetaan sijoittamalla $1\,\text{J} = \tfrac{1}{1{,}602 \cdot 10^{-19}}\,\text{eV}$: $\tfrac{2{,}0416 \cdot 10^{-18}}{1{,}602 \cdot 10^{-19}}\,\text{eV} = 12{,}744\,\text{eV}$.
**Sijoitus:** $E_n = -13{,}6\,\text{eV} + 12{,}744\,\text{eV} = -0{,}856\,\text{eV}$ ja $n = \sqrt{\dfrac{13{,}6\,\text{eV}}{0{,}856\,\text{eV}}} = \sqrt{15{,}9} = 3{,}99 \approx 4$. Orbitaaleja on siis $4^2 = 16$.
**Vastaus:** $16$ orbitaalia (kuori $n = 4$: $4\text{s}$, kolme $4\text{p}$, viisi $4\text{d}$ ja seitsemän $4\text{f}$). Luku $n$ on kokonaisluku, joten pyöristys $3{,}99 \to 4$ on luotettava.
**Järkevyys:** Kuoren $n = 4$ energia $-\tfrac{13{,}6\,\text{eV}}{16} = -0{,}85\,\text{eV}$ on sama kuin laskettu $-0{,}856\,\text{eV}$ aallonpituuden kolmen numeron tarkkuudella. Kuorien $n = 3$ ($-1{,}51\,\text{eV}$) ja $n = 5$ ($-0{,}54\,\text{eV}$) energiat ovat selvästi kauempana. Muu kuori ei siis sovi.

## fy8-5-L3-02
**Annettu:** täyttöjärjestys on $1\text{s}$, $2\text{s}$, $2\text{p}$, $3\text{s}$, $3\text{p}$. Orbitaalille mahtuu enintään kaksi elektronia. Alikuori $3\text{p}$ on puoliksi täynnä.
**Kysytty:** atomin elektronien määrä $N$
**Periaate:** Perustilassa elektronit täyttävät orbitaalit alimmasta energiasta alkaen. Alikuorelle $3\text{p}$ tulee elektroneja vasta, kun $1\text{s}$, $2\text{s}$, $2\text{p}$ ja $3\text{s}$ ovat täynnä. Alikuorella s on yksi orbitaali ja alikuorella p kolme, joten niille mahtuu $2$ ja $6$ elektronia. Puoliksi täyteen alikuoreen $3\text{p}$ kuuluu puolet sen enimmäismäärästä.
**Kaava:** $N = N_\text{1s} + N_\text{2s} + N_\text{2p} + N_\text{3s} + \dfrac{N_\text{3p,max}}{2}$
**Muunnokset:** Ei tarvita, koska kysytään lukumäärää.
**Sijoitus:** $N = 2 + 2 + 6 + 2 + \dfrac{6}{2} = 2 + 2 + 6 + 2 + 3 = 15$
**Vastaus:** $15$ elektronia (alkuaine on fosfori, konfiguraatio $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^2\,3\text{p}^3$). Tulos on tarkka kokonaisluku.
**Järkevyys:** Täysiin kuoriin $n = 1$ ja $n = 2$ mahtuu $2 + 8 = 10$ elektronia. Kuorella $n = 3$ on $2 + 3 = 5$ elektronia. Yhteensä niitä on $15$. Jaksollisessa järjestelmässä järjestysluku $15$ on fosfori. Se on kolmannen jakson keskellä, kuten puolillaan oleva alikuori $3\text{p}$ antaa odottaa.

## fy8-5-L3-03
**Annettu:** mittauksia $N = 5000$, orbitaalin raja $90\,\%$. Solmupallon sisäpuolelle osuu $5{,}3\,\%$ mittauksista, ja tämä sisäosa kuuluu käytännössä kokonaan orbitaalin alueeseen.
**Kysytty:** orbitaalin alueeseen solmupallon ulkopuolelle osuvien mittausten odotettu määrä $k$
**Periaate:** Orbitaalin alueen todennäköisyys $0{,}90$ jakautuu kahteen osaan: solmupallon sisäosaan ja solmupallon ulkopuoliseen kuoreen. Sisäosa kuuluu alueeseen kokonaan, joten ulko-osan todennäköisyys on erotus $0{,}90 - 0{,}053$. Monessa mittauksessa alueeseen osuvien osuus on likimain alueen todennäköisyys.
**Kaava:** $k = (p - p_\text{sisä})\,N$
**Muunnokset:** $p = 90\,\% = 0{,}90$ ja $p_\text{sisä} = 5{,}3\,\% = 0{,}053$
**Sijoitus:** $k = (0{,}90 - 0{,}053) \cdot 5000 = 0{,}847 \cdot 5000 = 4235$
**Vastaus:** noin $4240$ mittausta. Luku on odotusarvo, jonka todellinen sarja toteuttaa vain likimain. Sisäosan osuus $5{,}3\,\%$ rajaa tarkkuuden noin kahteen tai kolmeen merkitsevään numeroon.
**Järkevyys:** Alueeseen osuu kaikkiaan noin $0{,}90 \cdot 5000 = 4500$ mittausta. Solmupallon sisään niistä osuu noin $0{,}053 \cdot 5000 = 265$. Erotus $4235$ on selvästi suurin osa. Tämä sopii siihen, että $2\text{s}$-elektronin yleisin etäisyys on solmupallon ulkopuolella.
