## fy8-14-L1-01
**Annettu:** pehmytkudoksen paksuus $d = 6{,}8\,\text{cm}$, puoliintumispaksuus $d_{1/2} = 3{,}4\,\text{cm}$
**Kysytty:** läpi päässeen säteilyn osuus ${I : I_0}$ prosentteina
**Periaate:** Jokainen puoliintumispaksuuden kerros päästää läpi puolet siihen tulevasta röntgensäteilystä, koska jokaisella fotonilla on jokaisessa kerroksessa sama todennäköisyys vuorovaikuttaa.
**Kaava:** $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, josta $\dfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$
**Muunnokset:** Ei tarvita: paksuus ja puoliintumispaksuus ovat molemmat senttimetreinä. Lopuksi osuus muutetaan prosenteiksi kertomalla $100\,\%$:lla.
**Sijoitus:** $\dfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{6{,}8\,\text{cm} / 3{,}4\,\text{cm}} = \left(\tfrac{1}{2}\right)^{2} = 0{,}25 = 25\,\%$
**Vastaus:** $25\,\%$, kaksi merkitsevää numeroa kuten paksuuksissa $6{,}8\,\text{cm}$ ja $3{,}4\,\text{cm}$.
**Järkevyys:** Kerroksessa on täsmälleen kaksi puoliintumispaksuutta: ensimmäinen puolittaa säteilyn $50\,\%$:iin ja toinen $25\,\%$:iin. Säteily heikkenee mutta ei lopu, kuten fotonisäteilylle kuuluu.

## fy8-14-L1-02
**Annettu:** alkuaktiivisuus $A_0 = 600\,\text{MBq}$, puoliintumisaika $T_{1/2} = 6{,}01\,\text{h}$, aika $t = 24{,}0\,\text{h}$
**Kysytty:** aktiivisuus $A$ hetkellä $t$ megabecquereleinä
**Periaate:** Aktiivisuus on verrannollinen hajoamattomien ytimien määrään, joten se pienenee hajoamislain mukaan: jokainen puoliintumisaika puolittaa sen. Tehtävä olettaa, ettei ainetta poistu elimistöstä, joten vain hajoaminen pienentää aktiivisuutta.
**Kaava:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Muunnokset:** Ei tarvita: aika ja puoliintumisaika ovat molemmat tunteina.
**Sijoitus:** $A = 600\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{24{,}0\,\text{h} / 6{,}01\,\text{h}} = 600\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{3{,}9933} = 600\,\text{MBq} \cdot 0{,}062789 = 37{,}67\,\text{MBq}$
**Vastaus:** $38\,\text{MBq}$, kaksi merkitsevää numeroa, koska aktiivisuus $600\,\text{MBq}$ on annettu kahden tai kolmen merkitsevän numeron tarkkuudella.
**Järkevyys:** Vuorokaudessa kuluu lähes tasan neljä puoliintumisaikaa, ja $600\,\text{MBq} : 16 = 37{,}5\,\text{MBq}$. Todellisuudessa aktiivisuus on vielä pienempi, koska osa merkkiaineesta poistuu virtsan mukana.

## fy8-14-L1-03
**Annettu:** ruiskutettu aktiivisuus $A = 300\,\text{MBq}$, annos megabecquerelia kohti $0{,}019\,\tfrac{\text{mSv}}{\text{MBq}}$
**Kysytty:** potilaan efektiivinen annos $H_\text{E}$ millisieverteinä
**Periaate:** Jokainen ruiskutettu megabecquerel hajoaa elimistössä samalla tavalla ja antaa saman annoksen, joten efektiivinen annos on suoraan verrannollinen ruiskutettuun aktiivisuuteen.
**Kaava:** $H_\text{E} = 0{,}019\,\tfrac{\text{mSv}}{\text{MBq}} \cdot A$
**Muunnokset:** Ei tarvita: aktiivisuus on megabecquereleinä, ja kertoimen yksikkö on millisievert megabecquerelia kohti.
**Sijoitus:** $H_\text{E} = 0{,}019\,\tfrac{\text{mSv}}{\text{MBq}} \cdot 300\,\text{MBq} = 5{,}7\,\text{mSv}$
**Vastaus:** $5{,}7\,\text{mSv}$, kaksi merkitsevää numeroa kuten kertoimessa $0{,}019\,\tfrac{\text{mSv}}{\text{MBq}}$.
**Järkevyys:** Arviolla $0{,}02 \cdot 300 = 6$. Annos on samaa suuruusluokkaa kuin suomalaisen keskimääräinen vuosiannos $5{,}9\,\text{mSv}$, mikä sopii luvun annostaulukon arvoon noin $6\,\text{mSv}$.

## fy8-14-L1-04
**Annettu:** kasvaimen massa $m = 50\,\text{g}$, absorboitunut annos $D = 2{,}0\,\text{Gy}$
**Kysytty:** kasvaimen absorboima energia $E$ jouleina
**Periaate:** Absorboitunut annos on kudoksen absorboima energia massaa kohti (luku *Säteilyannos ja säteilyturvallisuus Suomessa*), joten energia on annos kertaa massa.
**Kaava:** $D = \dfrac{E}{m}$, josta $E = D m$
**Muunnokset:** $1\,\text{Gy} = 1\,\tfrac{\text{J}}{\text{kg}}$ ja $m = 50\,\text{g} = 50 \cdot 0{,}001\,\text{kg} = 0{,}050\,\text{kg}$
**Sijoitus:** $E = 2{,}0\,\tfrac{\text{J}}{\text{kg}} \cdot 0{,}050\,\text{kg} = 0{,}10\,\text{J}$
**Vastaus:** $0{,}10\,\text{J}$, kaksi merkitsevää numeroa kuten annoksessa $2{,}0\,\text{Gy}$ ja massassa $50\,\text{g}$.
**Järkevyys:** Energia on hyvin pieni: se lämmittäisi kasvainta vain noin $0{,}0005\,\text{K}$. Vaikutus perustuu siihen, että energia tulee ionisaatioina, jotka rikkovat DNA:ta, eikä lämpenemiseen.

## fy8-14-L1-05
**Annettu:** alkuaktiivisuus $A_0 = 37\,\text{kBq}$, amerikium-241:n puoliintumisaika $T_{1/2} = 432\,\text{a}$, aika $t = 100\,\text{a}$
**Kysytty:** aktiivisuus $A$ kilobecquereleinä
**Periaate:** Aktiivisuus on verrannollinen hajoamattomien ytimien määrään ja pienenee siksi hajoamislain mukaan. Savuilmaisimen lähde on suljettu, joten ainetta ei poistu muuten kuin hajoamalla.
**Kaava:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Muunnokset:** Ei tarvita: aika ja puoliintumisaika ovat molemmat vuosina.
**Sijoitus:** $A = 37\,\text{kBq} \cdot \left(\tfrac{1}{2}\right)^{100\,\text{a} / 432\,\text{a}} = 37\,\text{kBq} \cdot \left(\tfrac{1}{2}\right)^{0{,}23148} = 37\,\text{kBq} \cdot 0{,}85176 = 31{,}52\,\text{kBq}$
**Vastaus:** $32\,\text{kBq}$, kaksi merkitsevää numeroa kuten aktiivisuudessa $37\,\text{kBq}$.
**Järkevyys:** Sata vuotta on alle neljäsosa puoliintumisajasta, joten aktiivisuus ei ehdi puolittua vaan pienenee selvästi alle $50\,\%$: se pieneni noin $15\,\%$. Siksi savuilmaisimen lähde toimii koko laitteen käyttöiän.

## fy8-14-L2-01
**Annettu:** elävän puun hiilen aktiivisuus $A_0 = 0{,}23\,\text{Bq}$ grammaa kohti, löydön aktiivisuus $A = 0{,}029\,\text{Bq}$ grammaa kohti, hiili-14:n puoliintumisaika $T_{1/2} = 5700\,\text{a}$
**Kysytty:** puuhiilen ikä $t$ vuosina
**Periaate:** Elävä puu pitää hiili-14:n osuuden hiilestään samana kuin ilmakehässä. Kun puu kuolee, uutta hiili-14:ää ei tule, ja aktiivisuus grammaa kohti pienenee hajoamislain mukaan. Iän ratkaisemiseksi eksponentissa oleva aika ratkaistaan logaritmilla.
**Kaava:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, josta $\dfrac{A_0}{A} = 2^{t/T_{1/2}}$ ja $t = T_{1/2} \cdot \dfrac{\ln (A_0 : A)}{\ln 2}$
**Muunnokset:** Ei tarvita: aktiivisuudet ovat samassa yksikössä, joten niiden suhde on paljas luku, ja ikä saadaan vuosina kuten puoliintumisaika.
**Sijoitus:** $t = 5700\,\text{a} \cdot \dfrac{\ln (0{,}23 : 0{,}029)}{\ln 2} = 5700\,\text{a} \cdot \dfrac{\ln 7{,}931}{0{,}69315} = 5700\,\text{a} \cdot \dfrac{2{,}0708}{0{,}69315} = 5700\,\text{a} \cdot 2{,}9875 = 17\,029\,\text{a}$
**Vastaus:** $1{,}7 \cdot 10^{4}\,\text{a}$ eli noin $17\,000$ vuotta, kaksi merkitsevää numeroa kuten aktiivisuuksissa $0{,}23\,\text{Bq}$ ja $0{,}029\,\text{Bq}$.
**Järkevyys:** Aktiivisuus on pienentynyt noin kahdeksasosaan, ja $\left(\tfrac{1}{2}\right)^3 = \tfrac{1}{8}$, joten aikaa on kulunut lähes kolme puoliintumisaikaa: $3 \cdot 5700\,\text{a} = 17\,100\,\text{a}$. Ikä on alle radiohiiliajoituksen rajan, noin $50\,000$ vuotta.

## fy8-14-L2-02
**Annettu:** pulssitaajuus ilman nauhaa $I_0 = 1200\,\tfrac{1}{\text{s}}$, nauhan kanssa $I = 900\,\tfrac{1}{\text{s}}$ (taustasäteily vähennetty), teräksen puoliintumispaksuus $d_{1/2} = 0{,}73\,\text{mm}$
**Kysytty:** nauhan paksuus $d$ millimetreinä
**Periaate:** Fotonisäteilyn intensiteetti vaimenee teräksessä puoliintumispaksuuden mukaan, ja ilmaisimen nettopulssitaajuus on verrannollinen siihen osuvan säteilyn intensiteettiin. Siksi pulssitaajuuksien suhde on sama kuin intensiteettien suhde.
**Kaava:** $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, josta $\dfrac{I_0}{I} = 2^{d/d_{1/2}}$ ja $d = d_{1/2} \cdot \dfrac{\ln (I_0 : I)}{\ln 2}$
**Muunnokset:** Ei tarvita: pulssitaajuudet ovat samassa yksikössä, ja paksuus saadaan millimetreinä kuten puoliintumispaksuus.
**Sijoitus:** $d = 0{,}73\,\text{mm} \cdot \dfrac{\ln (1200 : 900)}{\ln 2} = 0{,}73\,\text{mm} \cdot \dfrac{0{,}28768}{0{,}69315} = 0{,}73\,\text{mm} \cdot 0{,}41504 = 0{,}3030\,\text{mm}$
**Vastaus:** $0{,}30\,\text{mm}$, kaksi merkitsevää numeroa kuten puoliintumispaksuudessa $0{,}73\,\text{mm}$.
**Järkevyys:** Nauha päästää läpi $900 : 1200 = 75\,\%$, mikä on enemmän kuin puolet, joten nauhan on oltava ohuempi kuin yksi puoliintumispaksuus $0{,}73\,\text{mm}$. Jos nauha paksunee, pulssitaajuus pienenee, ja mittari ohjaa valssia ohentamaan sitä.

## fy8-14-L2-03
**Annettu:** TT-tutkimuksen annos $H = 8{,}0\,\text{mSv}$, luonnon säteilyn annos $5{,}1\,\text{mSv}$ vuodessa, vuodessa $365$ vuorokautta
**Kysytty:** aika $t$ vuorokausina, jona luonnon säteily antaa saman annoksen
**Periaate:** Luonnon säteilyn annos kertyy vuoden mittaan keskimäärin tasaisesti, joten annos on suoraan verrannollinen aikaan: annos on annosnopeus kertaa aika.
**Kaava:** $H = \dot{H} t$, josta $t = \dfrac{H}{\dot{H}}$
**Muunnokset:** Annosnopeus muutetaan vuorokautta kohti sijoittamalla $1\,\text{a} = 365\,\text{d}$: $\dot{H} = \tfrac{5{,}1\,\text{mSv}}{1\,\text{a}} = \tfrac{5{,}1\,\text{mSv}}{365\,\text{d}}$
**Sijoitus:** $t = \dfrac{8{,}0\,\text{mSv}}{5{,}1\,\text{mSv} : 365\,\text{d}} = \dfrac{8{,}0}{5{,}1} \cdot 365\,\text{d} = 1{,}5686 \cdot 365\,\text{d} = 572{,}5\,\text{d}$
**Vastaus:** noin $570\,\text{d}$, kaksi merkitsevää numeroa kuten annoksissa $8{,}0\,\text{mSv}$ ja $5{,}1\,\text{mSv}$.
**Järkevyys:** TT-tutkimuksen annos on hieman suurempi kuin luonnon vuosiannos, joten ajan pitää olla vähän yli vuoden: $572\,\text{d}$ on noin puolitoista vuotta. Annos on merkittävä, ja siksi TT-tutkimuksen on oltava oikeutettu.

## fy8-14-L2-04
**Annettu:** annosnopeus $\dot{H}_1 = 30\,\mu\text{Sv/h}$ etäisyydellä $r_1 = 1{,}0\,\text{m}$, hoitajan etäisyys $r_2 = 0{,}50\,\text{m}$, aika $t = 5{,}0\,\text{min}$
**Kysytty:** hoitajan annos $H$ mikrosieverteinä
**Periaate:** Potilasta pidetään pistemäisenä lähteenä, joten annosnopeus on kääntäen verrannollinen etäisyyden neliöön (luku *Säteilyannos ja säteilyturvallisuus Suomessa*). Annosnopeus pysyy tämän ajan vakiona, joten annos on annosnopeus kertaa aika.
**Kaava:** $\dot{H}_2 = \dot{H}_1 \left(\tfrac{r_1}{r_2}\right)^2$ ja $H = \dot{H}_2 t$, joten $H = \dot{H}_1 \left(\dfrac{r_1}{r_2}\right)^2 t$
**Muunnokset:** $t = 5{,}0\,\text{min} = 5{,}0 \cdot \tfrac{1}{60}\,\text{h} = 0{,}08333\,\text{h}$
**Sijoitus:** $H = 30\,\mu\text{Sv/h} \cdot \left(\dfrac{1{,}0\,\text{m}}{0{,}50\,\text{m}}\right)^2 \cdot 0{,}08333\,\text{h} = 30\,\mu\text{Sv/h} \cdot 4 \cdot 0{,}08333\,\text{h} = 120\,\mu\text{Sv/h} \cdot 0{,}08333\,\text{h} = 10\,\mu\text{Sv}$
**Vastaus:** $10\,\mu\text{Sv}$, kaksi merkitsevää numeroa kuten annosnopeudessa $30\,\mu\text{Sv/h}$ ja ajassa $5{,}0\,\text{min}$.
**Järkevyys:** Puolet lyhyempi etäisyys nelinkertaistaa annosnopeuden $120\,\mu\text{Sv/h}$:iin, ja viisi minuuttia on kahdestoistaosa tunnista: $120 : 12 = 10$. Metrin päässä hoitaja saisi samassa ajassa vain $2{,}5\,\mu\text{Sv}$, joten etäisyys on tehokas suoja.

## fy8-14-L3-01
**Annettu:** $30$ hoitokertaa, kasvaimen annos kerralla $2{,}0\,\text{Gy}$, $5$ keilaa, joista kukin antaa kasvaimeen saman osan, tulokohdan annos $1{,}3$-kertainen keilan kasvainannokseen verrattuna
**Kysytty:** terveen kudoksen kokonaisannos $D$ yhden keilan tulokohdassa grayna
**Periaate:** Keilojen annokset summautuvat vain siellä, missä keilat leikkaavat, eli kasvaimessa. Tulokohdan kautta kulkee vain yksi keila, joten se saa vain tämän keilan annoksen, joka on $1{,}3$-kertainen keilan kasvaimeen antamaan annokseen. Hoitokertojen annokset lasketaan yhteen.
**Kaava:** yhden keilan kasvainannos $\tfrac{2{,}0\,\text{Gy}}{5}$, joten $D = 30 \cdot 1{,}3 \cdot \dfrac{D_\text{kerta}}{5}$, missä $D_\text{kerta} = 2{,}0\,\text{Gy}$
**Muunnokset:** Ei tarvita: kaikki annokset ovat grayna.
**Sijoitus:** $D = 30 \cdot 1{,}3 \cdot \dfrac{2{,}0\,\text{Gy}}{5} = 30 \cdot 1{,}3 \cdot 0{,}40\,\text{Gy} = 30 \cdot 0{,}52\,\text{Gy} = 15{,}6\,\text{Gy}$
**Vastaus:** noin $16\,\text{Gy}$, kaksi merkitsevää numeroa kuten kertoimessa $1{,}3$ ja annoksessa $2{,}0\,\text{Gy}$.
**Järkevyys:** Kasvain saa yhteensä $30 \cdot 2{,}0\,\text{Gy} = 60\,\text{Gy}$, terve kudos tulokohdassa noin neljäsosan siitä. Yhdellä keilalla tulokohta saisi $1{,}3 \cdot 60\,\text{Gy} = 78\,\text{Gy}$, enemmän kuin kasvain, joten useat suunnat ovat välttämättömiä.

## fy8-14-L3-02
**Annettu:** pehmytkudoksen puoliintumispaksuus $d_{1/2}^\text{kudos} = 1{,}8\,\text{cm}$, kalkkeuman $d_{1/2}^\text{luu} = 0{,}27\,\text{cm}$, korvautuneen kerroksen paksuus $d = 1{,}0\,\text{cm}$
**Kysytty:** intensiteettien suhde ${I_\text{A} : I_\text{B}}$, kun säde A kulkee pelkän pehmytkudoksen ja säde B kalkkeuman läpi
**Periaate:** Säteet ovat yhtä pitkiä ja kulkevat muuten saman pehmytkudoksen läpi, joten muiden kerrosten osuudet ovat molemmille samat ja supistuvat suhteesta. Ero tulee vain $1{,}0\,\text{cm}$:n kerroksesta: säteellä A se on pehmytkudosta, säteellä B kalkkeumaa. Kerrosten läpi päässeet osuudet kerrotaan.
**Kaava:** $\dfrac{I_\text{A}}{I_\text{B}} = \dfrac{\left(\tfrac{1}{2}\right)^{d/d_{1/2}^\text{kudos}}}{\left(\tfrac{1}{2}\right)^{d/d_{1/2}^\text{luu}}} = 2^{d/d_{1/2}^\text{luu} - d/d_{1/2}^\text{kudos}}$
**Muunnokset:** Ei tarvita: kaikki paksuudet ovat senttimetreinä.
**Sijoitus:** $\dfrac{I_\text{A}}{I_\text{B}} = 2^{1{,}0\,\text{cm} / 0{,}27\,\text{cm} - 1{,}0\,\text{cm} / 1{,}8\,\text{cm}} = 2^{3{,}7037 - 0{,}5556} = 2^{3{,}1481} = 8{,}87$
**Vastaus:** noin $8{,}9$, kaksi merkitsevää numeroa kuten puoliintumispaksuuksissa $1{,}8\,\text{cm}$ ja $0{,}27\,\text{cm}$.
**Järkevyys:** Kalkkeumassa on noin $3{,}7$ puoliintumispaksuutta, pehmytkudoksessa olisi ollut noin $0{,}56$, joten säde B puolittuu noin kolme kertaa useammin: $2^3 = 8$. Pienellä energialla kontrasti on suuri, ja siksi pienetkin kalkkeumat näkyvät mammografiassa.

## fy8-14-L3-03
**Annettu:** lyijyn puoliintumispaksuus $511\,\text{keV}$:n fotoneille $d_{1/2} = 3{,}9\,\text{mm}$, läpi pääsevä osuus ${I : I_0} = 5{,}0\,\% = 0{,}050$
**Kysytty:** lyijysuojan paksuus $d$ millimetreinä
**Periaate:** Jokainen puoliintumispaksuus puolittaa fotonisäteilyn intensiteetin, joten vaimeneminen noudattaa yhtälöä $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$. Paksuus on eksponentissa, joten se ratkaistaan logaritmilla.
**Kaava:** $\dfrac{I_0}{I} = 2^{d/d_{1/2}}$, josta $d = d_{1/2} \cdot \dfrac{\ln (I_0 : I)}{\ln 2}$
**Muunnokset:** $5{,}0\,\% = 0{,}050$, joten ${I_0 : I} = {1 : 0{,}050} = 20$. Paksuus saadaan millimetreinä kuten puoliintumispaksuus.
**Sijoitus:** $d = 3{,}9\,\text{mm} \cdot \dfrac{\ln 20}{\ln 2} = 3{,}9\,\text{mm} \cdot \dfrac{2{,}9957}{0{,}69315} = 3{,}9\,\text{mm} \cdot 4{,}3219 = 16{,}86\,\text{mm}$
**Vastaus:** noin $17\,\text{mm}$, kaksi merkitsevää numeroa kuten puoliintumispaksuudessa $3{,}9\,\text{mm}$ ja osuudessa $5{,}0\,\%$.
**Järkevyys:** Neljä puoliintumispaksuutta päästäisi läpi $\tfrac{1}{16} \approx 6{,}3\,\%$ ja viisi $\tfrac{1}{32} \approx 3{,}1\,\%$, joten paksuuden on oltava $4 \cdot 3{,}9\,\text{mm} = 15{,}6\,\text{mm}$:n ja $5 \cdot 3{,}9\,\text{mm} = 19{,}5\,\text{mm}$:n välissä. Teknetium-$99\text{m}$:n $140\,\text{keV}$:n fotoneille sama vaimennus vaatisi vain noin $1\,\text{mm}$ lyijyä, koska niiden puoliintumispaksuus on noin $0{,}26\,\text{mm}$.
