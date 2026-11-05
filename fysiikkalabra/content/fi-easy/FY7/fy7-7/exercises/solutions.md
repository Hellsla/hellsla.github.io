## fy7-7-L1-01
**Annettu:** kierroksia $N = 300$, pinta-ala $A = 0{,}0030\,\text{m}^2$, magneettivuon tiheys $B = 0{,}15\,\text{T}$, pyörimistaajuus $f = 10\,\text{Hz}$
**Kysytty:** jännitteen huippuarvo $e_0$ voltteina
**Periaate:** Käämi pyörii tasaisesti homogeenisessa kentässä. Siksi sen läpi kulkeva vuo vaihtelee sinimuotoisesti ja käämiin syntyy sinimuotoinen vaihtojännite. Sen huippuarvo on $e_0 = NBA \cdot 2\pi f$. Jännite on suurin, kun käämin taso on kentän suuntainen ja vuo muuttuu nopeimmin.
**Kaava:** $e_0 = NBA \cdot 2\pi f$
**Muunnokset:** Ei tarvita: suureet ovat SI-yksiköissä, ja $\text{T} \cdot \text{m}^2 \cdot \tfrac{1}{\text{s}} = \text{V}$.
**Sijoitus:** $e_0 = 300 \cdot 0{,}15\,\text{T} \cdot 0{,}0030\,\text{m}^2 \cdot 2\pi \cdot 10\,\tfrac{1}{\text{s}} = 8{,}482\,\text{V}$
**Vastaus:** $8{,}5\,\text{V}$, kaksi merkitsevää numeroa kuten lähtöarvoissa.
**Järkevyys:** Pyöreillä luvuilla $300 \cdot 0{,}15\,\text{T} \cdot 0{,}003\,\text{m}^2 \approx 0{,}14\,\text{Wb}$, ja kun tämä kerrotaan luvulla $2\pi \cdot 10 \approx 60$, tulos on noin $8\,\text{V}$. Muutaman voltin jännite sopii käsin pyöritettävään opetusgeneraattoriin.

## fy7-7-L1-02
**Annettu:** jännitteen tehollinen arvo $U = 115\,\text{V}$, taajuus $400\,\text{Hz}$
**Kysytty:** jännitteen huippuarvo $U_0$ voltteina
**Periaate:** Vaihtojännite ilmoitetaan tehollisarvona. Sinimuotoisen jännitteen tehollinen arvo on huippuarvo jaettuna luvulla $\sqrt{2}$. Siksi huippuarvo on $\sqrt{2}$-kertainen. Taajuus ei vaikuta tähän suhteeseen.
**Kaava:** $U = \dfrac{U_0}{\sqrt{2}}$, josta $U_0 = \sqrt{2} \cdot U$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $U_0 = \sqrt{2} \cdot 115\,\text{V} = 162{,}63\,\text{V}$
**Vastaus:** $163\,\text{V}$, kolme merkitsevää numeroa kuten jännitteessä $115\,\text{V}$.
**Järkevyys:** Huippuarvo on noin $1{,}4$-kertainen tehollisarvoon nähden: $1{,}4 \cdot 115\,\text{V} \approx 161\,\text{V}$. Samalla tavalla kodin $230\,\text{V}$:n huippuarvo on noin $325\,\text{V}$.

## fy7-7-L1-03
**Annettu:** virran huippuarvo $I_0 = 8{,}5\,\text{A}$, virta sinimuotoinen
**Kysytty:** virran tehollinen arvo $I$ ampeereina
**Periaate:** Tehollinen arvo on se tasavirta, joka tuottaisi vastukseen saman keskimääräisen tehon. Sinimuotoisella virralla vastuksen teho on keskimäärin puolet huipputehosta. Siksi tehollinen arvo on huippuarvo jaettuna luvulla $\sqrt{2}$.
**Kaava:** $I = \dfrac{I_0}{\sqrt{2}}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $I = \dfrac{8{,}5\,\text{A}}{\sqrt{2}} = 6{,}010\,\text{A}$
**Vastaus:** $6{,}0\,\text{A}$, kaksi merkitsevää numeroa kuten huippuarvossa $8{,}5\,\text{A}$.
**Järkevyys:** Tehollinen arvo on noin $0{,}7$ kertaa huippuarvo: $0{,}7 \cdot 8{,}5\,\text{A} \approx 6\,\text{A}$. Verkkojännitteellä $230\,\text{V}$ tämä vastaa noin $1{,}4\,\text{kW}$:n tehoa, mikä sopii vedenkeittimeen.

## fy7-7-L1-04
**Annettu:** akseli tekee $1500$ kierrosta minuutissa
**Kysytty:** pyörimistaajuus $f$ hertseinä
**Periaate:** Pyörimistaajuus on kierrosten lukumäärä sekunnissa. Tässä kierrokset tiedetään minuutissa. Siksi ne jaetaan minuutin sekunneilla.
**Kaava:** $f = \dfrac{n}{t}$, missä $n$ on kierrosten lukumäärä ajassa $t$
**Muunnokset:** $t = 1\,\text{min} = 60\,\text{s}$
**Sijoitus:** $f = \dfrac{1500}{60\,\text{s}} = 25\,\tfrac{1}{\text{s}} = 25\,\text{Hz}$
**Vastaus:** $25\,\text{Hz}$. Lukema $1500$ kierrosta minuutissa on tarkka, joten tulos on täsmälleen $25\,\text{Hz}$.
**Järkevyys:** Verkon taajuus $50\,\text{Hz}$ vastaisi yhdellä magneettinapaparilla $3000$ kierrosta minuutissa. Tässä kierroksia on vain puolet siitä, joten taajuuskin olisi puolet. Siksi tällaisessa generaattorissa on kaksi napaparia, jotta jännitteen taajuus olisi $50\,\text{Hz}$.

## fy7-7-L1-05
**Annettu:** jännitteen tehollinen arvo $U = 230\,\text{V}$, virran tehollinen arvo $I = 4{,}35\,\text{A}$
**Kysytty:** keskimääräinen teho $P$ kilowatteina
**Periaate:** Tehollinen arvo on määritelty niin, että keskimääräinen teho lasketaan tehollisarvoista samalla kaavalla kuin tasavirralla. Lämmitin on vastus, joten jännite ja virta ovat samassa tahdissa.
**Kaava:** $P = UI$
**Muunnokset:** Tulos muunnetaan kilowateiksi: $1\,\text{kW} = 1000\,\text{W}$.
**Sijoitus:** $P = 230\,\text{V} \cdot 4{,}35\,\text{A} = 1000{,}5\,\text{W} = 1000{,}5 \cdot 0{,}001\,\text{kW} = 1{,}0005\,\text{kW}$
**Vastaus:** $1{,}00\,\text{kW}$, kolme merkitsevää numeroa kuten virrassa $4{,}35\,\text{A}$ ja jännitteessä $230\,\text{V}$.
**Järkevyys:** Tavallisen sähkölämmittimen teho on $0{,}5$–$2\,\text{kW}$. Huippuarvoilla laskettu teho olisi $2{,}00\,\text{kW}$, kaksinkertainen. Se on kuitenkin vain hetkellinen huippuarvo, ei keskiarvo.

## fy7-7-L1-06
**Kysytty:** mikä väite pistorasian jännitteestä $230\,\text{V}$ on oikein.
**Periaate:** Vaihtojännite ilmoitetaan tehollisarvona. Tehollinen arvo on se tasajännite, joka antaisi vastukseen saman keskimääräisen tehon. Sinimuotoisen jännitteen huippuarvo on tehollinen arvo kerrottuna luvulla $\sqrt{2}$. Siksi huippuarvo on suurempi kuin tehollinen arvo. Jännitteen keskiarvo yhden jakson yli on nolla. Siksi se ei kelpaa jännitteen suuruuden mitaksi.
**Mallivastaus:** Luku $230\,\text{V}$ on tehollinen arvo. Se tuottaa saman tehon kuin tasajännite. Huippuarvo on suurempi, noin $230\,\text{V} \cdot \sqrt{2} \approx 325\,\text{V}$. Väite, että luku on huippuarvo, on väärin, koska mittarit näyttävät tehollisarvon. Väite keskiarvosta on väärin, koska keskiarvo on nolla. Väite, että huippuarvo on tehollista arvoa pienempi, on väärin, koska huippuarvo on tehollista arvoa suurempi.

## fy7-7-L1-07
**Annettu:** pyörimisnopeus $3000$ kierrosta minuutissa
**Kysytty:** jännitteen jaksonaika $T$ millisekunteina
**Periaate:** Jännitteen taajuus on sama kuin käämin pyörimistaajuus. Jaksonaika on taajuuden käänteisluku. Ensin kierrokset minuutissa muutetaan kierroksiksi sekunnissa.
**Kaava:** $f = \dfrac{n}{t}$ ja $T = \dfrac{1}{f}$
**Muunnokset:** $t = 1\,\text{min} = 60\,\text{s}$ ja lopuksi $1\,\text{s} = 1000\,\text{ms}$
**Sijoitus:** $f = \dfrac{3000}{60\,\text{s}} = 50\,\text{Hz}$ ja $T = \dfrac{1}{50\,\tfrac{1}{\text{s}}} = 0{,}020\,\text{s} = 0{,}020 \cdot 1000\,\text{ms} = 20\,\text{ms}$
**Vastaus:** $20\,\text{ms}$. Lukema $3000$ kierrosta minuutissa on tarkka, joten tulos on täsmälleen $20\,\text{ms}$.
**Järkevyys:** Taajuus $50\,\text{Hz}$ on sähköverkon taajuus. Sen jaksonaika on $20\,\text{ms}$. Tarkistus: $50 \cdot 20\,\text{ms} = 1000\,\text{ms} = 1\,\text{s}$.

## fy7-7-L1-08
**Annettu:** sinimuotoisen jännitteen huippuarvo $U_0 = 17{,}0\,\text{V}$
**Kysytty:** yleismittarin näyttämä jännite $U$ voltteina
**Periaate:** Yleismittari näyttää vaihtojännitteen tehollisarvon. Sinimuotoisen jännitteen tehollinen arvo on huippuarvo jaettuna luvulla $\sqrt{2}$.
**Kaava:** $U = \dfrac{U_0}{\sqrt{2}}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $U = \dfrac{17{,}0\,\text{V}}{\sqrt{2}} = 12{,}02\,\text{V}$
**Vastaus:** $12{,}0\,\text{V}$, kolme merkitsevää numeroa kuten huippuarvossa $17{,}0\,\text{V}$.
**Järkevyys:** Tehollinen arvo on noin $0{,}7$ kertaa huippuarvo: $0{,}7 \cdot 17{,}0\,\text{V} \approx 12\,\text{V}$. Tulos on huippuarvoa pienempi, kuten pitääkin.

## fy7-7-L2-01
**Annettu:** kierroksia $N = 150$, käämin sivut $6{,}0\,\text{cm}$ ja $8{,}0\,\text{cm}$, magneettivuon tiheys $B = 0{,}25\,\text{T}$, pyörimisnopeus $1200$ kierrosta minuutissa
**Kysytty:** jännitteen huippuarvo $e_0$ voltteina
**Periaate:** Käämi pyörii tasaisesti homogeenisessa kentässä. Siksi siihen syntyy sinimuotoinen vaihtojännite, jonka huippuarvo on $e_0 = NBA \cdot 2\pi f$. Ensin lasketaan käämin pinta-ala ja pyörimistaajuus SI-yksiköissä.
**Kaava:** $A = ab$ ja $e_0 = NBA \cdot 2\pi f$
**Muunnokset:** $A = 6{,}0 \cdot 0{,}01\,\text{m} \cdot 8{,}0 \cdot 0{,}01\,\text{m} = 0{,}0048\,\text{m}^2$ ja $f = \dfrac{1200}{60\,\text{s}} = 20\,\text{Hz}$
**Sijoitus:** $e_0 = 150 \cdot 0{,}25\,\text{T} \cdot 0{,}0048\,\text{m}^2 \cdot 2\pi \cdot 20\,\tfrac{1}{\text{s}} = 22{,}62\,\text{V}$
**Vastaus:** $23\,\text{V}$, kaksi merkitsevää numeroa kuten käämin mitoissa ja magneettivuon tiheydessä.
**Järkevyys:** Pyöreillä luvuilla $150 \cdot 0{,}25\,\text{T} \cdot 0{,}005\,\text{m}^2 \approx 0{,}19\,\text{Wb}$ ja $2\pi \cdot 20\,\tfrac{1}{\text{s}} \approx 125\,\tfrac{1}{\text{s}}$, joten $e_0 \approx 23\,\text{V}$. Jos pyörimisnopeutta $1200$ olisi käytetty hertseinä, tulos olisi $60$-kertainen.

## fy7-7-L2-02
**Annettu:** kierroksia $N = 200$, pinta-ala $A = 30\,\text{cm}^2$, kuvaajasta luettu huippuarvo ja jaksonaika
**Kysytty:** magneettivuon tiheys $B$ tesloina
**Periaate:** Käämi pyörii tasaisesti homogeenisessa kentässä. Siksi sen jännite on sinimuotoinen ja huippuarvo on $e_0 = NBA \cdot 2\pi f$. Kuvaajasta saadaan huippuarvo ja jaksonaika. Jaksonajasta saadaan pyörimistaajuus $f = 1 : T$.
**Kuvaajan lukeminen:** Käyrän huiput ovat ruudukon viivalla $12\,\text{V}$ (hetkillä $10\,\text{ms}$ ja $50\,\text{ms}$), joten $e_0 = 12\,\text{V}$. Käyrä on nolla ja nousemassa hetkillä $0\,\text{ms}$, $40\,\text{ms}$ ja $80\,\text{ms}$. Siksi yksi jakso kestää $T = 40\,\text{ms}$.
**Kaava:** $f = \dfrac{1}{T}$ ja $e_0 = NBA \cdot 2\pi f$, josta $B = \dfrac{e_0}{NA \cdot 2\pi f} = \dfrac{e_0 T}{NA \cdot 2\pi}$
**Muunnokset:** $T = 40\,\text{ms} = 40 \cdot 0{,}001\,\text{s} = 0{,}040\,\text{s}$ ja $A = 30\,\text{cm}^2 = 30 \cdot 0{,}0001\,\text{m}^2 = 0{,}0030\,\text{m}^2$
**Sijoitus:** $f = \dfrac{1}{0{,}040\,\text{s}} = 25\,\text{Hz}$ ja $B = \dfrac{12\,\text{V}}{200 \cdot 0{,}0030\,\text{m}^2 \cdot 2\pi \cdot 25\,\tfrac{1}{\text{s}}} = \dfrac{12\,\text{V}}{94{,}25\,\tfrac{\text{m}^2}{\text{s}}} = 0{,}1273\,\text{T}$
**Vastaus:** $0{,}13\,\text{T}$. Vastauksessa on kaksi merkitsevää numeroa, koska kuvaajasta luetut arvot $12\,\text{V}$ ja $40\,\text{ms}$ ovat kahden numeron tarkkuudella.
**Järkevyys:** Kestomagneetin kenttä on tyypillisesti kymmenesosia teslaa, joten $0{,}13\,\text{T}$ on uskottava. Tarkistus: $200 \cdot 0{,}13\,\text{T} \cdot 0{,}0030\,\text{m}^2 \cdot 2\pi \cdot 25\,\tfrac{1}{\text{s}} \approx 12{,}3\,\text{V}$, mikä vastaa kuvaajan huippua.

## fy7-7-L2-03
**Annettu:** jännitteen tehollinen arvo $U = 12\,\text{V}$, kierroksia $N = 200$, pinta-ala $A = 0{,}0050\,\text{m}^2$, magneettivuon tiheys $B = 0{,}30\,\text{T}$
**Kysytty:** pyörimistaajuus $f$ hertseinä
**Periaate:** Pyörivän käämin jännite on sinimuotoinen, ja sen huippuarvo on $e_0 = NBA \cdot 2\pi f$. Annettu $12\,\text{V}$ on tehollinen arvo, joten huippuarvo on $\sqrt{2}$-kertainen. Pyörimistaajuus ratkaistaan huippuarvon kaavasta.
**Kaava:** $e_0 = \sqrt{2} \cdot U$ ja $e_0 = NBA \cdot 2\pi f$, josta $f = \dfrac{\sqrt{2} \cdot U}{NBA \cdot 2\pi}$
**Muunnokset:** Ei tarvita: suureet ovat SI-yksiköissä.
**Sijoitus:** $e_0 = \sqrt{2} \cdot 12\,\text{V} = 16{,}97\,\text{V}$ ja $f = \dfrac{16{,}97\,\text{V}}{200 \cdot 0{,}30\,\text{T} \cdot 0{,}0050\,\text{m}^2 \cdot 2\pi} = \dfrac{16{,}97\,\text{V}}{1{,}885\,\text{V}\cdot\text{s}} = 9{,}003\,\text{Hz}$
**Vastaus:** $9{,}0\,\text{Hz}$, kaksi merkitsevää numeroa kuten jännitteessä $12\,\text{V}$ ja kentässä $0{,}30\,\text{T}$.
**Järkevyys:** Yhdeksän kierrosta sekunnissa on vauhdikasta mutta mahdollista kammella, jossa on välitys. Jos tehollinen arvo olisi sijoitettu huippuarvon paikalle, taajuudeksi olisi tullut liian pieni $6{,}4\,\text{Hz}$. Silloin jännitteen tehollinen arvo olisi jäänyt alle $12\,\text{V}$:n.

## fy7-7-L2-04
**Annettu:** tuotettu sähköenergia $E = 19{,}8\,\text{TWh}$ vuonna 2024, vuoden pituus $366$ vuorokautta, nimellisteho vuoden lopussa $P_\text{n} = 8358\,\text{MW}$ (Suomen Uusiutuvat ry)
**Kysytty:** keskimääräisen tehon osuus nimellistehosta prosentteina
**Periaate:** Keskimääräinen teho on vuoden aikana tuotettu energia jaettuna vuoden pituudella. Tuulivoimalat tuottavat nimellistehonsa eli suurimman tehonsa vain kovalla tuulella. Siksi keskiteho on selvästi nimellistehoa pienempi. Osuus saadaan jakamalla keskiteho nimellisteholla.
**Kaava:** $P = \dfrac{E}{t}$ ja osuus $= \dfrac{P}{P_\text{n}} \cdot 100\,\%$
**Muunnokset:** $t = 366 \cdot 24\,\text{h} = 8784\,\text{h}$, $E = 19{,}8\,\text{TWh} = 19{,}8 \cdot 10^{12}\,\text{Wh}$ ja $P_\text{n} = 8358\,\text{MW} = 8358 \cdot 10^{6}\,\text{W}$
**Sijoitus:** $P = \dfrac{19{,}8 \cdot 10^{12}\,\text{Wh}}{8784\,\text{h}} = 2{,}254 \cdot 10^{9}\,\text{W}$ ja osuus $= \dfrac{2{,}254 \cdot 10^{9}\,\text{W}}{8358 \cdot 10^{6}\,\text{W}} \cdot 100\,\% = 26{,}97\,\%$
**Vastaus:** $27\,\%$. Vastauksessa on kaksi merkitsevää numeroa, koska tuotanto $19{,}8\,\text{TWh}$ on ilmoitettu kolmella numerolla ja tulos on arvio.
**Järkevyys:** Tuulivoimaloiden keskiteho on tyypillisesti neljännes tai kolmannes nimellistehosta, joten $27\,\%$ on uskottava. Todellinen osuus on hieman suurempi. Nimellisteho kasvoi vuoden aikana, joten alkuvuonna voimaloita oli vähemmän kuin vuoden lopussa.

## fy7-7-L2-05
**Annettu:** taulukon $14$ mittapistettä, joissa jännite $e$ on ajan $t$ funktiona; jännite on sinimuotoinen
**Kysytty:** a) jaksonaika $T$ ja taajuus $f$, b) huippuarvo $e_0$, c) tehollinen arvo $U$ voltteina
**Periaate:** Jaksonaika on aika, jonka kuluttua jännite on taas samassa arvossa ja kulkee samaan suuntaan. Huippuarvo on jännitteen itseisarvon suurin arvo. Tehollinen arvo on huippuarvo jaettuna luvulla $\sqrt{2}$.
**Kuvaajan lukeminen:** Taulukossa jännite on nolla ja nousemassa hetkellä $0\,\text{ms}$ (arvo $0{,}1\,\text{V}$). Se on taas nolla ja nousemassa hetkellä $24\,\text{ms}$ (arvo $0{,}0\,\text{V}$). Siksi $T = 24\,\text{ms}$. Jännite on nolla myös hetkellä $12\,\text{ms}$ (arvo $-0{,}1\,\text{V}$) eli jakson puolivälissä. Suurin jännite on $8{,}4\,\text{V}$ hetkellä $6\,\text{ms}$ ja pienin $-8{,}4\,\text{V}$ hetkellä $18\,\text{ms}$. Siksi $e_0 = 8{,}4\,\text{V}$.
**Kaava:** $f = \dfrac{1}{T}$ ja $U = \dfrac{e_0}{\sqrt{2}}$
**Muunnokset:** $T = 24\,\text{ms} = 24 \cdot 0{,}001\,\text{s} = 0{,}024\,\text{s}$
**Sijoitus:** $f = \dfrac{1}{0{,}024\,\text{s}} = 41{,}7\,\text{Hz}$ ja $U = \dfrac{8{,}4\,\text{V}}{\sqrt{2}} = 5{,}94\,\text{V}$
**Vastaus:** a) $T = 24\,\text{ms}$ ja $f \approx 42\,\text{Hz}$, b) $e_0 = 8{,}4\,\text{V}$, c) $U \approx 5{,}9\,\text{V}$. Tulos kirjataan kahdella merkitsevällä numerolla, kuten jännitteen huippuarvo.
**Järkevyys:** Tehollinen arvo on noin $0{,}7$ kertaa huippuarvo: $0{,}7 \cdot 8{,}4\,\text{V} \approx 5{,}9\,\text{V}$. Jännite nousee nollasta huippuarvoon $8{,}4\,\text{V}$ neljänneksessä jaksosta, kuten sinikäyrällä: $24\,\text{ms} : 4 = 6\,\text{ms}$. Taulukossa huippu on hetkellä $6\,\text{ms}$.

## fy7-7-L2-06
**Annettu:** pyörimistaajuus $f_1 = 5{,}0\,\text{Hz}$ ja huippuarvo $e_{0,1} = 4{,}1\,\text{V}$; pyörimistaajuus $f_2 = 10{,}0\,\text{Hz}$ ja mitattu huippuarvo $e_{0,2} = 8{,}0\,\text{V}$; $N$, $B$ ja $A$ samat
**Kysytty:** a) ennustettu huippuarvo taajuudella $f_2$, b) mittauksen poikkeama ennusteesta prosentteina, c) taajuuden muutos ja mittauksen sopivuus
**Periaate:** Huippuarvo $e_0 = NBA \cdot 2\pi f$ on suoraan verrannollinen pyörimistaajuuteen, kun $N$, $B$ ja $A$ pysyvät samoina. Kaksinkertainen pyörimistaajuus antaa siis kaksinkertaisen huippuarvon. Poikkeama on ennusteen ja mittauksen erotus suhteessa ennusteeseen.
**Kaava:** $e_{0,2} = e_{0,1} \cdot \dfrac{f_2}{f_1}$ ja poikkeama $= \dfrac{|e_{0,\text{ennuste}} - e_{0,\text{mitattu}}|}{e_{0,\text{ennuste}}} \cdot 100\,\%$
**Muunnokset:** Ei tarvita: suhde $f_2 : f_1$ on lukuarvo.
**Sijoitus:** a) $e_{0,\text{ennuste}} = 4{,}1\,\text{V} \cdot \dfrac{10{,}0\,\text{Hz}}{5{,}0\,\text{Hz}} = 8{,}2\,\text{V}$. b) Poikkeama $= \dfrac{|8{,}2\,\text{V} - 8{,}0\,\text{V}|}{8{,}2\,\text{V}} \cdot 100\,\% = 2{,}44\,\%$
**Vastaus:** Poikkeama on $2{,}4\,\%$. c) Jännitteen taajuus on sama kuin pyörimistaajuus, joten sekin kaksinkertaistuu. Jaksonaika puolittuu arvosta $200\,\text{ms}$ arvoon $100\,\text{ms}$. Kunkin huippuarvon lukemisen epävarmuus on $\pm 0{,}1\,\text{V}$. Ennuste $2 \cdot 4{,}1\,\text{V}$ kaksinkertaistaa lukeman epävarmuuden ($\pm 0{,}2\,\text{V}$). Mitatun arvon epävarmuus $\pm 0{,}1\,\text{V}$ tulee siihen lisäksi, joten yhteensä epävarmuus on noin $\pm 0{,}3\,\text{V}$. Erotus $0{,}2\,\text{V}$ on tätä pienempi. Mittaus ei siis poikkea ennusteesta enempää kuin lukematarkkuus sallii. Eroa verrannollisuudesta ei voida osoittaa, ja mittaus sopii ennusteeseen.
**Järkevyys:** Kaksinkertaisella taajuudella huippuarvo on lähes kaksinkertainen: $8{,}0 : 4{,}1 = 1{,}95$. Jos huippuarvo riippuisi taajuudesta jotenkin muuten, esimerkiksi neliöllisesti, tulos olisi ollut noin $16\,\text{V}$.

## fy7-7-L2-07
**Annettu:** lampun teho $P = 60\,\text{W}$, verkkojännite $230\,\text{V}$; oppilaan ratkaisussa $230\,\text{V}$ on tulkittu huippuarvoksi ja virraksi on saatu $0{,}37\,\text{A}$
**Kysytty:** a) oppilaan virhe, b) lampun virran tehollinen arvo $I$ ampeereina
**Periaate:** Verkkojännite $230\,\text{V}$ on jo tehollinen arvo, koska vaihtojännite ilmoitetaan tehollisarvona. Keskimääräinen teho lasketaan tehollisarvoista samoin kuin tasavirralla: $P = UI$. Siksi virran tehollinen arvo saadaan suoraan tehosta ja tehollisesta jännitteestä. Huippuarvolla ei tarvitse laskea mitään.
**Kaava:** $P = UI$, josta $I = \dfrac{P}{U}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $I = \dfrac{60\,\text{W}}{230\,\text{V}} = 0{,}2609\,\text{A}$
**Vastaus:** a) Oppilas luuli verkkojännitettä huippuarvoksi ja jakoi sen luvulla $\sqrt{2}$. Pistorasian jännite on kuitenkin jo tehollinen arvo. Tehollinen jännite on siis $230\,\text{V}$, ei $163\,\text{V}$. Kun jännite oli liian pieni, virta tuli liian suureksi. b) Virran tehollinen arvo on $0{,}26\,\text{A}$, kaksi merkitsevää numeroa kuten tehossa $60\,\text{W}$.
**Järkevyys:** Tarkistus: $230\,\text{V} \cdot 0{,}26\,\text{A} \approx 60\,\text{W}$. Oppilaan tulos $0{,}37\,\text{A}$ olisi antanut tehoksi $230\,\text{V} \cdot 0{,}37\,\text{A} = 85\,\text{W}$. Se ei ole $60\,\text{W}$.

## fy7-7-L3-01
**Annettu:** jännitteen huippuarvo $e_0 = 20{,}0\,\text{V}$, hetkellä $t = 0$ käämin taso on kohtisuorassa kenttää vastaan, käämi kääntyy tästä asennosta $30^\circ$
**Kysytty:** jännitteen hetkellinen arvo $e$ voltteina
**Periaate:** Kun käämin taso on kohtisuorassa kenttää vastaan, vuo on suurin eikä hetkeen muutu. Silloin jännite on nolla. Siitä lähtien jännite kasvaa sinin tavoin, $e = e_0 \sin\theta$. Tässä $\theta$ on kulma, jonka käämi on kääntynyt tästä asennosta. Jännite on huippuarvossaan kulmassa $90^\circ$, kun käämin taso on kentän suuntainen.
**Kaava:** $e = e_0 \sin\theta$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $e = 20{,}0\,\text{V} \cdot \sin 30^\circ = 20{,}0\,\text{V} \cdot 0{,}5 = 10{,}0\,\text{V}$
**Vastaus:** $10{,}0\,\text{V}$, kolme merkitsevää numeroa kuten huippuarvossa $20{,}0\,\text{V}$.
**Järkevyys:** Kulma $30^\circ$ on kolmasosa matkasta nollajännitteen asennosta huippuasentoon. Jännite on silti jo puolet huippuarvosta, koska sinikäyrä nousee alussa jyrkimmin. Kosinilla laskettu $17{,}3\,\text{V}$ olisi väärin, koska se antaisi suurimman jännitteen asennossa, jossa vuo ei muutu.

## fy7-7-L3-02
**Annettu:** generaattorin jännitteen huippuarvo $U_0 = 40\,\text{V}$, vastus $R = 40\,\Omega$, generaattorin resistanssi mitätön
**Kysytty:** vastuksen keskimääräinen teho $P$ watteina
**Periaate:** Generaattorin resistanssi on mitätön, joten koko jännite on vastuksen yli. Keskimääräinen teho lasketaan tehollisarvoilla kuten tasavirralla: $P = UI$. Ohmin lain mukaan $I = U : R$, joten $P = U^2 : R$. Huippuarvolla laskettu teho olisi vain hetkellinen huipputeho.
**Kaava:** $U = \dfrac{U_0}{\sqrt{2}}$ ja $P = UI = \dfrac{U^2}{R} = \dfrac{U_0^2}{2R}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $U = \dfrac{40\,\text{V}}{\sqrt{2}} = 28{,}28\,\text{V}$ ja $P = \dfrac{(28{,}28\,\text{V})^2}{40\,\Omega} = \dfrac{800\,\text{V}^2}{40\,\Omega} = 20\,\text{W}$
**Vastaus:** $20\,\text{W}$, kaksi merkitsevää numeroa kuten jännitteessä $40\,\text{V}$ ja resistanssissa $40\,\Omega$.
**Järkevyys:** Hetkellinen huipputeho on $U_0^2 : R = 1600\,\text{V}^2 : 40\,\Omega = 40\,\text{W}$, ja keskiarvo on puolet siitä, koska teho vaihtelee nollan ja huippuarvon välillä. Yksiköt: $\tfrac{\text{V}^2}{\Omega} = \text{V} \cdot \text{A} = \text{W}$.

## fy7-7-L3-03
**Annettu:** tehollinen jännite $U_1 = 690\,\text{V}$ pyörimisnopeudella $15$ kierrosta minuutissa, uusi pyörimisnopeus $9{,}0$ kierrosta minuutissa, magneetit ja käämit samat
**Kysytty:** uusi tehollinen jännite $U_2$ voltteina
**Periaate:** Generaattorin huippujännite on $e_0 = NBA \cdot 2\pi f$. Kun $N$, $B$ ja $A$ pysyvät samoina, huippujännite on suoraan verrannollinen pyörimistaajuuteen. Silloin myös tehollinen arvo $U = e_0 : \sqrt{2}$ on suoraan verrannollinen pyörimistaajuuteen. Suoravetoisessa voimalassa generaattori pyörii samaa tahtia kuin roottori. Siksi taajuus on verrannollinen roottorin kierroksiin minuutissa.
**Kaava:** $\dfrac{U_2}{U_1} = \dfrac{f_2}{f_1}$, josta $U_2 = U_1 \cdot \dfrac{f_2}{f_1}$
**Muunnokset:** Ei tarvita. Suhteessa kierrokset minuutissa supistuvat pois, joten niitä ei tarvitse muuntaa hertseiksi.
**Sijoitus:** $U_2 = 690\,\text{V} \cdot \dfrac{9{,}0}{15} = 690\,\text{V} \cdot 0{,}60 = 414\,\text{V}$
**Vastaus:** noin $410\,\text{V}$, kaksi merkitsevää numeroa kuten pyörimisnopeuksissa $15$ ja $9{,}0$ kierrosta minuutissa.
**Järkevyys:** Pyörimisnopeus pieneni $40\,\%$, joten myös jännite pienenee $40\,\%$. Samalla jännitteen taajuus pienenee. Siksi tuulivoimalassa tarvitaan taajuusmuuttaja, joka sovittaa sekä jännitteen että taajuuden verkkoon.

## fy7-7-L3-04
**Annettu:** pullodynamon käämissä kierroksia $N = 240$, pinta-ala $A = 6{,}0\,\text{cm}^2$, taulukon kuusi mittapistettä $(f, e_0)$
**Kysytty:** a) suoran $e_0 = kf + c$ kulmakerroin $k$, b) magneettivuon tiheys $B$ ja perustelu sille, miksi suoran pitäisi kulkea origon kautta, c) huippuarvo taajuudella $22\,\text{Hz}$ ja vakiotermin merkitys
**Periaate:** Huippuarvo $e_0 = NBA \cdot 2\pi f$ on pyörimistaajuuden lineaarinen funktio. Sen kulmakerroin on $k = NBA \cdot 2\pi$. Mittapisteisiin sovitetaan suora laskimen lineaarisella sovituksella (tai silmämääräisesti), ja kulmakertoimesta ratkaistaan $B$. Pyörimättömässä käämissä jännite on nolla, joten suoran pitäisi kulkea origon kautta. Pullodynamon rulla pyörii rengasta vasten, ja taajuus $f$ on rullan ja käämin pyörimistaajuus.
**Kaava:** $k = NBA \cdot 2\pi$, josta $B = \dfrac{k}{NA \cdot 2\pi}$
**Muunnokset:** $A = 6{,}0\,\text{cm}^2 = 6{,}0 \cdot 0{,}0001\,\text{m}^2 = 6{,}0 \cdot 10^{-4}\,\text{m}^2$
**Sijoitus:** a) Tarkistus kahdella ääripisteellä: $k \approx \dfrac{(9{,}1 - 1{,}4)\,\text{V}}{(30 - 5)\,\text{Hz}} = 0{,}308\,\tfrac{\text{V}}{\text{Hz}}$. Laskimen sovitus antaa $k = 0{,}308\,\tfrac{\text{V}}{\text{Hz}} = 0{,}308\,\text{V}\cdot\text{s}$ ja $c = -0{,}107\,\text{V}$. b) $B = \dfrac{0{,}308\,\text{V}\cdot\text{s}}{240 \cdot 6{,}0 \cdot 10^{-4}\,\text{m}^2 \cdot 2\pi} = \dfrac{0{,}308\,\text{V}\cdot\text{s}}{0{,}9048\,\text{m}^2} = 0{,}3404\,\text{T}$. c) $e_0 = 0{,}308\,\tfrac{\text{V}}{\text{Hz}} \cdot 22\,\text{Hz} - 0{,}107\,\text{V} = 6{,}67\,\text{V}$; ilman vakiotermiä tulos olisi $6{,}78\,\text{V}$.
**Vastaus:** b) $B \approx 0{,}34\,\text{T}$, kaksi merkitsevää numeroa kuten käämin pinta-alassa. Kaavassa $e_0$ on suoraan verrannollinen taajuuteen, joten jännitteen pitäisi olla nolla, kun $f = 0$. Vakiotermi $c = -0{,}11\,\text{V}$ on pieni. Se johtuu todennäköisesti mittausvirheestä, kuten oskilloskoopin nollakohdasta tai lukematarkkuudesta ($\pm 0{,}1\,\text{V}$). c) $e_0 \approx 6{,}7\,\text{V}$. Vakiotermi muuttaa ennustetta vain $1{,}6\,\%$, joten sillä ei ole merkitystä.
**Järkevyys:** Kestomagneetin kenttä on tyypillisesti kymmenesosia teslaa, joten $0{,}34\,\text{T}$ on uskottava. Tarkistus: suora antaa taajuudella $30\,\text{Hz}$ arvon $9{,}13\,\text{V}$. Se vastaa mitattua arvoa $9{,}1\,\text{V}$.

## fy7-7-L3-05
**Annettu:** $N = 120$, $A = 0{,}0050\,\text{m}^2$, $B = 0{,}20\,\text{T}$, vastus $R = 8{,}0\,\Omega$, generaattorin resistanssi mitätön, pyörimistaajuudet $f_1 = 25\,\text{Hz}$ ja $f_2 = 40\,\text{Hz}$
**Kysytty:** a) huippuarvot $e_0$ ja tehollisarvot $U$ kummallakin taajuudella, b) vastuksen keskimääräiset tehot $P_1$ ja $P_2$ sekä suurin hetkellinen teho $p_{\max}$ taajuudella $f_2$, c) perustelu tehon kasvulle
**Periaate:** Huippuarvo on $e_0 = NBA \cdot 2\pi f$, ja tehollinen arvo on $U = e_0 : \sqrt{2}$. Koko jännite on vastuksen yli, ja keskimääräinen teho on $P = U^2 : R$. Hetkellinen teho $p = e^2 : R$ vaihtelee nollan ja huippuarvon $e_0^2 : R$ välillä.
**Kaava:** $e_0 = NBA \cdot 2\pi f$, $U = \dfrac{e_0}{\sqrt{2}}$, $P = \dfrac{U^2}{R}$ ja $p_{\max} = \dfrac{e_0^2}{R}$
**Muunnokset:** Ei tarvita: suureet ovat SI-yksiköissä.
**Sijoitus:** a) $NBA = 120 \cdot 0{,}20\,\text{T} \cdot 0{,}0050\,\text{m}^2 = 0{,}12\,\text{Wb}$. Taajuudella $f_1$: $e_{0,1} = 0{,}12\,\text{Wb} \cdot 2\pi \cdot 25\,\text{Hz} = 18{,}85\,\text{V}$ ja $U_1 = \dfrac{18{,}85\,\text{V}}{\sqrt{2}} = 13{,}33\,\text{V}$. Taajuudella $f_2$: $e_{0,2} = 0{,}12\,\text{Wb} \cdot 2\pi \cdot 40\,\text{Hz} = 30{,}16\,\text{V}$ ja $U_2 = \dfrac{30{,}16\,\text{V}}{\sqrt{2}} = 21{,}33\,\text{V}$. b) $P_1 = \dfrac{(13{,}33\,\text{V})^2}{8{,}0\,\Omega} = 22{,}2\,\text{W}$ ja $P_2 = \dfrac{(21{,}33\,\text{V})^2}{8{,}0\,\Omega} = 56{,}8\,\text{W}$. Suurin hetkellinen teho on $p_{\max} = \dfrac{(30{,}16\,\text{V})^2}{8{,}0\,\Omega} = 113{,}7\,\text{W}$.
**Vastaus:** b) Keskimääräinen teho on $P_2 \approx 57\,\text{W}$ pyörimistaajuudella $40\,\text{Hz}$, kaksi merkitsevää numeroa kuten käämin ja vastuksen arvot. Pyörimistaajuudella $25\,\text{Hz}$ teho on $22\,\text{W}$, ja suurin hetkellinen teho on $1{,}1 \cdot 10^{2}\,\text{W}$. c) Huippujännite on verrannollinen taajuuteen, ja teho on verrannollinen jännitteen neliöön. Siksi teho on verrannollinen taajuuden neliöön: $1{,}6^2 = 2{,}56$. Teho kasvaa siis $2{,}56$-kertaiseksi, ei $1{,}6$-kertaiseksi.
**Järkevyys:** Tarkistus: $P_2 : P_1 = 56{,}8\,\text{W} : 22{,}2\,\text{W} = 2{,}56$. Se vastaa lukua $1{,}6^2$. Keskimääräinen teho $56{,}8\,\text{W}$ on puolet huipputehosta $113{,}7\,\text{W}$, kuten sinimuotoisella jännitteellä pitääkin. Yksiköt: $\tfrac{\text{V}^2}{\Omega} = \text{W}$.
