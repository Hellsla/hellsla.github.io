## fy8-14-L1-01
**Annettu:** pehmytkudoksen paksuus $d = 6{,}8\,\text{cm}$, puoliintumispaksuus $d_{1/2} = 3{,}4\,\text{cm}$
**Kysytty:** läpi päässeen säteilyn osuus ${I : I_0}$ prosentteina
**Periaate:** Jokainen puoliintumispaksuuden paksuinen kerros päästää läpi puolet siihen tulevasta röntgensäteilystä. Syy on se, että jokaisella fotonilla on jokaisessa kerroksessa sama todennäköisyys vuorovaikuttaa aineen kanssa.
**Kaava:** $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, josta $\dfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$
**Muunnokset:** Niitä ei tarvita, koska paksuus ja puoliintumispaksuus ovat molemmat senttimetreinä. Lopuksi osuus muutetaan prosenteiksi kertomalla se luvulla $100\,\%$.
**Sijoitus:** $\dfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{6{,}8\,\text{cm} / 3{,}4\,\text{cm}} = \left(\tfrac{1}{2}\right)^{2} = 0{,}25 = 25\,\%$
**Vastaus:** $25\,\%$. Vastauksessa on kaksi merkitsevää numeroa, kuten paksuuksissa $6{,}8\,\text{cm}$ ja $3{,}4\,\text{cm}$.
**Järkevyys:** Kerroksessa on täsmälleen kaksi puoliintumispaksuutta. Ensimmäinen puolittaa säteilyn $50\,\%$:iin ja toinen $25\,\%$:iin. Säteily heikkenee mutta ei lopu kokonaan, kuten fotonisäteilylle kuuluu.

## fy8-14-L1-02
**Annettu:** alkuaktiivisuus $A_0 = 600\,\text{MBq}$, puoliintumisaika $T_{1/2} = 6{,}01\,\text{h}$, aika $t = 24{,}0\,\text{h}$
**Kysytty:** aktiivisuus $A$ hetkellä $t$ megabecquereleinä
**Periaate:** Aktiivisuus on verrannollinen hajoamattomien ytimien määrään. Se pienenee siis hajoamislain mukaan: jokainen puoliintumisaika puolittaa sen. Tehtävässä oletetaan, ettei ainetta poistu elimistöstä. Vain hajoaminen pienentää siis aktiivisuutta.
**Kaava:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Muunnokset:** Niitä ei tarvita, koska aika ja puoliintumisaika ovat molemmat tunteina.
**Sijoitus:** $A = 600\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{24{,}0\,\text{h} / 6{,}01\,\text{h}} = 600\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{3{,}9933} = 600\,\text{MBq} \cdot 0{,}062789 = 37{,}67\,\text{MBq}$
**Vastaus:** $38\,\text{MBq}$. Vastauksessa on kaksi merkitsevää numeroa, koska aktiivisuus $600\,\text{MBq}$ on annettu kahden tai kolmen merkitsevän numeron tarkkuudella.
**Järkevyys:** Vuorokaudessa kuluu lähes tasan neljä puoliintumisaikaa, ja $600\,\text{MBq} : 16 = 37{,}5\,\text{MBq}$. Todellisuudessa aktiivisuus on vielä pienempi, koska osa merkkiaineesta poistuu virtsan mukana.

## fy8-14-L1-03
**Annettu:** ruiskutettu aktiivisuus $A = 300\,\text{MBq}$, annos megabecquerelia kohti $0{,}019\,\tfrac{\text{mSv}}{\text{MBq}}$
**Kysytty:** potilaan efektiivinen annos $H_\text{E}$ millisieverteinä
**Periaate:** Jokainen ruiskutettu megabecquerel hajoaa elimistössä samalla tavalla ja antaa saman annoksen. Efektiivinen annos on siis suoraan verrannollinen ruiskutettuun aktiivisuuteen.
**Kaava:** $H_\text{E} = 0{,}019\,\tfrac{\text{mSv}}{\text{MBq}} \cdot A$
**Muunnokset:** Niitä ei tarvita. Aktiivisuus on megabecquereleinä, ja kertoimen yksikkö on millisievert megabecquerelia kohti.
**Sijoitus:** $H_\text{E} = 0{,}019\,\tfrac{\text{mSv}}{\text{MBq}} \cdot 300\,\text{MBq} = 5{,}7\,\text{mSv}$
**Vastaus:** $5{,}7\,\text{mSv}$. Vastauksessa on kaksi merkitsevää numeroa, kuten kertoimessa $0{,}019\,\tfrac{\text{mSv}}{\text{MBq}}$.
**Järkevyys:** Arvio: $0{,}02 \cdot 300 = 6$. Annos on samaa suuruusluokkaa kuin luonnon säteilyn keskimääräinen vuosiannos Suomessa, $5{,}1\,\text{mSv}$. Se sopii luvun annostaulukon arvoon, noin $6\,\text{mSv}$.

## fy8-14-L1-04
**Annettu:** kasvaimen massa $m = 50\,\text{g}$, absorboitunut annos $D = 2{,}0\,\text{Gy}$
**Kysytty:** kasvaimen absorboima energia $E$ jouleina
**Periaate:** Absorboitunut annos on kudoksen absorboima energia massaa kohti (luku *Säteilyannos ja säteilyturvallisuus Suomessa*). Energia on siis annos kertaa massa.
**Kaava:** $D = \dfrac{E}{m}$, josta $E = D m$
**Muunnokset:** Yksikkö $1\,\text{Gy} = 1\,\tfrac{\text{J}}{\text{kg}}$. Massa muutetaan kilogrammoiksi: $m = 50\,\text{g} = 50 \cdot 0{,}001\,\text{kg} = 0{,}050\,\text{kg}$.
**Sijoitus:** $E = 2{,}0\,\tfrac{\text{J}}{\text{kg}} \cdot 0{,}050\,\text{kg} = 0{,}10\,\text{J}$
**Vastaus:** $0{,}10\,\text{J}$. Vastauksessa on kaksi merkitsevää numeroa, kuten annoksessa $2{,}0\,\text{Gy}$ ja massassa $50\,\text{g}$.
**Järkevyys:** Energia on hyvin pieni. Se lämmittäisi kasvainta vain noin $0{,}0005\,\text{K}$. Vaikutus ei perustu lämpenemiseen. Energia tulee ionisaatioina, jotka rikkovat DNA:ta.

## fy8-14-L1-05
**Annettu:** alkuaktiivisuus $A_0 = 37\,\text{kBq}$, amerikium-241:n puoliintumisaika $T_{1/2} = 432\,\text{a}$, aika $t = 100\,\text{a}$
**Kysytty:** aktiivisuus $A$ kilobecquereleinä
**Periaate:** Aktiivisuus on verrannollinen hajoamattomien ytimien määrään. Se pienenee siksi hajoamislain mukaan. Savuilmaisimen lähde on suljettu, joten ainetta ei poistu muuten kuin hajoamalla.
**Kaava:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Muunnokset:** Niitä ei tarvita, koska aika ja puoliintumisaika ovat molemmat vuosina.
**Sijoitus:** $A = 37\,\text{kBq} \cdot \left(\tfrac{1}{2}\right)^{100\,\text{a} / 432\,\text{a}} = 37\,\text{kBq} \cdot \left(\tfrac{1}{2}\right)^{0{,}23148} = 37\,\text{kBq} \cdot 0{,}85176 = 31{,}52\,\text{kBq}$
**Vastaus:** $32\,\text{kBq}$. Vastauksessa on kaksi merkitsevää numeroa, kuten aktiivisuudessa $37\,\text{kBq}$.
**Järkevyys:** Sata vuotta on alle neljäsosa puoliintumisajasta. Aktiivisuus ei ehdi puolittua, vaan se pienenee selvästi alle $50\,\%$: se pieneni noin $15\,\%$. Siksi savuilmaisimen lähde toimii koko laitteen käyttöiän.

## fy8-14-L2-01
**Annettu:** elävän puun hiilen aktiivisuus $A_0 = 0{,}23\,\text{Bq}$ grammaa kohti, löydön aktiivisuus $A = 0{,}029\,\text{Bq}$ grammaa kohti, hiili-14:n puoliintumisaika $T_{1/2} = 5700\,\text{a}$
**Kysytty:** puuhiilen ikä $t$ vuosina
**Periaate:** Elävä puu pitää hiili-14:n osuuden hiilestään samana kuin ilmakehässä. Kun puu kuolee, uutta hiili-14:ää ei tule, ja aktiivisuus grammaa kohti pienenee hajoamislain mukaan. Aika on yhtälössä eksponentissa eli potenssin kohdalla. Se ratkaistaan logaritmilla.
**Kaava:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, josta $\dfrac{A_0}{A} = 2^{t/T_{1/2}}$. Otetaan molemmilta puolilta luonnollinen logaritmi ja käytetään sääntöä $\ln 2^{x} = x \ln 2$: $\ln \dfrac{A_0}{A} = \dfrac{t}{T_{1/2}} \cdot \ln 2$, josta $t = T_{1/2} \cdot \dfrac{\ln (A_0 : A)}{\ln 2}$
**Muunnokset:** Niitä ei tarvita. Aktiivisuudet ovat samassa yksikössä, joten niiden suhde on pelkkä luku. Ikä saadaan vuosina, kuten puoliintumisaika.
**Sijoitus:** $t = 5700\,\text{a} \cdot \dfrac{\ln (0{,}23 : 0{,}029)}{\ln 2} = 5700\,\text{a} \cdot \dfrac{\ln 7{,}931}{0{,}69315} = 5700\,\text{a} \cdot \dfrac{2{,}0708}{0{,}69315} = 5700\,\text{a} \cdot 2{,}9875 = 17\,029\,\text{a}$
**Vastaus:** $1{,}7 \cdot 10^{4}\,\text{a}$ eli noin $17\,000$ vuotta. Vastauksessa on kaksi merkitsevää numeroa, kuten aktiivisuuksissa $0{,}23\,\text{Bq}$ ja $0{,}029\,\text{Bq}$.
**Järkevyys:** Aktiivisuus on pienentynyt noin kahdeksasosaan, ja $\left(\tfrac{1}{2}\right)^3 = \tfrac{1}{8}$. Aikaa on siis kulunut lähes kolme puoliintumisaikaa: $3 \cdot 5700\,\text{a} = 17\,100\,\text{a}$. Ikä on alle radiohiiliajoituksen rajan, joka on noin $50\,000$ vuotta.

## fy8-14-L2-02
**Annettu:** pulssitaajuus ilman nauhaa $I_0 = 1200\,\tfrac{1}{\text{s}}$, nauhan kanssa $I = 900\,\tfrac{1}{\text{s}}$ (taustasäteily vähennetty), teräksen puoliintumispaksuus $d_{1/2} = 0{,}73\,\text{mm}$
**Kysytty:** nauhan paksuus $d$ millimetreinä
**Periaate:** Fotonisäteilyn intensiteetti vaimenee teräksessä puoliintumispaksuuden mukaan. Ilmaisimen nettopulssitaajuus on verrannollinen siihen osuvan säteilyn intensiteettiin. Pulssitaajuuksien suhde on siis sama kuin intensiteettien suhde.
**Kaava:** $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, josta $\dfrac{I_0}{I} = 2^{d/d_{1/2}}$. Otetaan molemmilta puolilta luonnollinen logaritmi ja käytetään sääntöä $\ln 2^{x} = x \ln 2$: $\ln \dfrac{I_0}{I} = \dfrac{d}{d_{1/2}} \cdot \ln 2$, josta $d = d_{1/2} \cdot \dfrac{\ln (I_0 : I)}{\ln 2}$
**Muunnokset:** Niitä ei tarvita. Pulssitaajuudet ovat samassa yksikössä, ja paksuus saadaan millimetreinä, kuten puoliintumispaksuus.
**Sijoitus:** $d = 0{,}73\,\text{mm} \cdot \dfrac{\ln (1200 : 900)}{\ln 2} = 0{,}73\,\text{mm} \cdot \dfrac{0{,}28768}{0{,}69315} = 0{,}73\,\text{mm} \cdot 0{,}41504 = 0{,}3030\,\text{mm}$
**Vastaus:** $0{,}30\,\text{mm}$. Vastauksessa on kaksi merkitsevää numeroa, kuten puoliintumispaksuudessa $0{,}73\,\text{mm}$.
**Järkevyys:** Nauha päästää läpi $900 : 1200 = 75\,\%$. Se on enemmän kuin puolet, joten nauhan on oltava ohuempi kuin yksi puoliintumispaksuus, $0{,}73\,\text{mm}$. Jos nauha paksunee, pulssitaajuus pienenee, ja mittari ohjaa valssia ohentamaan nauhaa.

## fy8-14-L2-03
**Annettu:** TT-tutkimuksen annos $H = 8{,}0\,\text{mSv}$, luonnon säteilyn annos $5{,}1\,\text{mSv}$ vuodessa, vuodessa $365$ vuorokautta
**Kysytty:** aika $t$ vuorokausina, jona luonnon säteily antaa saman annoksen
**Periaate:** Luonnon säteilyn annos kertyy vuoden mittaan keskimäärin tasaisesti. Annos on siis suoraan verrannollinen aikaan: annos on annosnopeus kertaa aika.
**Kaava:** $H = \dot{H} t$, josta $t = \dfrac{H}{\dot{H}}$
**Muunnokset:** Annosnopeus muutetaan vuorokautta kohti sijoittamalla $1\,\text{a} = 365\,\text{d}$: $\dot{H} = \tfrac{5{,}1\,\text{mSv}}{1\,\text{a}} = \tfrac{5{,}1\,\text{mSv}}{365\,\text{d}}$
**Sijoitus:** $t = \dfrac{8{,}0\,\text{mSv}}{5{,}1\,\text{mSv} : 365\,\text{d}} = \dfrac{8{,}0}{5{,}1} \cdot 365\,\text{d} = 1{,}5686 \cdot 365\,\text{d} = 572{,}5\,\text{d}$
**Vastaus:** noin $570\,\text{d}$. Vastauksessa on kaksi merkitsevää numeroa, kuten annoksissa $8{,}0\,\text{mSv}$ ja $5{,}1\,\text{mSv}$.
**Järkevyys:** TT-tutkimuksen annos on hieman suurempi kuin luonnon vuosiannos. Ajan pitää siis olla vähän yli vuoden, ja $572\,\text{d}$ on noin puolitoista vuotta. Annos on merkittävä, ja siksi TT-tutkimuksen on oltava oikeutettu.

## fy8-14-L2-04
**Annettu:** annosnopeus $\dot{H}_1 = 30\,\mu\text{Sv/h}$ etäisyydellä $r_1 = 1{,}0\,\text{m}$, hoitajan etäisyys $r_2 = 0{,}50\,\text{m}$, aika $t = 5{,}0\,\text{min}$
**Kysytty:** hoitajan annos $H$ mikrosieverteinä
**Periaate:** Potilasta pidetään pistemäisenä lähteenä. Annosnopeus on silloin kääntäen verrannollinen etäisyyden neliöön (luku *Säteilyannos ja säteilyturvallisuus Suomessa*). Annosnopeus pysyy tämän ajan vakiona, joten annos on annosnopeus kertaa aika.
**Kaava:** $\dot{H}_2 = \dot{H}_1 \left(\tfrac{r_1}{r_2}\right)^2$ ja $H = \dot{H}_2 t$, joten $H = \dot{H}_1 \left(\dfrac{r_1}{r_2}\right)^2 t$
**Muunnokset:** Aika muutetaan tunneiksi: $t = 5{,}0\,\text{min} = 5{,}0 \cdot \tfrac{1}{60}\,\text{h} = 0{,}08333\,\text{h}$
**Sijoitus:** $H = 30\,\mu\text{Sv/h} \cdot \left(\dfrac{1{,}0\,\text{m}}{0{,}50\,\text{m}}\right)^2 \cdot 0{,}08333\,\text{h} = 30\,\mu\text{Sv/h} \cdot 4 \cdot 0{,}08333\,\text{h} = 120\,\mu\text{Sv/h} \cdot 0{,}08333\,\text{h} = 10\,\mu\text{Sv}$
**Vastaus:** $10\,\mu\text{Sv}$. Vastauksessa on kaksi merkitsevää numeroa, kuten annosnopeudessa $30\,\mu\text{Sv/h}$ ja ajassa $5{,}0\,\text{min}$.
**Järkevyys:** Puolet lyhyempi etäisyys nelinkertaistaa annosnopeuden arvoon $120\,\mu\text{Sv/h}$. Viisi minuuttia on kahdestoistaosa tunnista, ja $120 : 12 = 10$. Metrin päässä hoitaja saisi samassa ajassa vain $2{,}5\,\mu\text{Sv}$. Etäisyys on siis tehokas suoja.

## fy8-14-L3-01
**Annettu:** $30$ hoitokertaa, kasvaimen annos kerralla $2{,}0\,\text{Gy}$, $5$ keilaa, joista kukin antaa kasvaimeen saman osan, tulokohdan annos $1{,}3$-kertainen keilan kasvainannokseen verrattuna
**Kysytty:** terveen kudoksen kokonaisannos $D$ yhden keilan tulokohdassa grayna
**Periaate:** Keilojen annokset summautuvat vain siellä, missä keilat leikkaavat, eli kasvaimessa. Tulokohdan kautta kulkee vain yksi keila. Tulokohta saa siis vain tämän keilan annoksen, joka on $1{,}3$-kertainen keilan kasvaimeen antamaan annokseen verrattuna. Hoitokertojen annokset lasketaan yhteen.
**Kaava:** yhden keilan kasvainannos on $\tfrac{2{,}0\,\text{Gy}}{5}$, joten $D = 30 \cdot 1{,}3 \cdot \dfrac{D_\text{kerta}}{5}$, missä $D_\text{kerta} = 2{,}0\,\text{Gy}$
**Muunnokset:** Niitä ei tarvita, koska kaikki annokset ovat grayna.
**Sijoitus:** $D = 30 \cdot 1{,}3 \cdot \dfrac{2{,}0\,\text{Gy}}{5} = 30 \cdot 1{,}3 \cdot 0{,}40\,\text{Gy} = 30 \cdot 0{,}52\,\text{Gy} = 15{,}6\,\text{Gy}$
**Vastaus:** noin $16\,\text{Gy}$. Vastauksessa on kaksi merkitsevää numeroa, kuten kertoimessa $1{,}3$ ja annoksessa $2{,}0\,\text{Gy}$.
**Järkevyys:** Kasvain saa yhteensä $30 \cdot 2{,}0\,\text{Gy} = 60\,\text{Gy}$. Terve kudos tulokohdassa saa noin neljäsosan siitä. Yhdellä keilalla tulokohta saisi $1{,}3 \cdot 60\,\text{Gy} = 78\,\text{Gy}$, enemmän kuin kasvain. Useat suunnat ovat siis välttämättömiä.

## fy8-14-L3-02
**Annettu:** pehmytkudoksen puoliintumispaksuus $d_{1/2}^\text{kudos} = 1{,}8\,\text{cm}$, kalkkeuman $d_{1/2}^\text{luu} = 0{,}27\,\text{cm}$, korvautuneen kerroksen paksuus $d = 1{,}0\,\text{cm}$
**Kysytty:** intensiteettien suhde ${I_\text{A} : I_\text{B}}$, kun säde A kulkee pelkän pehmytkudoksen ja säde B kalkkeuman läpi
**Periaate:** Säteet ovat yhtä pitkiä ja kulkevat muuten saman pehmytkudoksen läpi. Muiden kerrosten osuudet ovat siis molemmille samat, ja ne supistuvat suhteesta pois. Ero tulee vain $1{,}0\,\text{cm}$:n kerroksesta. Säteellä A se on pehmytkudosta ja säteellä B kalkkeumaa. Kerrosten läpi päässeet osuudet kerrotaan.
**Kaava:** $\dfrac{I_\text{A}}{I_\text{B}} = \dfrac{\left(\tfrac{1}{2}\right)^{d/d_{1/2}^\text{kudos}}}{\left(\tfrac{1}{2}\right)^{d/d_{1/2}^\text{luu}}} = 2^{d/d_{1/2}^\text{luu} - d/d_{1/2}^\text{kudos}}$
**Muunnokset:** Niitä ei tarvita, koska kaikki paksuudet ovat senttimetreinä.
**Sijoitus:** $\dfrac{I_\text{A}}{I_\text{B}} = 2^{1{,}0\,\text{cm} / 0{,}27\,\text{cm} - 1{,}0\,\text{cm} / 1{,}8\,\text{cm}} = 2^{3{,}7037 - 0{,}5556} = 2^{3{,}1481} = 8{,}87$
**Vastaus:** noin $8{,}9$. Vastauksessa on kaksi merkitsevää numeroa, kuten puoliintumispaksuuksissa $1{,}8\,\text{cm}$ ja $0{,}27\,\text{cm}$.
**Järkevyys:** Kalkkeumassa on noin $3{,}7$ puoliintumispaksuutta. Pehmytkudoksessa olisi ollut noin $0{,}56$. Säde B puolittuu siis noin kolme kertaa useammin, ja $2^3 = 8$. Pienellä energialla kontrasti on suuri. Siksi pienetkin kalkkeumat näkyvät mammografiassa.

## fy8-14-L3-03
**Annettu:** lyijyn puoliintumispaksuus fotoneille, joiden energia on $511\,\text{keV}$, $d_{1/2} = 3{,}9\,\text{mm}$, läpi pääsevä osuus ${I : I_0} = 5{,}0\,\% = 0{,}050$
**Kysytty:** lyijysuojan paksuus $d$ millimetreinä
**Periaate:** Jokainen puoliintumispaksuus puolittaa fotonisäteilyn intensiteetin. Vaimeneminen noudattaa siis yhtälöä $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$. Paksuus on eksponentissa, joten se ratkaistaan logaritmilla.
**Kaava:** $\dfrac{I_0}{I} = 2^{d/d_{1/2}}$. Otetaan molemmilta puolilta luonnollinen logaritmi ja käytetään sääntöä $\ln 2^{x} = x \ln 2$: $\ln \dfrac{I_0}{I} = \dfrac{d}{d_{1/2}} \cdot \ln 2$, josta $d = d_{1/2} \cdot \dfrac{\ln (I_0 : I)}{\ln 2}$
**Muunnokset:** Osuus muutetaan desimaaliluvuksi: $5{,}0\,\% = 0{,}050$, joten ${I_0 : I} = {1 : 0{,}050} = 20$. Paksuus saadaan millimetreinä, kuten puoliintumispaksuus.
**Sijoitus:** $d = 3{,}9\,\text{mm} \cdot \dfrac{\ln 20}{\ln 2} = 3{,}9\,\text{mm} \cdot \dfrac{2{,}9957}{0{,}69315} = 3{,}9\,\text{mm} \cdot 4{,}3219 = 16{,}86\,\text{mm}$
**Vastaus:** noin $17\,\text{mm}$. Vastauksessa on kaksi merkitsevää numeroa, kuten puoliintumispaksuudessa $3{,}9\,\text{mm}$ ja osuudessa $5{,}0\,\%$.
**Järkevyys:** Neljä puoliintumispaksuutta päästäisi läpi $\tfrac{1}{16} \approx 6{,}3\,\%$ ja viisi $\tfrac{1}{32} \approx 3{,}1\,\%$. Paksuuden on siis oltava lukujen $4 \cdot 3{,}9\,\text{mm} = 15{,}6\,\text{mm}$ ja $5 \cdot 3{,}9\,\text{mm} = 19{,}5\,\text{mm}$ välissä. Teknetium-$99\text{m}$:n fotoneille, joiden energia on $140\,\text{keV}$, sama vaimennus vaatisi vain noin $1\,\text{mm}$ lyijyä, koska niiden puoliintumispaksuus on noin $0{,}26\,\text{mm}$.

## fy8-14-L1-06
**Kysytty:** miksi positronia lähettävä merkkiaine sopii lähteen paikantamiseen kehon ulkopuolelta.
**Periaate:** Positroni on varattu hiukkanen. Se pysähtyy kudoksessa jo muutaman millimetrin matkalla ja annihiloituu elektronin kanssa. Annihilaatiossa hiukkaset häviävät ja niistä syntyy säteilyä. Alussa liikemäärä on lähes nolla. Siksi syntyy kaksi fotonia, jotka lähtevät vastakkaisiin suuntiin. Niillä on sama energia $E_\gamma = m_e c^2 = 511\,\text{keV}$.
**Mallivastaus:** Positroni annihiloituu elektronin kanssa kahdeksi vastakkaiseksi fotoniksi. Fotonien yhdistävä jana kulkee lähteen kautta. Ilmaisin havaitsee fotonit yhtä aikaa, ja lähde on tällä janalla. Kun piirretään monta janaa, niiden leikkauskohta näyttää merkkiaineen paikan. Ilmaisin ei havaitse positronia itseään. Positroni pysähtyy kudokseen, koska se on sähkövarauksellinen eikä kulje suoraan ulos. Fotonien energia on aina $511\,\text{keV}$. Energia ei kerro syvyyttä vaan sen, että kyseessä on annihilaatio.

## fy8-14-L1-07
**Kysytty:** onko annoksen pienentäminen kohinaisessa kuvassa säteilysuojelun kannalta järkevää.
**Periaate:** Säteilyn käytön periaatteita ovat oikeutus, optimointi ja annosrajat. Optimointi ei tarkoita mahdollisimman pientä annosta hinnalla millä hyvänsä. Se tarkoittaa pienintä annosta, jolla kuva vastaa kysymykseen.
**Mallivastaus:** Ehdotus ei ole järkevä. Kun annos on liian pieni, kuva jää kohinaiseksi. Siitä ei näe pientä keuhkomuutosta, jota etsittiin. Tutkimus joudutaan tekemään uudelleen, ja potilas saa kaksi annosta yhden sijasta. Siksi annosta ei pienennetä enempää. Kuvausasetukset valitaan niin, että kuva on juuri riittävän selvä.

## fy8-14-L1-08
**Annettu:** kiihdytysjännite $U = 80\,\text{kV}$, alkeisvaraus $e = 1{,}602 \cdot 10^{-19}\,\text{C}$
**Kysytty:** röntgenfotonin suurin mahdollinen energia $E_\text{max}$ jouleina
**Periaate:** Jännite $U$ antaa elektronille liike-energian $eU$. Fotoni saa suurimman energian silloin, kun elektroni antaa sille koko liike-energiansa. Näin käy, kun elektroni jarruttaa anodissa.
**Kaava:** $E_\text{max} = eU$
**Muunnokset:** $U = 80\,\text{kV} = 80 \cdot 1000\,\text{V} = 80\,000\,\text{V}$, ja $1\,\text{C} \cdot 1\,\text{V} = 1\,\text{J}$.
**Sijoitus:** $E_\text{max} = 1{,}602 \cdot 10^{-19}\,\text{C} \cdot 80\,000\,\text{V} = 1{,}2816 \cdot 10^{-14}\,\text{J}$
**Vastaus:** $1{,}3 \cdot 10^{-14}\,\text{J}$. Vastauksessa on kaksi merkitsevää numeroa, kuten jännitteessä $80\,\text{kV}$.
**Järkevyys:** Elektronin energia on $80\,\text{keV}$, ja $80\,000 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 1{,}28 \cdot 10^{-14}\,\text{J}$. Kuvauksessa fotonien energia on kymmeniä kiloelektronivoltteja. Tulos on siis oikeaa suuruusluokkaa. Useimmat fotonit saavat tätä pienemmän energian, koska jarruttava elektroni antaa usein vain osan energiastaan.

## fy8-14-L2-05
**Annettu:** taulukosta hammaskuva $0{,}010\,\text{mSv}$ kolme kertaa, keuhkokuva $0{,}10\,\text{mSv}$ kaksi kertaa ja pään TT $2{,}0\,\text{mSv}$ kerran. Luonnon säteilyn vuosiannos on $H_\text{luonto} = 5{,}1\,\text{mSv}$ (STUK-A263, 2020).
**Kysytty:** kokonaisannoksen osuus $p$ luonnon säteilyn vuosiannoksesta prosentteina
**Periaate:** Efektiivisiä annoksia voi verrata suoraan ja laskea yhteen. Kokonaisannos on jokaisen tutkimuksen annos kertaa tutkimusten lukumäärä, ja nämä tulot lasketaan yhteen. Vertailu tehdään yhdellä jakolaskulla.
**Kaava:** $H = n_1 H_1 + n_2 H_2 + n_3 H_3$ ja $p = \dfrac{H}{H_\text{luonto}} \cdot 100\,\%$
**Muunnokset:** Niitä ei tarvita, koska kaikki annokset ovat millisieverteinä. Osuus muutetaan prosenteiksi kertomalla se luvulla $100\,\%$.
**Sijoitus:** $H = 3 \cdot 0{,}010\,\text{mSv} + 2 \cdot 0{,}10\,\text{mSv} + 1 \cdot 2{,}0\,\text{mSv} = 0{,}030\,\text{mSv} + 0{,}20\,\text{mSv} + 2{,}0\,\text{mSv} = 2{,}23\,\text{mSv}$
$p = \dfrac{2{,}23\,\text{mSv}}{5{,}1\,\text{mSv}} \cdot 100\,\% = 43{,}73\,\%$
**Vastaus:** $44\,\%$. Vastauksessa on kaksi merkitsevää numeroa, kuten luonnon säteilyn annoksessa $5{,}1\,\text{mSv}$.
**Järkevyys:** Pään TT:n annos $2{,}0\,\text{mSv}$ on lähes koko summa, ja $2{,}0 : 5{,}1 \approx 0{,}39$. Pienet kuvat lisäävät vain $0{,}23\,\text{mSv}$. Kokonaisuus on siis $(2{,}0 + 0{,}23) : 5{,}1 \approx 0{,}44$ eli noin $44\,\%$. Annos on alle puolet vuosiannoksesta, ja suurin osa siitä tulee yhdestä TT-tutkimuksesta.

## fy8-14-L2-06
**Annettu:** taulukosta aktiivisuus $A = 500$; $355$; $252$; $123$ ja $64\,\text{MBq}$ ajanhetkinä $t = 0{,}0$; $2{,}0$; $4{,}0$; $8{,}0$ ja $12{,}0\,\text{h}$. Hajoamisen puoliintumisaika on $T_{1/2} = 6{,}01\,\text{h}$.
**Kysytty:** a) aika, jossa aktiivisuus potilaassa puolittuu. b) Mitatun aktiivisuuden osuus $p$ pelkän hajoamisen antamasta aktiivisuudesta hetkellä $12{,}0\,\text{h}$ prosentteina.
**Periaate:** Aktiivisuus potilaassa pienenee kahdesta syystä. Ydin hajoaa, ja elimistö poistaa merkkiainetta, esimerkiksi virtsan mukana. Pelkän hajoamisen antama aktiivisuus noudattaa lakia $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$.
**Kaava:** a) puolittumisaika luetaan taulukosta. b) $A_\text{hajoaminen} = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$ ja $p = \dfrac{A_\text{mitattu}}{A_\text{hajoaminen}} \cdot 100\,\%$
**Muunnokset:** Niitä ei tarvita, koska aika ja puoliintumisaika ovat molemmat tunteina ja aktiivisuudet megabecquereleinä.
**Sijoitus:**
a) Aktiivisuus $500\,\text{MBq}$ puolittuu noin arvoon $250\,\text{MBq}$ ajassa $4{,}0\,\text{h}$ (taulukossa $252\,\text{MBq}$). Se puolittuu edelleen noin arvoon $125\,\text{MBq}$ seuraavassa $4{,}0\,\text{h}$:ssa (taulukossa $123\,\text{MBq}$ hetkellä $8{,}0\,\text{h}$). Puolittumisaika on siis noin $4{,}0\,\text{h}$.
b) $A_\text{hajoaminen} = 500\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{12{,}0\,\text{h} / 6{,}01\,\text{h}} = 500\,\text{MBq} \cdot 0{,}2506 = 125{,}3\,\text{MBq}$, joten $p = \dfrac{64\,\text{MBq}}{125{,}3\,\text{MBq}} \cdot 100\,\% = 51{,}1\,\%$
**Vastaus:** b) $51\,\%$. Vastauksessa on kaksi merkitsevää numeroa, kuten mitatussa aktiivisuudessa $64\,\text{MBq}$. Kohdassa a) puolittumisaika on noin $4{,}0\,\text{h}$. Se on lyhyempi kuin hajoamisen puoliintumisaika, koska hajoamisen lisäksi merkkiainetta poistuu elimistöstä.
**Järkevyys:** Kaksitoista tuntia on kaksi puoliintumisaikaa hajoamiselle. Pelkällä hajoamisella aktiivisuus olisi siis noin $500 : 4 = 125\,\text{MBq}$, ja mitattu $64\,\text{MBq}$ on noin puolet siitä. Kolme puolittumisaikaa $4{,}0\,\text{h}$ antaisi $500 : 8 = 62{,}5\,\text{MBq}$. Se sopii mitattuun arvoon.

## fy8-14-L2-07
**Annettu:** läpi päästettävä osuus ${I : I_0} = 1{,}0\,\% = 0{,}010$, lyijyn puoliintumispaksuus $511\,\text{keV}$:n fotoneille $d_{1/2} = 3{,}9\,\text{mm}$ ja $140\,\text{keV}$:n fotoneille $0{,}26\,\text{mm}$
**Kysytty:** oppilaan virhe ja lyijysuojan oikea paksuus $d$ millimetreinä
**Periaate:** Puoliintumispaksuus riippuu fotonien energiasta. Suojan on pysäytettävä $511\,\text{keV}$:n fotonit. Laskussa pitää siis käyttää niiden puoliintumispaksuutta $3{,}9\,\text{mm}$. Oppilas käytti $140\,\text{keV}$:n fotonien arvoa $0{,}26\,\text{mm}$, joten suoja olisi liian ohut. Oppilaan luku $n = 6{,}64$ on muuten oikein.
**Kaava:** $\left(\tfrac{1}{2}\right)^{n} = \dfrac{I}{I_0}$, josta $n = \dfrac{\ln (I_0 : I)}{\ln 2}$ ja $d = n \, d_{1/2}$
**Muunnokset:** $1{,}0\,\% = 0{,}010$, joten ${I_0 : I} = {1 : 0{,}010} = 100$. Paksuus saadaan millimetreinä, kuten puoliintumispaksuus.
**Sijoitus:** $n = \dfrac{\ln 100}{\ln 2} = \dfrac{4{,}6052}{0{,}69315} = 6{,}644$ ja $d = 6{,}644 \cdot 3{,}9\,\text{mm} = 25{,}91\,\text{mm}$
**Vastaus:** oikea paksuus on $26\,\text{mm}$. Vastauksessa on kaksi merkitsevää numeroa, kuten puoliintumispaksuudessa $3{,}9\,\text{mm}$. Oppilaan tulos $1{,}7\,\text{mm}$ on väärä, koska se perustuu energian $140\,\text{keV}$ arvoon.
**Järkevyys:** Seitsemän puoliintumispaksuutta päästäisi läpi $\left(\tfrac{1}{2}\right)^{7} = \tfrac{1}{128} \approx 0{,}78\,\%$ ja kuusi $\tfrac{1}{64} \approx 1{,}6\,\%$. Paksuuden on siis oltava lukujen $6 \cdot 3{,}9\,\text{mm} = 23{,}4\,\text{mm}$ ja $7 \cdot 3{,}9\,\text{mm} = 27{,}3\,\text{mm}$ välissä. Oppilaan $1{,}7\,\text{mm}$ on $511\,\text{keV}$:n fotoneille vain $1{,}7 : 3{,}9 \approx 0{,}44$ puoliintumispaksuutta. Läpi pääsisi silloin noin $74\,\%$ eikä $1{,}0\,\%$.

## fy8-14-L3-04
**Annettu:** taulukosta massa $m = 75\,\text{kg}$, vaadittu aktiivisuus kuvauksen alussa $a = 2{,}0\,\tfrac{\text{MBq}}{\text{kg}}$, odotusaika $t = 60\,\text{min}$, fluori-$18$:n puoliintumisaika $T_{1/2} = 110\,\text{min}$, annoskerroin $k = 0{,}019\,\tfrac{\text{mSv}}{\text{MBq}}$, TT-osan annos $H_\text{TT} = 6{,}0\,\text{mSv}$. Luonnon säteilyn vuosiannos on $5{,}1\,\text{mSv}$.
**Kysytty:** a) potilaan efektiivinen kokonaisannos $H$ millisieverteinä. b) Vertailu luonnon säteilyyn ja tutkimuksen oikeutus.
**Periaate:** Kuvaukseen tarvittava aktiivisuus $A_\text{kuv} = a m$ on oltava jäljellä odotusajan jälkeen. Odotusaikana aktiivisuus pienenee vain hajoamalla. Siksi ruiskutettava aktiivisuus $A_0$ on suurempi kuin $A_\text{kuv}$. Pienin sopiva arvo saadaan hajoamislaista. Annos riippuu ruiskutetusta aktiivisuudesta. PET-osan ja TT-osan annokset lasketaan yhteen.
**Kaava:** $A_\text{kuv} = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, josta $A_0 = \dfrac{a m}{\left(\tfrac{1}{2}\right)^{t/T_{1/2}}}$, ja $H = k A_0 + H_\text{TT}$
**Muunnokset:** Niitä ei tarvita, koska odotusaika ja puoliintumisaika ovat molemmat minuutteina. Annoskerroin on millisievertteinä megabecquerelia kohti.
**Sijoitus:** $A_\text{kuv} = 2{,}0\,\tfrac{\text{MBq}}{\text{kg}} \cdot 75\,\text{kg} = 150\,\text{MBq}$ ja $\left(\tfrac{1}{2}\right)^{60\,\text{min} / 110\,\text{min}} = \left(\tfrac{1}{2}\right)^{0{,}5455} = 0{,}6853$, joten $A_0 = \dfrac{150\,\text{MBq}}{0{,}6853} = 218{,}9\,\text{MBq}$. Tällöin $H = 0{,}019\,\tfrac{\text{mSv}}{\text{MBq}} \cdot 218{,}9\,\text{MBq} + 6{,}0\,\text{mSv} = 4{,}16\,\text{mSv} + 6{,}0\,\text{mSv} = 10{,}16\,\text{mSv}$
**Vastaus:** a) $10\,\text{mSv}$. Vastauksessa on kaksi merkitsevää numeroa, kuten massassa $75\,\text{kg}$ ja aktiivisuudessa $2{,}0\,\tfrac{\text{MBq}}{\text{kg}}$. b) Kokonaisannos on noin kaksi luonnon säteilyn vuosiannosta ($10{,}16 : 5{,}1 = 2{,}0$). Se on siis selvästi suurempi kuin vuosiannos. Tutkimus on oikeutettu, kun lääkäri arvioi kaksi asiaa. Tulos ratkaisee hoitoa koskevan kysymyksen, eikä pienemmän annoksen menetelmällä saada samaa tietoa. Silloin hyöty potilaalle on suurempi kuin säteilyn aiheuttama pieni lisäriski. Annos optimoidaan käyttämällä pienintä aktiivisuutta, jolla kuva onnistuu.
**Järkevyys:** Odotusaika $60\,\text{min}$ on hieman yli puolet puoliintumisajasta. Noin kolmannes aktiivisuudesta ehtii siis hajota: $150 : 0{,}69 \approx 217\,\text{MBq}$. Tämä vastaa tulosta $218{,}9\,\text{MBq}$. PET-osan annos $4{,}2\,\text{mSv}$ on samaa suuruusluokkaa kuin muiden PET-tutkimusten annokset, ja TT-osa lisää siihen vielä enemmän.

## fy8-14-L3-05
**Annettu:** taulukosta paksuudet $d = 0{,}0$; $5{,}0$; $10{,}0$; $15{,}0$ ja $20{,}0\,\text{mm}$ ja laskentataajuudet $R = 1006$; $689$; $468$; $327$ ja $221\,\tfrac{1}{\text{s}}$. Tuntemattoman levyn laskentataajuus on $R_x = 402\,\tfrac{1}{\text{s}}$.
**Kysytty:** a) laskentataajuuksien suhteet. b) Alumiinin puoliintumispaksuus $d_{1/2}$. c) Tuntemattoman levyn paksuus $d_x$ millimetreinä.
**Periaate:** Oletetaan, että säteily vaimenee puoliintumispaksuuden mukaan. Silloin jokainen yhtä paksu lisäkerros pienentää laskentataajuutta samalla kertoimella. Laskentataajuus on verrannollinen ilmaisimeen osuvan säteilyn intensiteettiin. Siksi $R = R_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$. Tuntematon paksuus ratkaistaan logaritmilla.
**Kuvaajan lukeminen:** Taulukosta luetaan kaikkien levyjen laskentataajuudet. Kohdassa a) lasketaan suhteet $689 : 1006 = 0{,}685$, $468 : 689 = 0{,}679$, $327 : 468 = 0{,}699$ ja $221 : 327 = 0{,}676$. Ne ovat lähes samat, noin $0{,}68$, vaikka mittauksessa on pientä satunnaisvaihtelua. Jokainen $5{,}0\,\text{mm}$ levyä pienentää siis laskentataajuuden samaan murto-osaan. Se sopii eksponentiaaliseen vaimenemiseen. Kohdassa b) lasketaan puoliintumispaksuus taulukon ensimmäisestä ja viimeisestä rivistä. Tarkistuksena voi sovittaa suoran $\ln R$:n ja $d$:n välille kaikkiin viiteen pisteeseen. Se antaa $d_{1/2} = 9{,}18\,\text{mm}$ ja $d_x = 12{,}1\,\text{mm}$ eli saman vastauksen.
**Kaava:** $\dfrac{R_0}{R} = 2^{d/d_{1/2}}$, josta $d = d_{1/2} \cdot \dfrac{\ln (R_0 : R)}{\ln 2}$. Kalibroinnista $d_{1/2} = \dfrac{d_{20} \ln 2}{\ln (R_0 : R_{20})}$ ja tuntemattomalle $d_x = d_{1/2} \cdot \dfrac{\ln (R_0 : R_x)}{\ln 2}$.
**Muunnokset:** Niitä ei tarvita, koska paksuudet ovat millimetreinä. Laskentataajuuksien suhde on paljas luku.
**Sijoitus:** b) $d_{1/2} = \dfrac{20{,}0\,\text{mm} \cdot 0{,}69315}{\ln (1006 : 221)} = \dfrac{13{,}863\,\text{mm}}{1{,}5157} = 9{,}147\,\text{mm}$. c) $d_x = 9{,}147\,\text{mm} \cdot \dfrac{\ln (1006 : 402)}{0{,}69315} = 9{,}147\,\text{mm} \cdot \dfrac{0{,}9174}{0{,}69315} = 9{,}147\,\text{mm} \cdot 1{,}3236 = 12{,}11\,\text{mm}$
**Vastaus:** c) $12\,\text{mm}$. Vastauksessa on kaksi merkitsevää numeroa. Puoliintumispaksuus $d_{1/2}$ on määritetty kalibroinnista, ja mittausten satunnaisvaihtelu rajoittaa sen tarkkuuden noin kahteen numeroon (suhteet $0{,}68 \pm 0{,}01$). Kohdassa b) alumiinin puoliintumispaksuus on $9{,}1\,\text{mm}$.
**Järkevyys:** Laskentataajuus $402\,\tfrac{1}{\text{s}}$ on taulukon arvojen $468$ ($10{,}0\,\text{mm}$) ja $327$ ($15{,}0\,\text{mm}$) välissä. Paksuuden on siis oltava $10{,}0\,\text{mm}$:n ja $15{,}0\,\text{mm}$:n välissä, ja $12{,}1\,\text{mm}$ on. Tarkistus: $12{,}1\,\text{mm}$ on $12{,}1 : 9{,}147 = 1{,}32$ puoliintumispaksuutta, ja $1006 \cdot \left(\tfrac{1}{2}\right)^{1{,}32} = 403$, kuten mitattu $402$. Tulos pätee vain kalibroidulla välillä. Taustasäteily on vähennettävä, koska se ei vaimene levyssä.

## fy8-14-L1-09
**Kysytty:** lauseke lähtöaktiivisuudelle $A_0$, kun ruiskutushetkellä tarvitaan aktiivisuus $A$ ja kuljetus kestää ajan $t$.
**Periaate:** Aktiivisuus pienenee hajoamislain mukaan, $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$. Jokainen puoliintumisaika puolittaa jäljellä olevan aktiivisuuden. Kuljetuksen aikana puoliintumisia on $\tfrac{t}{T_{1/2}}$. Ratkaistaan laki lähtöaktiivisuudelle $A_0$.
**Mallivastaus:** Jaetaan hajoamislain molemmat puolet tekijällä $\left(\tfrac{1}{2}\right)^{t/T_{1/2}}$:

$$A_0 = \frac{A}{\left(\tfrac{1}{2}\right)^{t/T_{1/2}}}$$

Koska $\dfrac{1}{\left(\tfrac{1}{2}\right)^{n}} = 2^{n}$, saadaan

$$A_0 = A \cdot 2^{t/T_{1/2}}$$

Oikea lauseke on siis $A_0 = A \cdot 2^{t/T_{1/2}}$. Tarkistus: fluori-$18$:n puoliintumisaika on noin $110\,\text{min}$. Esimerkiksi kuljetus kestää $330\,\text{min}$. Silloin aktiivisuus puolittuu kolme kertaa, ja lähtiessä tarvitaan $2^{3} = 8$ kertaa aktiivisuus $A$. Tasaisen muutoksen lauseke antaisi vain $\tfrac{2 \cdot 330}{110} = 6$ kertaa $A$. Väärät lausekkeet: $A \cdot \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$ on pienempi kuin $A$, joten siinä hajoamislakia on käytetty väärään suuntaan. Lausekkeessa $A \cdot 2^{T_{1/2}/t}$ eksponentti on käännetty ylösalaisin, ja lauseke pienenisi kuljetusajan kasvaessa. Lauseke $A \cdot \tfrac{2t}{T_{1/2}}$ olettaa aktiivisuuden muuttuvan tasaisesti, ja ajalla $t = 0$ se antaisi nollan.
