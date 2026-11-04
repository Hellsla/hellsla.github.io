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
**Vastaus:** $0{,}061\,\text{N} \approx 0{,}06\,\text{N}$. Tukivoima on erotus, ja erotuksessa ratkaisee desimaalien määrä: noste $0{,}10\,\text{N}$ tunnetaan sadasosanewtonin tarkkuudella.
**Järkevyys:** Noste on suurempi kuin paino $0{,}039\,\text{N}$, joten ilman kattoa pallo nousisi. Katto pysäyttää sen työntämällä alaspäin juuri ylimäärän verran: $0{,}039\,\text{N} + 0{,}061\,\text{N} = 0{,}10\,\text{N}$. Tukivoima osoittaa tässä alas, ei ylös.


## fy4-5-L1-06
**Kysytty:** mitkä voimat piirretään voimakuvioon, kun laatikko liukuu vaakasuoralla lattialla ja hidastuu kitkan vaikutuksesta.
**Periaate:** Voimakuvioon piirretään vain valittuun kappaleeseen vaikuttavat voimat, ja jokaisella voimalla on aiheuttaja: Maa, pinta, naru tai työntäjä. Nopeus ja kiihtyvyys eivät ole voimia. Newtonin toisen lain mukaan kappale voi liikkua ilman liikkeen suuntaista voimaa.
**Mallivastaus:** Laatikkoon vaikuttavat kolme voimaa. Maa vetää laatikkoa alas (paino), lattia tukee sitä ylös (tukivoima) ja lattia vastustaa liukumista vasemmalle (kitka). Paino ja tukivoima ovat yhtä pitkät, koska laatikko ei liiku pystysuunnassa, ja kitka on ainoa vaakasuora voima, joten se hidastaa laatikkoa. Oikealle osoittavaa liikevoimaa ei ole, koska ei ole mitään kappaletta, joka sitä aiheuttaisi. Nopeutta ei piirretä voimaksi, vaan tarvittaessa erikseen voimakuvion viereen. Tukivoimaa ei saa jättää pois, vaikka se kumoaa painon.

## fy4-5-L1-07
**Annettu:** työntövoimat $F_1 = 120\,\text{N}$ ja $F_2 = 85\,\text{N}$ samaan suuntaan, kitkavoima $F_\mu = 150\,\text{N}$ vastakkaiseen suuntaan; paino ja tukivoima kumoavat toisensa
**Kysytty:** kokonaisvoiman suuruus $\Sigma F$ yksikössä $\text{N}$
**Periaate:** Kokonaisvoima on voimien vektorisumma. Voimat ovat samalla suoralla, joten summa lasketaan vaakasuunnan komponenteista, kun $x$ osoittaa työntämisen suuntaan. Pystysuunnassa kokonaisvoima on nolla.
**Voimakuvio:** Kaappi suorakulmiona, $x$ työntämisen suuntaan ja $y$ ylös. Kaksi työntövoimaa $\overline{F}_1$ ja $\overline{F}_2$ eteenpäin, kitkavoima $\overline{F}_\mu$ taaksepäin sekä paino $\overline{G}$ alas ja tukivoima $\overline{N}$ ylös yhtä pitkinä. Kitkavoima on pidempi kuin kumpikaan työntövoima mutta lyhyempi kuin niiden summa.
**Kaava:** $\Sigma F_x = F_1 + F_2 - F_\mu$
**Muunnokset:** Kaikki voimat ovat newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $\Sigma F_x = 120\,\text{N} + 85\,\text{N} - 150\,\text{N} = 55\,\text{N}$
**Vastaus:** $55\,\text{N}$ työntämisen suuntaan, kaksi merkitsevää numeroa kuten annetuissa voimissa.
**Järkevyys:** Työntövoimat ovat yhteensä $205\,\text{N}$, mikä on suurempi kuin kitka $150\,\text{N}$, joten kokonaisvoima osoittaa työntämisen suuntaan ja kaappi kiihtyy. Jos työntövoimat olisivat yhteensä alle $150\,\text{N}$, kaappi hidastuisi tai pysyisi paikallaan. Kokonaisvoima ei ole voimien suuruuksien summa $355\,\text{N}$.

## fy4-5-L1-08
**Kysytty:** miten lattian tukivoima $N$ suhtautuu laatikon painoon $G$, kun laatikkoa vedetään narulla vinosti ylöspäin eikä se liiku.
**Periaate:** Laatikko on levossa, joten Newtonin toisen lain mukaan voimien summa on nolla myös pystysuunnassa. Pystysuunnassa on kolme voimaa: paino alas sekä tukivoima ja narun jännitysvoiman pystykomponentti ylös.
**Mallivastaus:** Pystysuunnan yhtälö on $N + T\sin\alpha - G = 0$, joten $N = G - T\sin\alpha$. Narun pystykomponentti kannattelee osan painosta, ja lattian tarvitsee tukea vain loppuosa, joten tukivoima on painoa pienempi. Tukivoima ei siis ole aina yhtä suuri kuin paino: se on juuri niin suuri, kuin pystysuunnan tasapaino vaatii. Jos naru vetäisi vaakasuoraan, tukivoima olisi painon suuruinen, ja jos naru vetäisi laatikkoa vinosti alaspäin, tukivoima olisi painoa suurempi. Tukivoima olisi nolla vasta, kun narun pystykomponentti olisi yhtä suuri kuin koko paino, ja silloin laatikko olisi irtoamaisillaan lattiasta.

## fy4-5-L2-05
**Annettu:** rengas on paikallaan; mittaukset $(F_\text{A}, F_\text{C}, F_\text{B})$: $(3{,}0;\ 2{,}5;\ 3{,}9)\,\text{N}$, $(4{,}5;\ 3{,}8;\ 5{,}9)\,\text{N}$ ja $(6{,}0;\ 5{,}1;\ 7{,}9)\,\text{N}$
**Kysytty:** kulman $\alpha$ keskiarvo $\alpha_\text{ka}$ yksikössä $^\circ$
**Periaate:** Rengas on levossa, joten Newtonin toisen lain mukaan siihen vaikuttavien voimien summa on nolla sekä vaaka- että pystysuunnassa. Köysi B on vino, joten sen voima jaetaan komponentteihin.
**Voimakuvio:** Rengas suorakulmiona, $x$ oikealle ja $y$ ylös. Köyden A jännitysvoima $\overline{F}_\text{A}$ vasemmalle ja köyden C jännitysvoima $\overline{F}_\text{C}$ alas. Köyden B voima $\overline{F}_\text{B}$ lähtee vinosti ylös oikealle kulmassa $\alpha$, ja sen komponentit $F_\text{B}\cos\alpha$ ja $F_\text{B}\sin\alpha$ piirretään katkoviivoin. Komponentit ovat yhtä pitkät kuin $F_\text{A}$ ja $F_\text{C}$. Renkaan painoa ei piirretä, koska tehtävässä se jätetään huomiotta.
**Kuvaajan lukeminen:** Taulukosta luetaan kunkin mittauksen voimat $F_\text{A}$ ja $F_\text{C}$. Vertailuun otetaan myös anturin B lukema.
**Kaava:** $x$: $F_\text{B}\cos\alpha - F_\text{A} = 0$ ja $y$: $F_\text{B}\sin\alpha - F_\text{C} = 0$, joten $\alpha = \arctan\dfrac{F_\text{C}}{F_\text{A}}$
**Muunnokset:** Voimat ovat newtoneina ja kulma lasketaan asteina, joten muunnoksia ei tarvita; laskin on asteikolla DEG.
**Sijoitus:** Kulmat ovat
```latex
\begin{aligned}
\alpha_1 &= \arctan\dfrac{2{,}5}{3{,}0} = 39{,}8\,{}^\circ \\
\alpha_2 &= \arctan\dfrac{3{,}8}{4{,}5} = 40{,}2\,{}^\circ \\
\alpha_3 &= \arctan\dfrac{5{,}1}{6{,}0} = 40{,}4\,{}^\circ
\end{aligned}
```
Summa on $120{,}4\,{}^\circ$, joten keskiarvo on $\alpha_\text{ka} = 120{,}4\,{}^\circ : 3 = 40{,}1\,{}^\circ$. Tarkistus ensimmäisellä mittauksella: $F_\text{B} = \sqrt{(3{,}0\,\text{N})^2 + (2{,}5\,\text{N})^2} = 3{,}9\,\text{N}$.
**Vastaus:** a) Voimakuvio ja yhtälöt yllä. b) $\alpha_\text{ka} = 40{,}1\,{}^\circ \approx 40\,{}^\circ$, kahden merkitsevän numeron tarkkuudella kuten voimien lukemat. c) Laskettu $F_\text{B} = 3{,}9\,\text{N}$ on sama kuin anturin lukema.
**Järkevyys:** Kolme kulmaa poikkeaa toisistaan enintään $0{,}6\,{}^\circ$, joten ne kuvaavat samaa kulmaa ja pieni vaihtelu on mittauksen satunnaisvaihtelua. Voimat kasvavat samassa suhteessa, ja suhde $F_\text{C} : F_\text{A}$ pysyy noin $0{,}84$:ssä. Kulma on alle $45\,{}^\circ$, joten $F_\text{A} > F_\text{C}$ kuten taulukossa. Voima $F_\text{B}$ on suurempi kuin kumpikaan komponentti mutta pienempi kuin niiden summa $5{,}5\,\text{N}$.

## fy4-5-L2-06
**Annettu:** $m = 12\,\text{kg}$, kitkavoima $F_\mu = 30\,\text{N}$ vasemmalle, laatikko liukuu oikealle ja hidastuu; ilmanvastusta ei ole
**Kysytty:** a) opiskelijan virhe; b) kiihtyvyyden suuruus $a$ yksikössä $\text{m/s}^2$
**Periaate:** Voimakuvioon kuuluvat vain kappaleeseen vaikuttavat voimat, joilla on aiheuttaja. Opiskelija piirsi laatikkoon ”potkun voiman”, vaikka potkun jälkeen mikään kappale ei työnnä laatikkoa oikealle, ja päätteli kiihtyvyyden suunnan liikkeen suunnasta, vaikka laatikko hidastuu. Potkun voima vaikuttaa laatikkoon vain sen ajan, kun jalka koskee siihen. Kun laatikko on irronnut jalasta, sen vaakasuoraan liikkeeseen vaikuttaa vain kitka.
**Voimakuvio:** Laatikko suorakulmiona, $x$ oikealle ja $y$ ylös. Paino $\overline{G}$ alas ja lattian tukivoima $\overline{N}$ ylös yhtä pitkinä sekä kitkavoima $\overline{F}_\mu$ vasemmalle. Oikealle ei piirretä voimaa. Nopeus oikealle ja kiihtyvyys vasemmalle piirretään kuvion viereen erikseen.
```voimakuvio
pinta 0
G 117,72
N 117,72
F_mu 30 vasen
v oikea
a vasen
```
**Kaava:** $x$: $-F_\mu = m a_x$, joten $a_x = -\dfrac{F_\mu}{m}$ ja kiihtyvyyden suuruus on $a = \dfrac{F_\mu}{m}$
**Muunnokset:** Voima on newtoneina ja massa kilogrammoina, joten tulos tulee suoraan yksikössä $\text{m/s}^2$.
**Sijoitus:** $a = \dfrac{30\,\text{N}}{12\,\text{kg}} = 2{,}5\,\text{m/s}^2$
**Vastaus:** a) Voimakuvioon on otettu ylimääräinen voima, jolla ei ole aiheuttajaa. b) $a = 2{,}5\,\text{m/s}^2$ vasemmalle eli liikettä vastaan, kaksi merkitsevää numeroa kuten annetuissa arvoissa. Laatikko hidastuu.
**Järkevyys:** Kokonaisvoima $30\,\text{N}$ osoittaa vasemmalle, joten kiihtyvyys osoittaa vasemmalle ja laatikko hidastuu, kuten tehtävässä sanotaan. Opiskelijan tulos, jonka mukaan laatikko kiihtyy, on ristiriidassa tämän kanssa. Kitka on vain noin neljännes laatikon painosta $118\,\text{N}$.

## fy4-5-L2-07
**Annettu:** $F_1 = 6{,}0\,\text{N}$, $F_2 = 8{,}0\,\text{N}$, niiden suuntien välinen kulma $\varphi = 60\,{}^\circ$; taulukosta $F_3 = 12{,}3\,\text{N}$, kun $\varphi = 60\,{}^\circ$
**Kysytty:** voimien $\overline{F}_1$ ja $\overline{F}_2$ summan suuruus $\Sigma F$ yksikössä $\text{N}$, kun $\varphi = 60\,{}^\circ$
**Periaate:** a) Rengas on levossa, joten Newtonin toisen lain mukaan voimien $\overline{F}_1$, $\overline{F}_2$ ja $\overline{F}_3$ summa on nolla. Siksi anturin 3 voima on yhtä suuri ja vastakkaissuuntainen kuin voimien $\overline{F}_1$ ja $\overline{F}_2$ summa, ja sen lukema kertoo summan suuruuden. b) Vinojen voimien summa lasketaan komponenteittain.
**Voimakuvio:** Rengas suorakulmiona, $x$ voiman $\overline{F}_1$ suuntaan. Voima $\overline{F}_1$ lähtee suoraan $x$-akselin suuntaan ja voima $\overline{F}_2$ kulmassa $60\,{}^\circ$ ylöspäin. Voima $\overline{F}_3$ lähtee vastakkaiseen suuntaan kuin niiden summa. Komponentit $F_{2x}$ ja $F_{2y}$ piirretään katkoviivoin.
**Kuvaajan lukeminen:** Taulukosta luetaan rivi $\varphi = 60\,{}^\circ$: $F_3 = 12{,}3\,\text{N}$.
**Kaava:** $\Sigma F_x = F_1 + F_2\cos\varphi$ ja $\Sigma F_y = F_2\sin\varphi$, joten $\Sigma F = \sqrt{(\Sigma F_x)^2 + (\Sigma F_y)^2}$
**Muunnokset:** Voimat ovat newtoneina ja kulma asteina, joten muunnoksia ei tarvita.
**Sijoitus:** Ensin komponentit:
```latex
\begin{aligned}
\Sigma F_x &= 6{,}0\,\text{N} + 8{,}0\,\text{N}\cdot\cos 60\,{}^\circ \\
&= 10{,}0\,\text{N} \\
\Sigma F_y &= 8{,}0\,\text{N}\cdot\sin 60\,{}^\circ \\
&= 6{,}93\,\text{N}
\end{aligned}
```
Sitten suuruus: $\Sigma F = \sqrt{(10{,}0\,\text{N})^2 + (6{,}93\,\text{N})^2} = 12{,}2\,\text{N}$
**Vastaus:** a) Rengas on levossa, joten voima $\overline{F}_3$ kumoaa voimien $\overline{F}_1$ ja $\overline{F}_2$ summan. b) $\Sigma F \approx 12\,\text{N}$, kaksi merkitsevää numeroa kuten annetuissa voimissa. c) Mitattu $12{,}3\,\text{N}$ eroaa laskennallisesta $12{,}2\,\text{N}$:sta noin $0{,}1\,\text{N}$ eli noin yhden prosentin; ero on mittausepävarmuuden suuruusluokkaa. Se voi johtua kulman lukemisen epätarkkuudesta, anturien nollauksesta tai siitä, että rengas ei ole täysin paikallaan.
**Järkevyys:** Summa $12{,}2\,\text{N}$ on pienempi kuin voimien suuruuksien summa $14{,}0\,\text{N}$ ja suurempi kuin suurempi voima $8{,}0\,\text{N}$, kuten kulmalla $60\,{}^\circ$ pitääkin. Taulukossa lukema pienenee kulman kasvaessa ($13{,}4\,\text{N}$, $12{,}3\,\text{N}$, $10{,}1\,\text{N}$), ja kulmalla $90\,{}^\circ$ summa on $\sqrt{6{,}0^2 + 8{,}0^2}\,\text{N} = 10\,\text{N}$ kuten mittauksessa.

## fy4-5-L3-04
**Annettu:** $m = 25\,\text{kg}$, $T = 120\,\text{N}$, $\alpha = 30\,{}^\circ$, laatikko lähtee levosta; taulukosta $v = 0$ hetkellä $t = 0$ ja $v = 4{,}01\,\text{m/s}$ hetkellä $t = 5{,}0\,\text{s}$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** kitkavoima $F_\mu$ yksikössä $\text{N}$ ja tukivoima $N$
**Periaate:** Laatikko kiihtyy vaakasuunnassa eikä liiku pystysuunnassa. Kiihtyvyys saadaan nopeuden muutoksesta (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*), ja Newtonin toinen laki kirjoitetaan komponenteittain: vaakasuunnassa kokonaisvoima on $ma$, pystysuunnassa nolla.
**Voimakuvio:** Laatikko suorakulmiona, $x$ liikkeen suuntaan ja $y$ ylös. Paino $\overline{G}$ alas ja lattian tukivoima $\overline{N}$ ylös ja painoa lyhyempi, köyden jännitysvoima $\overline{T}$ vinosti ylös eteenpäin ja kitkavoima $\overline{F}_\mu$ taaksepäin. Komponentit $T_x$ ja $T_y$ katkoviivoin. Kiihtyvyys eteenpäin piirretään erikseen, ei voimaksi.
```voimakuvio
pinta 0
G 245,25
N 185,25
T 120 30
F_mu 83,87 vasen
a oikea
akselit 0
komponentit T
```
**Kuvaajan lukeminen:** Nopeus kasvaa suunnilleen yhtä paljon joka sekunti: peräkkäisten sekuntien muutokset ovat $0{,}78$, $0{,}85$, $0{,}75$, $0{,}84$ ja $0{,}79\,\text{m/s}$. Kiihtyvyys on siis likimain vakio, ja se saadaan koko aikavälin muutoksesta $\Delta v = 4{,}01\,\text{m/s} - 0 = 4{,}01\,\text{m/s}$ ja $\Delta t = 5{,}0\,\text{s}$.
**Kaava:** $a = \dfrac{\Delta v}{\Delta t}$, $x$: $T\cos\alpha - F_\mu = ma$ ja $y$: $N + T\sin\alpha - mg = 0$, joten $F_\mu = T\cos\alpha - ma$ ja $N = mg - T\sin\alpha$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä, ja $\text{N} / \text{kg} = \text{m/s}^2$.
**Sijoitus:** Kiihtyvyys on $a = \dfrac{4{,}01\,\text{m/s}}{5{,}0\,\text{s}} = 0{,}802\,\text{m/s}^2$. Kitkavoima:
```latex
\begin{aligned}
F_\mu &= 120\,\text{N}\cdot\cos 30\,{}^\circ \\
&\quad - 25\,\text{kg}\cdot 0{,}802\,\text{m/s}^2 \\
&= 103{,}9\,\text{N} - 20{,}05\,\text{N} \\
&= 83{,}9\,\text{N}
\end{aligned}
```
Tukivoima:
```latex
\begin{aligned}
N &= 25\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \\
&\quad - 120\,\text{N}\cdot\sin 30\,{}^\circ \\
&= 245{,}25\,\text{N} - 60\,\text{N} \\
&= 185\,\text{N}
\end{aligned}
```
**Vastaus:** a) Voimakuvio ja yhtälöt yllä. b) $a \approx 0{,}80\,\text{m/s}^2$. c) $F_\mu \approx 84\,\text{N}$, kaksi merkitsevää numeroa kuten massassa ja kulmassa. d) $N \approx 185\,\text{N} \approx 1{,}9\cdot 10^2\,\text{N}$, kaksi merkitsevää numeroa kuten massassa ja kulmassa. Tukivoima on painoa $245\,\text{N}$ pienempi, koska köyden pystykomponentti $T\sin\alpha = 60\,\text{N}$ kannattelee osan painosta: lattian tarvitsee tukea vain loppuosa, $N + T\sin\alpha = mg$.
**Järkevyys:** Köyden vaakakomponentti $104\,\text{N}$ on suurempi kuin kitka $84\,\text{N}$, joten kokonaisvoima $20\,\text{N}$ osoittaa eteenpäin ja laatikko kiihtyy, kuten taulukko näyttää. Kokonaisvoima $ma = 20\,\text{N}$ on noin viidennes vaakakomponentista. Tarkistus pystysuunnassa: $185\,\text{N} + 60\,\text{N} = 245\,\text{N} = mg$.

## fy4-5-L3-05
**Annettu:** $m = 80\,\text{kg}$, kuorma lähtee levosta ja pysähtyy; vaiheet $0$–$2{,}0\,\text{s}$, $2{,}0$–$6{,}0\,\text{s}$ ja $6{,}0$–$8{,}0\,\text{s}$; köyden voima taulukosta; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** nostokorkeus $h$ yksikössä $\text{m}$ sekä kiihtyvyys kussakin vaiheessa
**Periaate:** Kuormaan vaikuttavat paino ja köyden jännitysvoima. Newtonin toisen lain mukaan kiihtyvyys saadaan voimien erotuksesta, ja kiihtyvyyden suunta on kokonaisvoiman suunta: ylös, kun köyden voima on painoa suurempi, ja alas, kun se on painoa pienempi. Kun kiihtyvyys tunnetaan, korkeus saadaan liikkeen vaiheiden matkoista (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*).
**Voimakuvio:** Ensimmäisessä vaiheessa kuorma on suorakulmio, $y$ ylös. Paino $\overline{G}$ alas ja köyden jännitysvoima $\overline{T}$ ylös, jännitysvoima painoa pidempänä. Nopeus ylös ja kiihtyvyys ylös piirretään kuvion viereen erikseen, ei voimiksi. Toisessa vaiheessa nuolet ovat yhtä pitkät ja kolmannessa jännitysvoima on painoa lyhyempi.
```voimakuvio
pinta 0
G 784,8
T 880,7 ylös
v ylös
a ylös
```
**Kuvaajan lukeminen:** Taulukon lukemat jaetaan vaiheisiin hetkien $2{,}0\,\text{s}$ ja $6{,}0\,\text{s}$ mukaan. Vaiheen 1 lukemien summa on $881\,\text{N} + 878\,\text{N} + 883\,\text{N} = 2642\,\text{N}$, joten keskiarvo on $880{,}7\,\text{N}$. Vaiheessa 2 summa on $2354\,\text{N}$ ja keskiarvo $784{,}7\,\text{N}$, vaiheessa 3 summa on $2069\,\text{N}$ ja keskiarvo $689{,}7\,\text{N}$.
**Kaava:** $T - mg = m a_y$, joten $a_y = \dfrac{T - mg}{m}$. Suurin nopeus on $v_\text{max} = a_1 \Delta t_1$, ja matkat ovat $h_1 = \tfrac12 a_1 \Delta t_1^2$, $h_2 = v_\text{max}\,\Delta t_2$ ja $h_3 = \tfrac12 v_\text{max}\,\Delta t_3$, koska kolmannessa vaiheessa nopeus pienenee tasaisesti nollaan. Korkeus on $h = h_1 + h_2 + h_3$
**Muunnokset:** Voimat ovat newtoneina, massa kilogrammoina ja ajat sekunteina, joten muunnoksia ei tarvita. Paino on $mg = 80\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 784{,}8\,\text{N}$.
**Sijoitus:** Kiihtyvyydet:
```latex
\begin{aligned}
a_1 &= \frac{880{,}7 - 784{,}8}{80}\,\frac{\text{m}}{\text{s}^2} \\
&= 1{,}20\,\text{m/s}^2 \\
a_2 &= \frac{784{,}7 - 784{,}8}{80}\,\frac{\text{m}}{\text{s}^2} \\
&\approx 0 \\
a_3 &= \frac{689{,}7 - 784{,}8}{80}\,\frac{\text{m}}{\text{s}^2} \\
&= -1{,}19\,\text{m/s}^2
\end{aligned}
```
Suurin nopeus on $v_\text{max} = 1{,}198\,\text{m/s}^2\cdot 2{,}0\,\text{s} = 2{,}397\,\text{m/s}$. Matkat:
```latex
\begin{aligned}
h_1 &= \tfrac12\cdot 1{,}198\,\tfrac{\text{m}}{\text{s}^2}\cdot (2{,}0\,\text{s})^2 \\
&= 2{,}40\,\text{m} \\
h_2 &= 2{,}397\,\tfrac{\text{m}}{\text{s}}\cdot 4{,}0\,\text{s} \\
&= 9{,}59\,\text{m} \\
h_3 &= \tfrac12\cdot 2{,}397\,\tfrac{\text{m}}{\text{s}}\cdot 2{,}0\,\text{s} \\
&= 2{,}40\,\text{m}
\end{aligned}
```
Korkeus on $h = 2{,}40\,\text{m} + 9{,}59\,\text{m} + 2{,}40\,\text{m} = 14{,}38\,\text{m}$.
**Vastaus:** a) Voimakuvio ja yhtälö yllä. b) $a_1 \approx 1{,}2\,\text{m/s}^2$ ylös, $a_2 \approx 0$ ja $a_3 \approx -1{,}2\,\text{m/s}^2$ eli kiihtyvyys alas. c) Kolmannessa vaiheessa kokonaisvoima osoittaa alas, joten köyden voima on painoa pienempi, vaikka nopeus osoittaa ylös: kuorma hidastuu. Kiihtyvyyden suunta on kokonaisvoiman suunta, ei liikkeen suunta. d) $h \approx 14{,}4\,\text{m}$ eli kahden merkitsevän numeron tarkkuudella $14\,\text{m}$ kuten massassa $80\,\text{kg}$; vastauslaatikkoon käy tarkempi arvo $14{,}4\,\text{m}$.
**Järkevyys:** Tasaisessa vaiheessa köyden voima $785\,\text{N}$ on sama kuin paino $785\,\text{N}$, kuten pitää. Nopeuden muutokset kumoavat toisensa: vaiheessa 3 nopeus pienenee $1{,}19\,\text{m/s}^2\cdot 2{,}0\,\text{s} = 2{,}38\,\text{m/s}$, eli lähes arvosta $2{,}40\,\text{m/s}$ nollaan, joten nosto päättyy levossa kuten tehtävässä. Korkeus on myös suurimman nopeuden ja ajan tulo: kiihdytys- ja hidastusvaihe kattavat yhdessä saman matkan kuin tasainen nopeus ajassa $2{,}0\,\text{s}$, joten $h = v_\text{max}\cdot 6{,}0\,\text{s} = 2{,}397\,\text{m/s}\cdot 6{,}0\,\text{s} = 14{,}4\,\text{m}$.
