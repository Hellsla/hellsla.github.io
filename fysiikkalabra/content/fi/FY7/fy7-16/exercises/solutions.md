## fy7-16-L1-01
**Annettu:** vaimennuskerroin $a = 0{,}18\,\text{dB/km}$, kuidun pituus $L = 50\,\text{km}$
**Kysytty:** kuidun vaimennus $A$ desibeleinä
**Periaate:** Kuitu on koko matkalta samanlaista, joten jokainen kilometri vaimentaa saman määrän desibelejä, ja desibelit lasketaan yhteen. Koko kuidun vaimennus on vaimennuskerroin kertaa pituus.
**Kaava:** $A = aL$
**Muunnokset:** Ei tarvita: kilometrit supistuvat tulossa, ja vaimennus saadaan desibeleinä.
**Sijoitus:** $A = 0{,}18\,\tfrac{\text{dB}}{\text{km}} \cdot 50\,\text{km} = 9{,}0\,\text{dB}$
**Vastaus:** $9{,}0\,\text{dB}$, kaksi merkitsevää numeroa kuten vaimennuskerroin $0{,}18\,\text{dB/km}$.
**Järkevyys:** $9\,\text{dB}$ on vähän alle $10\,\text{dB}$, joten tehosta on jäljellä vähän yli kymmenesosa. Se sopii siihen, että teho puolittuu noin $17\,\text{km}$:n matkalla: $50\,\text{km}$ on noin kolme puolittumista, ja $0{,}5^3 \approx 0{,}13$.

## fy7-16-L1-02
**Annettu:** teho alussa $P_0 = 2{,}0\,\text{mW}$, teho lopussa $P = 0{,}50\,\text{mW}$
**Kysytty:** vaimennus $A$ desibeleinä
**Periaate:** Vaimennus desibeleinä määritellään tehojen suhteen kymmenkantaisesta logaritmista. Teho pienenee, joten suhde $P_0 : P$ on suurempi kuin yksi ja vaimennus positiivinen.
**Kaava:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$
**Muunnokset:** Ei tarvita: kumpikin teho on milliwatteina, ja yksikkö supistuu.
**Sijoitus:** $A = 10\,\text{dB} \cdot \lg \dfrac{2{,}0\,\text{mW}}{0{,}50\,\text{mW}} = 10\,\text{dB} \cdot \lg 4{,}0 = 6{,}021\,\text{dB}$
**Vastaus:** $6{,}0\,\text{dB}$, kaksi merkitsevää numeroa kuten tehot.
**Järkevyys:** Teho pienenee neljäsosaan eli puolittuu kahdesti. Yksi puolittuminen on noin $3\,\text{dB}$, joten kaksi on noin $6\,\text{dB}$, kuten tuloksessa.

## fy7-16-L1-03
**Annettu:** pyörrevirtasilmukan resistanssi $R = 0{,}010\,\Omega$, virran tehollinen arvo $I = 400\,\text{A}$
**Kysytty:** teho $P$, jolla sähköenergia muuttuu pohjan sisäenergiaksi, kilowatteina
**Periaate:** Pyörrevirta kulkee pohjan resistanssin läpi, ja resistanssissa sähköenergia muuttuu sisäenergiaksi teholla $RI^2$. Vaihtovirralla kaava antaa keskimääräisen tehon, kun $I$ on virran tehollinen arvo (luku *Generaattori ja vaihtovirta*).
**Kaava:** $P = RI^2$
**Muunnokset:** Lopuksi $1\,\text{kW} = 1000\,\text{W}$.
**Sijoitus:** $P = 0{,}010\,\Omega \cdot (400\,\text{A})^2 = 0{,}010\,\Omega \cdot 160\,000\,\text{A}^2 = 1600\,\text{W} = 1{,}6\,\text{kW}$
**Vastaus:** $1{,}6\,\text{kW}$, kaksi merkitsevää numeroa kuten resistanssi $0{,}010\,\Omega$.
**Järkevyys:** Induktiolieden keittoalueen teho on yleensä joitakin kilowatteja, joten $1{,}6\,\text{kW}$ on oikeaa suuruusluokkaa. Yksiköt: $\Omega \cdot \text{A}^2 = \text{V} \cdot \text{A} = \text{W}$.

## fy7-16-L1-04
**Annettu:** magneettivuon tiheyden huippuarvo $B_0 = 0{,}50\,\text{mT}$, yhden kierroksen pinta-ala $A = 12\,\text{cm}^2$, kenttä homogeeninen ja kohtisuorassa käämin tasoa vastaan
**Kysytty:** vuon huippuarvo $\Phi_0$ yhden kierroksen läpi mikroweebereinä
**Periaate:** Homogeenisessa kentässä, joka on kohtisuorassa pintaa vastaan, vuo on magneettivuon tiheys kertaa pinta-ala (luku *Sähkömagneettinen induktio*). Kun vuon tiheys on suurimmillaan, myös vuo on suurimmillaan.
**Kaava:** $\Phi = BA$, joten $\Phi_0 = B_0 A$
**Muunnokset:** $B_0 = 0{,}50\,\text{mT} = 0{,}50 \cdot 10^{-3}\,\text{T}$ ja $A = 12\,\text{cm}^2 = 12 \cdot (0{,}01\,\text{m})^2 = 1{,}2 \cdot 10^{-3}\,\text{m}^2$. Lopuksi $1\,\text{Wb} = 10^{6}\,\mu\text{Wb}$.
**Sijoitus:** $\Phi_0 = 0{,}50 \cdot 10^{-3}\,\text{T} \cdot 1{,}2 \cdot 10^{-3}\,\text{m}^2 = 6{,}0 \cdot 10^{-7}\,\text{Wb} = 0{,}60\,\mu\text{Wb}$
**Vastaus:** $0{,}60\,\mu\text{Wb}$, kaksi merkitsevää numeroa kuten lähtötiedot.
**Järkevyys:** Yksiköt: $\text{T} \cdot \text{m}^2 = \text{Wb}$. Vuo on pieni, koska sekä kenttä että pinta-ala ovat pieniä; suuren taajuuden vuoksi näin pienikin vuo indusoi käämiin voltteja.

## fy7-16-L1-05
**Annettu:** laturin ottama teho $P_\text{otto} = 10{,}0\,\text{W}$, akkuun siirtyvä teho $P_\text{akku} = 7{,}2\,\text{W}$
**Kysytty:** latauksen hyötysuhde $\eta$ prosentteina
**Periaate:** Hyötysuhde on hyödyllisen tehon osuus otetusta tehosta. Hyödyllinen teho on tässä akkuun siirtyvä teho; loput muuttuu laturin ja puhelimen käämien ja elektroniikan sisäenergiaksi.
**Kaava:** $\eta = \dfrac{P_\text{akku}}{P_\text{otto}}$
**Muunnokset:** Ei tarvita: kumpikin teho on watteina. Lopuksi suhde kerrotaan sadalla prosenteiksi.
**Sijoitus:** $\eta = \dfrac{7{,}2\,\text{W}}{10{,}0\,\text{W}} = 0{,}72 = 72\,\%$
**Vastaus:** $72\,\%$, kaksi merkitsevää numeroa kuten akkuun siirtyvä teho $7{,}2\,\text{W}$.
**Järkevyys:** Hyötysuhde on alle $100\,\%$, kuten pitää. Hukkaan menee $10{,}0\,\text{W} - 7{,}2\,\text{W} = 2{,}8\,\text{W}$, mikä näkyy siinä, että laturi ja puhelin lämpenevät latauksen aikana.

## fy7-16-L2-01
**Annettu:** kierrosten lukumäärä $N = 10$, taajuus $f = 140\,\text{kHz}$, vuon huippuarvo yhden kierroksen läpi $\Phi_0 = 0{,}40\,\mu\text{Wb}$
**Kysytty:** indusoituvan jännitteen huippuarvo $e_0$
**Periaate:** Vuo vaihtelee sinimuotoisesti, joten jokaiseen kierrokseen indusoituu sinimuotoinen jännite, jonka huippuarvo on vuon muutosnopeuden huippuarvo $2\pi f \cdot \Phi_0$, kuten generaattorissa. Kierrosten jännitteet summautuvat.
**Kaava:** $e_0 = N \cdot 2\pi f \cdot \Phi_0$
**Muunnokset:** $f = 140\,\text{kHz} = 140 \cdot 1000\,\text{Hz} = 1{,}40 \cdot 10^{5}\,\text{Hz}$ ja $\Phi_0 = 0{,}40\,\mu\text{Wb} = 0{,}40 \cdot 10^{-6}\,\text{Wb}$
**Sijoitus:** $e_0 = 10 \cdot 2\pi \cdot 1{,}40 \cdot 10^{5}\,\text{Hz} \cdot 0{,}40 \cdot 10^{-6}\,\text{Wb} = 3{,}519\,\text{V}$
**Vastaus:** $3{,}5\,\text{V}$, kaksi merkitsevää numeroa kuten vuo $0{,}40\,\mu\text{Wb}$.
**Järkevyys:** Yksiköt: $\text{Hz} \cdot \text{Wb} = \tfrac{1}{\text{s}} \cdot \text{V}\cdot\text{s} = \text{V}$. Muutaman voltin jännite riittää puhelimen elektroniikalle, joka tasasuuntaa sen akun lataamiseen.

## fy7-16-L2-02
**Annettu:** lähetetty teho $P_0 = 1{,}0\,\text{mW}$, pienin vastaanotettava teho $P = 1{,}0\,\mu\text{W}$, vaimennuskerroin $a = 0{,}20\,\text{dB/km}$
**Kysytty:** yhteyden suurin pituus $L$ kilometreinä
**Periaate:** Vastaanotin tunnistaa pulssit, kun teho on vähintään $1{,}0\,\mu\text{W}$, joten suurin sallittu vaimennus saadaan tehojen suhteesta. Kuitu on koko matkalta samanlaista, joten vaimennus on $A = aL$, ja siitä ratkaistaan pituus.
**Kaava:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$ ja $A = aL$, josta $L = \dfrac{A}{a}$
**Muunnokset:** $P_0 = 1{,}0\,\text{mW} = 1{,}0 \cdot 10^{-3}\,\text{W}$ ja $P = 1{,}0\,\mu\text{W} = 1{,}0 \cdot 10^{-6}\,\text{W}$
**Sijoitus:** $A = 10\,\text{dB} \cdot \lg \dfrac{1{,}0 \cdot 10^{-3}\,\text{W}}{1{,}0 \cdot 10^{-6}\,\text{W}} = 10\,\text{dB} \cdot \lg 1000 = 30\,\text{dB}$, joten $L = \dfrac{30\,\text{dB}}{0{,}20\,\text{dB/km}} = 150\,\text{km}$
**Vastaus:** $150\,\text{km}$ eli $1{,}5 \cdot 10^{2}\,\text{km}$, kaksi merkitsevää numeroa kuten vaimennuskerroin $0{,}20\,\text{dB/km}$.
**Järkevyys:** Teho saa pienentyä tuhannesosaan, eli kolme kertaa kymmenesosaan, mikä on $3 \cdot 10\,\text{dB}$. Kun jokainen $10\,\text{dB}$ vaatii $50\,\text{km}$ kuitua, pituus on $150\,\text{km}$. Se on samaa suuruusluokkaa kuin todellisten yhteyksien vahvistinväli.

## fy7-16-L2-03
**Annettu:** keittoalueen teho $P = 2{,}0\,\text{kW}$, veteen siirtyvä osuus $\eta = 85\,\%$, veden massa $m = 1{,}5\,\text{kg}$, alkulämpötila $15\,{}^\circ\text{C}$, loppulämpötila $100\,{}^\circ\text{C}$, taulukosta veden ominaislämpökapasiteetti $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$
**Kysytty:** lämmitysaika $t$ minuutteina
**Periaate:** Vesi pysyy nesteenä koko lämmityksen ajan, joten sen tarvitsema energia on $Q = cm\Delta T$. Pyörrevirrat lämmittävät pohjaa, ja oletuksen mukaan $85\,\%$ lieden ottamasta tehosta siirtyy veteen, joten veteen siirtyvä teho on $\eta P$. Aika on energia jaettuna teholla.
**Kaava:** $Q = cm\Delta T$ ja $Q = \eta P t$, josta $t = \dfrac{cm\Delta T}{\eta P}$
**Muunnokset:** $\Delta T = 100\,{}^\circ\text{C} - 15\,{}^\circ\text{C} = 85\,{}^\circ\text{C} = 85\,\text{K}$ (lämpötilaero on sama celsiusasteina ja kelvineinä), $P = 2{,}0\,\text{kW} = 2000\,\text{W}$ ja $\eta = 85\,\% = 0{,}85$. Lopuksi $1\,\text{min} = 60\,\text{s}$.
**Sijoitus:** $t = \dfrac{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 1{,}5\,\text{kg} \cdot 85\,\text{K}}{0{,}85 \cdot 2000\,\text{W}} = \dfrac{534\,225\,\text{J}}{1700\,\text{W}} = 314{,}3\,\text{s} = 5{,}238\,\text{min}$
**Vastaus:** $5{,}2\,\text{min}$, kaksi merkitsevää numeroa kuten teho $2{,}0\,\text{kW}$ ja massa $1{,}5\,\text{kg}$.
**Järkevyys:** Noin puolentoista litran vesimäärä kiehuu induktioliedellä kokemuksen mukaan muutamassa minuutissa. Arvio pyöreillä luvuilla: $4000 \cdot 1{,}5 \cdot 85 \approx 500\,000\,\text{J}$ ja $500\,000\,\text{J} : 1700\,\text{W} \approx 300\,\text{s} = 5\,\text{min}$.

## fy7-16-L2-04
**Annettu:** mittauksesta johtolaturin energia $E_1 = 14{,}26\,\text{Wh}$ ja latausalustan energia $E_2 = 21{,}01\,\text{Wh}$ yhtä latausta kohti, $365$ latausta vuodessa
**Kysytty:** latausalustan ylimääräinen energiankulutus $\Delta E$ vuodessa kilowattitunteina
**Periaate:** Jokaisessa latauksessa alusta ottaa pistorasiasta $E_2 - E_1$ enemmän energiaa kuin johtolaturi. Oletuksen mukaan puhelin ladataan joka päivä samalla tavalla tyhjästä täyteen, joten vuoden lisäys on yhden latauksen lisäys kertaa latausten määrä.
**Kaava:** $\Delta E = 365 \cdot (E_2 - E_1)$
**Muunnokset:** Lopuksi $1\,\text{kWh} = 1000\,\text{Wh}$.
**Sijoitus:** $\Delta E = 365 \cdot (21{,}01\,\text{Wh} - 14{,}26\,\text{Wh}) = 365 \cdot 6{,}75\,\text{Wh} = 2463{,}75\,\text{Wh} = 2{,}464\,\text{kWh}$
**Vastaus:** $2{,}46\,\text{kWh}$, kolme merkitsevää numeroa kuten erotus $6{,}75\,\text{Wh}$.
**Järkevyys:** Arvio: noin $7\,\text{Wh}$ päivässä on noin $2{,}5\,\text{kWh}$ vuodessa. Määrä on pieni yhdelle ihmiselle, suunnilleen saman verran kuin $1\,\text{kW}$:n vedenkeitin käyttää kahdessa ja puolessa tunnissa, mutta miljoonien puhelinten yhteinen hukka on suuri.

## fy7-16-L3-01
**Annettu:** kaapelin pituus $L = 1172\,\text{km}$, vaimennuskerroin $a = 0{,}18\,\text{dB/km}$, yhden osuuden suurin vaimennus $A_\text{max} = 20\,\text{dB}$
**Kysytty:** vahvistimien vähimmäismäärä
**Periaate:** Kuitu on koko matkalta samanlaista, joten osuuden vaimennus on $A = a\,l$, missä $l$ on osuuden pituus. Osuus saa olla enintään niin pitkä, että vaimennus on $20\,\text{dB}$. Osuuksia tarvitaan niin monta, että ne kattavat koko kaapelin, ja koska lähetin ja vastaanotin ovat päissä, vahvistimia on yksi vähemmän kuin osuuksia.
**Kaava:** $A_\text{max} = a\,l_\text{max}$, josta $l_\text{max} = \dfrac{A_\text{max}}{a}$; osuuksien määrä $k \ge \dfrac{L}{l_\text{max}}$ ja vahvistimien määrä $k - 1$
**Muunnokset:** Ei tarvita: pituudet ovat kilometreinä ja vaimennukset desibeleinä.
**Sijoitus:** $l_\text{max} = \dfrac{20\,\text{dB}}{0{,}18\,\text{dB/km}} = 111{,}1\,\text{km}$, joten $\dfrac{L}{l_\text{max}} = \dfrac{1172\,\text{km}}{111{,}1\,\text{km}} = 10{,}55$. Osuuksia tarvitaan siis $k = 11$, ja vahvistimia $11 - 1 = 10$.
**Vastaus:** vähintään $10$ vahvistinta. Lukumäärä on kokonaisluku, ja se pyöristetään ylöspäin osuuksien määränä, koska $10$ osuutta olisi liian pitkiä.
**Järkevyys:** Koko kaapelin vaimennus olisi ilman vahvistimia $0{,}18\,\text{dB/km} \cdot 1172\,\text{km} = 211\,\text{dB}$, ja $211\,\text{dB} : 20\,\text{dB} \approx 10{,}5$ osuutta. Osuuden pituus $1172\,\text{km} : 11 = 107\,\text{km}$ sopii todellisten yhteyksien vahvistinväliin $50$–$100\,\text{km}$:n luokkaa.

## fy7-16-L3-02
**Annettu:** taajuus $f = 25\,\text{kHz}$, magneettivuon tiheyden huippuarvo $B_0 = 4{,}0\,\text{mT}$, silmukan säde $r = 8{,}0\,\text{cm}$, silmukan resistanssi $R = 0{,}050\,\Omega$, kenttä homogeeninen ja kohtisuorassa pohjaa vastaan
**Kysytty:** pohjan lämpenemisen keskimääräinen teho $P$ kilowatteina
**Periaate:** Silmukan läpi kulkeva vuo $\Phi = BA$ vaihtelee sinimuotoisesti, joten silmukkaan indusoituu sinimuotoinen jännite, jonka huippuarvo on $e_0 = 2\pi f \cdot \Phi_0$ kuten yhden kierroksen generaattorissa (luku *Generaattori ja vaihtovirta*). Pyörrevirran sähköenergia muuttuu resistanssissa sisäenergiaksi; keskimääräinen teho lasketaan tehollisesta jännitteestä $U = e_0 : \sqrt{2}$.
**Kaava:** $\Phi_0 = B_0 \cdot \pi r^2$, $e_0 = 2\pi f \cdot \Phi_0$, $U = \dfrac{e_0}{\sqrt{2}}$ ja $P = \dfrac{U^2}{R}$, josta $P = \dfrac{(2\pi f \cdot B_0 \cdot \pi r^2)^2}{2R}$
**Muunnokset:** $f = 25\,\text{kHz} = 25 \cdot 1000\,\text{Hz} = 2{,}5 \cdot 10^{4}\,\text{Hz}$, $B_0 = 4{,}0\,\text{mT} = 4{,}0 \cdot 10^{-3}\,\text{T}$ ja $r = 8{,}0\,\text{cm} = 8{,}0 \cdot 0{,}01\,\text{m} = 0{,}080\,\text{m}$. Lopuksi $1\,\text{kW} = 1000\,\text{W}$.
**Sijoitus:** $e_0 = 2\pi \cdot 2{,}5 \cdot 10^{4}\,\text{Hz} \cdot 4{,}0 \cdot 10^{-3}\,\text{T} \cdot \pi \cdot (0{,}080\,\text{m})^2 = 12{,}63\,\text{V}$, joten $P = \dfrac{(12{,}63\,\text{V})^2}{2 \cdot 0{,}050\,\Omega} = 1596\,\text{W} = 1{,}596\,\text{kW}$
**Vastaus:** $1{,}6\,\text{kW}$, kaksi merkitsevää numeroa kuten vuon tiheys $4{,}0\,\text{mT}$, säde $8{,}0\,\text{cm}$ ja resistanssi $0{,}050\,\Omega$.
**Järkevyys:** Tehollinen jännite on $12{,}63\,\text{V} : \sqrt{2} = 8{,}93\,\text{V}$ ja tehollinen virta $8{,}93\,\text{V} : 0{,}050\,\Omega = 179\,\text{A}$; teho $8{,}93\,\text{V} \cdot 179\,\text{A} \approx 1600\,\text{W}$ täsmää. Tulos on keittoalueen tehon suuruusluokkaa; malli on karkea, koska todelliset pyörrevirrat jakautuvat koko pohjaan.

## fy7-16-L3-03
**Annettu:** lähetetty teho $P_0 = 1{,}0\,\text{mW}$, pienin tarvittava teho $P = 10\,\mu\text{W}$, vaimennuskerroin $a = 0{,}20\,\text{dB/km}$, neljä liitosta, joista kukin vaimentaa $0{,}50\,\text{dB}$, lasin taitekerroin $n = 1{,}47$, valon nopeus tyhjiössä $c = 3{,}00 \cdot 10^8\,\text{m/s}$
**Kysytty:** valopulssin kulkuaika $t$ pisimmän yhteyden päästä päähän millisekunteina
**Periaate:** Yhteyden koko vaimennus saa olla enintään tehojen suhteen antama määrä. Desibelit lasketaan yhteen, joten kuidulle jää se osa, joka ei kulu liitoksiin, ja siitä saadaan suurin pituus. Lasissa valo etenee nopeudella $v = c : n$ (luku *Kokonaisheijastuminen ja valokuitu*), ja akselin suuntainen pulssi kulkee kuidun pituuden.
**Kaava:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$, $A = aL + 4 \cdot 0{,}50\,\text{dB}$, josta $L = \dfrac{A - 4 \cdot 0{,}50\,\text{dB}}{a}$, ja $t = \dfrac{L}{v} = \dfrac{nL}{c}$
**Muunnokset:** $P_0 = 1{,}0\,\text{mW} = 1{,}0 \cdot 10^{-3}\,\text{W}$, $P = 10\,\mu\text{W} = 1{,}0 \cdot 10^{-5}\,\text{W}$; pituus $90\,\text{km} = 90 \cdot 1000\,\text{m}$; lopuksi $1\,\text{s} = 1000\,\text{ms}$.
**Sijoitus:** $A = 10\,\text{dB} \cdot \lg \dfrac{1{,}0 \cdot 10^{-3}\,\text{W}}{1{,}0 \cdot 10^{-5}\,\text{W}} = 10\,\text{dB} \cdot \lg 100 = 20\,\text{dB}$, $L = \dfrac{20\,\text{dB} - 2{,}0\,\text{dB}}{0{,}20\,\text{dB/km}} = 90\,\text{km} = 90\,000\,\text{m}$, joten $t = \dfrac{1{,}47 \cdot 90\,000\,\text{m}}{3{,}00 \cdot 10^8\,\text{m/s}} = 4{,}41 \cdot 10^{-4}\,\text{s} = 0{,}441\,\text{ms}$
**Vastaus:** $0{,}44\,\text{ms}$, kaksi merkitsevää numeroa kuten tehot ja vaimennuskerroin.
**Järkevyys:** Ilman liitoksia kuitu voisi olla $100\,\text{km}$, joten liitokset lyhentävät yhteyttä vähän, kuten pitää. Lasissa valo kulkee noin $200\,\text{km}$ millisekunnissa, joten $90\,\text{km}$:iin kuluu vajaa puoli millisekuntia.
