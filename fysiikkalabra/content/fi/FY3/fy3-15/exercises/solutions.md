## fy3-15-L1-01
**Annettu:** turbiinin hyötysuhde $\eta_1 = 92{,}0\,\% = 0{,}920$, generaattorin hyötysuhde $\eta_2 = 98{,}0\,\% = 0{,}980$
**Kysytty:** koko laitoksen hyötysuhde $\eta$ prosentteina
**Periaate:** Laitos on ketju, jossa turbiinin ulostuloteho on generaattorin sisäänmenoteho. Kumpikin vaihe päästää läpi vain osan siihen tulevasta energiasta, joten ketjun hyötysuhde on osahyötysuhteiden tulo.
**Kaava:** $P_1 = \eta_1 P_0$ ja $P_2 = \eta_2 P_1$, joten $\eta = \dfrac{P_2}{P_0} = \eta_1 \eta_2$
**Muunnokset:** Hyötysuhteet ovat luvun osia: $92{,}0\,\% = 0{,}920$ ja $98{,}0\,\% = 0{,}980$. Lopuksi tulos kerrotaan sadalla prosenteiksi.
**Sijoitus:** $\eta = 0{,}920 \cdot 0{,}980 = 0{,}9016 = 90{,}16\,\%$
**Vastaus:** $90{,}2\,\%$, kolme merkitsevää numeroa kuten annetuissa hyötysuhteissa $92{,}0\,\%$ ja $98{,}0\,\%$.
**Järkevyys:** Tulo on pienempi kuin kumpikaan osahyötysuhde, kuten pitääkin, kun tekijät ovat alle 1. Arvio: $0{,}92 \cdot 0{,}98 \approx 0{,}92 - 0{,}02 \cdot 0{,}92 \approx 0{,}90$. Vesivoimalaitos ei ole lämpövoimakone, joten sen hyötysuhde voi olla yli $90\,\%$.

## fy3-15-L1-02
**Annettu:** ilmavirran liike-energian teho $P_\text{tuuli} = 2{,}50\,\text{MW}$ ja sähköteho $P_\text{sähkö} = 1{,}05\,\text{MW}$
**Kysytty:** voimalan hyötysuhde $\eta$ prosentteina
**Periaate:** Hyötysuhde on hyödyksi saadun tehon osuus laitokseen tulevasta tehosta. Tässä tulotehona on roottorin läpi virtaavan ilman liike-energian teho ja hyötytehona sähköverkkoon menevä teho; loput energiasta jää ilman liikkeeseen tai muuttuu lämmöksi.
**Kaava:** $\eta = \dfrac{P_\text{sähkö}}{P_\text{tuuli}}$
**Muunnokset:** Molemmat tehot ovat megawatteina, joten yksiköt supistuvat. Tulos kerrotaan sadalla prosenteiksi.
**Sijoitus:** $\eta = \dfrac{1{,}05\,\text{MW}}{2{,}50\,\text{MW}} = 0{,}420 = 42{,}0\,\%$
**Vastaus:** $42{,}0\,\%$, kolme merkitsevää numeroa kuten tehoissa $2{,}50\,\text{MW}$ ja $1{,}05\,\text{MW}$.
**Järkevyys:** Arvio: $1 / 2{,}5 = 0{,}4$, mikä vastaa tulosta. Nykyaikaisen tuulivoimalan hyötysuhde on parhaimmillaan noin 40–$45\,\%$. Tuulesta ei voi ottaa kaikkea energiaa, koska ilman on liikuttava vielä roottorin jälkeenkin. Osa roottorin ottamasta energiasta muuttuu kitkassa ja sähköisissä häviöissä sisäenergiaksi, joka siirtyy lämpönä ympäristöön.

## fy3-15-L1-03
**Annettu:** pinta-ala $A = 20{,}0\,\text{m}^2$, säteilyn teho pinta-alaa kohti $I = 1{,}00\,\tfrac{\text{kW}}{\text{m}^2}$, hyötysuhde $\eta = 0{,}210$
**Kysytty:** paneelin sähköteho $P$ kilowatteina
**Periaate:** Paneeliin osuvan säteilyn teho on intensiteetti kertaa pinta-ala, ja hyötysuhde kertoo, kuinka suuri osa siitä muuttuu sähköksi. Loput muuttuu lämmöksi tai heijastuu, joten sähköteho on tulotehon $\eta$-osa.
**Kaava:** $P = \eta P_\text{tulo} = \eta I A$
**Muunnokset:** Yksiköt kulkevat mukana: $\tfrac{\text{kW}}{\text{m}^2} \cdot \text{m}^2 = \text{kW}$, joten tulos tulee suoraan kilowatteina eikä muunnoksia tarvita.
**Sijoitus:** $P = 0{,}210 \cdot 1{,}00\,\tfrac{\text{kW}}{\text{m}^2} \cdot 20{,}0\,\text{m}^2 = 0{,}210 \cdot 20{,}0\,\text{kW} = 4{,}20\,\text{kW}$
**Vastaus:** $4{,}20\,\text{kW}$, kolme merkitsevää numeroa, koska pinta-ala $20{,}0\,\text{m}^2$, säteilyteho $1{,}00\,\tfrac{\text{kW}}{\text{m}^2}$ ja hyötysuhde $0{,}210$ ovat kaikki kolmella numerolla.
**Järkevyys:** Paneeliin osuu säteilyä $20{,}0\,\text{kW}$, josta noin viidennes ($0{,}210 \approx 0{,}2$) on $\approx 4\,\text{kW}$. Loput $20{,}0\,\text{kW} - 4{,}20\,\text{kW} = 15{,}8\,\text{kW}$ lämmittää paneelia tai heijastuu pois. Pientalon katolla $4\,\text{kW}$ on tavallinen huipputeho kirkkaalla säällä.

## fy3-15-L1-04
**Annettu:** kuvan pylväistä luettuna $P_0 = 400\,\text{MW}$, $P_1 = 350\,\text{MW}$, $P_2 = 150\,\text{MW}$ ja $P_3 = 140\,\text{MW}$
**Kysytty:** vaihe, jossa teho pienenee eniten, ja siinä ympäristöön lämpönä siirtyvä teho
**Periaate:** Voimalaitos toimii tasaisesti ja energia säilyy, joten kun teho pienenee vaiheessa, ero siirtyy lämpönä ympäristöön. Vaiheessa ulos tuleva teho on pienempi kuin sisään tuleva, ja ero on siinä syntyvä hukkalämpö.
**Kuvaajan lukeminen:** Pylväiden $P_0$, $P_1$ ja $P_2$ päät ovat ruudukon viivoilla, ja ne kertovat tehot $400$, $350$ ja $150\,\text{MW}$. Sähköteho $P_3$ on vähän viivan $150\,\text{MW}$ alapuolella, noin $140\,\text{MW}$; sitä ei tarvita vastaukseen. Tehon pieneneminen vaiheittain on $P_0 - P_1 = 50\,\text{MW}$ kattilassa, $P_1 - P_2 = 200\,\text{MW}$ höyrykierrossa ja $P_2 - P_3 = 10\,\text{MW}$ generaattorissa ja muuntajassa. Suurin pudotus on pylväiden $P_1$ ja $P_2$ välissä eli höyrykierrossa.
**Kaava:** $P_\text{h} = P_\text{sisään} - P_\text{ulos}$, tässä $P_\text{h} = P_1 - P_2$
**Muunnokset:** Ei tarvita: kaikki tehot ovat megawatteina.
**Sijoitus:** $P_\text{h} = 350\,\text{MW} - 150\,\text{MW} = 200\,\text{MW}$
**Vastaus:** Eniten teho pienenee höyrykierrossa, jossa lämpönä ympäristöön siirtyy $200\,\text{MW}$. Arvot luetaan ruudukon viivoilta täysinä megawatteina, joten tulos on kolmen numeron tarkkuudella $200\,\text{MW}$.
**Järkevyys:** Vaiheiden häviöt ovat yhteensä $50 + 200 + 10 = 260\,\text{MW} = P_0 - P_3 = 400\,\text{MW} - 140\,\text{MW}$, joten tase täsmää. Höyrykierron hyötysuhde on $150 / 350 \approx 0{,}43$, joka sopii höyrykierrolle, ja sen häviö on yli $75\,\%$ koko laitoksen hukkalämmöstä.

## fy3-15-L1-05
**Annettu:** polttoaineteho $P_0 = 250\,\text{MW}$, sähköteho $P_\text{s} = 75{,}0\,\text{MW}$ ja kaukolämpöteho $P_\text{k} = 150\,\text{MW}$
**Kysytty:** kokonaishyötysuhde $\eta_\text{kok}$ prosentteina
**Periaate:** Yhteistuotantolaitoksessa sekä sähkö että kaukolämpö ovat hyötyä, joten molemmat lasketaan hyötytehoon. Hukkaan menee vain loppu, ja kokonaishyötysuhde on hyötytehon osuus polttoainetehosta.
**Kaava:** $\eta_\text{kok} = \dfrac{P_\text{s} + P_\text{k}}{P_0}$
**Muunnokset:** Kaikki tehot ovat megawatteina ja yksiköt supistuvat. Tulos kerrotaan sadalla prosenteiksi.
**Sijoitus:** $\eta_\text{kok} = \dfrac{75{,}0\,\text{MW} + 150\,\text{MW}}{250\,\text{MW}} = \dfrac{225\,\text{MW}}{250\,\text{MW}} = 0{,}900 = 90{,}0\,\%$
**Vastaus:** $90{,}0\,\%$, kolme merkitsevää numeroa, koska kaikki tehot on annettu megawatin tarkkuudella ja summa $75{,}0 + 150 = 225\,\text{MW}$ säilyttää saman tarkkuuden; osamäärässä $225/250$ on siis kolme numeroa.
**Järkevyys:** Tulos on yhteistuotannon tavallisella välillä 85–$90\,\%$. Hukkalämmön teho on $250\,\text{MW} - 225\,\text{MW} = 25\,\text{MW}$, ja $225 + 25 = 250$ eli tase täsmää. Sähkön osuus on vain $\dfrac{75{,}0\,\text{MW}}{250\,\text{MW}} = 30\,\%$, joten sähköhyötysuhde on pienempi kuin lauhdevoimalaitoksessa.

## fy3-15-L2-01
**Annettu:** polttoaineteho $P_0 = 300\,\text{MW}$, kattilan hyötysuhde $\eta_1 = 0{,}880$, höyrykierron $\eta_2 = 0{,}420$ ja generaattorin $\eta_3 = 0{,}980$
**Kysytty:** laitoksen sähköteho $P_3$ megawatteina
**Periaate:** Vaiheet ovat peräkkäin, ja jokaisen ulostuloteho on seuraavan sisäänmenoteho. Kukin vaihe säilyttää vain $\eta$-osan tehostaan, joten sähköteho on polttoaineteho kerrottuna kaikilla kolmella hyötysuhteella.
**Kaava:** $P_1 = \eta_1 P_0$, $P_2 = \eta_2 P_1$ ja $P_3 = \eta_3 P_2$, joten $P_3 = \eta_1 \eta_2 \eta_3 P_0$
**Muunnokset:** Hyötysuhteet ovat dimensiottomia ja teho on jo megawatteina, joten muunnoksia ei tarvita.
**Sijoitus:** $P_3 = 0{,}880 \cdot 0{,}420 \cdot 0{,}980 \cdot 300\,\text{MW} = 0{,}362208 \cdot 300\,\text{MW} = 108{,}6624\,\text{MW}$
**Vastaus:** $109\,\text{MW}$, kolme merkitsevää numeroa, koska hyötysuhteet $0{,}880$, $0{,}420$ ja $0{,}980$ ovat kolmella numerolla ja polttoaineteho $300\,\text{MW}$ on annettu megawatin tarkkuudella.
**Järkevyys:** Arvio: $0{,}9 \cdot 0{,}4 \cdot 1{,}0 \cdot 300\,\text{MW} \approx 110\,\text{MW}$. Koko ketjun hyötysuhde on $0{,}362$ eli $36\,\%$, vähemmän kuin heikoin vaihe ($0{,}420$) antaisi yksin. Kattilan ja höyrykierron häviöt vievät yhdessä $1 - 0{,}880 \cdot 0{,}420 = 0{,}630$ eli lähes kaksi kolmasosaa (noin $63\,\%$) polttoaineen energiasta.

## fy3-15-L2-02
**Annettu:** koko ketjun hyötysuhde $\eta = 0{,}380$, kattilan $\eta_1 = 0{,}900$ ja generaattorin $\eta_3 = 0{,}980$
**Kysytty:** höyrykierron hyötysuhde $\eta_2$ prosentteina
**Periaate:** Ketju on kolmen peräkkäisen vaiheen tulo, joten koko ketjun hyötysuhde on vaiheiden hyötysuhteiden tulo. Kun kaksi vaihetta ja kokonaisuus tunnetaan, puuttuva vaihe saadaan jakamalla.
**Kaava:** $\eta = \eta_1 \eta_2 \eta_3$, joten $\eta_2 = \dfrac{\eta}{\eta_1 \eta_3}$
**Muunnokset:** Hyötysuhteet ovat dimensiottomia lukuja, joten yksikkömuunnoksia ei tarvita. Lopuksi tulos kerrotaan sadalla prosenteiksi.
**Sijoitus:** $\eta_2 = \dfrac{0{,}380}{0{,}900 \cdot 0{,}980} = \dfrac{0{,}380}{0{,}882} = 0{,}43084 = 43{,}08\,\%$
**Vastaus:** $43{,}1\,\%$, kolme merkitsevää numeroa, koska kaikki kolme hyötysuhdetta, $0{,}380$, $0{,}900$ ja $0{,}980$, ovat kolmella numerolla.
**Järkevyys:** Tarkistus: $0{,}900 \cdot 0{,}4308 \cdot 0{,}980 = 0{,}380$. Höyrykierron hyötysuhde on suurempi kuin koko ketjun $0{,}380$, kuten pitääkin, koska muut vaiheet vain pienentävät sitä. Se on hieman suurempi kuin koko lauhdevoimalaitoksen tavallinen hyötysuhde (noin $40\,\%$, tyypillisesti $38$–$42\,\%$), koska kattilan ja generaattorin häviöt eivät sisälly siihen, ja se on ketjun heikoin lenkki.

## fy3-15-L2-03
**Annettu:** sähköteho $P_\text{s} = 150\,\text{MW}$, hyötysuhde $\eta = 0{,}360$, lämpöarvo $H = 9{,}00\,\tfrac{\text{MJ}}{\text{kg}}$, aika $t = 1\,\text{h}$
**Kysytty:** poltetun hakkeen massa tunnissa $m$ tonneina
**Periaate:** Energia säilyy: polttoaineen kemiallinen energia on joko sähköä tai hukkalämpöä. Hyötysuhde yhdistää sähkötehon polttoainetehoon, ja polttoaineteho on lämpöarvo kertaa massavirta, koska lämpöarvo kertoo energian massayksikköä kohti.
**Kaava:** $P_0 = \dfrac{P_\text{s}}{\eta}$ ja $P_0 = \dfrac{H m}{t}$, joten $m = \dfrac{P_\text{s}\, t}{\eta H}$
**Muunnokset:** $150\,\text{MW} = 150 \cdot 10^6\,\text{W}$, $9{,}00\,\tfrac{\text{MJ}}{\text{kg}} = 9{,}00 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}$ ja $1\,\text{h} = 3600\,\text{s}$. Lopuksi $1\,\text{t} = 1000\,\text{kg}$.
**Sijoitus:** $m = \dfrac{150 \cdot 10^6\,\text{W} \cdot 3600\,\text{s}}{0{,}360 \cdot 9{,}00 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}} = 1{,}66667 \cdot 10^5\,\text{kg} = 166{,}67\,\text{t}$
**Vastaus:** $167\,\text{t}$, kolme merkitsevää numeroa, koska hyötysuhde $0{,}360$ ja lämpöarvo $9{,}00\,\tfrac{\text{MJ}}{\text{kg}}$ ovat kolmella numerolla ja sähköteho $150\,\text{MW}$ on annettu megawatin tarkkuudella; tunti on tarkka ($3600\,\text{s}$) eikä rajoita.
**Järkevyys:** Polttoaineteho on $\dfrac{150\,\text{MW}}{0{,}360} = 417\,\text{MW}$, ja massavirta $\dfrac{417 \cdot 10^6\,\text{W}}{9{,}00 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}} = 46\,\tfrac{\text{kg}}{\text{s}}$. Vuorokaudessa se on $46 \cdot 86\,400\,\text{kg} \approx 4000\,\text{t}$, mikä vaatii jatkuvaa rekka- tai junakuljetusta ja sopii isoon biovoimalaitokseen.

## fy3-15-L2-04
**Annettu:** lauhduttimeen siirtyvä lämpöteho $P_\text{L} = 270\,\text{MW}$, veden lämpötilan nousu $\Delta T = 9{,}00\,\text{K}$ ja annettu ominaislämpökapasiteetti $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$
**Kysytty:** lauhduttimen läpi virtaava vesivirta $q_m = m/t$ tonneina sekunnissa
**Periaate:** Lauhduttimen luovuttama lämpö siirtyy kokonaan jäähdytysveteen, kun muita häviöitä ei ole. Vesi vain lämpenee eikä höyrysty, joten lämpömäärälle pätee $Q = c m \Delta T$; jakamalla ajalla saadaan teho.
**Kaava:** $P_\text{L} = \dfrac{Q}{t} = c\, q_m \Delta T$, joten $q_m = \dfrac{P_\text{L}}{c\, \Delta T}$
**Muunnokset:** $270\,\text{MW} = 270 \cdot 10^6\,\text{W}$ ja $1\,\text{W} = 1\,\tfrac{\text{J}}{\text{s}}$. Lämpötilan muutos $9{,}00\,\text{K}$ on sama kelvineinä ja celsiusasteina. Lopuksi $1\,\text{t} = 1000\,\text{kg}$.
**Sijoitus:** $q_m = \dfrac{270 \cdot 10^6\,\text{W}}{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 9{,}00\,\text{K}} = 7159{,}9\,\tfrac{\text{kg}}{\text{s}} = 7{,}1599\,\tfrac{\text{t}}{\text{s}}$
**Vastaus:** $7{,}16\,\tfrac{\text{t}}{\text{s}}$, kolme merkitsevää numeroa, koska lämpötilan muutos $9{,}00\,\text{K}$ ja ominaislämpökapasiteetti $4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$ ovat kolmella numerolla ja teho $270\,\text{MW}$ on annettu megawatin tarkkuudella.
**Järkevyys:** Tarkistus: $4190 \cdot 7160 \cdot 9{,}00\,\text{W} = 2{,}70 \cdot 10^8\,\text{W}$. Vesivirta vastaa noin $7\,\tfrac{\text{m}^3}{\text{s}}$, mikä on pienen joen virtaama. Lauhdevoimalaitos tarvitsee rannalle suuren määrän jäähdytysvettä, ja siksi ne rakennetaan merenrannalle tai joen varteen.

## fy3-15-L3-01
**Annettu:** $P_0 = 600\,\text{MW}$. Pelkkä sähkö: $P_\text{s,0} = 240\,\text{MW}$. Täysi yhteistuotanto: $P_\text{s,täysi} = 180\,\text{MW}$ ja $P_\text{k,täysi} = 348\,\text{MW}$. Nyt kaukolämpöteho on $P_\text{k} = 200\,\text{MW}$.
**Kysytty:** sähköteho $P_\text{s}$ megawatteina ja kokonaishyötysuhde $\eta_\text{kok}$
**Periaate:** Tehtävän mukaan sähköteho pienenee lineaarisesti, kun kaukolämpöteho kasvaa, joten kaksi ääritilaa määrittävät suoran. Kaukolämpöä otetaan välitilassa, joten sähköteho saadaan siltä suoralta. Kokonaishyötysuhde on sähkön ja kaukolämmön yhteisteho jaettuna polttoainetehosta.
**Kaava:** $P_\text{s} = P_\text{s,0} - k P_\text{k}$, missä $k = \dfrac{P_\text{s,0} - P_\text{s,täysi}}{P_\text{k,täysi}}$, ja $\eta_\text{kok} = \dfrac{P_\text{s} + P_\text{k}}{P_0}$
**Muunnokset:** Kaikki tehot ovat megawatteina ja $k$ on dimensioton luku, joten muunnoksia ei tarvita.
**Sijoitus:** $k = \dfrac{240\,\text{MW} - 180\,\text{MW}}{348\,\text{MW}} = 0{,}17241$ ja $P_\text{s} = 240\,\text{MW} - 0{,}17241 \cdot 200\,\text{MW} = 205{,}517\,\text{MW}$. Sitten $\eta_\text{kok} = \dfrac{205{,}517\,\text{MW} + 200\,\text{MW}}{600\,\text{MW}} = 0{,}67586 = 67{,}6\,\%$.
**Vastaus:** $P_\text{s} = 206\,\text{MW}$ ja $\eta_\text{kok} = 67{,}6\,\%$, kolme merkitsevää numeroa eli megawatin tarkkuus, koska kaikki tehot on annettu megawatin tarkkuudella: erotus $240 - 180 = 60\,\text{MW}$ on sillä tarkkuudella, ja vähennettävä $0{,}172 \cdot 200 \approx 34\,\text{MW}$ on ykkösten tarkkuudella.
**Järkevyys:** Tulokset ovat ääritilojen välissä: sähköteho välillä $180$–$240\,\text{MW}$ ja hyötysuhde välillä $40\,\%$ ja $88\,\%$. Rajatapaus: kun $P_\text{k} = 348\,\text{MW}$, kaava antaa $240 - 60 = 180\,\text{MW}$. Jokaista kaukolämpömegawattia kohti sähköä menetetään $\tfrac{60}{348} = 0{,}17\,\text{MW}$. Yhteenlaskettu hyötysuhde ei kerro kannattavuutta, koska sähkö kelpaa kaikkeen mutta kaukolämpö vain lämmitykseen; kannattavuus riippuu tarpeesta ja hinnoista.

## fy3-15-L3-02
**Annettu:** sähköenergia $E = 36{,}0\,\text{GWh}$, hyötysuhde $\eta = 0{,}380$ ja hiilen lämpöarvo $H = 25{,}0\,\tfrac{\text{MJ}}{\text{kg}}$; annettu $1\,\text{GWh} = 3{,}60 \cdot 10^{12}\,\text{J}$
**Kysytty:** vuodessa poltettavan hiilen massa $m$ kilotonneina
**Periaate:** Energia säilyy: hiilen kemiallinen energia $Q_1$ muuttuu sähköksi hyötysuhteella $\eta$ ja loput hukkalämmöksi. Hyötysuhteen nimittäjä on ostettu polttoaine, ja polttoaineen energia on lämpöarvo kertaa massa.
**Kaava:** $E = \eta Q_1$ ja $Q_1 = H m$, joten $m = \dfrac{E}{\eta H}$
**Muunnokset:** $E = 36{,}0 \cdot 3{,}60 \cdot 10^{12}\,\text{J} = 1{,}296 \cdot 10^{14}\,\text{J}$ ja $H = 25{,}0 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}$. Lopuksi $1\,\text{kt} = 10^6\,\text{kg}$.
**Sijoitus:** $m = \dfrac{1{,}296 \cdot 10^{14}\,\text{J}}{0{,}380 \cdot 25{,}0 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}} = 1{,}3642 \cdot 10^7\,\text{kg} = 13{,}642\,\text{kt}$
**Vastaus:** $13{,}6\,\text{kt}$, kolme merkitsevää numeroa, koska sähköenergia $36{,}0\,\text{GWh}$, hyötysuhde $0{,}380$, lämpöarvo $25{,}0\,\tfrac{\text{MJ}}{\text{kg}}$ ja muuntokerroin $3{,}60 \cdot 10^{12}\,\text{J}/\text{GWh}$ ovat kaikki kolmella numerolla.
**Järkevyys:** Arvio: $\tfrac{1{,}3 \cdot 10^{14}\,\text{J}}{0{,}4 \cdot 2{,}5 \cdot 10^7\,\tfrac{\text{J}}{\text{kg}}} \approx 1{,}3 \cdot 10^7\,\text{kg}$. Määrä vastaa noin 270 junavaunullista hiiltä, kun vaunuun mahtuu $50\,\text{t}$. Hyötysuhteita ei voi verrata suoraan: hiilivoimalassa nimittäjä on ostettu polttoaine, joka kuluu: sen energiasta noin $38\,\%$ muuttuu sähköksi ja loput hukkalämmöksi, ja palamisessa syntyy päästöjä, mutta tuulen energia ei ole varasto, jota kuluu. Tuulipuiston hyötysuhde kertoo vain, kuinka suuri osa roottorin läpi virtaavan ilman liike-energiasta saadaan sähköksi.

## fy3-15-L3-03
**Annettu:** lämmitystarve $Q = 100\,\text{kWh}$, lämpökerroin $\varepsilon = 3{,}00$, voimalan hyötysuhde $\eta_\text{voimala} = 0{,}400$ ja siirron osuus $\eta_\text{siirto} = 0{,}950$
**Kysytty:** voimalaitoksen polttoaineen energia $E_\text{polttoaine}$ kilowattitunteina
**Periaate:** Lämpöpumppu siirtää lämpöä ulkoa sisälle ja käyttää siihen sähköä, joten lämpökerroin kertoo lämmön ja sähkön suhteen. Sähkö on tuotettu polttoaineesta ketjussa, jonka jokainen vaihe päästää läpi vain osan energiasta, joten polttoaine saadaan jakamalla sähkö ketjun hyötysuhteella.
**Kaava:** $\varepsilon = \dfrac{Q}{E_\text{s}}$, joten $E_\text{s} = \dfrac{Q}{\varepsilon}$, ja $E_\text{polttoaine} = \dfrac{E_\text{s}}{\eta_\text{siirto}\, \eta_\text{voimala}}$, siis $E_\text{polttoaine} = \dfrac{Q}{\eta_\text{siirto}\, \eta_\text{voimala}\, \varepsilon}$
**Muunnokset:** Kaikki energiat ovat kilowattitunteina ja kertoimet dimensiottomia, joten muunnoksia ei tarvita.
**Sijoitus:** $E_\text{polttoaine} = \dfrac{100\,\text{kWh}}{0{,}950 \cdot 0{,}400 \cdot 3{,}00} = \dfrac{100\,\text{kWh}}{1{,}14} = 87{,}719\,\text{kWh}$
**Vastaus:** $87{,}7\,\text{kWh}$, kolme merkitsevää numeroa, koska kertoimet $0{,}950$, $0{,}400$ ja $3{,}00$ ovat kolmella numerolla ja lämmitystarve $100\,\text{kWh}$ on annettu kilowattitunnin tarkkuudella.
**Järkevyys:** Suora sähkölämmitys vaatisi $\dfrac{100\,\text{kWh}}{0{,}380} = 263\,\text{kWh}$ polttoainetta ja öljykattila $\dfrac{100\,\text{kWh}}{0{,}900} = 111\,\text{kWh}$. Lämpöpumppu säästää polttoainetta eniten, koska sisälle tulee käytetyn sähkön lisäksi ulkoilmasta siirretty lämpö, joten sähköä tarvitaan vain kolmasosa lämmöstä. Suora sähkölämmitys on huonoin, koska sähkön tuotannossa on jo hukkaantunut yli $60\,\%$ polttoaineen energiasta.
