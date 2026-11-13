## fy5-16-L1-01
**Annettu:** melutaso $L = 91\,\text{dB}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** päivittäinen vertailuaika $t_\text{v}$ tunteina
**Periaate:** Melualtistus lasketaan energian keskiarvona. Jokainen $3\,\text{dB}$:n nousu kaksinkertaistaa intensiteetin. Sama annos täyttyy silloin puolessa ajassa.
**Kaava:** $t_\text{v} = \dfrac{t_0}{2^{\,n}}$, missä $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Muunnokset:** Ei tarvita. Tasot ovat desibeleinä ja aika saadaan tunteina.
**Sijoitus:** $n = \dfrac{91\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 2$, $t_\text{v} = \dfrac{8\,\text{h}}{2^2} = 2{,}0\,\text{h}$
**Vastaus:** $2{,}0\,\text{h}$. Tasot ovat kokonaisia desibelejä ja sääntö on arvio. Kaksi merkitsevää numeroa riittää siksi.
**Järkevyys:** Kaksi puolitusta: $8\,\text{h} \to 4\,\text{h} \to 2\,\text{h}$. Intensiteetti on nelinkertainen, ja $4 \cdot 2\,\text{h} = 8\,\text{h}$. Annos on siis sama kuin vertailussa.

## fy5-16-L1-02
**Annettu:** yhden puhaltimen taso $L_1 = 70\,\text{dB}$; kaksi samanlaista puhallinta
**Kysytty:** yhteinen taso $L$ desibeleinä
**Periaate:** Kahden lähteen intensiteetit summautuvat, eivät tasot. Kaksi yhtä voimakasta lähdettä kaksinkertaistaa intensiteetin (luku *Intensiteetti ja desibeliasteikko*).
**Kaava:** $L = L_1 + 10\,\text{dB} \cdot \lg \dfrac{2 I_1}{I_1} = L_1 + 10\,\text{dB} \cdot \lg 2$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $L = 70\,\text{dB} + 10\,\text{dB} \cdot \lg 2 = 70\,\text{dB} + 3{,}01\,\text{dB} = 73{,}01\,\text{dB}$
**Vastaus:** $73\,\text{dB}$, kokonaisina desibeleinä kuten lähtötieto.
**Järkevyys:** Taso nousee vain vähän, vaikka melua tuottavia laitteita on kaksi kertaa enemmän. Tulos $140\,\text{dB}$ olisi kipukynnyksen yläpuolella. Se ei sovi kahdelle puhaltimelle.

## fy5-16-L1-03
**Annettu:** $L_1 = 88\,\text{dB}$ etäisyydellä $r_1 = 4{,}0\,\text{m}$, uusi etäisyys $r_2 = 8{,}0\,\text{m}$; pistemäinen lähde avoimessa tilassa
**Kysytty:** taso $L_2$ etäisyydellä $r_2$
**Periaate:** Pistemäisen lähteen intensiteetti on kääntäen verrannollinen etäisyyden neliöön. Kaksinkertainen etäisyys antaa siis neljäsosan intensiteetistä. Se laskee tasoa $10\,\text{dB} \cdot \lg 4 \approx 6\,\text{dB}$ (luku *Intensiteetti ja desibeliasteikko*).
**Kaava:** $L_2 = L_1 - 6\,\text{dB}$, kun $r_2 = 2 r_1$
**Muunnokset:** Ei tarvita. Suhde on $r_2 : r_1 = 8{,}0\,\text{m} : 4{,}0\,\text{m} = 2$.
**Sijoitus:** $L_2 = 88\,\text{dB} - 6\,\text{dB} = 82\,\text{dB}$
**Vastaus:** $82\,\text{dB}$, kokonaisina desibeleinä kuten lähtötieto.
**Järkevyys:** Taso pienenee mutta pysyy samaa suuruusluokkaa. Neljäsosa intensiteetistä ei ole neljäsosa desibeliluvusta. Heijastavassa tilassa pudotus olisi pienempi.

## fy5-16-L1-04
**Annettu:** melutaso $L_\text{m} = 106\,\text{dB}$, suojainten vaimennus $\Delta L = 23\,\text{dB}$
**Kysytty:** korvaan pääsevä taso $L$
**Periaate:** Kuulonsuojaimen vaimennus kertoo, kuinka monta desibeliä se pienentää korvaan pääsevää tasoa. Vaimennus vähennetään siis melutasosta.
**Kaava:** $L = L_\text{m} - \Delta L$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $L = 106\,\text{dB} - 23\,\text{dB} = 83\,\text{dB}$
**Vastaus:** $83\,\text{dB}$, kokonaisina desibeleinä kuten lähtötiedot.
**Järkevyys:** Toiminta-arvoihin verrataan altistusta ilman suojaimia. Taso $106\,\text{dB}$ ylittää kummankin toiminta-arvon, joten suojaimia on käytettävä. Korvalle tuleva $83\,\text{dB}$ jää altistuksen raja-arvon $87\,\text{dB(A)}$ alle. Koska $83\,\text{dB}$ on alle $85\,\text{dB}$, vertailuannos ei täyty työpäivän aikana, jos suojaimet ovat hyvin paikallaan ja niitä pidetään koko ajan. Vertailuannosta pienempi annos ei silti takaa, että kuulo on turvassa. Ilman suojaimia vertailuaika olisi noin $4\,\text{min}$.

## fy5-16-L1-05
**Kysytty:** kuuluuko kukin keino lähteeseen, kulkutiehen vai korvaan
**Periaate:** Lähteessä vähennetään syntyvää ääntä. Kulkutiellä estetään tai vaimennetaan äänen eteneminen lähteestä kuulijaan. Korvalla vähennetään korvaan pääsevää ääntä.
**Mallivastaus:** a) Meluseinä pysäyttää suoran äänen tien ja asuntojen välissä. Se on siis kulkutien keino. b) Kotelo sulkee äänen heti koneen ympärille. Se torjuu siis melua lähteessä. c) Korvatulpat vaimentavat ääntä vasta korvalla. d) Kattoon asennetut levyt eivät hiljennä konetta. Ne vaimentavat heijastuksia, joiden kautta ääni kulkee työntekijälle. Ne ovat siis kulkutien keino.

## fy5-16-L2-01
**Annettu:** kaksi samanlaista konetta, kumpikin $L_1 = 85\,\text{dB}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** päivittäinen vertailuaika $t_\text{v}$ tunteina
**Periaate:** Kahden yhtä voimakkaan lähteen intensiteetit summautuvat. Intensiteetti kaksinkertaistuu, ja taso nousee noin $3\,\text{dB}$. Sitten jokainen $3\,\text{dB}$ toiminta-arvon yli puolittaa vertailuajan.
**Kaava:** $L = L_1 + 3\,\text{dB}$ ja $t_\text{v} = \dfrac{t_0}{2^{\,n}}$, missä $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $L = 85\,\text{dB} + 3\,\text{dB} = 88\,\text{dB}$, $n = \dfrac{88\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 1$, $t_\text{v} = \dfrac{8\,\text{h}}{2^1} = 4{,}0\,\text{h}$
**Vastaus:** $4{,}0\,\text{h}$. Sääntö on arvio. Kaksi merkitsevää numeroa riittää siksi.
**Järkevyys:** Toinen kone tuo saman energian lisää. Kokonaisenergia kertyy siis kaksi kertaa nopeammin, ja annos täyttyy puolessa ajassa. Tulos on johdonmukainen: $2 \cdot 4\,\text{h} = 8\,\text{h}$.

## fy5-16-L2-02
**Annettu:** taso korvassa $L = 94\,\text{dB}$, kuunteluaika $t = 1{,}5\,\text{h}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** annos prosentteina vertailuannoksesta
**Periaate:** Lasketaan ensin vertailuaika tasolla $94\,\text{dB}$. Siinä ajassa kertyy täsmälleen vertailuannos. Annoksen osuus on kuunteluajan ja vertailuajan suhde, koska taso on koko ajan sama.
**Kaava:** $t_\text{v} = \dfrac{t_0}{2^{\,n}}$, missä $n = \dfrac{L - L_0}{3\,\text{dB}}$, ja osuus $= \dfrac{t}{t_\text{v}} \cdot 100\,\%$
**Muunnokset:** Ei tarvita. Ajat ovat tunteina, ja yksikkö supistuu.
**Sijoitus:** $n = \dfrac{94\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 3$, $t_\text{v} = \dfrac{8\,\text{h}}{2^3} = 1{,}0\,\text{h}$, osuus $= \dfrac{1{,}5\,\text{h}}{1{,}0\,\text{h}} \cdot 100\,\% = 150\,\%$
**Vastaus:** $150\,\%$, kaksi merkitsevää numeroa kuten ajassa $1{,}5\,\text{h}$.
**Järkevyys:** Kuunteluaika on pidempi kuin vertailuaika. Annos ylittää siis vertailun, ja yli $100\,\%$ on odotettu. Jos ääntä pienennettäisiin $3\,\text{dB}$, annos puolittuisi $75\,\%$:iin.

## fy5-16-L2-03
**Annettu:** $L_1 = 78\,\text{dB}$ etäisyydellä $r_1 = 2{,}0\,\text{m}$, toivottu taso $L_2 = 60\,\text{dB}$; pistemäinen lähde avoimessa tilassa
**Kysytty:** etäisyys $r_2$ metreinä
**Periaate:** Avoimessa tilassa jokainen etäisyyden kaksinkertaistuminen laskee tasoa $6\,\text{dB}$, koska intensiteetti pienenee neljäsosaan (luku *Intensiteetti ja desibeliasteikko*). Lasketaan, montako kaksinkertaistumista tarvitaan.
**Kaava:** $k = \dfrac{L_1 - L_2}{6\,\text{dB}}$ ja $r_2 = 2^{\,k} \cdot r_1$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $k = \dfrac{78\,\text{dB} - 60\,\text{dB}}{6\,\text{dB}} = 3$, $r_2 = 2^3 \cdot 2{,}0\,\text{m} = 16\,\text{m}$
**Vastaus:** $16\,\text{m}$, kaksi merkitsevää numeroa kuten etäisyydessä $2{,}0\,\text{m}$.
**Järkevyys:** Etäisyydet $2\,\text{m}$, $4\,\text{m}$, $8\,\text{m}$ ja $16\,\text{m}$ antavat tasot $78\,\text{dB}$, $72\,\text{dB}$, $66\,\text{dB}$ ja $60\,\text{dB}$. Pihalla talojen seinät heijastavat ääntä. Todellisuudessa tarvittaisiin siis hieman pidempi matka.

## fy5-16-L2-04
**Annettu:** taso laskee $L_1 = 92\,\text{dB}$:stä $L_2 = 62\,\text{dB}$:iin ajassa $\Delta t = 0{,}45\,\text{s}$; lasku on tasainen
**Kysytty:** jälkikaiunta-aika $T$ eli aika, jossa taso laskee $60\,\text{dB}$
**Periaate:** Kun taso laskee tasaisesti, se laskee yhtä monta desibeliä jokaisessa sekunnissa. Jälkikaiunta-aika saadaan laskunopeudesta. Pudotus $60\,\text{dB}$ vaatii yhtä monta kertaa pidemmän ajan kuin mitattu lasku on pienempi. Mittaus tehdään usein näin, koska huoneen taustamelu peittää täyden $60\,\text{dB}$:n pudotuksen.
**Kaava:** $T = \dfrac{60\,\text{dB}}{L_1 - L_2} \cdot \Delta t$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $T = \dfrac{60\,\text{dB}}{92\,\text{dB} - 62\,\text{dB}} \cdot 0{,}45\,\text{s} = 2 \cdot 0{,}45\,\text{s} = 0{,}90\,\text{s}$
**Vastaus:** $0{,}90\,\text{s}$, kaksi merkitsevää numeroa kuten ajassa $0{,}45\,\text{s}$.
**Järkevyys:** Mitattu lasku $30\,\text{dB}$ on puolet $60\,\text{dB}$:stä, joten aika kaksinkertaistuu. Tulos on pidempi kuin luokille tavoiteltu noin puoli sekuntia. Se sopii tyhjään, kovapintaiseen luokkaan.

## fy5-16-L2-08
**Kysytty:** minkä päätelmän kompressorin melutason mittaukset neljältä etäisyydeltä tukevat, kun lukeman epävarmuus on $\Delta L = 1\,\text{dB}$
**Periaate:** Pistemäisen lähteen intensiteetti on avoimessa tilassa kääntäen verrannollinen etäisyyden neliöön. Kun etäisyys kaksinkertaistuu, intensiteetti pienenee neljäsosaan ja taso pienenee $10\,\text{dB} \cdot \lg 4 \approx 6{,}0\,\text{dB}$. Kahden lukeman erotuksen epävarmuus on enintään $2\Delta L = 2\,\text{dB}$. Tätä pienempiä eroja ei voi mitata.
**Mallivastaus:** Aineisto tukee päätelmää, että taso laskee noin $6\,\text{dB}$ joka kerta, kun etäisyys kaksinkertaistuu. Peräkkäisten lukemien erotukset ovat

$91\,\text{dB} - 85\,\text{dB} = 6\,\text{dB}$

$85\,\text{dB} - 79\,\text{dB} = 6\,\text{dB}$

$79\,\text{dB} - 74\,\text{dB} = 5\,\text{dB}$

Kaikki erotukset ovat lähellä odotettua $6{,}0\,\text{dB}$:ä. Suurin poikkeama $1\,\text{dB}$ on pienempi kuin erotuksen epävarmuus $2\,\text{dB}$. Siksi viimeisen välin pienempikään lasku ei osoita, että ääni vaimenisi kauempana hitaammin. Taso ei puolitu: puolet $91\,\text{dB}$:stä olisi noin $46\,\text{dB}$, kun mitattiin $85\,\text{dB}$. Etäisyydellä $4{,}0\,\text{m}$ lukema on $85\,\text{dB}$. Epävarmuuden vuoksi todellinen taso voi kuitenkin olla $84$–$86\,\text{dB}$, joten ylempi toiminta-arvo voi ylittyä. Toiminta-arvo ei myöskään ole turvallisuusraja. Mittaus ei siis osoita $8\,\text{h}$:n työskentelyä turvalliseksi.

## fy5-16-L3-01
**Annettu:** $t_1 = 4{,}0\,\text{h}$ tasolla $L_1 = 88\,\text{dB}$, $t_2 = 4{,}0\,\text{h}$ tasolla $L_2 = 82\,\text{dB}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** päivän annos prosentteina vertailuannoksesta
**Periaate:** Annos on korvaan kertynyt energia. Eri jaksojen osuudet lasketaan siis yhteen. Kunkin jakson osuus on sen keston ja kyseisen tason vertailuajan suhde.
**Kaava:** $t_{\text{v},i} = \dfrac{t_0}{2^{\,n_i}}$, missä $n_i = \dfrac{L_i - L_0}{3\,\text{dB}}$, ja annos $= \left(\dfrac{t_1}{t_{\text{v},1}} + \dfrac{t_2}{t_{\text{v},2}}\right) \cdot 100\,\%$
**Muunnokset:** Ei tarvita. Ajat ovat tunteina, ja yksikkö supistuu.
**Sijoitus:** $n_1 = 1$, joten $t_{\text{v},1} = 8\,\text{h} : 2 = 4{,}0\,\text{h}$. $n_2 = \dfrac{82\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = -1$, joten $t_{\text{v},2} = 8\,\text{h} \cdot 2 = 16\,\text{h}$. Annos $D = \dfrac{4{,}0\,\text{h}}{4{,}0\,\text{h}} + \dfrac{4{,}0\,\text{h}}{16\,\text{h}} = 1 + 0{,}25 = 1{,}25 = 125\,\%$
**Vastaus:** $125\,\%$. Ajat on annettu kahden numeron tarkkuudella, joten tulos on arvio, noin $1{,}3$-kertainen annos. Päivittäinen altistus ylittää ylemmän toiminta-arvon. Kuulonsuojaimia on siis käytettävä, ja melua on vähennettävä.
**Järkevyys:** Jo lastauslaiturin $4\,\text{h}$ täyttää koko annoksen, joten tuloksen täytyy olla yli $100\,\%$. Pakkaamon osuus on pieni. Siellä intensiteetti on vain neljäsosa laiturin intensiteetistä.

## fy5-16-L3-02
**Annettu:** kaksi samanlaista yksikköä, kumpikin $L_1 = 55\,\text{dB}$ etäisyydellä $r_1 = 3{,}0\,\text{m}$; ikkunan etäisyys kummastakin $r_2 = 12\,\text{m}$; pistemäiset lähteet avoimessa tilassa
**Kysytty:** taso $L$ ikkunan kohdalla, kun molemmat käyvät
**Periaate:** Lasketaan ensin yhden yksikön taso ikkunalla. Jokainen etäisyyden kaksinkertaistuminen laskee tasoa $6\,\text{dB}$. Kahden yhtä voimakkaan lähteen intensiteetit summautuvat, joten yhteinen taso on $3\,\text{dB}$ suurempi.
**Kaava:** $L_\text{yksi} = L_1 - k \cdot 6\,\text{dB}$, missä $2^{\,k} = \dfrac{r_2}{r_1}$, ja $L = L_\text{yksi} + 3\,\text{dB}$
**Muunnokset:** Ei tarvita. Suhde on $r_2 : r_1 = 12\,\text{m} : 3{,}0\,\text{m} = 4$, joten $2^{\,k} = 4$ ja $k = 2$.
**Sijoitus:** $L_\text{yksi} = 55\,\text{dB} - 2 \cdot 6\,\text{dB} = 43\,\text{dB}$. $L = 43\,\text{dB} + 3\,\text{dB} = 46\,\text{dB}$
**Vastaus:** $46\,\text{dB}$, kokonaisina desibeleinä kuten lähtötieto.
**Järkevyys:** Yhden yksikön taso on etäisyyden vuoksi selvästi pienempi kuin lähellä, ja toinen yksikkö nostaa sitä vain vähän. Tulos on hiljaisen keskustelun alapuolella. Makuuhuoneessa tasainen humina voi silti häiritä unta.

## fy5-16-L3-03
**Kysytty:** miksi vastamelu vaimentaa matalaa huminaa paremmin kuin puhetta
**Periaate:** Vastamelu kumoaa melun heikentävällä interferenssillä vain, jos se on korvan kohdalla vastakkaisessa vaiheessa. Aallonpituus $\lambda = \dfrac{v}{f}$ ja jaksonaika $T = \dfrac{1}{f}$ kertovat, kuinka tarkasti ajoituksen ja paikan on osuttava.
**Mallivastaus:** Huminan aallonpituus on $\lambda = \dfrac{343\,\text{m/s}}{100\,\text{Hz}} \approx 3{,}4\,\text{m}$ ja jaksonaika $10\,\text{ms}$. Koko korvakäytävä ja kuvun sisus ovat pieniä aallonpituuteen verrattuna. Elektroniikalla on aikaa muodostaa vastakkainen signaali. Vastamelu pysyy siis korvan kohdalla vastakkaisessa vaiheessa. Puheen aallonpituudet ovat $\dfrac{343\,\text{m/s}}{3000\,\text{Hz}} \approx 11\,\text{cm}$ ja $\dfrac{343\,\text{m/s}}{1000\,\text{Hz}} \approx 34\,\text{cm}$, ja jaksonaika on enintään $1\,\text{ms}$. Pienikin ajoitusvirhe tai muutaman senttimetrin paikkaero siirtää vaihetta paljon. Silloin aallot eivät enää kumoa toisiaan. Lisäksi puhe vaihtelee nopeasti, mutta humina on tasaista. Korkeita ääniä vaimentavat lähinnä kuulokkeiden kuvut.

## fy5-16-L1-06
**Kysytty:** mikä toimenpide lyhentää luokan jälkikaiunta-aikaa
**Periaate:** Jälkikaiunta-aika on aika, jossa taso laskee $60\,\text{dB}$ äänilähteen vaiettua. Kovat pinnat heijastavat ääntä ja pitävät sen huoneessa. Pehmeät ja huokoiset pinnat vaimentavat heijastuksia. Silloin taso laskee nopeammin.
**Mallivastaus:** Jälkikaiunta-aikaa lyhentää se, että kattoon asennetaan huokoisia vaimennuslevyjä. Ne imevät osan niihin osuvasta äänestä. Kiiltävät laatat ja lasipinnat ovat kovia pintoja. Ne heijastavat ääntä takaisin huoneeseen ja pidentäisivät aikaa. Äänen voimakkuuden pienentäminen ei auta. Jälkikaiunta-aika mitataan $60\,\text{dB}$:n pudotuksena, eikä se riipu alkutasosta.

## fy5-16-L1-07
**Annettu:** ulkotaso $L_\text{ulko} = 68\,\text{dB}$, sisätaso $L_\text{sisä} = 41\,\text{dB}$
**Kysytty:** seinän ja ikkunoiden vaimennus $\Delta L$
**Periaate:** Vaimennus kertoo, kuinka monta desibeliä rakenne pienentää tasoa. Se on siis ulko- ja sisätason erotus.
**Kaava:** $\Delta L = L_\text{ulko} - L_\text{sisä}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $\Delta L = 68\,\text{dB} - 41\,\text{dB} = 27\,\text{dB}$
**Vastaus:** $27\,\text{dB}$, kokonaisina desibeleinä kuten lähtötiedot.
**Järkevyys:** Kun vaimennus lisätään sisätasoon, saadaan ulkotaso: $41\,\text{dB} + 27\,\text{dB} = 68\,\text{dB}$. Sisällä on hiljaisempaa kuin ulkona, kuten pitääkin.

## fy5-16-L1-08
**Kysytty:** miten kaiutin tuottaa äänen sähköisestä signaalista
**Periaate:** Kaiuttimessa signaali on vaihtovirta. Se kulkee kelassa, joka on magneetin kentässä. Magneettikenttä kohdistaa virtaan vaihtuvan voiman. Siksi kela ja siihen kiinnitetty kartio värähtelevät. Kartio synnyttää ilmaan ääniaallon.
**Mallivastaus:** Kelan vaihtovirta ja magneetti saavat kartion värähtelemään signaalin tahdissa. Kartio työntää ilmaa edestakaisin. Jos ääni liikuttaa kalvoa ja synnyttää jännitteen, kyse on mikrofonista eikä kaiuttimesta. Kaiuttimessa magneetti on paikallaan. Ääni ei myöskään synny siitä, että ilma lämpenee.

## fy5-16-L2-05
**Annettu:** ennen levyjä taso laskee $90{,}3\,\text{dB}$:stä $74{,}4\,\text{dB}$:iin. Levyjen jälkeen se laskee $90{,}2\,\text{dB}$:stä $50{,}1\,\text{dB}$:iin. Aika on $\Delta t = 0{,}40\,\text{s}$. Lasku on tasainen.
**Kysytty:** jälkikaiunta-ajan lyhenemä prosentteina
**Periaate:** Kun taso laskee tasaisesti, jälkikaiunta-aika on aika, jossa lasku on $60\,\text{dB}$. Lasketaan se kummallekin mittaukselle mitatun pudotuksen ja ajan avulla. Sitten verrataan aikoja.
**Taulukon lukeminen:** Pudotus ennen levyjä on $\Delta L_1 = 90{,}3\,\text{dB} - 74{,}4\,\text{dB} = 15{,}9\,\text{dB}$. Levyjen jälkeen pudotus on $\Delta L_2 = 90{,}2\,\text{dB} - 50{,}1\,\text{dB} = 40{,}1\,\text{dB}$.
**Kaava:** $T = \dfrac{60\,\text{dB}}{\Delta L} \cdot \Delta t$ ja lyhenemä $= \dfrac{T_1 - T_2}{T_1} \cdot 100\,\%$
**Muunnokset:** Ei tarvita.
**Sijoitus:**
$$\begin{aligned}
T_1 &= \frac{60\,\text{dB}}{15{,}9\,\text{dB}} \cdot 0{,}40\,\text{s} \\
&= 1{,}51\,\text{s} \\
T_2 &= \frac{60\,\text{dB}}{40{,}1\,\text{dB}} \cdot 0{,}40\,\text{s} \\
&= 0{,}599\,\text{s} \\
\text{lyhenemä} &= \frac{1{,}51 - 0{,}599}{1{,}51} \cdot 100\,\% \\
&= 60{,}3\,\%
\end{aligned}$$
**Vastaus:** $60{,}3\,\%$. Lähtötiedoissa on kolme merkitsevää numeroa. Siksi tulos annetaan kolmella.
**Järkevyys:** Jälkikaiunta-aika lyheni noin $1{,}5\,\text{s}$:sta noin $0{,}6\,\text{s}$:iin. Uusi aika on siis noin $0{,}4$-kertainen. Levyjen jälkeen taso laskee $40{,}1\,\text{dB} : 15{,}9\,\text{dB} \approx 2{,}5$ kertaa nopeammin. Lasku $1 - 1 : 2{,}5 = 0{,}6$ vastaa tulosta. Aika $0{,}6\,\text{s}$ sopii puheluokkaan.

## fy5-16-L2-06
**Annettu:** vaimennus $\Delta L = L_\text{ilman} - L_\text{este}$ taajuuksilla $125$, $500$, $2000$ ja $4000\,\text{Hz}$ taulukon arvoista. Äänen nopeus on $v = 343\,\text{m/s}$.
**Kysytty:** a) ero vaimennuksessa taajuuksilla $4000\,\text{Hz}$ ja $500\,\text{Hz}$; b) miksi matala ääni vaimenee huonommin
**Periaate:** Esteen vaimennus on tason pudotus esteen takana. Aalto kiertyy esteen ohi sitä paremmin, mitä pidempi sen aallonpituus $\lambda = \dfrac{v}{f}$ on esteen kokoon verrattuna.
**Taulukon lukeminen:** Taulukosta vaimennukset ovat $125\,\text{Hz}$: $8{,}1\,\text{dB}$, $500\,\text{Hz}$: $13{,}4\,\text{dB}$, $2000\,\text{Hz}$: $22{,}2\,\text{dB}$ ja $4000\,\text{Hz}$: $25{,}2\,\text{dB}$.
**Kaava:** $\Delta L = L_\text{ilman} - L_\text{este}$ ja $\lambda = \dfrac{v}{f}$
**Muunnokset:** Ei tarvita.
**Sijoitus:**
$$\begin{aligned}
\Delta L_{500} &= 68{,}4\,\text{dB} - 55{,}0\,\text{dB} \\
&= 13{,}4\,\text{dB} \\
\Delta L_{4000} &= 60{,}3\,\text{dB} - 35{,}1\,\text{dB} \\
&= 25{,}2\,\text{dB} \\
\Delta L_{4000} - \Delta L_{500} &= 11{,}8\,\text{dB}
\end{aligned}$$
Aallonpituudet ovat $\lambda_{125} = \dfrac{343\,\text{m/s}}{125\,\text{Hz}} = 2{,}7\,\text{m}$ ja $\lambda_{4000} = \dfrac{343\,\text{m/s}}{4000\,\text{Hz}} = 0{,}086\,\text{m}$.
**Vastaus:** a) $11{,}8\,\text{dB}$. b) Matalan äänen aallonpituus $2{,}7\,\text{m}$ on esteen korkeuden luokkaa. Aalto taipuu siis esteen yli, ja taso esteen takana pysyy suurempana. Korkean äänen aallonpituus $0{,}086\,\text{m}$ on paljon esteen kokoa pienempi. Este jättää sen varjoonsa.
**Järkevyys:** Vaimennus kasvaa taajuuden mukana joka rivillä: $8{,}1 < 13{,}4 < 22{,}2 < 25{,}2\,\text{dB}$. Siksi tulos on positiivinen. Ero on myös pienempi kuin suurin vaimennus $25{,}2\,\text{dB}$.

## fy5-16-L2-07
**Annettu:** työpisteen taso $L = 109\,\text{dB}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$; opiskelijan tulos $1{,}0\,\text{h}$
**Kysytty:** a) mikä opiskelijan päättelyssä on väärin; b) oikea vertailuaika $t_\text{v}$ minuutteina
**Periaate:** Jokainen $3\,\text{dB}$ toiminta-arvon yli puolittaa vertailuajan. Aika jaetaan siis kahdella jokaista $3\,\text{dB}$:n askelta kohti. Askeleet kertautuvat: aika jaetaan luvulla $2^{\,n}$, ei luvulla $n$.
**Kaava:** $n = \dfrac{L - L_0}{3\,\text{dB}}$ ja $t_\text{v} = \dfrac{t_0}{2^{\,n}}$
**Muunnokset:** $1\,\text{h} = 60\,\text{min}$.
**Sijoitus:**
$$\begin{aligned}
n &= \frac{109\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} \\
&= 8 \\
t_\text{v} &= \frac{8\,\text{h}}{2^{\,8}} \\
&= \frac{480\,\text{min}}{256} \\
&= 1{,}875\,\text{min} \\
&\approx 1{,}9\,\text{min}
\end{aligned}$$
**Vastaus:** a) Opiskelija laski askelten määrän $n = 8$ oikein, mutta jakoi ajan luvulla $8$. Jokainen askel puolittaa jäljellä olevan ajan. Aika jaetaan siis kahdella kahdeksan kertaa eli kaikkiaan luvulla $256$. b) Vertailuaika on noin $1{,}9\,\text{min}$, eli vajaat kaksi minuuttia.
**Järkevyys:** Opiskelijan tulos $1{,}0\,\text{h}$ eli $60\,\text{min}$ on $32$-kertainen oikeaan nähden. Hänen tavallaan jokainen lisäaskel lyhentäisi aikaa yhä vähemmän. Energia kuitenkin kasvaa joka askeleella samassa suhteessa. Tarkistus puolittamalla: kolme puolitusta vie ajan $8\,\text{h} \to 1\,\text{h}$. Viisi lisää vie ajan $60\,\text{min} \to 1{,}875\,\text{min}$. Yhteensä puolituksia on kahdeksan.

## fy5-16-L3-04
**Annettu:** sahaus $L_1 = 97\,\text{dB}$, $t_1 = 1{,}0\,\text{h}$; höyläys $L_2 = 91\,\text{dB}$, $t_2 = 2{,}0\,\text{h}$; kokoaminen $L_3 = 85\,\text{dB}$, $t_3 = 3{,}0\,\text{h}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** a) päivän annos prosentteina; b) kuulonsuojainten pienin vaimennus $\Delta L$; c) riittääkö sahan koteloiminen
**Periaate:** Annos on korvaan kertynyt energia. Vaiheiden osuudet lasketaan siis yhteen. Osuus on keston ja kyseisen tason vertailuajan suhde. Kuulonsuojain pienentää kaikkien vaiheiden intensiteettiä samalla kertoimella. Siksi annos jaetaan luvulla $2^{\,\Delta L / (3\,\text{dB})}$.
**Kaava:** $t_{\text{v},i} = \dfrac{t_0}{2^{\,n_i}}$, missä $n_i = \dfrac{L_i - L_0}{3\,\text{dB}}$; annos $D = \sum \dfrac{t_i}{t_{\text{v},i}}$; ehto $\dfrac{D}{2^{\,\Delta L / (3\,\text{dB})}} \le 1$
**Muunnokset:** Ei tarvita. Ajat ovat tunteina, ja yksikkö supistuu.
**Sijoitus:**
Sahaus: $n_1 = \dfrac{97 - 85}{3} = 4$, joten $t_{\text{v},1} = 8\,\text{h} : 16 = 0{,}50\,\text{h}$ ja osuus on $1{,}0\,\text{h} : 0{,}50\,\text{h} = 2{,}0$. Höyläys: $n_2 = 2$, $t_{\text{v},2} = 2{,}0\,\text{h}$ ja osuus $1{,}0$. Kokoaminen: $n_3 = 0$, $t_{\text{v},3} = 8\,\text{h}$ ja osuus $0{,}375$.
$$\begin{aligned}
D &= 2{,}0 + 1{,}0 + 0{,}375 \\
&= 3{,}375
\end{aligned}$$
Kohta b:
$$\begin{aligned}
2^{\,\Delta L / (3\,\text{dB})} &\ge 3{,}375 \\
\Delta L &\ge 3\,\text{dB} \cdot \frac{\lg 3{,}375}{\lg 2} \\
&= 3\,\text{dB} \cdot 1{,}755 \\
&= 5{,}26\,\text{dB}
\end{aligned}$$
Kohta c: kotelo laskee sahauksen tason arvoon $87\,\text{dB}$. Silloin $n_1 = \dfrac{2}{3}$ ja $t_{\text{v},1} = \dfrac{8\,\text{h}}{2^{2/3}} = 5{,}04\,\text{h}$. Osuus on $1{,}0 : 5{,}04 = 0{,}198$. Uusi annos on $D = 0{,}198 + 1{,}0 + 0{,}375 = 1{,}57$.
**Vastaus:** a) noin $340\,\%$. b) vähintään $5{,}3\,\text{dB}$. c) Kotelo ei riitä yksin, koska annos on edelleen noin $160\,\%$ vertailuannoksesta. Kotelon lisäksi tarvitaan esimerkiksi kuulonsuojaimet, joiden vaimennus on vähintään $\dfrac{3\,\text{dB} \cdot \lg 1{,}57}{\lg 2} = 2{,}0\,\text{dB}$. Toinen keino on sijoittaa höyläyskone erilleen työpisteestä.
**Järkevyys:** Sahaus ja höyläys ovat yli toiminta-arvon. Annoksen täytyy siis olla yli $100\,\%$. Tavalliset suojaimet vaimentavat $20$–$30\,\text{dB}$, joten $5{,}3\,\text{dB}$ täyttyy helposti.

## fy5-16-L3-05
**Annettu:** $L_1 = 112\,\text{dB}$ etäisyydellä $r_1 = 2{,}0\,\text{m}$, kuulija etäisyydellä $r_2 = 8{,}0\,\text{m}$; tulppien vaimennus $\Delta L = 8\,\text{dB}$; konsertin kesto $t = 3{,}0\,\text{h}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** a) taso ilman tulppia; b) vertailuaika tulppien kanssa; c) annos prosentteina ja jääkö se vertailuannosta pienemmäksi etäisyydellä $16\,\text{m}$
**Periaate:** Pistemäisen lähteen taso laskee $6\,\text{dB}$ jokaisella etäisyyden kaksinkertaistumisella. Tulpat vähentävät korvaan pääsevää tasoa vaimennuksensa verran. Vertailuaika saadaan säännöstä, jossa jokainen $3\,\text{dB}$ toiminta-arvon yli puolittaa ajan. Annos on kuunteluajan ja vertailuajan suhde.
**Kaava:** $L_2 = L_1 - k \cdot 6\,\text{dB}$, missä $2^{\,k} = \dfrac{r_2}{r_1}$; $L = L_2 - \Delta L$; $t_\text{v} = \dfrac{t_0}{2^{\,n}}$, missä $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Muunnokset:** Ei tarvita. Suhde on $r_2 : r_1 = 8{,}0\,\text{m} : 2{,}0\,\text{m} = 4$, joten $k = 2$.
**Sijoitus:**
Kohta a: $L_2 = 112\,\text{dB} - 2 \cdot 6\,\text{dB} = 100\,\text{dB}$.
Kohta b: tulppien kanssa taso on $L = 100\,\text{dB} - 8\,\text{dB} = 92\,\text{dB}$.
$$\begin{aligned}
n &= \frac{92\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} \\
&= 2{,}33 \\
t_\text{v} &= \frac{8\,\text{h}}{2^{\,2{,}33}} \\
&= 1{,}59\,\text{h}
\end{aligned}$$
Kohta c: annos on $\dfrac{3{,}0\,\text{h}}{1{,}59\,\text{h}} = 1{,}89$ eli $190\,\%$. Etäisyydellä $16\,\text{m}$ taso on $100\,\text{dB} - 6\,\text{dB} = 94\,\text{dB}$. Tulpat korvissa taso on $86\,\text{dB}$. Silloin $n = \dfrac{1}{3}$ ja $t_\text{v} = \dfrac{8\,\text{h}}{2^{1/3}} = 6{,}35\,\text{h}$. Annos on $\dfrac{3{,}0\,\text{h}}{6{,}35\,\text{h}} = 0{,}47$ eli $47\,\%$.
**Vastaus:** a) $100\,\text{dB}$. b) $1{,}6\,\text{h}$, kaksi merkitsevää numeroa kuten vaimennuksessa ja kestossa. c) Paikallaan etäisyydellä $8{,}0\,\text{m}$ annos on $190\,\%$ vertailuannoksesta. Jos kuulija pitää tulpat korvissa myös etäisyydellä $16\,\text{m}$, annos putoaa noin $47\,\%$:iin. Se jää siis vertailuannosta pienemmäksi. Kuulo ei silti ole varmasti turvassa, mutta rasitus pienenee selvästi.
**Järkevyys:** Ilman tulppia vertailuaika olisi vain $8\,\text{h} : 2^5 = 0{,}25\,\text{h}$. Vaimennus $8\,\text{dB}$ pidentää aikaa siis noin kuusinkertaiseksi: $1{,}59\,\text{h} : 0{,}25\,\text{h} = 6{,}3 \approx 2^{8/3} = 6{,}35$.

## fy5-16-L1-09
**Annettu:** kuvasta ruohonleikkurin taso $L = 90\,\text{dB}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** vertailuaika $t_\text{v}$ tunteina
**Periaate:** Melualtistus lasketaan energian keskiarvona. Jokainen $3\,\text{dB}$:n nousu kaksinkertaistaa intensiteetin. Sama annos täyttyy silloin puolessa ajassa.
**Kuvaajan lukeminen:** Asteikolla ruohonleikkurin merkki on kohdassa $90\,\text{dB}$. Se on punaisella alueella, jossa kuulo vaurioituu. Alue alkaa kohdasta $85\,\text{dB}$.
**Kaava:** $t_\text{v} = \dfrac{t_0}{2^{\,n}}$, missä $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Muunnokset:** Ei tarvita. Tasot ovat desibeleinä ja aika saadaan tunteina.
**Sijoitus:** $n = \dfrac{90\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = \dfrac{5}{3}$, $t_\text{v} = \dfrac{8\,\text{h}}{2^{5/3}} = \dfrac{8\,\text{h}}{3{,}175} = 2{,}52\,\text{h}$
**Vastaus:** $2{,}5\,\text{h}$. Taso luetaan kuvasta kokonaisena desibelinä ja sääntö on arvio. Kaksi merkitsevää numeroa riittää siksi.
**Järkevyys:** Taso $90\,\text{dB}$ on tasojen $88\,\text{dB}$ ($4\,\text{h}$) ja $91\,\text{dB}$ ($2\,\text{h}$) välissä, lähempänä jälkimmäistä. Tulos $2{,}5\,\text{h}$ on kahden ja neljän tunnin välissä.

## fy5-16-L2-09
**Annettu:** kuvasta rock-konsertin taso $L = 105\,\text{dB}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** vertailuaika $t_\text{v}$ minuutteina
**Periaate:** Annos riippuu tasosta ja ajasta. Jokainen $3\,\text{dB}$:n nousu puolittaa vertailuajan, koska melualtistus lasketaan energian keskiarvona.
**Kuvaajan lukeminen:** Rock-konsertin merkki on asteikolla kohdassa $105\,\text{dB}$. Se on alueella, jossa kuulo vaurioituu. Taso on $20\,\text{dB}$ korkeammalla kuin ylempi toiminta-arvo $85\,\text{dB}$.
**Kaava:** $t_\text{v} = \dfrac{t_0}{2^{\,n}}$, missä $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Muunnokset:** $t_0 = 8\,\text{h} = 8 \cdot 60\,\text{min} = 480\,\text{min}$.
**Sijoitus:** $n = \dfrac{105\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = \dfrac{20}{3}$, $t_\text{v} = \dfrac{480\,\text{min}}{2^{20/3}} = \dfrac{480\,\text{min}}{101{,}6} = 4{,}72\,\text{min}$
**Vastaus:** $4{,}7\,\text{min}$. Taso luetaan kuvasta kokonaisena desibelinä ja sääntö on arvio. Kaksi merkitsevää numeroa riittää siksi.
**Järkevyys:** Taso on $20\,\text{dB}$ vertailutason yläpuolella. Intensiteetti on silloin noin $100$-kertainen ja aika noin sadasosa: $480\,\text{min} : 100 = 4{,}8\,\text{min}$. Konsertti kestää tunteja, joten kuulonsuojaimet tarvitaan.
