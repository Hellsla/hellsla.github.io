## fy4-5-L1-01
**Annettu:** $m = 1{,}5\,\text{kg}$, lamppu on paikallaan; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** johdon jännitysvoima $T$ yksikössä $\text{N}$
**Periaate:** Lamppu on levossa, joten Newtonin toisen lain mukaan siihen vaikuttavien voimien summa on nolla.
**Voimakuvio:** Lamppu suorakulmiona, $y$-akseli ylös. Lamppuun vaikuttavat Maa ja johto: paino $\overline{G}$ alas ja johdon jännitysvoima $\overline{T}$ johtoa pitkin ylös. Nuolet ovat yhtä pitkät.
```voimakuvio
G 14,715
T 14,715 ylös
a 0
```
**Kaava:** $T - mg = 0$, joten $T = mg$
**Muunnokset:** Massa on kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $T = 1{,}5\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 14{,}715\,\text{N}$
**Vastaus:** $14{,}7\,\text{N} \approx 15\,\text{N}$, kaksi merkitsevää numeroa kuten massassa $1{,}5\,\text{kg}$.
**Järkevyys:** Kilogramman paino on noin $10\,\text{N}$, joten puolentoista kilon lampun paino on noin $15\,\text{N}$. Johto kannattelee koko painon, koska muita ylöspäin vaikuttavia voimia ei ole.

## fy4-5-L1-02
**Annettu:** kuviosta luetut voimat: $F_1 = 40\,\text{N}$ oikealle, $F_2 = 25\,\text{N}$ vasemmalle, $F_3 = 30\,\text{N}$ ylös ja $F_4 = 30\,\text{N}$ alas
**Kysytty:** kokonaisvoiman suuruus $\Sigma F$ yksikössä $\text{N}$
**Periaate:** Kokonaisvoima on voimien vektorisumma. Lasketaan komponenttien summat kummankin akselin suuntaan erikseen, kun $x$ osoittaa oikealle ja $y$ ylös.
**Kuvaajan lukeminen:** Nuolten pituudet luetaan ruuduista: $F_1$ on neljä ruutua, $F_2$ kaksi ja puoli ruutua, $F_3$ ja $F_4$ kolme ruutua kumpikin. Yksi ruutu on $10\,\text{N}$.
**Kaava:** $\Sigma F_x = F_1 - F_2$ ja $\Sigma F_y = F_3 - F_4$. Kun $\Sigma F_y = 0$, kokonaisvoiman suuruus on $\Sigma F = |\Sigma F_x|$
**Muunnokset:** Ruudut muunnetaan newtoneiksi: $4\cdot 10\,\text{N} = 40\,\text{N}$ ja $2{,}5\cdot 10\,\text{N} = 25\,\text{N}$.
**Sijoitus:** $\Sigma F_y = 30\,\text{N} - 30\,\text{N} = 0$ ja $\Sigma F = 40\,\text{N} - 25\,\text{N} = 15\,\text{N}$
**Vastaus:** $15\,\text{N}$ oikealle, kahden merkitsevän numeron tarkkuudella; ruudukosta luetaan puolen ruudun eli $5\,\text{N}$:n tarkkuudella.
**Järkevyys:** Pystysuorat voimat ovat yhtä pitkät ja kumoavat toisensa. Vaakasuunnassa oikealle osoittava nuoli on puolitoista ruutua pidempi, eli $15\,\text{N}$, joten kokonaisvoima osoittaa oikealle. Kokonaisvoima ei ole voimien suuruuksien summa $125\,\text{N}$.

## fy4-5-L1-03
**Annettu:** $m = 0{,}50\,\text{kg}$, käden voima $F = 20\,\text{N}$ vaakasuoraan seinää kohti, kirja on paikallaan; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** seinän kitkavoima $F_\mu$ yksikössä $\text{N}$
**Periaate:** Kirja on levossa, joten voimien summa on nolla sekä vaaka- että pystysuunnassa. Seinä on pystysuora, joten sen tukivoima on vaakasuora ja kitkavoima pystysuora.
**Voimakuvio:** Kirja suorakulmiona, $x$ kohti seinää ja $y$ ylös. Käden voima $\overline{F}$ kohti seinää ja seinän tukivoima $\overline{N}$ seinästä poispäin, molemmat vaakasuoria. Paino $\overline{G}$ alas ja seinän kitkavoima $\overline{F}_\mu$ ylös, koska kirja pyrkii liukumaan alas.
```voimakuvio
pinta 0
F 20 0 työntö
N 20 @oikea
G 4,905
F_mu 4,905 ylös @oikea
a 0
akselit 0
```
**Kaava:** $y$: $F_\mu - mg = 0$, joten $F_\mu = mg$
**Muunnokset:** Massa on kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_\mu = 0{,}50\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 4{,}905\,\text{N}$
**Vastaus:** $4{,}9\,\text{N}$, kaksi merkitsevää numeroa kuten massassa $0{,}50\,\text{kg}$.
**Järkevyys:** Kitka kannattelee kirjan koko painon, koska vain se vaikuttaa ylöspäin. Käden voima $20\,\text{N}$ ei suoraan näy vastauksessa: se määrää tukivoiman $N = 20\,\text{N}$, mutta kitka on juuri niin suuri, kuin paikallaan pysyminen vaatii. Tukivoima ei tässä osoita ylös vaan vaakasuoraan.

## fy4-5-L1-04
**Annettu:** $m = 65\,\text{kg}$, hissi liikkuu tasaisella nopeudella; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** lattian tukivoima $N$ yksikössä $\text{N}$
**Periaate:** Tasaisessa liikkeessä kiihtyvyys on nolla, joten Newtonin toisen lain mukaan voimien summa on nolla, vaikka ihminen liikkuu.
**Voimakuvio:** Ihminen suorakulmiona, $y$-akseli ylös. Paino $\overline{G}$ alas ja lattian tukivoima $\overline{N}$ ylös, yhtä pitkinä. Nopeutta ei piirretä voimaksi.
```voimakuvio
pinta 0
G 637,65
N 637,65
a 0
```
**Kaava:** $N - mg = 0$, joten $N = mg$
**Muunnokset:** Massa on kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $N = 65\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 637{,}65\,\text{N}$
**Vastaus:** $640\,\text{N}$ eli $6{,}4\cdot 10^{2}\,\text{N}$, kaksi merkitsevää numeroa kuten massassa $65\,\text{kg}$.
**Järkevyys:** Tukivoima on sama kuin ihmisen paino, aivan kuin hissi seisoisi. Liike tasaisella nopeudella ei vaadi kokonaisvoimaa. Vaa'alla seisova ihminen näkisi tavallisen painonsa.

## fy4-5-L1-05
**Annettu:** $T = 250\,\text{N}$, kulma vaakatasoon $\alpha = 40^\circ$
**Kysytty:** jännitysvoiman vaakakomponentti $T_x$ yksikössä $\text{N}$
**Periaate:** Voima ja sen komponentit muodostavat suorakulmaisen kolmion, jonka hypotenuusa on voima. Vaakakomponentti on kulman $\alpha$ viereinen kateetti.
**Voimakuvio:** Köyden voima $\overline{T}$ yhtenäisenä nuolena kiinnityskohdasta vinosti ylös $40^\circ$:n kulmassa, komponentit $T_x$ ja $T_y$ katkoviivoin samasta kohdasta.
```voimakuvio
T 250 40
akselit 0
komponentit T
```
**Kaava:** $T_x = T\cos\alpha$
**Muunnokset:** Voima on newtoneina ja kulma asteina, joten muunnoksia ei tarvita; laskin on asteikolla DEG.
**Sijoitus:** $T_x = 250\,\text{N}\cdot\cos 40^\circ = 191{,}5\,\text{N}$
**Vastaus:** $190\,\text{N}$ eli $1{,}9\cdot 10^{2}\,\text{N}$, kaksi merkitsevää numeroa, koska kulma $40^\circ$ on annettu kahdella numerolla eikä voima $250\,\text{N}$ ole sitä tarkempi.
**Järkevyys:** Komponentti on pienempi kuin voima $250\,\text{N}$, kuten pitää. Kulma on alle $45^\circ$, joten vaakakomponentti on suurempi kuin pystykomponentti $250\,\text{N}\cdot\sin 40^\circ \approx 161\,\text{N}$.

## fy4-5-L2-01
**Annettu:** $m = 15\,\text{kg}$, $T = 60\,\text{N}$, $\alpha = 30^\circ$, pulkka liikkuu tasaisella nopeudella
**Kysytty:** lumen kitkavoima $F_\mu$ yksikössä $\text{N}$
**Periaate:** Tasaisessa liikkeessä kiihtyvyys on nolla, joten voimien summa on nolla myös liikkeen suunnassa: kitka on yhtä suuri kuin narun voiman vaakakomponentti.
**Voimakuvio:** Pulkka suorakulmiona, $x$ liikkeen suuntaan ja $y$ ylös. Paino $\overline{G}$ alas, lumen tukivoima $\overline{N}$ ylös ja painoa lyhyempi, narun jännitysvoima $\overline{T}$ vinosti ylös eteenpäin ja lumen kitkavoima $\overline{F}_\mu$ taaksepäin. Komponentti $T_x$ katkoviivalla.
```voimakuvio
pinta 0
G 147,15
N 117,15
T 60 30
F_mu 51,96 vasen
a 0
akselit 0
komponentit T
```
**Kaava:** $x$: $T\cos\alpha - F_\mu = 0$, joten $F_\mu = T\cos\alpha$
**Muunnokset:** Voima on newtoneina, joten muunnoksia ei tarvita. Massaa ei tarvita, koska kitka saadaan vaakasuunnan yhtälöstä.
**Sijoitus:** $F_\mu = 60\,\text{N}\cdot\cos 30^\circ = 51{,}96\,\text{N}$
**Vastaus:** $52\,\text{N}$, kaksi merkitsevää numeroa kuten voimassa $60\,\text{N}$.
**Järkevyys:** Kitka on vähän pienempi kuin narun voima $60\,\text{N}$, koska vain osa narun voimasta vetää eteenpäin. Pystysuunnasta tukivoima on $N = mg - T\sin\alpha \approx 147\,\text{N} - 30\,\text{N} = 117\,\text{N}$, painoa pienempi.

## fy4-5-L2-02
**Annettu:** $m = 60\,\text{kg}$, kiihtyvyys ylöspäin $a = 1{,}2\,\text{m/s}^2$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** lattian tukivoima $N$ yksikössä $\text{N}$
**Periaate:** Ihminen kiihtyy ylöspäin hissin mukana, joten kokonaisvoima osoittaa ylös ja on Newtonin toisen lain mukaan $ma$.
**Voimakuvio:** Ihminen suorakulmiona, $y$-akseli ylös. Paino $\overline{G}$ alas ja tukivoima $\overline{N}$ ylös, tukivoima pidempänä. Kiihtyvyys piirretään erikseen, ei voimaksi.
```voimakuvio
pinta 0
G 588,6
N 660,6
a ylös
```
**Kaava:** $N - mg = ma$, joten $N = m(g + a)$
**Muunnokset:** Massa on kilogrammoina ja kiihtyvyydet yksikössä $\text{m/s}^2$, joten muunnoksia ei tarvita.
**Sijoitus:** $N = 60\,\text{kg}\cdot(9{,}81\,\text{m/s}^2 + 1{,}2\,\text{m/s}^2) = 60\,\text{kg}\cdot 11{,}01\,\text{m/s}^2 = 660{,}6\,\text{N}$
**Vastaus:** $660\,\text{N}$ eli $6{,}6\cdot 10^{2}\,\text{N}$, kaksi merkitsevää numeroa kuten massassa $60\,\text{kg}$ ja kiihtyvyydessä $1{,}2\,\text{m/s}^2$.
**Järkevyys:** Paino on noin $590\,\text{N}$, ja tukivoima on sitä noin $70\,\text{N}$ suurempi, mikä on $ma = 60\,\text{kg}\cdot 1{,}2\,\text{m/s}^2 = 72\,\text{N}$. Hissin lähtiessä ylös tunnet itsesi painavammaksi, koska lattia painaa jalkoja tavallista enemmän.

## fy4-5-L2-03
**Annettu:** $m = 40\,\text{kg}$, $F = 120\,\text{N}$ kulmassa $\alpha = 30^\circ$ vaakatason alapuolelle, $F_\mu = 80\,\text{N}$
**Kysytty:** laatikon kiihtyvyys $a$ yksikössä $\text{m/s}^2$
**Periaate:** Laatikko kiihtyy vaakasuunnassa. Newtonin toisen lain mukaan vaakasuuntaisten voimakomponenttien summa on $ma$. Pystysuuntaista yhtälöä ei tarvita, koska kitka on annettu.
**Voimakuvio:** Laatikko suorakulmiona, $x$ liikkeen suuntaan ja $y$ ylös. Paino $\overline{G}$ alas, lattian tukivoima $\overline{N}$ ylös ja painoa pidempi, kahvan voima $\overline{F}$ vinosti alas eteenpäin ja kitkavoima $\overline{F}_\mu$ taaksepäin. Komponentit $F_x$ ja $F_y$ katkoviivalla.
```voimakuvio
pinta 0
G 392,4
N 452,4
F 120 -30 työntö @ylä
F_mu 80 vasen
a oikea
akselit 0
komponentit F
```
**Kaava:** $x$: $F\cos\alpha - F_\mu = ma$, joten $a = \dfrac{F\cos\alpha - F_\mu}{m}$
**Muunnokset:** Voimat ovat newtoneina ja massa kilogrammoina, joten tulos tulee suoraan yksikössä $\text{m/s}^2$.
**Sijoitus:** $a = \dfrac{120\,\text{N}\cdot\cos 30^\circ - 80\,\text{N}}{40\,\text{kg}} = \dfrac{103{,}9\,\text{N} - 80\,\text{N}}{40\,\text{kg}} = 0{,}598\,\text{m/s}^2$
**Vastaus:** $0{,}60\,\text{m/s}^2$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Vaakakomponentti $104\,\text{N}$ on vain vähän suurempi kuin kitka $80\,\text{N}$, joten kokonaisvoima $24\,\text{N}$ on pieni ja $40\,\text{kg}$:n laatikko kiihtyy hitaasti. Jos koko voima $120\,\text{N}$ vaikuttaisi eteenpäin, kiihtyvyys olisi $1{,}0\,\text{m/s}^2$.

## fy4-5-L2-04
**Annettu:** $m = 50\,\text{kg}$, $F_1 = 30\,\text{N}$ ja $F_2 = 40\,\text{N}$ vaakasuoraan, kohtisuorassa toisiaan vastaan; kitkaa ei ole
**Kysytty:** kelkan kiihtyvyyden suuruus $a$ yksikössä $\text{m/s}^2$
**Periaate:** Kokonaisvoima on voimien vektorisumma, ja Newtonin toisen lain mukaan se määrää kiihtyvyyden. Pystysuunnassa paino ja jään tukivoima kumoavat toisensa.
**Voimakuvio:** Kelkka suorakulmiona ylhäältä katsottuna, $x$ voiman $\overline{F}_1$ suuntaan ja $y$ voiman $\overline{F}_2$ suuntaan. Sivulta katsottuna paino $\overline{G}$ alas ja tukivoima $\overline{N}$ ylös, yhtä pitkinä.
```voimakuvio
F_1 30 0
F_2 40 90
a 53,13
akselit 0
```
**Kaava:** $\Sigma F_x = F_1$ ja $\Sigma F_y = F_2$, joten $\Sigma F = \sqrt{F_1^2 + F_2^2}$. Newtonin toisesta laista $\Sigma F = ma$, joten $a = \dfrac{\Sigma F}{m}$
**Muunnokset:** Voimat ovat newtoneina ja massa kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $\Sigma F = \sqrt{(30\,\text{N})^2 + (40\,\text{N})^2} = 50\,\text{N}$ ja $a = \dfrac{50\,\text{N}}{50\,\text{kg}} = 1{,}0\,\text{m/s}^2$
**Vastaus:** $1{,}0\,\text{m/s}^2$, kaksi merkitsevää numeroa kuten voimissa $30\,\text{N}$ ja $40\,\text{N}$.
**Järkevyys:** Kokonaisvoima $50\,\text{N}$ on suurempi kuin kumpikaan voima mutta pienempi kuin niiden summa $70\,\text{N}$, koska voimat ovat eri suuntiin. Kiihtyvyys osoittaa voimien väliin, lähemmäs suurempaa voimaa.

## fy4-5-L3-01
**Annettu:** $m = 70\,\text{kg}$, hissi liikkuu ylöspäin ja hidastaa, kiihtyvyyden suuruus $1{,}5\,\text{m/s}^2$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** lattian tukivoima $N$ yksikössä $\text{N}$
**Periaate:** Ylöspäin liikkuva hissi hidastuu, joten sen kiihtyvyys osoittaa alas, vaikka nopeus osoittaa ylös. Newtonin toisen lain mukaan kokonaisvoima osoittaa kiihtyvyyden suuntaan eli alas.
**Voimakuvio:** Ihminen suorakulmiona, $y$-akseli ylös. Paino $\overline{G}$ alas ja tukivoima $\overline{N}$ ylös, tukivoima lyhyempänä. Nopeus $\overline{v}$ ylös (sininen) ja kiihtyvyys $\overline{a}$ alas (oranssi) piirretään kuvion viereen ohuina nuolina, ei voimiksi. Kiihtyvyyden komponentti on $a_y = -1{,}5\,\text{m/s}^2$.
```voimakuvio
pinta 0
G 686,7
N 581,7
v ylös
a alas
```
**Kaava:** $N - mg = m a_y$, joten $N = m(g + a_y)$
**Muunnokset:** Massa on kilogrammoina ja kiihtyvyydet yksikössä $\text{m/s}^2$, joten muunnoksia ei tarvita.
**Sijoitus:** $N = 70\,\text{kg}\cdot(9{,}81\,\text{m/s}^2 - 1{,}5\,\text{m/s}^2) = 70\,\text{kg}\cdot 8{,}31\,\text{m/s}^2 = 581{,}7\,\text{N}$
**Vastaus:** $580\,\text{N}$ eli $5{,}8\cdot 10^{2}\,\text{N}$, kaksi merkitsevää numeroa kuten massassa $70\,\text{kg}$ ja kiihtyvyydessä $1{,}5\,\text{m/s}^2$.
**Järkevyys:** Paino on noin $690\,\text{N}$, ja tukivoima on sitä pienempi, koska kokonaisvoima osoittaa alas. Hissin pysähtyessä ylhäällä tunnet itsesi hetken kevyemmäksi. Jos tukivoimaksi saisi painoa suuremman, kiihtyvyyden suunta olisi valittu nopeuden mukaan, mikä on yleinen virhe.

## fy4-5-L3-02
**Annettu:** $m = 19\,\text{kg}$, alkunopeus $v_0 = 2{,}0\,\text{m/s}$, loppunopeus $v = 0$, aika $\Delta t = 20\,\text{s}$; hidastuminen tasaista
**Kysytty:** kitkavoima $F_\mu$ yksikössä $\text{N}$
**Periaate:** Kiven vauhti muuttuu tasaisesti, joten kiihtyvyys on $a = \dfrac{\Delta v}{\Delta t}$ (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*). Newtonin toisen lain mukaan liikkeen suuntainen kokonaisvoima on $ma$, ja ainoa vaakasuora voima on kitka.
**Voimakuvio:** Kivi suorakulmiona, $x$ liikkeen suuntaan ja $y$ ylös. Paino $\overline{G}$ alas, jään tukivoima $\overline{N}$ ylös ja kitkavoima $\overline{F}_\mu$ taaksepäin. Eteenpäin vievää voimaa ei ole, koska heittäjä ei enää koske kiveen.
```voimakuvio
pinta 0
G 186,39
N 186,39
F_mu 1,9 vasen
v oikea
a vasen
```
**Kaava:** $a_x = \dfrac{v - v_0}{\Delta t}$ ja $x$: $-F_\mu = m a_x$, joten $F_\mu = \dfrac{m(v_0 - v)}{\Delta t}$
**Muunnokset:** Massa on kilogrammoina, nopeudet yksikössä $\text{m/s}$ ja aika sekunteina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_\mu = \dfrac{19\,\text{kg}\cdot(2{,}0\,\text{m/s} - 0)}{20\,\text{s}} = 19\,\text{kg}\cdot 0{,}10\,\text{m/s}^2 = 1{,}9\,\text{N}$
**Vastaus:** $1{,}9\,\text{N}$, kaksi merkitsevää numeroa kuten massassa, nopeudessa ja ajassa.
**Järkevyys:** Kiven paino on noin $190\,\text{N}$, ja kitka on vain noin prosentti siitä, mikä sopii sileälle jäälle. Kiihtyvyyden komponentti on negatiivinen, koska kivi hidastuu, ja kitka osoittaa taaksepäin kuten kuviossa.

## fy4-5-L3-03
**Annettu:** $m = 4{,}0\,\text{g}$, noste $F_\text{noste} = 0{,}10\,\text{N}$, pallo on paikallaan katossa; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** katon tukivoima $N$ yksikössä $\text{N}$
**Periaate:** Pallo on levossa, joten Newtonin toisen lain mukaan voimien summa on nolla. Katto koskettaa palloa yläpuolelta, joten sen tukivoima on kohtisuorassa kattoa vastaan ja työntää palloa poispäin katosta eli alas.
**Voimakuvio:** Pallo suorakulmiona, $y$-akseli ylös. Noste $\overline{F}_\text{noste}$ ylös, paino $\overline{G}$ alas ja katon tukivoima $\overline{N}$ alas. Noste on yhtä pitkä kuin paino ja tukivoima yhteensä. Ilmanvastusta ei ole, koska pallo ei liiku.
```voimakuvio
pinta 0
F_noste 0,10 ylös
G 0,03924
N 0,06076 @ylä
a 0
```
**Kaava:** $F_\text{noste} - mg - N = 0$, joten $N = F_\text{noste} - mg$
**Muunnokset:** $m = 4{,}0\,\text{g} = 4{,}0 \cdot 0{,}001\,\text{kg} = 0{,}0040\,\text{kg}$
**Sijoitus:** $N = 0{,}10\,\text{N} - 0{,}0040\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 0{,}10\,\text{N} - 0{,}03924\,\text{N} = 0{,}06076\,\text{N}$
**Vastaus:** $0{,}061\,\text{N}$, kaksi merkitsevää numeroa kuten massassa $4{,}0\,\text{g}$ ja nosteessa $0{,}10\,\text{N}$.
**Järkevyys:** Noste on suurempi kuin paino $0{,}039\,\text{N}$, joten ilman kattoa pallo nousisi. Katto pysäyttää sen työntämällä alaspäin juuri ylimäärän verran: $0{,}039\,\text{N} + 0{,}061\,\text{N} = 0{,}10\,\text{N}$. Tukivoima osoittaa tässä alas, ei ylös.
