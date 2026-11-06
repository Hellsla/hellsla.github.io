
## fy6-13-L1-01
**Annettu:** jännite $U = 12\,\text{V}$, varaus $Q = 4{,}8\,\mu\text{C}$
**Kysytty:** kapasitanssi $C$ mikrofaradeina
**Periaate:** Kondensaattorin varaus on suoraan verrannollinen sen jännitteeseen, ja niiden suhde on kapasitanssi. Kun lataus on päättynyt, kondensaattorin jännite on lähteen jännite.
**Kaava:** $C = \dfrac{Q}{U}$
**Muunnokset:** $Q = 4{,}8\,\mu\text{C} = 4{,}8 \cdot 10^{-6}\,\text{C}$
**Sijoitus:** $C = \dfrac{4{,}8 \cdot 10^{-6}\,\text{C}}{12\,\text{V}} = 0{,}40 \cdot 10^{-6}\,\text{F} = 0{,}40\,\mu\text{F}$
**Vastaus:** $0{,}40\,\mu\text{F}$, kaksi merkitsevää numeroa kuten varauksessa ja jännitteessä.
**Järkevyys:** Kapasitanssin $0{,}40\,\mu\text{F}$ kondensaattoriin tulee $0{,}40\,\mu\text{C}$ jokaista volttia kohti, ja $12 \cdot 0{,}40\,\mu\text{C} = 4{,}8\,\mu\text{C}$. Kymmenesosamikrofaradeja on tavallinen kapasitanssi pienelle kondensaattorille.

## fy6-13-L1-02
**Annettu:** kapasitanssi $C = 470\,\mu\text{F}$, jännite $U = 9{,}0\,\text{V}$
**Kysytty:** varaus $Q$ millicoulombeina
**Periaate:** Latauksen jälkeen kondensaattorin jännite on pariston jännite, ja varaus on kapasitanssi kertaa jännite, koska kapasitanssi on varauksen ja jännitteen suhde.
**Kaava:** $C = \dfrac{Q}{U}$, josta $Q = CU$
**Muunnokset:** $C = 470\,\mu\text{F} = 470 \cdot 10^{-6}\,\text{F}$
**Sijoitus:** $Q = 470 \cdot 10^{-6}\,\text{F} \cdot 9{,}0\,\text{V} = 4{,}23 \cdot 10^{-3}\,\text{C} = 4{,}23\,\text{mC}$
**Vastaus:** $4{,}2\,\text{mC}$, kaksi merkitsevää numeroa kuten jännitteessä $9{,}0\,\text{V}$.
**Järkevyys:** Arvio $500\,\mu\text{F} \cdot 10\,\text{V} = 5000\,\mu\text{C} = 5\,\text{mC}$ on hieman suurempi, koska molemmat luvut pyöristettiin ylöspäin. Yksikkö täsmää: $\text{F} \cdot \text{V} = \tfrac{\text{C}}{\text{V}} \cdot \text{V} = \text{C}$.

## fy6-13-L1-03
**Annettu:** kapasitanssi $C = 2200\,\mu\text{F}$, jännite $U = 16\,\text{V}$
**Kysytty:** varastoitunut energia $W$ jouleina
**Periaate:** Ladatun kondensaattorin energia on levyjen välisessä sähkökentässä. Kun kapasitanssi ja jännite tunnetaan, energia saadaan muodosta $\tfrac{1}{2} C U^2$, joka seuraa $(Q, U)$-kuvaajan kolmion pinta-alasta.
**Kaava:** $W = \tfrac{1}{2} C U^2$
**Muunnokset:** $C = 2200\,\mu\text{F} = 2200 \cdot 10^{-6}\,\text{F}$
**Sijoitus:** $W = \tfrac{1}{2} \cdot 2200 \cdot 10^{-6}\,\text{F} \cdot (16\,\text{V})^2 = 0{,}2816\,\text{J}$
**Vastaus:** $0{,}28\,\text{J}$, kaksi merkitsevää numeroa kuten jännitteessä $16\,\text{V}$.
**Järkevyys:** Varaus on $Q = CU \approx 0{,}035\,\text{C}$, ja $\tfrac{1}{2} \cdot 0{,}035\,\text{C} \cdot 16\,\text{V} \approx 0{,}28\,\text{J}$, sama tulos. Alle joulen energia on pieni, mikä sopii pienjännitteiselle kondensaattorille.

## fy6-13-L1-04
**Annettu:** levyn pinta-ala $A = 0{,}025\,\text{m}^2$, levyjen etäisyys $d = 1{,}0\,\text{mm}$, eristeenä ilma, taulukosta $\varepsilon_\text{r} = 1{,}0$, sähkövakio $\varepsilon_0 = 8{,}854 \cdot 10^{-12}\,\text{F/m}$
**Kysytty:** kapasitanssi $C$ pikofaradeina
**Periaate:** Kondensaattori on levykondensaattori, jonka kapasitanssi riippuu vain levyjen pinta-alasta, niiden etäisyydestä ja eristeestä. Ilman suhteellinen permittiivisyys on lähes yksi.
**Kaava:** $C = \dfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$, josta ilmalle $C = \dfrac{\varepsilon_0 A}{d}$
**Muunnokset:** $d = 1{,}0\,\text{mm} = 1{,}0 \cdot 10^{-3}\,\text{m}$
**Sijoitus:** $C = \dfrac{8{,}854 \cdot 10^{-12}\,\text{F/m} \cdot 0{,}025\,\text{m}^2}{1{,}0 \cdot 10^{-3}\,\text{m}} = 221 \cdot 10^{-12}\,\text{F} = 221\,\text{pF}$
**Vastaus:** $2{,}2 \cdot 10^{2}\,\text{pF} = 220\,\text{pF}$ (laskettu arvo $221\,\text{pF}$ pyöristettynä kahteen merkitsevään numeroon kuten pinta-alassa ja etäisyydessä).
**Järkevyys:** Suhde $A : d = 0{,}025\,\text{m}^2 : 0{,}0010\,\text{m} = 25\,\text{m}$, ja $25\,\text{m} \cdot 8{,}854\,\text{pF/m} \approx 220\,\text{pF}$. Ilmaeristeisen levykondensaattorin kapasitanssi on tyypillisesti satoja pikofaradeja.

## fy6-13-L1-05
**Annettu:** kuvaajan jännite varauksen funktiona, jännite $U = 12\,\text{V}$
**Kysytty:** varastoitunut energia $W$ mikrojouleina
**Periaate:** Latauksessa jännite kasvaa samassa suhteessa kuin varaus. Energia on kuvaajan ja varausakselin väliin jäävän kolmion pinta-ala eli puolet varauksen ja jännitteen tulosta.
**Kuvaajan lukeminen:** Jännitteen $12\,\text{V}$ ruudukkoviiva kohtaa suoran varauksen $60\,\mu\text{C}$ ruudukkoviivalla. Kolmion kanta on siis $60\,\mu\text{C}$ ja korkeus $12\,\text{V}$.
**Kaava:** $W = \tfrac{1}{2} Q U$
**Muunnokset:** Ei tarvita: $\mu\text{C} \cdot \text{V} = \mu\text{J}$, koska $1\,\text{C} \cdot 1\,\text{V} = 1\,\text{J}$.
**Sijoitus:** $W = \tfrac{1}{2} \cdot 60\,\mu\text{C} \cdot 12\,\text{V} = 360\,\mu\text{J}$
**Vastaus:** $360\,\mu\text{J}$, kaksi merkitsevää numeroa, koska arvot luetaan ruudukkoviivoilta, joiden väli on $10\,\mu\text{C}$ ja $2\,\text{V}$.
**Järkevyys:** Kapasitanssi on $60\,\mu\text{C} : 12\,\text{V} = 5{,}0\,\mu\text{F}$, ja $\tfrac{1}{2} \cdot 5{,}0\,\mu\text{F} \cdot (12\,\text{V})^2 = 360\,\mu\text{J}$, sama tulos. Suorakulmion $60\,\mu\text{C} \cdot 12\,\text{V} = 720\,\mu\text{J}$ puolikas on kolmio, kuten pitää.

## fy6-13-L2-01
**Annettu:** paperikerroksen paksuus $d = 0{,}020\,\text{mm}$, läpilyöntilujuus $E_\text{max} = 16\,\text{MV/m}$
**Kysytty:** suurin jännite $U_\text{max}$ voltteina
**Periaate:** Levyjen välissä on homogeeninen kenttä $E = \tfrac{U}{d}$. Läpilyönti tapahtuu, kun kenttä ylittää eristeen läpilyöntilujuuden, joten suurin sallittu jännite saadaan, kun kenttä on täsmälleen läpilyöntilujuus.
**Kaava:** $E_\text{max} = \dfrac{U_\text{max}}{d}$, josta $U_\text{max} = E_\text{max} d$
**Muunnokset:** $E_\text{max} = 16\,\text{MV/m} = 16 \cdot 10^{6}\,\text{V/m}$ ja $d = 0{,}020\,\text{mm} = 0{,}020 \cdot 10^{-3}\,\text{m}$
**Sijoitus:** $U_\text{max} = 16 \cdot 10^{6}\,\tfrac{\text{V}}{\text{m}} \cdot 0{,}020 \cdot 10^{-3}\,\text{m} = 320\,\text{V}$
**Vastaus:** $320\,\text{V}$ eli $3{,}2 \cdot 10^{2}\,\text{V}$, kaksi merkitsevää numeroa kuten paksuudessa ja läpilyöntilujuudessa.
**Järkevyys:** Yksi millimetri paperia kestäisi $16\,\text{kV}$, ja $0{,}020\,\text{mm}$ on siitä viideskymmenesosa: $16\,000\,\text{V} : 50 = 320\,\text{V}$. Ohut eriste antaa suuren kapasitanssin, mutta kestää vain pienen jännitteen.

## fy6-13-L2-02
**Annettu:** levyn pinta-ala $A = 100\,\text{cm}^2$, eristekerroksen paksuus $d = 0{,}10\,\text{mm}$, kapasitanssi $C = 3{,}3\,\text{nF}$, sähkövakio $\varepsilon_0 = 8{,}854 \cdot 10^{-12}\,\text{F/m}$
**Kysytty:** eristeen suhteellinen permittiivisyys $\varepsilon_\text{r}$
**Periaate:** Kondensaattori on levykondensaattori, ja eriste täyttää levyjen välin, joten sen kapasitanssi on $\varepsilon_\text{r}$-kertainen tyhjiöön verrattuna. Kun kapasitanssi ja mitat tunnetaan, suhteellinen permittiivisyys voidaan ratkaista.
**Kaava:** $C = \dfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$, josta $\varepsilon_\text{r} = \dfrac{C d}{\varepsilon_0 A}$
**Muunnokset:** $A = 100\,\text{cm}^2 = 100 \cdot (0{,}01\,\text{m})^2 = 10^{-2}\,\text{m}^2$, $d = 0{,}10\,\text{mm} = 0{,}10 \cdot 10^{-3}\,\text{m} = 10^{-4}\,\text{m}$ ja $C = 3{,}3\,\text{nF} = 3{,}3 \cdot 10^{-9}\,\text{F}$
**Sijoitus:** $\varepsilon_\text{r} = \dfrac{3{,}3 \cdot 10^{-9}\,\text{F} \cdot 10^{-4}\,\text{m}}{8{,}854 \cdot 10^{-12}\,\text{F/m} \cdot 10^{-2}\,\text{m}^2} \approx 3{,}73$
**Vastaus:** $3{,}7$, kaksi merkitsevää numeroa kuten kapasitanssissa ja paksuudessa. Suhteellinen permittiivisyys on suhdeluku, jolla ei ole yksikköä.
**Järkevyys:** Ilmalla kapasitanssi olisi $\varepsilon_0 A : d \approx 0{,}89\,\text{nF}$, ja $3{,}3\,\text{nF}$ on siitä noin $3{,}7$-kertainen. Taulukon mukaan paperin suhteellinen permittiivisyys on $3{,}7$, joten eriste voi olla paperia.

## fy6-13-L2-03
**Annettu:** energia $W = 200\,\text{J}$, jännite $U = 2{,}0\,\text{kV}$
**Kysytty:** kapasitanssi $C$ mikrofaradeina
**Periaate:** Kondensaattorin energia riippuu kapasitanssista ja jännitteestä, $W = \tfrac{1}{2} C U^2$. Kun energia ja jännite tunnetaan, kapasitanssi ratkaistaan tästä yhtälöstä.
**Kaava:** $W = \tfrac{1}{2} C U^2$, josta $C = \dfrac{2W}{U^2}$
**Muunnokset:** $U = 2{,}0\,\text{kV} = 2{,}0 \cdot 1000\,\text{V} = 2000\,\text{V}$
**Sijoitus:** $C = \dfrac{2 \cdot 200\,\text{J}}{(2000\,\text{V})^2} = \dfrac{400\,\text{J}}{4{,}0 \cdot 10^{6}\,\text{V}^2} = 1{,}0 \cdot 10^{-4}\,\text{F} = 100\,\mu\text{F}$
**Vastaus:** $1{,}0 \cdot 10^{2}\,\mu\text{F}$ eli $100\,\mu\text{F}$, kaksi merkitsevää numeroa kuten jännitteessä $2{,}0\,\text{kV}$.
**Järkevyys:** Tarkistus: $\tfrac{1}{2} \cdot 100 \cdot 10^{-6}\,\text{F} \cdot (2000\,\text{V})^2 = 200\,\text{J}$. Yksikkö: $\tfrac{\text{J}}{\text{V}^2} = \tfrac{\text{C} \cdot \text{V}}{\text{V}^2} = \tfrac{\text{C}}{\text{V}} = \text{F}$.

## fy6-13-L2-04
**Annettu:** kapasitanssi $C = 10\,\text{F}$, jännite $U = 2{,}7\,\text{V}$, valaisimen teho $P = 0{,}50\,\text{W}$
**Kysytty:** paloaika $t$ sekunteina
**Periaate:** Kondensaattorin koko energia $\tfrac{1}{2} C U^2$ oletetaan saatavan valaisimen käyttöön. Teho on energia aikayksikköä kohti, ja teho oletetaan vakioksi, joten aika on energia jaettuna teholla.
**Kaava:** $W = \tfrac{1}{2} C U^2$ ja $P = \dfrac{W}{t}$, josta $t = \dfrac{C U^2}{2P}$
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä, ja $\tfrac{\text{J}}{\text{W}} = \text{s}$.
**Sijoitus:** $t = \dfrac{10\,\text{F} \cdot (2{,}7\,\text{V})^2}{2 \cdot 0{,}50\,\text{W}} = \dfrac{72{,}9\,\text{J}}{1{,}0\,\text{W}} = 72{,}9\,\text{s}$
**Vastaus:** $73\,\text{s}$, kaksi merkitsevää numeroa kuten kapasitanssissa ja tehossa.
**Järkevyys:** Energia on $\tfrac{1}{2} \cdot 10\,\text{F} \cdot 7{,}29\,\text{V}^2 \approx 36\,\text{J}$, ja $0{,}50\,\text{W}$ kuluttaa sen noin $70$ sekunnissa. Superkondensaattorin energia riittää vain noin minuutiksi, kun pieni akku riittäisi tunneiksi, mikä vastaa kokemusta.

## fy6-13-L3-01
**Annettu:** kapasitanssi $C_1 = 120\,\text{pF}$, jännite $U_1 = 500\,\text{V}$, lähde irrotetaan, levyjen etäisyys kaksinkertaistuu
**Kysytty:** energian muutos $\Delta W$ mikrojouleina
**Periaate:** Irrotetun kondensaattorin varaus ei voi muuttua, koska varauksella ei ole reittiä levyltä toiselle. Levykondensaattorin kapasitanssi on kääntäen verrannollinen levyjen etäisyyteen, joten se puolittuu, ja jännite $U = \tfrac{Q}{C}$ kaksinkertaistuu. Energian lisäys on levyjen erilleen vetämiseen tehty työ.
**Kaava:** $Q = C_1 U_1$, $C_2 = \tfrac{1}{2} C_1$, $U_2 = \dfrac{Q}{C_2}$ ja $\Delta W = \tfrac{1}{2} Q U_2 - \tfrac{1}{2} Q U_1$, josta $\Delta W = \tfrac{1}{2} Q (U_2 - U_1)$
**Muunnokset:** $C_1 = 120\,\text{pF} = 120 \cdot 10^{-12}\,\text{F}$
**Sijoitus:** $Q = 120 \cdot 10^{-12}\,\text{F} \cdot 500\,\text{V} = 60 \cdot 10^{-9}\,\text{C}$, $U_2 = \dfrac{60 \cdot 10^{-9}\,\text{C}}{60 \cdot 10^{-12}\,\text{F}} = 1000\,\text{V}$ ja $\Delta W = \tfrac{1}{2} \cdot 60 \cdot 10^{-9}\,\text{C} \cdot 500\,\text{V} = 15 \cdot 10^{-6}\,\text{J}$
**Vastaus:** $15\,\mu\text{J}$, kaksi merkitsevää numeroa kuten kapasitanssissa $120\,\text{pF}$.
**Järkevyys:** Energia kasvaa $15\,\mu\text{J}$:sta $30\,\mu\text{J}$:iin eli kaksinkertaistuu, koska varaus pysyy samana ja jännite kaksinkertaistuu. Energia ei synny tyhjästä: levyt vetävät toisiaan puoleensa, ja niiden erottaminen vaatii työn $15\,\mu\text{J}$.

## fy6-13-L3-02
**Annettu:** kapasitanssi ilmaeristeisenä $C_1 = 220\,\text{pF}$, jännite $U = 1{,}5\,\text{kV}$, lasin $\varepsilon_\text{r} = 5{,}6$, lähde pysyy kytkettynä
**Kysytty:** lähteestä kondensaattoriin siirtyvä lisävaraus $\Delta Q$ mikrocoulombeina
**Periaate:** Lähde pitää jännitteen samana koko ajan. Eriste kasvattaa kapasitanssin $\varepsilon_\text{r}$-kertaiseksi, joten samalla jännitteellä levyillä on $\varepsilon_\text{r}$-kertainen varaus, ja erotuksen tuo lähde.
**Kaava:** $Q_1 = C_1 U$ ja $Q_2 = \varepsilon_\text{r} C_1 U$, josta $\Delta Q = Q_2 - Q_1 = (\varepsilon_\text{r} - 1) C_1 U$
**Muunnokset:** $C_1 = 220\,\text{pF} = 220 \cdot 10^{-12}\,\text{F}$ ja $U = 1{,}5\,\text{kV} = 1{,}5 \cdot 1000\,\text{V} = 1500\,\text{V}$
**Sijoitus:** $\Delta Q = (5{,}6 - 1) \cdot 220 \cdot 10^{-12}\,\text{F} \cdot 1500\,\text{V} = 1{,}518 \cdot 10^{-6}\,\text{C}$
**Vastaus:** $1{,}5\,\mu\text{C}$, kaksi merkitsevää numeroa kuten jännitteessä $1{,}5\,\text{kV}$ ja suhteellisessa permittiivisyydessä $5{,}6$.
**Järkevyys:** Alussa varaus on $220\,\text{pF} \cdot 1500\,\text{V} = 0{,}33\,\mu\text{C}$, ja lasin kanssa $5{,}6$ kertaa niin paljon eli $1{,}85\,\mu\text{C}$. Lisäys $1{,}5\,\mu\text{C}$ on näiden erotus. Jos lähde olisi irrotettu, varaus ei olisi muuttunut lainkaan.

## fy6-13-L3-03
**Annettu:** kapasitanssi $C = 1{,}0\,\text{nF}$, jännite $U = 6{,}0\,\text{kV}$, polystyreenin $\varepsilon_\text{r} = 2{,}6$ ja $E_\text{max} = 24\,\text{MV/m}$, kenttä enintään $\tfrac{1}{2} E_\text{max}$, $\varepsilon_0 = 8{,}854 \cdot 10^{-12}\,\text{F/m}$
**Kysytty:** levyn pinta-ala $A$ neliösenttimetreinä
**Periaate:** Levyjen välinen kenttä on $E = \tfrac{U}{d}$. Kenttä saa olla enintään puolet läpilyöntilujuudesta, joten eristeen on oltava vähintään niin paksu, että kenttä on tämä raja-arvo. Kun paksuus tunnetaan, levykondensaattorin kaavasta ratkaistaan pinta-ala, jolla kapasitanssi on haluttu.
**Kaava:** $\tfrac{1}{2} E_\text{max} = \dfrac{U}{d}$, josta $d = \dfrac{2U}{E_\text{max}}$, ja $C = \dfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$, josta $A = \dfrac{C d}{\varepsilon_0 \varepsilon_\text{r}}$
**Muunnokset:** $U = 6{,}0\,\text{kV} = 6000\,\text{V}$, $E_\text{max} = 24 \cdot 10^{6}\,\text{V/m}$, $C = 1{,}0 \cdot 10^{-9}\,\text{F}$ ja lopuksi $1\,\text{m}^2 = 100\,\text{cm} \cdot 100\,\text{cm} = 10\,000\,\text{cm}^2$
**Sijoitus:** $d = \dfrac{2 \cdot 6000\,\text{V}}{24 \cdot 10^{6}\,\text{V/m}} = 5{,}0 \cdot 10^{-4}\,\text{m}$ ja $A = \dfrac{1{,}0 \cdot 10^{-9}\,\text{F} \cdot 5{,}0 \cdot 10^{-4}\,\text{m}}{8{,}854 \cdot 10^{-12}\,\text{F/m} \cdot 2{,}6} \approx 0{,}0217\,\text{m}^2 = 217\,\text{cm}^2$
**Vastaus:** $220\,\text{cm}^2$ eli $2{,}2 \cdot 10^{2}\,\text{cm}^2$, kaksi merkitsevää numeroa kuten kapasitanssissa ja jännitteessä.
**Järkevyys:** Eriste on $0{,}50\,\text{mm}$ paksu, ja kenttä on siinä $6000\,\text{V} : 0{,}50\,\text{mm} = 12\,\text{MV/m}$, puolet läpilyöntilujuudesta. Neliön sivu olisi noin $15\,\text{cm}$. Ohuempi eriste pienentäisi levyjä, mutta kondensaattori ei enää kestäisi jännitettä varmasti.

## fy6-13-L1-06
**Kysytty:** mitä kapasitanssille tapahtuu, kun jännite kaksinkertaistuu.
**Periaate:** Kapasitanssi on varauksen ja jännitteen suhde $C = \tfrac{Q}{U}$. Se määräytyy levyjen pinta-alasta, niiden etäisyydestä ja eristeestä, ei siitä, kuinka suureen jännitteeseen kondensaattori ladataan. Kun jännite kasvaa, varaus kasvaa samassa suhteessa.
**Mallivastaus:** Kapasitanssi pysyy samana, koska se määräytyy kondensaattorin rakenteesta. Jännitteellä $5{,}0\,\text{V}$ varaus on $Q_1 = 5{,}0\,\text{V} \cdot C$ ja jännitteellä $10\,\text{V}$ se on $Q_2 = 10\,\text{V} \cdot C$, joten varaus kaksinkertaistuu mutta suhde $\tfrac{Q}{U}$ ei muutu. Kapasitanssi ei kaksinkertaistu, pienene eikä nelinkertaistu. Energia sen sijaan nelinkertaistuu, koska $W = \tfrac{1}{2} C U^2$ riippuu jännitteen neliöstä.

## fy6-13-L1-07
**Kysytty:** mitä jännitteelle tapahtuu, kun irrotettuun kondensaattoriin työnnetään eriste.
**Periaate:** Irrotetun kondensaattorin varaus ei voi muuttua, koska varauksella ei ole reittiä levyltä toiselle. Eriste kasvattaa kapasitanssin $\varepsilon_\text{r}$-kertaiseksi, ja jännite saadaan kaavasta $U = \tfrac{Q}{C}$.
**Mallivastaus:** Jännite pienenee. Varaus $Q$ pysyy samana, koska lähde on irrotettu, ja kapasitanssi $C$ kasvaa eristeen vuoksi. Koska $U = \tfrac{Q}{C}$, jännite pienenee samassa suhteessa kuin kapasitanssi kasvaa: se on $\tfrac{1}{\varepsilon_\text{r}}$-kertainen. Eriste ei johda varausta levyltä toiselle, ja jännite ei pysy samana, koska lähde ei enää pidä sitä vakiona. Myös energia $W = \tfrac{1}{2} Q U$ pienenee.

## fy6-13-L1-08
**Annettu:** kapasitanssi $C = 1000\,\mu\text{F}$, jännite $U_1 = 6{,}0\,\text{V}$ ja $U_2 = 18\,\text{V}$
**Kysytty:** energian kasvu $\Delta W$ millijouleina
**Periaate:** Kondensaattorin energia on $\tfrac{1}{2} C U^2$ ja riippuu jännitteen neliöstä. Kapasitanssi ei muutu, joten energian kasvu on loppu- ja alkuenergian erotus.
**Kaava:** $W = \tfrac{1}{2} C U^2$ ja $\Delta W = W_2 - W_1 = \tfrac{1}{2} C (U_2^2 - U_1^2)$
**Muunnokset:** $C = 1000\,\mu\text{F} = 1000 \cdot 10^{-6}\,\text{F} = 1{,}0 \cdot 10^{-3}\,\text{F}$
**Sijoitus:** $W_1 = \tfrac{1}{2} \cdot 1{,}0 \cdot 10^{-3}\,\text{F} \cdot (6{,}0\,\text{V})^2 = 0{,}018\,\text{J}$, $W_2 = \tfrac{1}{2} \cdot 1{,}0 \cdot 10^{-3}\,\text{F} \cdot (18\,\text{V})^2 = 0{,}162\,\text{J}$ ja $\Delta W = 0{,}162\,\text{J} - 0{,}018\,\text{J} = 0{,}144\,\text{J} = 144\,\text{mJ}$
**Vastaus:** $144\,\text{mJ}$, kolme merkitsevää numeroa, koska kapasitanssi $1000\,\mu\text{F}$ ja jännite $18\,\text{V}$ määräävät tuloksen riittävän tarkasti.
**Järkevyys:** Jännite kolminkertaistuu, joten energia kasvaa $3^2 = 9$-kertaiseksi: $W_2 : W_1 = 162\,\text{mJ} : 18\,\text{mJ} = 9$. Kasvu on $9W_1 - W_1 = 8W_1 = 8 \cdot 18\,\text{mJ} = 144\,\text{mJ}$.

## fy6-13-L1-09
**Kysytty:** mitkä viidestä väitteestä ladatusta kondensaattorista ovat tosia.
**Periaate:** Latauksessa paristo siirtää varausta levystä toiseen, joten levyillä on varaukset $+Q$ ja $-Q$, ja $Q = CU$. Varaus ei kulje eristeen läpi, ja virta lakkaa, kun kondensaattorin jännite on pariston jännite. Kapasitanssi riippuu vain rakenteesta, ja energia on $W = \tfrac{1}{2} C U^2$.
**Mallivastaus:** Varaus on

$Q = CU$

$Q = 100 \cdot 10^{-6}\,\text{F} \cdot 12\,\text{V}$

$Q = 1{,}2 \cdot 10^{-3}\,\text{C} = 1{,}2\,\text{mC}$

ja energia

$W = \tfrac{1}{2} C U^2$

$W = \tfrac{1}{2} \cdot 100 \cdot 10^{-6}\,\text{F} \cdot (12\,\text{V})^2$

$W = 7{,}2 \cdot 10^{-3}\,\text{J} = 7{,}2\,\text{mJ}$

1 tosi: levyjen varaukset ovat $+1{,}2\,\text{mC}$ ja $-1{,}2\,\text{mC}$, ja niiden summa on nolla.

2 epätosi: eriste ei johda sähköä, joten varaus ei kulje sen läpi. Virta kulkee johtimissa vain latauksen aikana; kun virta on lakannut, levyjen varaus ei enää muutu.

3 epätosi: kaksinkertainen jännite tuo kaksinkertaisen varauksen, joten $C = \tfrac{Q}{U}$ on yhä $100\,\mu\text{F}$.

4 epätosi: $14{,}4\,\text{mJ}$ on $QU$ eli pariston antama energia. Kondensaattoriin varastoituu siitä puolet, $7{,}2\,\text{mJ}$, ja toinen puoli muuttuu vastuksen sisäenergiaksi.

5 tosi: kun $C$ pysyy samana, energia on verrannollinen jännitteen neliöön. Jännitteellä $24\,\text{V}$ se on $4 \cdot 7{,}2\,\text{mJ} = 28{,}8\,\text{mJ}$.

## fy6-13-L2-05
**Annettu:** taulukon pisteet $(U;\ Q)$: $(2{,}0\,\text{V};\ 94\,\mu\text{C})$, $(4{,}0\,\text{V};\ 189\,\mu\text{C})$, $(6{,}0\,\text{V};\ 281\,\mu\text{C})$, $(8{,}0\,\text{V};\ 380\,\mu\text{C})$, $(10{,}0\,\text{V};\ 471\,\mu\text{C})$ ja $(12{,}0\,\text{V};\ 567\,\mu\text{C})$
**Kysytty:** energia $W$ jännitteellä $12\,\text{V}$ millijouleina
**Periaate:** Koska $Q = CU$, pisteet asettuvat origon kautta kulkevalle suoralle, jonka kulmakerroin on kapasitanssi $C$. Kun kapasitanssi tunnetaan, energia saadaan kaavasta $W = \tfrac{1}{2} C U^2$. Sama energia on $(U, Q)$-kuvaajan suoran ja $Q$-akselin väliin jäävän kolmion pinta-ala $\tfrac{1}{2} Q U$.
**Kuvaajan lukeminen:** Pisteet asettuvat nousevalle suoralle, jonka molemmille puolille jää pisteitä, ja suora kulkee origon kautta. Kulmakerroin luetaan sovitetun suoran kahdesta kaukana toisistaan olevasta pisteestä, origosta ja pisteestä $(12\,\text{V};\ 566\,\mu\text{C})$: $\tfrac{566\,\mu\text{C}}{12\,\text{V}} \approx 47{,}2\,\tfrac{\mu\text{C}}{\text{V}}$, joten kapasitanssi on noin $47{,}2\,\mu\text{F}$.
**Kaava:** $C = \dfrac{Q}{U}$ (suoran kulmakerroin) ja $W = \tfrac{1}{2} C U^2$
**Muunnokset:** $C = 47{,}2\,\tfrac{\mu\text{C}}{\text{V}} = 47{,}2\,\mu\text{F} = 47{,}2 \cdot 10^{-6}\,\text{F}$
**Sijoitus:** $W = \tfrac{1}{2} \cdot 47{,}2 \cdot 10^{-6}\,\text{F} \cdot (12\,\text{V})^2 = 3{,}40 \cdot 10^{-3}\,\text{J} = 3{,}40\,\text{mJ}$
**Vastaus:** $3{,}4\,\text{mJ}$, kaksi merkitsevää numeroa kuten jännitteessä ja kulmakertoimessa. Silmämääräinen sovitus vaihtelee, joten noin $3{,}3\text{–}3{,}5\,\text{mJ}$ on hyvä vastaus.
**Järkevyys:** Kolmion pinta-ala on $\tfrac{1}{2} \cdot 567\,\mu\text{C} \cdot 12\,\text{V} = 3402\,\mu\text{J} \approx 3{,}4\,\text{mJ}$, sama tulos. Kapasitanssi $47\,\mu\text{F}$ on tavallinen elektrolyyttikondensaattorin arvo.

## fy6-13-L2-06
**Kysytty:** aikaväli, jolla latausvirta on suurin.
**Periaate:** Virta on varauksen siirtymisnopeus. Koska $Q = CU$ ja kapasitanssi on vakio, varaus muuttuu samaa tahtia kuin jännite, joten virta on suoraan verrannollinen jännitteen kasvunopeuteen eli kuvaajan jyrkkyyteen. Virta ei siis riipu jännitteen suuruudesta vaan siitä, kuinka nopeasti jännite kasvaa.
**Mallivastaus:** Latausvirta on suurin välillä $0\text{–}1\,\text{s}$, koska jännite kasvaa silloin nopeimmin, $3{,}5\,\text{V}$ sekunnissa, ja varaus siirtyy levyille nopeimmin. Alussa kondensaattorin jännite on nolla, joten lähteen koko jännite ajaa virtaa. Kun kondensaattoriin kertyy varausta, sen jännite vastustaa lähdettä, jännitteen kasvu hidastuu ja virta pienenee kohti nollaa. Virta ei ole suurin silloin, kun jännite tai varaus on suurin, vaan silloin, kun ne muuttuvat nopeimmin.
**Kuvaajan lukeminen:** Jännitteen kasvu sekunnin aikana on $3{,}5\,\text{V}$ välillä $0\text{–}1\,\text{s}$, $2{,}0\,\text{V}$ välillä $1\text{–}2\,\text{s}$, $1{,}4\,\text{V}$ välillä $2\text{–}3\,\text{s}$, $0{,}8\,\text{V}$ välillä $3\text{–}4\,\text{s}$, $0{,}5\,\text{V}$ välillä $4\text{–}5\,\text{s}$ ja $0{,}3\,\text{V}$ välillä $5\text{–}6\,\text{s}$. Kuvaaja on jyrkimmillään alussa ja muuttuu koko ajan loivemmaksi.

## fy6-13-L2-07
**Annettu:** kapasitanssi $C = 220\,\mu\text{F}$, lähteen jännite $U = 24\,\text{V}$, oppilaan tulos $QU = 127\,\text{mJ}$
**Kysytty:** a) oppilaan päättelyn virhe, b) varastoitunut energia $W$ millijouleina
**Periaate:** Lähde siirtää varauksen $Q$ levystä toiseen koko jännitteensä $U$ yli ja antaa siis energian $QU$. Kondensaattorin jännite kasvaa latauksessa nollasta arvoon $U$, joten varaus siirtyy keskimäärin jännitteen $\tfrac{U}{2}$ yli ja kondensaattoriin varastoituu vain puolet lähteen antamasta energiasta.
**Kaava:** $W = \tfrac{1}{2} C U^2$
**Muunnokset:** $C = 220\,\mu\text{F} = 220 \cdot 10^{-6}\,\text{F}$
**Sijoitus:** $W = \tfrac{1}{2} \cdot 220 \cdot 10^{-6}\,\text{F} \cdot (24\,\text{V})^2 = 0{,}0634\,\text{J} = 63{,}4\,\text{mJ}$
**Vastaus:** $63\,\text{mJ}$, kaksi merkitsevää numeroa kuten kapasitanssissa ja jännitteessä.
**Mallivastaus virheestä:** Oppilaan laskema $QU = 127\,\text{mJ}$ on lähteen antama energia, mutta kondensaattoriin varastoituu siitä vain puolet. Latauksen aikana kondensaattorin jännite on aluksi nolla ja kasvaa vasta vähitellen arvoon $24\,\text{V}$, joten varaus ei siirry koko ajan täyden jännitteen yli. Toinen puoli, noin $63\,\text{mJ}$, muuttuu johtimien ja vastusten sisäenergiaksi ja siirtyy lämpönä ympäristöön.
**Järkevyys:** Varastoitunut energia on $\tfrac{1}{2} \cdot 5{,}28\,\text{mC} \cdot 24\,\text{V} = 63{,}4\,\text{mJ}$, sama tulos, ja se on tasan puolet oppilaan luvusta $127\,\text{mJ}$.

## fy6-13-L3-04
**Annettu:** latausvirta $I = 15\,\text{mA}$, taulukon pisteet $(t;\ U)$: $(0\,\text{s};\ 0\,\text{V})$, $(2\,\text{s};\ 203\,\text{V})$, $(4\,\text{s};\ 396\,\text{V})$, $(6\,\text{s};\ 607\,\text{V})$, $(8\,\text{s};\ 805\,\text{V})$, $(10\,\text{s};\ 992\,\text{V})$ ja $(12\,\text{s};\ 1201\,\text{V})$, iskun jännite $1{,}8\,\text{kV}$, purkautumisaika $5{,}0\,\text{ms}$
**Kysytty:** iskun keskimääräinen teho $P$ kilowatteina, lisäksi latausaika ja perustelu kondensaattorin koskemattomuudelle
**Periaate:** Vakiovirralla varaus on $Q = It$ ja kondensaattorille $Q = CU$, joten $U = \tfrac{I}{C} t$: jännite kasvaa suoraan ajan mukana, ja suoran kulmakerroin on $\tfrac{I}{C}$. Kun kapasitanssi tunnetaan, iskussa vapautuva energia on kondensaattorin energia $\tfrac{1}{2} C U^2$, ja keskimääräinen teho saadaan jakamalla se purkautumisajalla.
**Kuvaajan lukeminen:** Pisteet asettuvat origon kautta kulkevalle suoralle, ja jännite kasvaa noin $100\,\text{V}$ sekunnissa. Kulmakerroin luetaan sovitetun suoran kahdesta kaukana toisistaan olevasta pisteestä, origosta ja pisteestä $(12\,\text{s};\ 1200\,\text{V})$: $\tfrac{1200\,\text{V}}{12\,\text{s}} = 100\,\tfrac{\text{V}}{\text{s}}$.
**Kaava:** $\dfrac{I}{C} = k$, josta $C = \dfrac{I}{k}$, sekä $W = \tfrac{1}{2} C U^2$ ja $P = \dfrac{W}{t}$
**Muunnokset:** $I = 15\,\text{mA} = 15 \cdot 10^{-3}\,\text{A}$, $U = 1{,}8\,\text{kV} = 1800\,\text{V}$ ja $t = 5{,}0\,\text{ms} = 5{,}0 \cdot 10^{-3}\,\text{s}$
**Sijoitus:** $C = \dfrac{15 \cdot 10^{-3}\,\text{A}}{100\,\text{V/s}} = 1{,}5 \cdot 10^{-4}\,\text{F} = 150\,\mu\text{F}$, $W = \tfrac{1}{2} \cdot 1{,}5 \cdot 10^{-4}\,\text{F} \cdot (1800\,\text{V})^2 = 243\,\text{J}$ ja $P = \dfrac{243\,\text{J}}{5{,}0 \cdot 10^{-3}\,\text{s}} = 4{,}86 \cdot 10^{4}\,\text{W}$
**Vastaus:** $48{,}6\,\text{kW}$ eli noin $49\,\text{kW}$, kaksi merkitsevää numeroa kuten purkautumisajassa.
**Mallivastaus latausajasta ja turvallisuudesta:** Lataus kestää $t = \tfrac{U}{k} = \tfrac{1800\,\text{V}}{100\,\text{V/s}} = 18\,\text{s}$. Laitteen kondensaattoriin ei saa koskea irrotettunakaan, koska ladattu kondensaattori säilyttää varauksensa ja energiansa, kunnes sille tulee virtatie: tässä energiaa on $243\,\text{J}$ ja jännite $1{,}8\,\text{kV}$. Kosketus napoihin päästäisi virran kehon läpi, ja purkautuminen olisi vaarallinen isku.
**Järkevyys:** Varaus on $Q = It = 15\,\text{mA} \cdot 18\,\text{s} = 0{,}27\,\text{C}$, ja $\tfrac{1}{2} \cdot 0{,}27\,\text{C} \cdot 1800\,\text{V} = 243\,\text{J}$, sama tulos. Latauksen keskimääräinen teho on vain $243\,\text{J} : 18\,\text{s} = 13{,}5\,\text{W}$, kun taas iskussa sama energia vapautuu $5{,}0\,\text{ms}$:ssa, joten teho on tuhansia kertoja suurempi.

## fy6-13-L3-05
**Annettu:** levyn pinta-ala $A = 100\,\text{cm}^2$, eristekerroksen paksuus $d = 0{,}050\,\text{mm}$, taulukosta teflonille $\varepsilon_\text{r} = 2{,}1$ ja $E_\text{max} = 60\,\text{MV/m}$ sekä lasille $\varepsilon_\text{r} = 5{,}6$ ja $E_\text{max} = 14\,\text{MV/m}$, kenttä enintään $\tfrac{1}{2} E_\text{max}$, $\varepsilon_0 = 8{,}854 \cdot 10^{-12}\,\text{F/m}$
**Kysytty:** teflon- ja lasikondensaattorin energioiden suhde $\tfrac{W_\text{teflon}}{W_\text{lasi}}$ sekä perustelu
**Periaate:** Sallittu kenttä on $\tfrac{1}{2} E_\text{max}$, joten suurin jännite on $U = \tfrac{1}{2} E_\text{max} d$. Levykondensaattorin kapasitanssi saadaan kaavasta $C = \tfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$, ja energia on $W = \tfrac{1}{2} C U^2$. Energioiden suhteesta nähdään, kumpi eriste varastoi enemmän samassa tilavuudessa.
**Kaava:** $U = \tfrac{1}{2} E_\text{max} d$, $C = \dfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$ ja $W = \tfrac{1}{2} C U^2$
**Muunnokset:** $A = 100\,\text{cm}^2 = 1{,}0 \cdot 10^{-2}\,\text{m}^2$, $d = 0{,}050\,\text{mm} = 5{,}0 \cdot 10^{-5}\,\text{m}$, $60\,\text{MV/m} = 60 \cdot 10^{6}\,\text{V/m}$ ja $14\,\text{MV/m} = 14 \cdot 10^{6}\,\text{V/m}$
**Sijoitus:** Teflon: $U = \tfrac{1}{2} \cdot 60 \cdot 10^{6}\,\tfrac{\text{V}}{\text{m}} \cdot 5{,}0 \cdot 10^{-5}\,\text{m} = 1500\,\text{V}$, $\varepsilon_0 \varepsilon_\text{r} A = 1{,}86 \cdot 10^{-13}\,\text{F} \cdot \text{m}$, josta $C = \dfrac{1{,}86 \cdot 10^{-13}\,\text{F} \cdot \text{m}}{5{,}0 \cdot 10^{-5}\,\text{m}} = 3{,}72\,\text{nF}$ ja $W = \tfrac{1}{2} \cdot 3{,}72 \cdot 10^{-9}\,\text{F} \cdot (1500\,\text{V})^2 = 4{,}18\,\text{mJ}$. Lasille $U = 350\,\text{V}$, $C = 9{,}92\,\text{nF}$ ja $W = \tfrac{1}{2} \cdot 9{,}92 \cdot 10^{-9}\,\text{F} \cdot (350\,\text{V})^2 = 0{,}607\,\text{mJ}$. Suhde on $\dfrac{4{,}18\,\text{mJ}}{0{,}607\,\text{mJ}} = 6{,}89$.
**Vastaus:** $6{,}9$, kaksi merkitsevää numeroa kuten taulukon arvoissa. Suhde on pelkkä luku, jolla ei ole yksikköä.
**Mallivastaus c):** Sijoittamalla $C$ ja $U$ energian kaavaan saadaan $W = \tfrac{1}{8} \varepsilon_0 \varepsilon_\text{r} E_\text{max}^2 A d$, joten samoilla mitoilla energia on verrannollinen suureeseen $\varepsilon_\text{r} E_\text{max}^2$. Lasin suhteellinen permittiivisyys on teflonia $\tfrac{5{,}6}{2{,}1} = 2{,}7$-kertainen, mutta teflonin läpilyöntilujuus on lasia $\tfrac{60}{14} = 4{,}3$-kertainen ja se tulee kaavaan neliönä: $4{,}3^2 = 18{,}4$. Suhde on $\tfrac{18{,}4}{2{,}7} \approx 6{,}9$: teflon kestää paljon suuremman jännitteen ja varastoi siksi enemmän energiaa, vaikka lasin kapasitanssi on suurempi.
**Järkevyys:** Teflonilla jännite on $1500\,\text{V}$ ja lasilla $350\,\text{V}$, ja kapasitanssit ovat $3{,}72\,\text{nF}$ ja $9{,}92\,\text{nF}$. Suhde saadaan myös näistä: $\tfrac{3{,}72}{9{,}92} \cdot \left(\tfrac{1500}{350}\right)^2 = 0{,}375 \cdot 18{,}4 = 6{,}9$.
