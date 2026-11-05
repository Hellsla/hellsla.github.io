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

## fy3-15-L1-06
**Kysytty:** miksi yhteistuotantolaitoksen kokonaishyötysuhde on suurempi kuin lauhdevoimalaitoksen, kun polttoaine on sama
**Periaate:** Hyötysuhde kertoo, kuinka suuri osa polttoaineen energiasta tulee hyötykäyttöön. Polttoaineesta vapautuva energia on molemmissa sama, joten ero syntyy siitä, mitä hyödyksi lasketaan: lauhdevoimalaitoksessa vain sähkö, yhteistuotannossa sähkö ja kaukolämpö, $\eta_\text{kok} = \dfrac{P_\text{s} + P_\text{k}}{P_0}$.
**Mallivastaus:** Yhteistuotannossa lauhduttimen lämpö johdetaan kaukolämpöverkkoon eikä mereen, joten suurempi osa polttoaineen energiasta tulee hyötykäyttöön. Polttoaineesta ei vapaudu enemmän energiaa, koska lämpöarvo on sama. Turbiini ei myöskään muuta suurempaa osaa lämmöstä sähköksi: sähköä saadaan yleensä vähemmän kuin lauhdevoimalaitoksessa. Kaukolämpöverkko ei tuota energiaa lisää, sillä sähkö ja lämpö yhteensä eivät ylitä polttoainetehoa. Hukkalämpöä syntyy edelleen, mutta vähemmän.

## fy3-15-L1-07
**Annettu:** reaktorin lämpöteho $P_0 = 1500\,\text{MW}$ ja sähköteho $P_\text{s} = 510\,\text{MW}$
**Kysytty:** sähköntuotannon hyötysuhde $\eta$ prosentteina
**Periaate:** Hyötysuhde on hyödyksi saadun tehon osuus laitokseen tuodusta tehosta. Hyötytehona on tässä vain sähkö, ja loput reaktorin lämmöstä siirtyy hukkalämpönä ympäristöön.
**Kaava:** $\eta = \dfrac{P_\text{s}}{P_0}$
**Muunnokset:** Molemmat tehot ovat megawatteina, joten yksiköt supistuvat. Tulos kerrotaan sadalla prosenteiksi.
**Sijoitus:** $\eta = \dfrac{510\,\text{MW}}{1500\,\text{MW}} = 0{,}340 = 34{,}0\,\%$
**Vastaus:** $34{,}0\,\%$, kolme merkitsevää numeroa kuten sähkötehossa $510\,\text{MW}$.
**Järkevyys:** Arvio: $1500 : 3 = 500$, ja $510\,\text{MW}$ on hieman enemmän, joten hyötysuhde on hieman yli kolmannes. Hukkalämpöä syntyy $1500\,\text{MW} - 510\,\text{MW} = 990\,\text{MW}$, noin kaksi kolmasosaa. Lämpövoimalaitoksen sähköhyötysuhde on tyypillisesti 30–$40\,\%$, ja tulos on sillä välillä.

## fy3-15-L1-08
**Annettu:** polttoaineteho $P_0 = 500\,\text{MW}$ ja käyntiaika $t = 1\,\text{vrk} = 24\,\text{h}$
**Kysytty:** polttoaineen energia $E$ gigawattitunteina
**Periaate:** Teho on energia aikayksikköä kohti. Kun teho on vakio, energia on teho kerrottuna ajalla.
**Kaava:** $P = \dfrac{E}{t}$, joten $E = P_0\,t$
**Muunnokset:** $1\,\text{vrk} = 24\,\text{h}$. Teho muunnetaan gigawateiksi: $500\,\text{MW} = 0{,}500\,\text{GW}$. Tällöin tulos tulee suoraan gigawattitunteina.
**Sijoitus:** $E = 0{,}500\,\text{GW} \cdot 24\,\text{h} = 12{,}0\,\text{GWh}$
**Vastaus:** $12{,}0\,\text{GWh}$, kolme merkitsevää numeroa. Teho $500\,\text{MW}$ on annettu kolmella numerolla, ja vuorokausi on täsmälleen $24\,\text{h}$.
**Järkevyys:** Arvio: $500\,\text{MW} \cdot 24\,\text{h} \approx 500 \cdot 24\,\text{MWh} = 12\,000\,\text{MWh}$, joka on $12\,\text{GWh}$. Yksi tunti antaisi $0{,}5\,\text{GWh}$, ja vuorokaudessa on 24 tuntia, joten luku on oikeaa kokoluokkaa. Sama energia on $12{,}0 \cdot 3{,}6 \cdot 10^{12}\,\text{J} \approx 4{,}3 \cdot 10^{13}\,\text{J}$.

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

## fy3-15-L2-05
**Annettu:** taulukosta vuonna 2023 polttoaineen energia $E_0 = 2450\,\text{GWh}$, sähkö $E_\text{s} = 735\,\text{GWh}$ ja kaukolämpö $E_\text{k} = 1470\,\text{GWh}$; vuosien 2021 ja 2022 arvot ovat taulukossa
**Kysytty:** vuoden 2023 kokonaishyötysuhde $\eta_\text{kok}$ prosentteina
**Periaate:** Yhteistuotantolaitoksessa hyödyksi saadaan sekä sähkö että kaukolämpö, joten kokonaishyötysuhteessa lasketaan molemmat. Sama suhde energioina kuin tehoina, koska laitos toimii saman ajan.
**Kaava:** $\eta_\text{s} = \dfrac{E_\text{s}}{E_0}$ ja $\eta_\text{kok} = \dfrac{E_\text{s} + E_\text{k}}{E_0}$
**Muunnokset:** Kaikki energiat ovat gigawattitunteina, joten yksiköt supistuvat eikä muunnoksia tarvita. Tulokset kerrotaan sadalla prosenteiksi.
**Sijoitus:** Vuonna 2023 sähkön ja kaukolämmön summa on $735\,\text{GWh} + 1470\,\text{GWh} = 2205\,\text{GWh}$, joten $\eta_\text{kok} = \dfrac{2205\,\text{GWh}}{2450\,\text{GWh}} = 0{,}900 = 90{,}0\,\%$. Sähköhyötysuhteet ovat $\eta_\text{s} = \tfrac{840}{2400} = 35{,}0\,\%$ (2021), $\tfrac{800}{2500} = 32{,}0\,\%$ (2022) ja $\tfrac{735}{2450} = 30{,}0\,\%$ (2023). Kokonaishyötysuhteet ovat $\tfrac{2030}{2400} = 84{,}6\,\%$ (2021) ja $\tfrac{2210}{2500} = 88{,}4\,\%$ (2022).
**Vastaus:** $90{,}0\,\%$, kolme merkitsevää numeroa kuten taulukon energioissa.
**Järkevyys:** Kokonaishyötysuhde on enintään $100\,\%$ ja suurempi kuin sähköhyötysuhde, kuten pitääkin. Hukkalämpöä jää vuonna 2023 $2450\,\text{GWh} - 2205\,\text{GWh} = 245\,\text{GWh}$, noin kymmenesosa. Kylmänä vuonna kaukolämpöä tarvitaan enemmän, joten suurempi osa lauhduttimen lämmöstä tulee hyötykäyttöön ja sähköä saadaan vähemmän: sähköhyötysuhde pieneni arvosta $35{,}0\,\%$ arvoon $30{,}0\,\%$, mutta kokonaishyötysuhde kasvoi arvosta $84{,}6\,\%$ arvoon $90{,}0\,\%$. Sähkö ja lämpö eivät silti ole yhtä arvokkaita, vaikka ne lasketaan yhteen.

## fy3-15-L2-06
**Annettu:** taulukosta ydinvoimala $P_0 = 2400\,\text{MW}$ ja $P_\text{s} = 840\,\text{MW}$, kivihiilivoimala $1200\,\text{MW}$ ja $432\,\text{MW}$, biovoimala $350\,\text{MW}$ ja $112\,\text{MW}$
**Kysytty:** suurin hukkalämmön teho $P_\text{h}$ megawatteina
**Periaate:** Lauhdevoimalaitoksessa hyödyksi saadaan vain sähkö, ja energia säilyy, joten polttoaine- tai reaktoriteho on sähköä tai hukkalämpöä: $P_0 = P_\text{s} + P_\text{h}$. Hyötysuhde on suhdeluku, mutta hukkalämmön teho riippuu myös laitoksen koosta.
**Kaava:** $\eta = \dfrac{P_\text{s}}{P_0}$ ja $P_\text{h} = P_0 - P_\text{s}$
**Muunnokset:** Kaikki tehot ovat megawatteina, joten muunnoksia ei tarvita.
**Sijoitus:** Ydinvoimala: $\eta = \tfrac{840\,\text{MW}}{2400\,\text{MW}} = 0{,}350$ ja $P_\text{h} = 2400\,\text{MW} - 840\,\text{MW} = 1560\,\text{MW}$. Kivihiilivoimala: $\eta = \tfrac{432}{1200} = 0{,}360$ ja $P_\text{h} = 1200\,\text{MW} - 432\,\text{MW} = 768\,\text{MW}$. Biovoimala: $\eta = \tfrac{112}{350} = 0{,}320$ ja $P_\text{h} = 350\,\text{MW} - 112\,\text{MW} = 238\,\text{MW}$.
**Vastaus:** $1560\,\text{MW}$ (ydinvoimala), kolme merkitsevää numeroa kuten sähkötehoissa.
**Järkevyys:** Kunkin laitoksen $P_\text{s} + P_\text{h}$ on yhtä suuri kuin $P_0$: esimerkiksi $840 + 1560 = 2400$. Heikoin hyötysuhde on biovoimalalla ($32{,}0\,\%$), mutta sillä on pienin hukkalämmön teho ($238\,\text{MW}$), koska sen koko on pieni. Suurin hukkalämmön teho on ydinvoimalalla, vaikka sen hyötysuhde ($35{,}0\,\%$) on lähes yhtä suuri kuin kivihiilivoimalan ($36{,}0\,\%$). Hyötysuhde ja hukkalämmön teho eivät siis järjesty samaan järjestykseen.

## fy3-15-L2-07
**Annettu:** $\eta_1 = 0{,}920$ (kattila), $\eta_2 = 0{,}410$ (höyrykierto) ja $\eta_3 = 0{,}970$ (generaattori); oppilaan tulos $230\,\%$
**Kysytty:** laitoksen oikea hyötysuhde $\eta$ prosentteina ja virheen selitys
**Periaate:** Vaiheet ovat peräkkäin, ja kukin vaihe päästää läpi vain hyötysuhteensa verran siihen tulevasta tehosta. Kun $P_1 = \eta_1 P_0$, $P_2 = \eta_2 P_1$ ja $P_3 = \eta_3 P_2$, ketjun hyötysuhde on $\eta = \dfrac{P_3}{P_0} = \eta_1\,\eta_2\,\eta_3$ eli hyötysuhteet kerrotaan.
**Kaava:** $\eta = \eta_1\,\eta_2\,\eta_3$
**Muunnokset:** Hyötysuhteet ovat dimensiottomia lukuja, joten muunnoksia ei tarvita. Lopuksi tulos kerrotaan sadalla prosenteiksi.
**Sijoitus:** $\eta = 0{,}920 \cdot 0{,}410 \cdot 0{,}970 = 0{,}3659 = 36{,}6\,\%$
**Vastaus:** $36{,}6\,\%$, kolme merkitsevää numeroa kuten annetuissa hyötysuhteissa.
**Järkevyys:** Oppilaan virhe: hyötysuhteiden summa $230\,\%$ olisi yli $100\,\%$, mikä on mahdotonta, koska laitos ei voi tuottaa enemmän sähköä kuin polttoaineessa on energiaa. Jokainen vaihe pienentää jäljellä olevaa tehoa, joten hyötysuhteet kerrotaan eikä lasketa yhteen. Tulo $0{,}366$ on pienempi kuin heikoin vaihe $0{,}410$, kuten pitääkin, kun kaikki tekijät ovat alle 1. Arvio: $0{,}9 \cdot 0{,}4 \cdot 1{,}0 = 0{,}36$. Hukkalämpöä on $100\,\% - 36{,}6\,\% = 63{,}4\,\%$ polttoaineteholle.

## fy3-15-L2-08
**Annettu:** polttoaineteho $P_0 = 1200\,\text{MW}$, vesivirta $12\,\tfrac{\text{m}^3}{\text{s}}$, veden lämpötila $8\,{}^\circ\text{C} \to 18\,{}^\circ\text{C}$, $\rho = 1000\,\tfrac{\text{kg}}{\text{m}^3}$ ja $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$
**Kysytty:** lauhduttimesta veteen siirtyvän lämpötehon $P_\text{L}$ suuruusluokka
**Periaate:** Veteen siirtyvä lämpöteho on $P_\text{L} = c\,q_m\,\Delta T$, missä $q_m$ on massavirta ($\text{kg/s}$) ja $\Delta T$ veden lämpötilan nousu lauhduttimessa. Suuruusluokka riittää, joten arvot voi pyöristää, mutta tiheys on käytettävä ja $\Delta T$ on lämpötilojen erotus kelvineinä.
**Mallivastaus:** Massavirta:

$q_m = \rho\,\dfrac{V}{t}$

$q_m = 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 12\,\tfrac{\text{m}^3}{\text{s}} = 12\,000\,\tfrac{\text{kg}}{\text{s}}$

Lämpötilan nousu:

$\Delta T = 18\,{}^\circ\text{C} - 8\,{}^\circ\text{C} = 10\,\text{K}$

Lämpöteho:

$P_\text{L} = c\,q_m\,\Delta T$

$P_\text{L} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 12\,000\,\tfrac{\text{kg}}{\text{s}} \cdot 10\,\text{K}$

$P_\text{L} \approx 5{,}0 \cdot 10^8\,\text{W} = 500\,\text{MW}$

Lähin vaihtoehto on $500\,\text{MW}$. Järkevyys: tulos on noin $42\,\%$ polttoainetehosta $1200\,\text{MW}$, mikä sopii siihen, että lauhduttimen kautta siirtyy suuri osa polttoaineen energiasta. Muut vaihtoehdot syntyvät virheistä: $0{,}5\,\text{MW}$ kun tiheys jää käyttämättä, $50\,\text{MW}$ kun kuutiometri luetaan sadaksi kilogrammaksi ja $15\,000\,\text{MW}$ kun nousuna käytetään loppulämpötilaa kelvineinä.

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

## fy3-15-L3-04
**Annettu:** sähkön tarve $P_\text{s} = 100\,\text{MW}$ ja kaukolämmön tarve $P_\text{k} = 200\,\text{MW}$. A: lauhdevoimalaitoksen hyötysuhde $\eta_\text{s,A} = 0{,}400$ ja lämpökattilan $\eta_\text{kat} = 0{,}900$. B: yhteistuotantolaitoksen sähköhyötysuhde $\eta_\text{s,B} = 0{,}320$ ja kaukolämpöteho $0{,}560\,P_{0,\text{B}}$; puuttuva lämpö tuotetaan samanlaisella lämpökattilalla ($\eta_\text{kat} = 0{,}900$)
**Kysytty:** polttoainetehojen erotus $P_{0,\text{A}} - P_{0,\text{B}}$ megawatteina
**Periaate:** Polttoaineteho saadaan jakamalla hyötyteho hyötysuhteella. Vaihtoehdossa A sähkö ja lämpö tuotetaan erikseen, joten polttoainetehot lasketaan yhteen. Vaihtoehdossa B laitos mitoitetaan sähkötarpeen mukaan, ja sen tuottama kaukolämpö vähennetään lämpötarpeesta; jäljelle jäävä lämpö tuotetaan kattilassa.
**Kaava:** A: $P_{0,\text{A}} = \dfrac{P_\text{s}}{\eta_\text{s,A}} + \dfrac{P_\text{k}}{\eta_\text{kat}}$. B: $P_{0,\text{CHP}} = \dfrac{P_\text{s}}{\eta_\text{s,B}}$, $P_\text{k,CHP} = 0{,}560\,P_{0,\text{CHP}}$ ja $P_{0,\text{B}} = P_{0,\text{CHP}} + \dfrac{P_\text{k} - P_\text{k,CHP}}{\eta_\text{kat}}$. Erotus on $P_{0,\text{A}} - P_{0,\text{B}}$.
**Muunnokset:** Kaikki tehot ovat megawatteina ja hyötysuhteet dimensiottomia lukuja, joten muunnoksia ei tarvita.
**Sijoitus:** A: $P_{0,\text{A}} = \dfrac{100\,\text{MW}}{0{,}400} + \dfrac{200\,\text{MW}}{0{,}900} = 250\,\text{MW} + 222{,}22\,\text{MW} = 472{,}22\,\text{MW}$. B: $P_{0,\text{CHP}} = \dfrac{100\,\text{MW}}{0{,}320} = 312{,}5\,\text{MW}$ ja $P_\text{k,CHP} = 0{,}560 \cdot 312{,}5\,\text{MW} = 175{,}0\,\text{MW}$. Kattilan on tuotettava $200\,\text{MW} - 175{,}0\,\text{MW} = 25{,}0\,\text{MW}$, joten kattilan polttoaineteho on $\dfrac{25{,}0\,\text{MW}}{0{,}900} = 27{,}78\,\text{MW}$ ja $P_{0,\text{B}} = 312{,}5\,\text{MW} + 27{,}78\,\text{MW} = 340{,}28\,\text{MW}$. Erotus on $472{,}22\,\text{MW} - 340{,}28\,\text{MW} = 131{,}94\,\text{MW}$.
**Vastaus:** $132\,\text{MW}$, kolme merkitsevää numeroa kuten annetuissa hyötysuhteissa. Vaihtoehto B tarvitsee noin $28\,\%$ vähemmän polttoainetta.
**Järkevyys:** Yhteistuotannon kokonaishyötysuhde on $0{,}320 + 0{,}560 = 0{,}880$, ja $0{,}880 \cdot 312{,}5\,\text{MW} = 275\,\text{MW}$ on sähkön ja lämmön summa $100\,\text{MW} + 175\,\text{MW}$. Vaihtoehdon A kokonaishyötysuhde on vain $\dfrac{300\,\text{MW}}{472{,}22\,\text{MW}} = 0{,}635$. Säästö syntyy siitä, että yhteistuotannossa lauhduttimen lämpö, joka lauhdevoimalaitoksessa menisi mereen, lämmittää kaupunkia.

## fy3-15-L3-05
**Annettu:** $P_0 = 2700\,\text{MW}$, $P_\text{s} = 900\,\text{MW}$, vesivirta $q_m = 38{,}0\,\text{t/s}$ ja $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$; taulukosta lämpötilat sisään ja ulos tammikuussa $1{,}2\,{}^\circ\text{C}$ ja $12{,}1\,{}^\circ\text{C}$, huhtikuussa $3{,}5\,{}^\circ\text{C}$ ja $14{,}2\,{}^\circ\text{C}$, heinäkuussa $17{,}8\,{}^\circ\text{C}$ ja $28{,}4\,{}^\circ\text{C}$ sekä syyskuussa $12{,}3\,{}^\circ\text{C}$ ja $23{,}2\,{}^\circ\text{C}$
**Kysytty:** lauhduttimeen siirtyvä lämpöteho $P_\text{L}$ megawatteina
**Periaate:** Lauhduttimen lämpö lämmittää jäähdytysvettä, ja lämpömäärä on $Q = cm\,\Delta T$, kun vesi pysyy nesteenä. Teho on lämpömäärä aikayksikköä kohti, joten $P_\text{L} = c\,q_m\,\Delta T$. Lämpötilan nousu vaihtelee kuukausittain hieman, joten käytetään keskiarvoa.
**Kuvaajan lukeminen:** Taulukosta lasketaan nousu $\Delta T = T_\text{ulos} - T_\text{sisään}$ kunakin kuukautena: tammikuu $10{,}9\,\text{K}$, huhtikuu $10{,}7\,\text{K}$, heinäkuu $10{,}6\,\text{K}$ ja syyskuu $10{,}9\,\text{K}$. Lämpötilaero on sama celsius- ja kelvinasteikolla.
**Kaava:** $\Delta T_\text{ka} = \dfrac{\Sigma\,\Delta T}{4}$ ja $P_\text{L} = c\,q_m\,\Delta T_\text{ka}$
**Muunnokset:** $q_m = 38{,}0\,\text{t/s} = 38\,000\,\text{kg/s}$. Tulos muunnetaan wateista megawateiksi, $1\,\text{MW} = 10^6\,\text{W}$.
**Sijoitus:** Nousujen summa on $10{,}9 + 10{,}7 + 10{,}6 + 10{,}9 = 43{,}1\,\text{K}$, joten $\Delta T_\text{ka} = 10{,}775\,\text{K}$. Tällöin
$P_\text{L} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 38\,000\,\tfrac{\text{kg}}{\text{s}} \cdot 10{,}775\,\text{K} = 1{,}7156 \cdot 10^{9}\,\text{W} = 1716\,\text{MW}$
**Vastaus:** $1720\,\text{MW}$, kolme merkitsevää numeroa kuten vesivirrassa ja lämpötilan nousussa.
**Järkevyys:** Arvio: $4000 \cdot 4 \cdot 10^4 \cdot 11\,\text{W} \approx 1{,}8 \cdot 10^9\,\text{W}$. Hukkalämmön teho on $P_\text{h} = 2700\,\text{MW} - 900\,\text{MW} = 1800\,\text{MW}$, ja lauhduttimen osuus on $\tfrac{1716}{1800} = 95\,\%$ siitä; loput noin $84\,\text{MW}$ lähtee esimerkiksi generaattorin ja muuntajan häviöinä ilmaan. Lämpöä siirtyy meriveteen vähemmän kuin hukkalämpöä, kuten pitääkin. Vesi on lauhduttimen jälkeen vain noin $11\,\text{K}$ ympäristöä lämpimämpää, joten sillä ei voi enää tuottaa sähköä, mutta energia ei ole kadonnut vaan lämmittää merta. Heinäkuussa vesi lähtee lämpötilassa $28{,}4\,{}^\circ\text{C}$, joten purkualueella meri on lämpimämpää kuin muualla ja vesieliöstön olot voivat heiketä.
