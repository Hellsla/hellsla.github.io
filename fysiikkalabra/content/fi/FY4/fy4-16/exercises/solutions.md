## fy4-16-L1-01
**Annettu:** $m = 70{,}0\,\text{kg}$, hissin kiihtyvyys $a = 0{,}80\,\text{m/s}^2$ ylöspäin; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** lattian tukivoima $N$ yksikössä $\text{N}$
**Periaate:** Ihminen seisoo hississä paikallaan, joten hän kiihtyy hissin mukana. Newtonin toisen lain mukaan kiihtyvyyden määrää kokonaisvoima, joten ylöspäin kiihtyvässä hississä tukivoiman on oltava painoa suurempi.
**Voimakuvio:** Ihminen suorakulmiona, positiivinen suunta ylös. Paino $\overline{G}$ keskipisteestä alas ja lattian tukivoima $\overline{N}$ alhaalta ylös alapintaan asti, painoa pidempänä. Kiihtyvyys ylös merkitään erikseen eikä voimaksi.
```voimakuvio
pinta 0
G 686,7
N 742,7 työntö
a ylös
```
**Kaava:** $N - mg = ma$, joten $N = m(g + a)$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $N = 70{,}0\,\text{kg}\cdot(9{,}81 + 0{,}80)\,\text{m/s}^2 = 70{,}0\,\text{kg}\cdot 10{,}61\,\text{m/s}^2 = 742{,}7\,\text{N}$
**Vastaus:** $743\,\text{N}$ ylöspäin, kolme merkitsevää numeroa kuten massassa $70{,}0\,\text{kg}$.
**Järkevyys:** Paino on $70{,}0\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \approx 687\,\text{N}$, ja tukivoima on siitä $ma = 56\,\text{N}$ suurempi, noin $8\,\%$. Kiihtyvyys on noin $8\,\%$ putoamiskiihtyvyydestä, joten osuus täsmää.

## fy4-16-L1-02
**Annettu:** $m = 90{,}0\,\text{kg}$, ilmanvastus $F_\text{v} = 2{,}10\,\text{kN}$, hyppääjä liikkuu alas; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** kokonaisvoima $\Sigma F$ yksikössä $\text{kN}$ ja sen suunta
**Periaate:** Hyppääjään vaikuttavat Maa (paino) ja ilma (ilmanvastus). Kokonaisvoima on voimien vektorisumma. Hyppääjä liikkuu alas, joten ilmanvastus osoittaa ylös, painoa vastaan.
**Voimakuvio:** Hyppääjä varjoineen suorakulmiona, positiivinen suunta ylös. Paino $\overline{G}$ keskipisteestä alas ja ilmanvastus $\overline{F}_\text{v}$ yläpinnasta ylös, yli kaksi kertaa painon pituisena.
```voimakuvio
G 882,9
F_v 2100 ylös
a ylös
```
**Kaava:** $\Sigma F = F_\text{v} - G$, ja $G = mg$, joten $\Sigma F = F_\text{v} - mg$
**Muunnokset:** $2{,}10\,\text{kN} = 2{,}10\cdot 1000\,\text{N} = 2100\,\text{N}$; tulos muutetaan lopuksi takaisin kilonewtoneiksi.
**Sijoitus:** $\Sigma F = 2100\,\text{N} - 90{,}0\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 2100\,\text{N} - 882{,}9\,\text{N} = 1217{,}1\,\text{N} \approx 1{,}22\,\text{kN}$
**Vastaus:** $1{,}22\,\text{kN}$ ylöspäin, kolme merkitsevää numeroa kuten massassa $90{,}0\,\text{kg}$ ja ilmanvastuksessa $2{,}10\,\text{kN}$.
**Järkevyys:** Ilmanvastus on noin $2{,}4$ kertaa paino $883\,\text{N}$, joten ylöspäin jää noin $1{,}4$ painon verran eli noin $1{,}2\,\text{kN}$. Kokonaisvoima osoittaa ylös, vaikka hyppääjä liikkuu alas, joten hän hidastuu.

## fy4-16-L1-03
**Annettu:** korkeusero $h = 3{,}20\,\text{m}$, alkunopeus $v_1 = 0$, kitka ja ilmanvastus jätetään huomiotta; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** nopeus $v_2$ kourun lopussa yksikössä $\text{m/s}$
**Voimakuvio:** Lapsi suorakulmiona, kourun pinnan suuntaan kallistettuna. Paino $\overline{G}$ keskipisteestä suoraan alas ja kourun tukivoima $\overline{N}$ alapinnasta kohtisuoraan pinnasta ulos. Kitkaa ei ole, eikä liikesuuntaan osoittavaa voimaa. Nopeus merkitään erikseen eikä voimaksi.
```voimakuvio
pinta -30
G 300
N 259,8
a alas
v alas
```
**Periaate:** Lapseen vaikuttavat paino ja kourun tukivoima. Tukivoima on kohtisuorassa liikettä vastaan eikä tee työtä, ja kitka jätetään huomiotta, joten mekaaninen energia säilyy. Kourun muodolla ei ole merkitystä, vain korkeuserolla.
**Kaava:** Nollataso kourun loppuun: $mgh = \tfrac12 mv_2^2$, joten $v_2 = \sqrt{2gh}$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita. Massaa ei tarvita, koska se supistuu pois.
**Sijoitus:** $v_2 = \sqrt{2\cdot 9{,}81\,\text{m/s}^2\cdot 3{,}20\,\text{m}} = \sqrt{62{,}78\,\text{m}^2/\text{s}^2} = 7{,}924\,\text{m/s}$
**Vastaus:** $7{,}92\,\text{m/s}$, kolme merkitsevää numeroa kuten korkeudessa $3{,}20\,\text{m}$.
**Järkevyys:** $7{,}9\,\text{m/s}$ on noin $29\,\text{km/h}$, mikä sopii jäiseen kouruun. Todellisuudessa kitka ja ilmanvastus pienentävät nopeutta hieman, joten tulos on yläraja.

## fy4-16-L1-04
**Annettu:** alkunopeus $v_1 = 6{,}0\,\text{m/s}$, loppunopeus $v_2 = 0$, $\mu = 0{,}080$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** liukumismatka $s$ yksikössä $\text{m}$
**Periaate:** Kysytään matkaa, jolla liike-energia kuluu, joten käytetään energiaperiaatetta. Korkeus ei muutu, ja kitka on ainoa työtä tekevä voima: sen negatiivinen työ muuttaa liike-energian sisäenergiaksi. Kitkavoima saadaan voimakuviosta.
**Voimakuvio:** Pulkka suorakulmiona. Paino $\overline{G}$ keskipisteestä alas, lumen tukivoima $\overline{N}$ alapinnasta ylös yhtä pitkänä ja liikekitka $\overline{F}_\mu$ alapinnan takakulmasta taaksepäin. Eteenpäin osoittavaa voimaa ei ole. Pystysuunnassa $N - mg = 0$, joten $F_\mu = \mu mg$.
```voimakuvio
pinta 0
G 100
N 100
F_mu 8 vasen
a vasen
```
**Kaava:** $\tfrac12 mv_1^2 - \mu mg s = 0$, joten $s = \dfrac{v_1^2}{2\mu g}$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita. Massa supistuu pois.
**Sijoitus:** $s = \dfrac{(6{,}0\,\text{m/s})^2}{2\cdot 0{,}080\cdot 9{,}81\,\text{m/s}^2} = \dfrac{36\,\text{m}^2/\text{s}^2}{1{,}5696\,\text{m/s}^2} = 22{,}94\,\text{m}$
**Vastaus:** $23\,\text{m}$, kaksi merkitsevää numeroa kuten nopeudessa $6{,}0\,\text{m/s}$ ja kitkakertoimessa $0{,}080$.
**Järkevyys:** Hidastuvuus on $\mu g \approx 0{,}8\,\text{m/s}^2$, joten pysähtyminen kestää noin $6\,\text{s} : 0{,}8 \approx 7{,}5\,\text{s}$, ja keskinopeudella $3\,\text{m/s}$ matka on noin $23\,\text{m}$. Pulkkamäen tasaisella tämä on tavallinen liukumismatka.

## fy4-16-L1-05
**Annettu:** $\mu = 0{,}15$, nopeus on vakio, ilmanvastus jätetään huomiotta
**Kysytty:** rinteen kaltevuuskulma $\alpha$ asteina
**Periaate:** Nopeus on vakio, joten Newtonin toisen lain mukaan kokonaisvoima on nolla sekä rinteen suunnassa että sitä vastaan kohtisuorassa. Painon rinteen suuntainen komponentti ja liikekitka kumoavat toisensa.
**Voimakuvio:** Pulkka suorakulmiona rinteen suuntaisesti, $x$ rinnettä alas ja $y$ kohtisuoraan rinteestä ulos. Paino $\overline{G}$ keskipisteestä suoraan alas, tukivoima $\overline{N}$ alapinnasta kohtisuoraan rinteestä ulos ja liikekitka $\overline{F}_\mu$ alapinnan ylemmästä kulmasta rinnettä ylös. Painon komponentit katkoviivoin.
```voimakuvio
pinta -8,53
G 100
N 98,89
F_mu 14,83 ylös
a 0
akselit -8,53
komponentit G
```
**Kaava:** $y$: $N - mg\cos\alpha = 0$; $x$: $mg\sin\alpha - \mu N = 0$, joten $mg\sin\alpha = \mu mg\cos\alpha$, $\tan\alpha = \mu$ ja $\alpha = \tan^{-1}\mu$
**Muunnokset:** Kitkakerroin on yksikötön, ja kulma saadaan asteina laskimen asteasetuksella, joten muunnoksia ei tarvita.
**Sijoitus:** $\alpha = \tan^{-1} 0{,}15 = 8{,}531^\circ$
**Vastaus:** $8{,}5^\circ$, kaksi merkitsevää numeroa kuten kitkakertoimessa $0{,}15$.
**Järkevyys:** Pienillä kulmilla $\tan\alpha \approx \alpha$ radiaaneina, ja $0{,}15\,\text{rad} \approx 8{,}6^\circ$. Kulma on loiva, mikä sopii: jyrkemmässä rinteessä pulkka kiihtyisi, loivemmassa se hidastuisi. Massa supistui pois.

## fy4-16-L2-01
**Annettu:** $m = 60{,}0\,\text{kg}$, vaa'an lukema $\tfrac{N}{g} = 66{,}5\,\text{kg}$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** hissin kiihtyvyys $a$ yksikössä $\text{m/s}^2$ ja sen suunta
**Periaate:** Vaaka mittaa tukivoimaa. Lukema on suurempi kuin massa, joten tukivoima on painoa suurempi, kokonaisvoima osoittaa ylös ja Newtonin toisen lain mukaan myös kiihtyvyys osoittaa ylös.
**Voimakuvio:** Opiskelija suorakulmiona, positiivinen suunta ylös. Paino $\overline{G}$ keskipisteestä alas ja tukivoima $\overline{N}$ alhaalta ylös alapintaan asti, painoa pidempänä.
```voimakuvio
pinta 0
G 588,6
N 652,4 työntö
a ylös
```
**Kaava:** $N - mg = ma$, joten $a = \dfrac{N - mg}{m}$. Kun lukema on $L = \tfrac{N}{g}$, $N = Lg$ ja $a = g\left(\dfrac{L}{m} - 1\right)$
**Muunnokset:** Lukema muutetaan tukivoimaksi kertomalla luvulla $g$: $N = 66{,}5\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 652{,}4\,\text{N}$.
**Sijoitus:** $a = 9{,}81\,\text{m/s}^2\cdot\left(\dfrac{66{,}5\,\text{kg}}{60{,}0\,\text{kg}} - 1\right) = 9{,}81\,\text{m/s}^2\cdot 0{,}10833 = 1{,}063\,\text{m/s}^2$
**Vastaus:** $1{,}06\,\text{m/s}^2$ ylöspäin, kolme merkitsevää numeroa kuten massassa $60{,}0\,\text{kg}$ ja lukemassa $66{,}5\,\text{kg}$.
**Järkevyys:** Lukema on noin $11\,\%$ suurempi kuin massa, joten kiihtyvyys on noin $11\,\%$ putoamiskiihtyvyydestä, noin $1\,\text{m/s}^2$. Hissi joko lähtee ylös tai hidastaa liikkuessaan alas: kumpikin antaa ylöspäin osoittavan kiihtyvyyden.

## fy4-16-L2-02
**Annettu:** $L = 18{,}0\,\text{m}$, $\alpha = 12{,}0^\circ$, $v_1 = 0$, $v_2 = 5{,}10\,\text{m/s}$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** liikekitkakerroin $\mu$ (yksikötön)
**Periaate:** Nopeus tunnetaan rinteen alussa ja lopussa, joten käytetään energiaperiaatetta. Paino tekee työtä potentiaalienergian kautta, tukivoima ei tee työtä, ja liikekitka tekee negatiivisen työn koko rinteen matkalla. Kitkavoima saadaan voimakuviosta.
**Voimakuvio:** Pulkka suorakulmiona rinteen suuntaisesti, $x$ rinnettä alas ja $y$ kohtisuoraan rinteestä ulos. Paino $\overline{G}$ keskipisteestä suoraan alas, tukivoima $\overline{N}$ alapinnasta kohtisuoraan rinteestä ulos ja liikekitka $\overline{F}_\mu$ alapinnan ylemmästä kulmasta rinnettä ylös. $y$-suunnassa $N = mg\cos\alpha$, joten $F_\mu = \mu mg\cos\alpha$.
```voimakuvio
pinta -12
G 100
N 97,81
F_mu 13,43 ylös
a alas
akselit -12
komponentit G
```
**Kaava:** Nollataso juurelle: $mgL\sin\alpha - \mu mg\cos\alpha\cdot L = \tfrac12 mv_2^2$, joten $\mu = \dfrac{gL\sin\alpha - \tfrac12 v_2^2}{gL\cos\alpha}$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita. Massa supistuu pois.
**Sijoitus:** Osoittaja on $9{,}81\cdot 18{,}0\cdot\sin 12{,}0^\circ\,\tfrac{\text{m}^2}{\text{s}^2} - \tfrac12\cdot 5{,}10^2\,\tfrac{\text{m}^2}{\text{s}^2} = 36{,}71\,\tfrac{\text{m}^2}{\text{s}^2} - 13{,}01\,\tfrac{\text{m}^2}{\text{s}^2} = 23{,}71\,\tfrac{\text{m}^2}{\text{s}^2}$ ja nimittäjä $9{,}81\cdot 18{,}0\cdot\cos 12{,}0^\circ\,\tfrac{\text{m}^2}{\text{s}^2} = 172{,}72\,\tfrac{\text{m}^2}{\text{s}^2}$, joten $\mu = \dfrac{23{,}71}{172{,}72} = 0{,}1373$
**Vastaus:** $0{,}137$, kolme merkitsevää numeroa kuten rinteen pituudessa $18{,}0\,\text{m}$, kulmassa $12{,}0^\circ$ ja nopeudessa $5{,}10\,\text{m/s}$.
**Järkevyys:** Ilman kitkaa nopeus olisi pudotuskorkeudesta $h = 18{,}0\,\text{m}\cdot\sin 12{,}0^\circ \approx 3{,}74\,\text{m}$ laskettu $\sqrt{2\cdot 9{,}81\cdot 3{,}74}\,\text{m/s} \approx 8{,}6\,\text{m/s}$, joten kitka vie noin kaksi kolmasosaa energiasta. Kerroin on pienempi kuin $\tan 12{,}0^\circ \approx 0{,}21$, kuten pitää, koska pulkka kiihtyy.

## fy4-16-L2-03
**Annettu:** $m = 80{,}0\,\text{kg}$, $v_1 = 52{,}0\,\text{m/s}$, $v_2 = 6{,}0\,\text{m/s}$, pudotus $h = 145\,\text{m}$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** muiksi energiamuodoiksi muuttuva mekaaninen energia $|\Delta E_\text{mek}|$ yksikössä $\text{kJ}$
**Voimakuvio:** Hyppääjä varjoineen suorakulmiona, positiivinen suunta alas. Paino $\overline{G}$ keskipisteestä alas ja ilmanvastus $\overline{F}_\text{v}$ yläpinnasta ylös. Nopeus alas merkitään erikseen eikä voimaksi. Ilmanvastus on liikettä vastaan, joten sen työ on negatiivinen.
```voimakuvio
G 784,8
F_v 1520,8 ylös
a ylös
v alas
```
**Periaate:** Energiaperiaatteen mukaan mekaanisen energian muutos on muiden voimien kuin painon tekemä työ, tässä ilmanvastuksen negatiivinen työ. Sekä liike-energia että potentiaalienergia pienenevät, ja molempien muutos lasketaan mukaan.
**Kaava:** Nollataso lopputilanteen korkeudelle: $\Delta E_\text{mek} = \left(\tfrac12 mv_2^2 - \tfrac12 mv_1^2\right) - mgh$, ja $|\Delta E_\text{mek}| = \dfrac{m\left(v_1^2 - v_2^2\right)}{2} + mgh$
**Muunnokset:** Lasketaan jouleina ja muutetaan lopuksi kilojouleiksi: $1\,\text{kJ} = 1000\,\text{J}$.
**Sijoitus:** $|\Delta E_\text{mek}| = \tfrac12\cdot 80{,}0\,\text{kg}\cdot\left(52{,}0^2 - 6{,}0^2\right)\,\text{m}^2/\text{s}^2 + 80{,}0\,\text{kg}\cdot 9{,}81\,\text{m/s}^2\cdot 145\,\text{m} = 106\,720\,\text{J} + 113\,796\,\text{J} = 220\,516\,\text{J} \approx 221\,\text{kJ}$
**Vastaus:** $221\,\text{kJ}$, kolme merkitsevää numeroa kuten massassa $80{,}0\,\text{kg}$ ja nopeudessa $52{,}0\,\text{m/s}$.
**Järkevyys:** Kumpikin osa on noin $110\,\text{kJ}$: liike-energia pienenee lähes kokonaan ($\tfrac12\cdot 80\cdot 52^2\,\text{J} \approx 108\,\text{kJ}$), ja potentiaalienergia pienenee $mgh \approx 800\,\text{N}\cdot 145\,\text{m} \approx 116\,\text{kJ}$. Energia ei häviä, vaan muuttuu ilman liikkeeksi ja lopulta sisäenergiaksi.

## fy4-16-L2-04
**Annettu:** $m = 850\,\text{kg}$, nostokorkeus $h = 12{,}0\,\text{m}$, aika $t = 15{,}0\,\text{s}$, nopeus on vakio; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** köyden teho $P$ yksikössä $\text{kW}$
**Periaate:** Nopeus on vakio, joten Newtonin toisen lain mukaan köyden jännitysvoima on yhtä suuri kuin paino. Köysi vetää liikkeen suuntaan, joten se tekee positiivisen työn $W = Th$, joka kasvattaa korin potentiaalienergiaa. Teho on työ jaettuna ajalla, kuten luvussa *Vesi- ja tuulivoima energian muuntajina*, $E = Pt$.
**Voimakuvio:** Hissikori kuormineen suorakulmiona, positiivinen suunta ylös. Paino $\overline{G}$ keskipisteestä alas ja köyden jännitysvoima $\overline{T}$ yläpinnasta ylös, yhtä pitkinä. Nopeus ylös merkitään erikseen eikä voimaksi.
```voimakuvio
G 8338,5
T 8338,5 90
a 0
v ylös
```
**Kaava:** $T - mg = 0$, joten $T = mg$. Työ on $W = Th = mgh$, ja teho $P = \dfrac{W}{t} = \dfrac{mgh}{t}$
**Muunnokset:** Lasketaan watteina ja muutetaan lopuksi kilowateiksi: $1\,\text{kW} = 1000\,\text{W}$.
**Sijoitus:** $P = \dfrac{850\,\text{kg}\cdot 9{,}81\,\text{m/s}^2\cdot 12{,}0\,\text{m}}{15{,}0\,\text{s}} = \dfrac{100\,062\,\text{J}}{15{,}0\,\text{s}} = 6670{,}8\,\text{W} \approx 6{,}67\,\text{kW}$
**Vastaus:** $6{,}67\,\text{kW}$, kolme merkitsevää numeroa kuten korkeudessa $12{,}0\,\text{m}$ ja ajassa $15{,}0\,\text{s}$.
**Järkevyys:** Nopeus on $12{,}0\,\text{m} : 15{,}0\,\text{s} = 0{,}80\,\text{m/s}$, ja jännitysvoima noin $8{,}3\,\text{kN}$. Tulo $8{,}3\,\text{kN}\cdot 0{,}80\,\text{m/s} \approx 6{,}7\,\text{kW}$ täsmää. Hissimoottorin teho on tyypillisesti muutamia kilowatteja, ja moottori tarvitsee häviöiden vuoksi enemmän.

## fy4-16-L3-01
**Annettu:** korkeusero $h = 4{,}50\,\text{m}$, $\mu = 0{,}120$ koko matkalla, rinteen osat $25^\circ$ ja $10^\circ$, $v_1 = 0$ ja lopussa $v_2 = 0$
**Kysytty:** vaakasuora matka $x$ huipusta pysähtymiskohtaan yksikössä $\text{m}$
**Periaate:** Pulkka on alussa ja lopussa levossa, joten energiaperiaatteen mukaan kitkan negatiivinen työ on yhtä suuri kuin potentiaalienergian väheneminen. Suoralla pinnalla kitkan työ on $-\mu mg$ kertaa vaakasuora matka, koska rinteessä $N = mg\cos\alpha$ ja $L\cos\alpha$ on rinteen vaakasuora pituus. Siksi rinteen osien kulmia ei tarvita.
**Voimakuvio:** Kummallakin rinteen osalla pulkka suorakulmiona rinteen suuntaisesti: paino $\overline{G}$ keskipisteestä alas, tukivoima $\overline{N}$ kohtisuoraan rinteestä ulos, $N = mg\cos\alpha$, ja liikekitka $\overline{F}_\mu$ rinnettä ylös. Tasaisella $N = mg$ ja kitka taaksepäin. Tukivoima ei tee työtä missään kohdassa.
```voimakuvio
pinta -25
G 100
N 90,63
F_mu 10,88 ylös
a alas
---
pinta 0
G 100
N 100
F_mu 12 vasen
a vasen
```
**Kaava:** Osien vaakamatkat $x_\text{a}$, $x_\text{b}$ ja $x_\text{c}$: $mgh - \mu mg(x_\text{a} + x_\text{b} + x_\text{c}) = 0$, joten $x = x_\text{a} + x_\text{b} + x_\text{c} = \dfrac{h}{\mu}$
**Muunnokset:** Suureet ovat SI-yksiköissä, ja kitkakerroin on yksikötön, joten muunnoksia ei tarvita.
**Sijoitus:** $x = \dfrac{4{,}50\,\text{m}}{0{,}120} = 37{,}5\,\text{m}$
**Vastaus:** $37{,}5\,\text{m}$, kolme merkitsevää numeroa kuten korkeudessa $4{,}50\,\text{m}$ ja kitkakertoimessa $0{,}120$.
**Järkevyys:** Kummankin rinteen osan kaltevuus on suurempi kuin $\tan^{-1} 0{,}120 \approx 6{,}8^\circ$, joten pulkka liukuu koko rinteen eikä pysähdy kesken. Tulos ei riipu massasta eikä rinteen muodosta. Pienempi kitka antaisi pidemmän matkan, kuten pitää. Todellisuudessa mutkissa tukivoima ja kitka kasvavat hetkeksi, joten pulkka pysähtyisi hieman aikaisemmin.

## fy4-16-L3-02
**Annettu:** $m = 75{,}0\,\text{kg}$; kuvaajasta tukivoima $N = 650\,\text{N}$ hetkestä $1{,}0\,\text{s}$ hetkeen $3{,}0\,\text{s}$; hissi lähtee levosta; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** hissin suurin nopeus $v$ yksikössä $\text{m/s}$
**Periaate:** Hissi kiihtyy alaspäin silloin, kun tukivoima on painoa pienempi, ja nopeus on suurimmillaan tämän vaiheen lopussa. Newtonin toisen lain mukaan kiihtyvyys saadaan voimista. Kun voimat ovat vakiot, kiihtyvyys on vakio, ja luvun *Kiihtyvyys ja tasaisesti kiihtyvä liike* mukaan $v = v_0 + at$.
**Voimakuvio:** Ihminen suorakulmiona, positiivinen suunta alas. Paino $\overline{G}$ keskipisteestä alas ja tukivoima $\overline{N}$ alhaalta ylös alapintaan asti, painoa lyhyempänä.
```voimakuvio
pinta 0
G 735,8
N 650 työntö
a alas
```
**Kuvaajan lukeminen:** Paino on $75{,}0\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 735{,}75\,\text{N}$, ja lukema on sen suuruinen levossa ja tasaisella nopeudella. Hetkestä $1{,}0\,\text{s}$ hetkeen $3{,}0\,\text{s}$ käyrä on $650\,\text{N}$:n ruudukkoviivalla, painoa pienempi, joten hissi kiihtyy alaspäin $\Delta t = 2{,}0\,\text{s}$. Hetkestä $6{,}0\,\text{s}$ alkaen lukema on painoa suurempi, joten hissi hidastuu.
**Kaava:** $mg - N = ma$, joten $a = g - \dfrac{N}{m}$, ja levosta lähtiessä $v = a\Delta t = \left(g - \dfrac{N}{m}\right)\Delta t$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $v = \left(9{,}81\,\text{m/s}^2 - \dfrac{650\,\text{N}}{75{,}0\,\text{kg}}\right)\cdot 2{,}0\,\text{s} = 1{,}1433\,\text{m/s}^2\cdot 2{,}0\,\text{s} = 2{,}287\,\text{m/s}$
**Vastaus:** $2{,}3\,\text{m/s}$ alaspäin, kaksi merkitsevää numeroa kuten kuvaajasta luetussa ajassa $2{,}0\,\text{s}$.
**Järkevyys:** Hidastusvaiheessa lukema on $800\,\text{N}$, joten hidastuvuus on $(800 - 735{,}75)\,\text{N} : 75{,}0\,\text{kg} \approx 0{,}86\,\text{m/s}^2$, ja nopeus $2{,}3\,\text{m/s}$ häviää noin $2{,}7\,\text{s}$:ssa, mikä vastaa kuvaajan hidastusvaihetta noin hetkestä $6{,}0\,\text{s}$ hetkeen $8{,}7\,\text{s}$. Tavallisen hissin nopeus on $1$–$3\,\text{m/s}$.

## fy4-16-L3-03
**Annettu:** $m = 70{,}0\,\text{kg}$, $v_1 = 50{,}0\,\text{m/s}$, $v_2 = 6{,}0\,\text{m/s}$, pudotus $h = 60{,}0\,\text{m}$, ilmanvastus oletetaan vakioksi; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** ilmanvastuksen suuruus $F_\text{v}$ yksikössä $\text{kN}$
**Periaate:** Nopeudet tunnetaan matkan alussa ja lopussa, joten käytetään energiaperiaatetta. Ilmanvastus on ainoa muu voima kuin paino, ja se osoittaa liikettä vastaan, joten sen työ on $W_\text{v} = -F_\text{v} h$. Energiaperiaatteesta saadaan työ ja siitä voima.
**Voimakuvio:** Hyppääjä varjoineen suorakulmiona. Paino $\overline{G}$ keskipisteestä alas ja ilmanvastus $\overline{F}_\text{v}$ yläpinnasta ylös, painoa paljon pidempänä, koska hyppääjä hidastuu. Nopeus alas merkitään erikseen eikä voimaksi.
```voimakuvio
G 686,7
F_v 2124 ylös
a ylös
v alas
```
**Kaava:** Liike-energiat ovat $E_{\text{k},1} = \tfrac12 mv_1^2$ ja $E_{\text{k},2} = \tfrac12 mv_2^2$. Nollataso lopputilanteen korkeudelle: $E_{\text{k},1} + mgh - F_\text{v} h = E_{\text{k},2}$, joten $F_\text{v} = mg + \dfrac{E_{\text{k},1} - E_{\text{k},2}}{h}$
**Muunnokset:** Lasketaan newtoneina ja muutetaan lopuksi kilonewtoneiksi: $1\,\text{kN} = 1000\,\text{N}$.
**Sijoitus:** $E_{\text{k},1} = \tfrac12\cdot 70{,}0\,\text{kg}\cdot(50{,}0\,\text{m/s})^2 = 87\,500\,\text{J}$ ja $E_{\text{k},2} = \tfrac12\cdot 70{,}0\,\text{kg}\cdot(6{,}0\,\text{m/s})^2 = 1260\,\text{J}$, joten $F_\text{v} = 70{,}0\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 + \dfrac{87\,500\,\text{J} - 1260\,\text{J}}{60{,}0\,\text{m}} = 686{,}7\,\text{N} + 1437{,}3\,\text{N} = 2124\,\text{N} \approx 2{,}12\,\text{kN}$
**Vastaus:** $2{,}12\,\text{kN}$ ylöspäin, kolme merkitsevää numeroa kuten massassa $70{,}0\,\text{kg}$, nopeudessa $50{,}0\,\text{m/s}$ ja matkassa $60{,}0\,\text{m}$.
**Järkevyys:** Ilmanvastus on noin kolme kertaa paino $687\,\text{N}$, joten kokonaisvoima osoittaa ylös ja hyppääjä hidastuu, kuten pitää. Liikeyhtälöstä hidastuvuus on $(2124 - 687)\,\text{N} : 70{,}0\,\text{kg} \approx 20\,\text{m/s}^2$, ja silloin $\tfrac12(v_1^2 - v_2^2) : a \approx 1232 : 20{,}5 \approx 60\,\text{m}$, kuten tehtävässä.
