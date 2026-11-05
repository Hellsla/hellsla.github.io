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
**Järkevyys:** Koko kaapelin vaimennus olisi ilman vahvistimia $0{,}18\,\text{dB/km} \cdot 1172\,\text{km} = 211\,\text{dB}$, ja $211\,\text{dB} : 20\,\text{dB} \approx 10{,}5$ osuutta. Osuuden pituus $1172\,\text{km} : 11 = 107\,\text{km}$ on hieman yli todellisten yhteyksien tyypillisen $50$–$100\,\text{km}$:n vahvistinvälin.

## fy7-16-L3-02
**Annettu:** taajuus $f = 25\,\text{kHz}$, magneettivuon tiheyden huippuarvo $B_0 = 4{,}0\,\text{mT}$, silmukan säde $r = 8{,}0\,\text{cm}$, silmukan resistanssi $R = 0{,}050\,\Omega$, kenttä homogeeninen ja kohtisuorassa pohjaa vastaan
**Kysytty:** pohjan lämpenemisen keskimääräinen teho $P$ kilowatteina
**Periaate:** Silmukan läpi kulkeva vuo $\Phi = BA$ vaihtelee sinimuotoisesti, joten silmukkaan indusoituu sinimuotoinen jännite, jonka huippuarvo on $e_0 = 2\pi f \cdot \Phi_0$ kuten yhden kierroksen generaattorissa (luku *Generaattori ja vaihtovirta*). Pyörrevirran sähköenergia muuttuu resistanssissa sisäenergiaksi; keskimääräinen teho lasketaan tehollisesta jännitteestä $U = e_0 : \sqrt{2}$.
**Kaava:** $\Phi_0 = B_0 \cdot \pi r^2$, $e_0 = 2\pi f \cdot \Phi_0$, $U = \dfrac{e_0}{\sqrt{2}}$ ja $P = \dfrac{U^2}{R}$, josta $P = \dfrac{(2\pi f \cdot B_0 \cdot \pi r^2)^2}{2R}$
**Muunnokset:** $f = 25\,\text{kHz} = 25 \cdot 1000\,\text{Hz} = 2{,}5 \cdot 10^{4}\,\text{Hz}$, $B_0 = 4{,}0\,\text{mT} = 4{,}0 \cdot 10^{-3}\,\text{T}$ ja $r = 8{,}0\,\text{cm} = 8{,}0 \cdot 0{,}01\,\text{m} = 0{,}080\,\text{m}$. Lopuksi $1\,\text{kW} = 1000\,\text{W}$.
**Sijoitus:** $e_0 = 2\pi \cdot 2{,}5 \cdot 10^{4}\,\text{Hz} \cdot 4{,}0 \cdot 10^{-3}\,\text{T} \cdot \pi \cdot (0{,}080\,\text{m})^2 = 12{,}63\,\text{V}$, joten $P = \dfrac{(12{,}63\,\text{V})^2}{2 \cdot 0{,}050\,\Omega} = 1596\,\text{W} = 1{,}596\,\text{kW}$
**Vastaus:** $1{,}6\,\text{kW}$, kaksi merkitsevää numeroa kuten vuon tiheys $4{,}0\,\text{mT}$, säde $8{,}0\,\text{cm}$ ja resistanssi $0{,}050\,\Omega$.
**Järkevyys:** Tehollinen jännite on $12{,}63\,\text{V} : \sqrt{2} = 8{,}93\,\text{V}$ ja tehollinen virta $8{,}93\,\text{V} : 0{,}050\,\Omega = 179\,\text{A}$; teho $8{,}93\,\text{V} \cdot 179\,\text{A} \approx 1600\,\text{W}$ täsmää. Tulos on keittoalueen tehon suuruusluokkaa; pyörrevirran oma kenttä pienentää todellisuudessa virtaa, joten tulos on yläraja.

## fy7-16-L3-03
**Annettu:** lähetetty teho $P_0 = 1{,}0\,\text{mW}$, pienin tarvittava teho $P = 10\,\mu\text{W}$, vaimennuskerroin $a = 0{,}20\,\text{dB/km}$, neljä liitosta, joista kukin vaimentaa $0{,}50\,\text{dB}$, lasin taitekerroin $n = 1{,}47$, valon nopeus tyhjiössä $c = 3{,}00 \cdot 10^8\,\text{m/s}$
**Kysytty:** valopulssin kulkuaika $t$ pisimmän yhteyden päästä päähän millisekunteina
**Periaate:** Yhteyden koko vaimennus saa olla enintään tehojen suhteen antama määrä. Desibelit lasketaan yhteen, joten kuidulle jää se osa, joka ei kulu liitoksiin, ja siitä saadaan suurin pituus. Lasissa valo etenee nopeudella $v = c : n$ (luku *Kokonaisheijastuminen ja valokuitu*), ja akselin suuntainen pulssi kulkee kuidun pituuden.
**Kaava:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$, $A = aL + 4 \cdot 0{,}50\,\text{dB}$, josta $L = \dfrac{A - 4 \cdot 0{,}50\,\text{dB}}{a}$, ja $t = \dfrac{L}{v} = \dfrac{nL}{c}$
**Muunnokset:** $P_0 = 1{,}0\,\text{mW} = 1{,}0 \cdot 10^{-3}\,\text{W}$, $P = 10\,\mu\text{W} = 1{,}0 \cdot 10^{-5}\,\text{W}$; pituus $90\,\text{km} = 90 \cdot 1000\,\text{m}$; lopuksi $1\,\text{s} = 1000\,\text{ms}$.
**Sijoitus:** $A = 10\,\text{dB} \cdot \lg \dfrac{1{,}0 \cdot 10^{-3}\,\text{W}}{1{,}0 \cdot 10^{-5}\,\text{W}} = 10\,\text{dB} \cdot \lg 100 = 20\,\text{dB}$, $L = \dfrac{20\,\text{dB} - 2{,}0\,\text{dB}}{0{,}20\,\text{dB/km}} = 90\,\text{km} = 90\,000\,\text{m}$, joten $t = \dfrac{1{,}47 \cdot 90\,000\,\text{m}}{3{,}00 \cdot 10^8\,\text{m/s}} = 4{,}41 \cdot 10^{-4}\,\text{s} = 0{,}441\,\text{ms}$
**Vastaus:** $0{,}44\,\text{ms}$, kaksi merkitsevää numeroa kuten tehot ja vaimennuskerroin.
**Järkevyys:** Ilman liitoksia kuitu voisi olla $100\,\text{km}$, joten liitokset lyhentävät yhteyttä vähän, kuten pitää. Lasissa valo kulkee noin $200\,\text{km}$ millisekunnissa, joten $90\,\text{km}$:iin kuluu vajaa puoli millisekuntia.

## fy7-16-L1-06
**Kysytty:** miksi induktiolieden lasilevy ei lämpene itsestään, vaikka kelan magneettikenttä kulkee sen läpi
**Periaate:** Induktioliedessä kela synnyttää vaihtuvan magneettikentän, ja vaihtuva vuo indusoi johtavaan kappaleeseen pyörrevirtoja. Pyörrevirrat muuttavat sähköenergiaa sisäenergiaksi resistanssissa teholla $RI^2$. Lämpeneminen vaatii siis sen, että kappaleessa voi kulkea sähkövirta.
**Mallivastaus:** Lasi ei johda sähköä, joten siihen ei synny pyörrevirtoja, jotka muuttaisivat sähköenergiaa sisäenergiaksi. Vaihtoehto, jonka mukaan lasi estää magneettikentän kulun, on väärä, koska kenttä kulkee lasin läpi ja lämmittää kattilan pohjaa. Vaihtoehto, jonka mukaan sulamislämpötila estää lämpenemisen, on väärä, koska lämpeneminen riippuu virrasta eikä sulamislämpötilasta. Vaihtoehto, jonka mukaan pyörrevirrat kumoavat toisensa Lenzin lain mukaan, on väärä, koska Lenzin laki kertoo virran suunnan eikä poista virtaa.

## fy7-16-L1-07
**Annettu:** teho alussa $P_0 = 4{,}0\,\text{mW}$, vaimennuskerroin $a = 0{,}20\,\text{dB/km}$, pituus $L = 45\,\text{km}$
**Kysytty:** teho $P$ kuidun lopussa milliwatteina
**Periaate:** Kuitu on koko matkalta samanlaista, joten vaimennus lasketaan kaavalla $A = aL$. Sen jälkeen tehojen suhde saadaan vaimennuksen määritelmästä ratkaisemalla teho $P$.
**Kaava:** $A = aL$ ja $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$, josta $P = P_0 \cdot 10^{-A / (10\,\text{dB})}$
**Muunnokset:** Ei tarvita: teho säilyy milliwatteina, koska suhde $P : P_0$ on yksikötön.
**Sijoitus:** $A = 0{,}20\,\tfrac{\text{dB}}{\text{km}} \cdot 45\,\text{km} = 9{,}0\,\text{dB}$, joten $P = 4{,}0\,\text{mW} \cdot 10^{-9{,}0 / 10} = 4{,}0\,\text{mW} \cdot 0{,}1259 = 0{,}5036\,\text{mW}$
**Vastaus:** $0{,}50\,\text{mW}$, kaksi merkitsevää numeroa kuten lähtötiedot.
**Järkevyys:** Vaimennus $9{,}0\,\text{dB}$ on noin kolme kertaa $3\,\text{dB}$, eli teho puolittuu kolme kertaa: $4{,}0\,\text{mW} : 8 = 0{,}50\,\text{mW}$, kuten tuloksessa. Teho on pienentynyt, mutta ei kymmenesosaan, koska $9\,\text{dB}$ on vähemmän kuin $10\,\text{dB}$.

## fy7-16-L1-08
**Annettu:** vaimennuskerroin $a = 0{,}20\,\text{dB/km}$, teho puolittuu eli $P_0 : P = 2$
**Kysytty:** matka $L$ kilometreinä, jonka kuluessa teho puolittuu
**Periaate:** Puolittuminen tarkoittaa tehojen suhdetta $2$, joten siitä saadaan vaimennus desibeleinä. Kuitu on koko matkalta samanlaista, joten vaimennus on $A = aL$, ja siitä ratkaistaan matka.
**Kaava:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$ ja $A = aL$, josta $L = \dfrac{A}{a}$
**Muunnokset:** Ei tarvita: vaimennus on desibeleinä ja vaimennuskerroin desibelejä kilometriä kohti.
**Sijoitus:** $A = 10\,\text{dB} \cdot \lg 2 = 3{,}010\,\text{dB}$, joten $L = \dfrac{3{,}010\,\text{dB}}{0{,}20\,\text{dB/km}} = 15{,}05\,\text{km}$
**Vastaus:** $15\,\text{km}$, kaksi merkitsevää numeroa kuten vaimennuskerroin $0{,}20\,\text{dB/km}$.
**Järkevyys:** Puolittuminen vastaa noin $3\,\text{dB}$:ä, ja kuitu vaimentaa $0{,}20\,\text{dB}$ kilometrillä, joten $3 : 0{,}2 = 15$ kilometriä. Teho puolittuu noin $15\,\text{km}$:n välein, joten $45\,\text{km}$:n matkalla se puolittuu kolme kertaa.

## fy7-16-L2-05
**Annettu:** taulukon mittauspisteet $(d;\ \eta)$, rajaksi $\eta = 50\,\%$
**Kysytty:** etäisyys $d$, jolla hyötysuhde laskee arvoon $50\,\%$, millimetreinä
**Periaate:** Etäisyyden kasvaessa vastaanotinkäämin läpi kulkeva vuo pienenee jyrkästi, joten hyötysuhde laskee. Raja $50\,\%$ on mittausten $58\,\%$ ja $44\,\%$ välissä, joten etäisyys saadaan kuvaajasta tai lineaarisella interpoloinnilla näiden kahden pisteen välillä.
**Kuvaajan lukeminen:** Piirrä pisteet $(3;\ 81)$, $(6;\ 73)$, $(10;\ 58)$, $(15;\ 44)$, $(20;\ 31)$ ja $(25;\ 22)$ ja yhdistä ne sujuvalla käyrällä. Vedä vaakasuora viiva korkeudelle $50\,\%$. Käyrä leikkaa sen pisteiden $d = 10\,\text{mm}$ ja $d = 15\,\text{mm}$ välissä, vähän yli puolivälin eli yli $12{,}5\,\text{mm}$.
**Kaava:** $d = d_1 + (d_2 - d_1) \cdot \dfrac{\eta_1 - 50\,\%}{\eta_1 - \eta_2}$, missä $(d_1;\ \eta_1)$ ja $(d_2;\ \eta_2)$ ovat rajan ympärillä olevat mittauspisteet
**Muunnokset:** Ei tarvita: etäisyydet ovat millimetreinä ja hyötysuhteet prosentteina, ja yksiköt supistuvat suhteessa.
**Sijoitus:** $d = 10\,\text{mm} + 5\,\text{mm} \cdot \dfrac{58\,\% - 50\,\%}{58\,\% - 44\,\%} = 10\,\text{mm} + 5\,\text{mm} \cdot 0{,}571 = 12{,}86\,\text{mm}$
**Vastaus:** $13\,\text{mm}$, kaksi merkitsevää numeroa. Mittaus on tehty noin millimetrin tarkkuudella, joten kuvaajasta luettu arvo $12$–$13\,\text{mm}$ on yhtä hyvä (sujuva käyrä kulkee lineaarista välistä hieman alempana).
**Järkevyys:** Hyötysuhde $50\,\%$ on lähempänä arvoa $44\,\%$ kuin arvoa $58\,\%$ (eroa $6$ ja $8$ prosenttiyksikköä), joten tulos on vähän yli puolivälin eli yli $12{,}5\,\text{mm}$, kuten pitää. Hyötysuhde laskee kaikilla väleillä, mikä sopii siihen, että vuo heikkenee etäisyyden kasvaessa.

## fy7-16-L2-06
**Annettu:** alkuteho $P_0 = 800\,\mu\text{W}$, taulukon pituudet $L$ ja tehot $P$
**Kysytty:** vaimennuskerroin $a$ yksikössä $\text{dB/km}$
**Periaate:** Kuitu on koko matkalta samanlaista, joten vaimennus kasvaa suoraan verrannollisena pituuteen: $A = aL$. Kun $A$ piirretään pituuden $L$ funktiona, pisteet asettuvat origon kautta kulkevalle suoralle, jonka kulmakerroin on $a$. Suora kulkee origon kautta, koska nollan pituisella kuidulla ei ole vaimennusta.
**Kuvaajan lukeminen:** Vaimennukset ovat $A = 2{,}15;\ 3{,}89;\ 6{,}11;\ 7{,}93;\ 10{,}05\,\text{dB}$ pituuksilla $10;\ 20;\ 30;\ 40;\ 50\,\text{km}$. Todellisissa mittauksissa pisteet eivät ole täsmälleen samalla suoralla, joten suora piirretään pisteiden lomaan. Sovitettu suora kulkee pisteiden $(0;\ 0)$ ja $(50;\ 10{,}0)$ kautta.
**Kaava:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$ ja $A = aL$, joten suoran kulmakerroin $a = \dfrac{\Delta A}{\Delta L}$
**Muunnokset:** Ei tarvita: tehot ovat mikrowatteina ja niiden suhde on yksikötön.
**Sijoitus:** Esimerkiksi pituudella $10\,\text{km}$: $A = 10\,\text{dB} \cdot \lg \dfrac{800\,\mu\text{W}}{488\,\mu\text{W}} = 2{,}15\,\text{dB}$. Kulmakerroin $a = \dfrac{10{,}0\,\text{dB} - 0}{50\,\text{km} - 0} = 0{,}200\,\text{dB/km}$. Pienimmän neliösumman suora origon kautta antaa kulmakertoimeksi $0{,}2003\,\text{dB/km}$.
**Vastaus:** $0{,}20\,\text{dB/km}$, kaksi merkitsevää numeroa; teho on mitattu kolmen merkitsevän numeron tarkkuudella, mutta pisteiden hajonta rajoittaa tulosta.
**Järkevyys:** Yksittäisten pisteiden suhteet $A : L$ ovat välillä $0{,}194$–$0{,}215\,\text{dB/km}$, joten $0{,}20\,\text{dB/km}$ on niiden keskellä. Arvo on tyypillinen tietoliikennekuidulle, jonka vaimennuskerroin on luokkaa $0{,}2\,\text{dB/km}$.

## fy7-16-L2-07
**Annettu:** vaimennus $A = 20\,\text{dB}$; opiskelijan väite: teho pienenee $20\,\%$ ja perille saapuu $80\,\%$
**Kysytty:** a) opiskelijan päättelyn virhe; b) perille saapuva osuus lähetetystä tehosta prosentteina
**Periaate:** Desibeli on logaritminen yksikkö, ei prosentti. Vaimennus $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$ kertoo tehojen suhteen kymmenpotenssina, ja jokainen $10\,\text{dB}$ pienentää tehon kymmenesosaan. Siksi $20\,\text{dB}$ on kaksi kertaa kymmenesosaan pienentyminen.
**Kaava:** $\dfrac{P}{P_0} = 10^{-A / (10\,\text{dB})}$
**Muunnokset:** Lopuksi suhde kerrotaan sadalla prosenteiksi.
**Sijoitus:** $\dfrac{P}{P_0} = 10^{-20\,\text{dB} / (10\,\text{dB})} = 10^{-2} = 0{,}010$, joten perille saapuu $0{,}010 \cdot 100\,\% = 1{,}0\,\%$
**Vastaus:** a) Virhe on se, että desibelit tulkittiin prosenteiksi. Desibelit lasketaan yhteen ja tehojen suhteet kerrotaan: kaksi $10\,\text{dB}$:n osuutta pienentää tehon kymmenesosaan kahdesti. b) $1{,}0\,\%$ lähetetystä tehosta saapuu perille. Opiskelijan arvo $80\,\%$ vastaisi vaimennusta vain noin $1\,\text{dB}$.
**Järkevyys:** Vaimennus $20\,\text{dB}$ on $2 \cdot 10\,\text{dB}$, joten teho on $\tfrac{1}{10} \cdot \tfrac{1}{10} = \tfrac{1}{100}$ eli $1\,\%$. Opiskelijan arvon tarkistus: $10\,\text{dB} \cdot \lg \dfrac{1}{0{,}80} = 0{,}97\,\text{dB}$, joten $80\,\%$ vastaisi noin $1\,\text{dB}$:n vaimennusta eikä $20\,\text{dB}$:ä.

## fy7-16-L3-04
**Annettu:** $N = 15$, $f = 130\,\text{kHz}$, taulukon $d$ ja $e_0$, latauksen raja $e_0 = 1{,}0\,\text{V}$, uusi taajuus $f' = 100\,\text{kHz}$ ja sama vuo
**Kysytty:** suurin etäisyys $d$ millimetreinä, jolla lataus toimii taajuudella $100\,\text{kHz}$
**Periaate:** Vuo vaihtelee sinimuotoisesti, joten $e_0 = N \cdot 2\pi f \cdot \Phi_0$. Taulukon jännitteistä lasketaan vuo jokaisella etäisyydellä. Jännite $1{,}0\,\text{V}$ vaatii taajuudella $100\,\text{kHz}$ tietyn vuon, ja etäisyys saadaan interpoloimalla.
**Kaava:** $\Phi_0 = \dfrac{e_0}{N \cdot 2\pi f}$, $\Phi_{\min} = \dfrac{1{,}0\,\text{V}}{N \cdot 2\pi f'}$ ja $d = d_1 + (d_2 - d_1) \cdot \dfrac{\Phi_1 - \Phi_{\min}}{\Phi_1 - \Phi_2}$
**Muunnokset:** $f = 1{,}30 \cdot 10^{5}\,\text{Hz}$, $f' = 1{,}00 \cdot 10^{5}\,\text{Hz}$ ja $1\,\text{Wb} = 10^{6}\,\mu\text{Wb}$.
**Sijoitus:** a) Nimittäjä on $15 \cdot 2\pi \cdot 1{,}30 \cdot 10^{5}\,\text{Hz} = 1{,}225 \cdot 10^{7}\,\text{Hz}$, joten vuot ovat $0{,}377;\ 0{,}221;\ 0{,}124;\ 0{,}0677;\ 0{,}0384\,\mu\text{Wb}$ etäisyyksillä $4;\ 8;\ 12;\ 16;\ 20\,\text{mm}$.
b) $\Phi_{\min} = \dfrac{1{,}0\,\text{V}}{15 \cdot 2\pi \cdot 1{,}00 \cdot 10^{5}\,\text{Hz}} = 0{,}1061\,\mu\text{Wb}$ on vuoarvojen $0{,}1241\,\mu\text{Wb}$ ($12\,\text{mm}$) ja $0{,}0677\,\mu\text{Wb}$ ($16\,\text{mm}$) välissä: $d = 12\,\text{mm} + 4\,\text{mm} \cdot \dfrac{0{,}1241 - 0{,}1061}{0{,}1241 - 0{,}0677} = 13{,}28\,\text{mm}$
**Vastaus:** $13\,\text{mm}$, kaksi merkitsevää numeroa; interpolointi on arvio, koska vuo ei pienene lineaarisesti. c) Sama vuo vaihtelee taajuudella $100\,\text{kHz}$ hitaammin kuin taajuudella $130\,\text{kHz}$, joten indusoituva jännite on pienempi. Raja $1{,}0\,\text{V}$ ylittyy vain suuremmalla vuolla eli lähempänä laturia. Etäisyyden saisi takaisin lisäämällä vastaanotinkäämin kierroksia, koska jännite on suoraan verrannollinen kierrosten lukumäärään.
**Järkevyys:** Raja-arvo $0{,}1061\,\mu\text{Wb}$ on pienempi kuin vuo etäisyydellä $12\,\text{mm}$ mutta suurempi kuin etäisyydellä $16\,\text{mm}$, joten $13{,}3\,\text{mm}$ on näiden välissä. Taajuudella $130\,\text{kHz}$ raja-arvo olisi $0{,}0816\,\mu\text{Wb}$ ja etäisyys noin $15{,}0\,\text{mm}$, joten taajuuden lasku lyhentää toimintaetäisyyttä, kuten c-kohdassa. Kierrosten lisäys $15$:stä $20$:een kasvattaisi jännitettä kertoimella $1{,}33$ ja korvaisi taajuuden laskun kertoimella $1{,}30$.

## fy7-16-L3-05
**Annettu:** $f = 30\,\text{kHz}$, $B_0 = 3{,}0\,\text{mT}$, $r = 9{,}0\,\text{cm}$, $R_\text{A} = 0{,}040\,\Omega$, $R_\text{B} = 0{,}050\,\Omega$, $R_\text{C} = 0{,}080\,\Omega$, kenttä homogeeninen ja kohtisuorassa pohjaa vastaan
**Kysytty:** taajuus $f_\text{C}$ kilohertseinä, jolla kattilan C pohja lämpenee samalla teholla kuin kattilan A pohja taajuudella $30\,\text{kHz}$
**Periaate:** Silmukan vuo $\Phi = BA$ vaihtelee sinimuotoisesti, joten huippujännite on $e_0 = 2\pi f \cdot \Phi_0$ ja teho $P = U^2 : R$ tehollisella jännitteellä $U = e_0 : \sqrt{2}$. Huippujännite on verrannollinen taajuuteen, joten teho on verrannollinen taajuuden neliöön ja kääntäen verrannollinen resistanssiin.
**Kaava:** $\Phi_0 = B_0 \cdot \pi r^2$, $e_0 = 2\pi f \cdot \Phi_0$ ja $P = \dfrac{e_0^2}{2R} \sim \dfrac{f^2}{R}$. Yhtäsuuret tehot: $\dfrac{f_\text{C}^2}{R_\text{C}} = \dfrac{f^2}{R_\text{A}}$, josta $f_\text{C} = f \cdot \sqrt{\dfrac{R_\text{C}}{R_\text{A}}}$
**Muunnokset:** $f = 3{,}0 \cdot 10^{4}\,\text{Hz}$, $B_0 = 3{,}0 \cdot 10^{-3}\,\text{T}$, $r = 0{,}090\,\text{m}$ ja $1\,\text{kW} = 1000\,\text{W}$.
**Sijoitus:** a) $\Phi_0 = 3{,}0 \cdot 10^{-3}\,\text{T} \cdot \pi \cdot (0{,}090\,\text{m})^2 = 7{,}63 \cdot 10^{-5}\,\text{Wb}$ ja $e_0 = 2\pi \cdot 3{,}0 \cdot 10^{4}\,\text{Hz} \cdot 7{,}63 \cdot 10^{-5}\,\text{Wb} = 14{,}39\,\text{V}$. Tehot $P = \dfrac{(14{,}39\,\text{V})^2}{2R}$ ovat kattilalle A $2{,}59\,\text{kW}$, B $2{,}07\,\text{kW}$ ja C $1{,}29\,\text{kW}$.
b) $f_\text{C} = 30\,\text{kHz} \cdot \sqrt{\dfrac{0{,}080\,\Omega}{0{,}040\,\Omega}} = 30\,\text{kHz} \cdot \sqrt{2} = 42{,}43\,\text{kHz}$
**Vastaus:** $42\,\text{kHz}$, kaksi merkitsevää numeroa kuten lähtötiedot. Kattilan C resistanssi on kaksinkertainen, joten sen teho on puolet; taajuuden nosto kasvattaa vuon muutosnopeutta ja jännitettä, ja teho kasvaa taajuuden neliössä. c) Pyörrevirran oma magneettikenttä jätettiin huomiotta: Lenzin lain mukaan se vastustaa vuon muutosta, joten todellinen virta ja teho ovat mallin antamaa pienemmät. Hyvin johtavassa pohjassa (alumiini, kupari) pyörrevirran oma kenttä kumoaa suuren osan vuosta, joten malli ei päde niille; teräksen ferromagnetismi taas lisää lämpenemistä.
**Järkevyys:** Tehojen suhde $2{,}59\,\text{kW} : 1{,}29\,\text{kW} = 2{,}0$ vastaa resistanssien suhdetta $0{,}080 : 0{,}040 = 2{,}0$. Taajuuden nosto kertoimella $\sqrt{2} = 1{,}414$ kasvattaa tehon kertoimella $1{,}414^2 = 2{,}0$, joten kattilan C teho taajuudella $42{,}4\,\text{kHz}$ on $1{,}29\,\text{kW} \cdot 2{,}0 = 2{,}59\,\text{kW}$.
