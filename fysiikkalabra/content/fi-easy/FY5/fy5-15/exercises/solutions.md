## fy5-15-L1-01
**Annettu:** ikkuna-aukon pinta-ala $A = 1{,}5\,\text{m}^2$ ja aukon läpi kulkeva ääniteho $P = 3{,}0\,\text{mW}$. Teho jakautuu tasaisesti.
**Kysytty:** intensiteetti $I$ yksikössä $\text{W/m}^2$
**Periaate:** Intensiteetti on pinnan läpi kulkeva teho jaettuna pinnan pinta-alalla. Teho jakautuu tasaisesti koko aukolle. Siksi intensiteetti on sama joka kohdassa aukkoa.
**Kaava:** $I = \dfrac{P}{A}$
**Muunnokset:** $P = 3{,}0\,\text{mW} = 3{,}0 \cdot 10^{-3}\,\text{W}$
**Sijoitus:** $I = \dfrac{3{,}0 \cdot 10^{-3}\,\text{W}}{1{,}5\,\text{m}^2} = 2{,}0 \cdot 10^{-3}\,\text{W/m}^2 = 0{,}0020\,\text{W/m}^2$
**Vastaus:** $0{,}0020\,\text{W/m}^2$. Vastauksessa on kaksi merkitsevää numeroa kuten tehossa $3{,}0\,\text{mW}$ ja pinta-alassa $1{,}5\,\text{m}^2$.
**Järkevyys:** Pinta-ala on suurempi kuin $1\,\text{m}^2$. Siksi intensiteetin lukuarvon pitää olla pienempi kuin tehon lukuarvo watteina, ja $0{,}0020 < 0{,}0030$. Intensiteettitasona tämä olisi noin $93\,\text{dB}$. Se sopii aivan ikkunan alla käyvään ruohonleikkuriin.

## fy5-15-L1-02
**Annettu:** intensiteetti $I = 3{,}2 \cdot 10^{-5}\,\text{W/m}^2$, kuulokynnys $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$
**Kysytty:** intensiteettitaso $L$ desibeleinä
**Periaate:** Intensiteettitaso vertaa intensiteettiä kuulokynnykseen logaritmin avulla. Se kertoo, kuinka monta kymmenkertaistusta intensiteetti on kuulokynnyksen yläpuolella, kerrottuna kymmenellä.
**Kaava:** $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$
**Muunnokset:** Niitä ei tarvita. Kumpikin intensiteetti on yksikössä $\text{W/m}^2$, ja yksiköt supistuvat osamäärässä.
**Sijoitus:** $L = 10\,\text{dB} \cdot \lg \dfrac{3{,}2 \cdot 10^{-5}\,\text{W/m}^2}{1{,}0 \cdot 10^{-12}\,\text{W/m}^2} = 10\,\text{dB} \cdot \lg (3{,}2 \cdot 10^{7}) = 10\,\text{dB} \cdot 7{,}505 = 75{,}05\,\text{dB}$
**Vastaus:** $75\,\text{dB}$. Vastaus annetaan kokonaisina desibeleinä, koska intensiteetti on annettu kahdella merkitsevällä numerolla.
**Järkevyys:** Intensiteetti on välillä $10^{-5}$–$10^{-4}\,\text{W/m}^2$. Siksi tason pitää olla välillä $70$–$80\,\text{dB}$. Pölynimuri on tavallisesti suunnilleen yhtä äänekäs kuin vilkas katu.

## fy5-15-L1-03
**Annettu:** intensiteettitaso $L = 95\,\text{dB}$, kuulokynnys $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$
**Kysytty:** intensiteetti $I$ yksikössä $\text{W/m}^2$
**Periaate:** Taso on kymmenen kertaa intensiteettien suhteen logaritmi. Intensiteetti saadaan jakamalla yhtälö $10\,\text{dB}$:llä ja käyttämällä logaritmin määritelmää: jos $\lg x = y$, niin $x = 10^y$.
**Kaava:** $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$, joten $\lg \dfrac{I}{I_0} = \dfrac{L}{10\,\text{dB}}$ ja $I = I_0 \cdot 10^{\,L/(10\,\text{dB})}$
**Muunnokset:** Niitä ei tarvita. Desibelit supistuvat: $\dfrac{L}{10\,\text{dB}} = \dfrac{95\,\text{dB}}{10\,\text{dB}} = 9{,}5$.
**Sijoitus:** $I = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2 \cdot 10^{9{,}5} = 3{,}16 \cdot 10^{-3}\,\text{W/m}^2 = 0{,}00316\,\text{W/m}^2$
**Vastaus:** $0{,}0032\,\text{W/m}^2$. Vastauksessa on kaksi merkitsevää numeroa, koska taso on annettu kokonaisina desibeleinä.
**Järkevyys:** $90\,\text{dB}$ vastaa intensiteettiä $10^{-3}\,\text{W/m}^2$ ja $100\,\text{dB}$ intensiteettiä $10^{-2}\,\text{W/m}^2$, joten $95\,\text{dB}$:n intensiteetin pitää olla näiden välissä. Puolen kymmenkertaistuksen kerroin on $\sqrt{10} \approx 3{,}16$. Tulos $3{,}16 \cdot 10^{-3}\,\text{W/m}^2$ on juuri tämä.

## fy5-15-L1-04
**Annettu:** sireenin ääniteho $P = 2{,}0\,\text{W}$ ja etäisyys $r = 25\,\text{m}$. Ääni leviää tasaisesti joka suuntaan eikä heijastu.
**Kysytty:** intensiteetti $I$ yksikössä $\text{W/m}^2$
**Periaate:** Sireeni toimii pistemäisenä lähteenä. Ääni ei heijastu eikä vaimene. Siksi koko teho kulkee sireeniä ympäröivän $25\,\text{m}$:n säteisen pallopinnan läpi ja jakautuu sille tasaisesti.
**Kaava:** $I = \dfrac{P}{A} = \dfrac{P}{4\pi r^2}$
**Muunnokset:** Niitä ei tarvita. Teho on watteina ja etäisyys metreinä.
**Sijoitus:** $I = \dfrac{2{,}0\,\text{W}}{4\pi \cdot (25\,\text{m})^2} = \dfrac{2{,}0\,\text{W}}{7854\,\text{m}^2} = 2{,}55 \cdot 10^{-4}\,\text{W/m}^2 = 0{,}000255\,\text{W/m}^2$
**Vastaus:** $0{,}00025\,\text{W/m}^2$. Vastauksessa on kaksi merkitsevää numeroa kuten tehossa $2{,}0\,\text{W}$ ja etäisyydessä $25\,\text{m}$.
**Järkevyys:** Pallon pinta-ala on noin $8000\,\text{m}^2$, ja $2\,\text{W} : 8000\,\text{m}^2 = 0{,}00025\,\text{W/m}^2$. Tasona tämä on noin $84\,\text{dB}$. Se on uskottava sireenille $25\,\text{m}$:n päässä.

## fy5-15-L1-05
**Annettu:** intensiteettien suhde $\dfrac{I_2}{I_1} = 100$
**Kysytty:** tasojen erotus $L_2 - L_1$ desibeleinä
**Periaate:** Tasojen erotus riippuu vain intensiteettien suhteesta. Kuulokynnys $I_0$ supistuu pois, kun tasot vähennetään toisistaan.
**Kaava:** $L_2 - L_1 = 10\,\text{dB} \cdot \lg \dfrac{I_2}{I_1}$
**Muunnokset:** Niitä ei tarvita. Suhde on paljas luku.
**Sijoitus:** $L_2 - L_1 = 10\,\text{dB} \cdot \lg 100 = 10\,\text{dB} \cdot 2 = 20\,\text{dB}$
**Vastaus:** $20\,\text{dB}$. Kerroin $100$ on tarkka, joten tulos on tarkka.
**Järkevyys:** Satakertaistus on kaksi peräkkäistä kymmenkertaistusta. Kumpikin lisää tasoa $10\,\text{dB}$: $10\,\text{dB} + 10\,\text{dB} = 20\,\text{dB}$. Taso kasvaa $20\,\text{dB}$, ei satakertaiseksi. Desibeliasteikko on logaritminen.

## fy5-15-L2-01
**Annettu:** kaiuttimen ääniteho $P = 0{,}050\,\text{W}$, etäisyys $r = 3{,}0\,\text{m}$ ja kuulokynnys $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$. Ääni leviää tasaisesti eikä heijastu.
**Kysytty:** intensiteettitaso $L$ desibeleinä
**Periaate:** Kaiutin on pistemäinen lähde. Sen teho jakautuu tasaisesti $3{,}0\,\text{m}$:n säteiselle pallopinnalle. Ensin lasketaan intensiteetti. Sitten sitä verrataan kuulokynnykseen.
**Kaava:** $I = \dfrac{P}{4\pi r^2}$ ja $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$, joten $L = 10\,\text{dB} \cdot \lg \dfrac{P}{4\pi r^2 I_0}$
**Muunnokset:** Niitä ei tarvita. Teho on watteina ja etäisyys metreinä.
**Sijoitus:** $I = \dfrac{0{,}050\,\text{W}}{4\pi \cdot (3{,}0\,\text{m})^2} = 4{,}42 \cdot 10^{-4}\,\text{W/m}^2$, joten $L = 10\,\text{dB} \cdot \lg \dfrac{4{,}42 \cdot 10^{-4}\,\text{W/m}^2}{1{,}0 \cdot 10^{-12}\,\text{W/m}^2} = 10\,\text{dB} \cdot \lg (4{,}42 \cdot 10^{8}) = 86{,}45\,\text{dB}$
**Vastaus:** $86\,\text{dB}$. Vastaus annetaan kokonaisina desibeleinä, koska teho ja etäisyys on annettu kahdella merkitsevällä numerolla.
**Järkevyys:** Intensiteetti on välillä $10^{-4}$–$10^{-3}\,\text{W/m}^2$. Siksi tason pitää olla välillä $80$–$90\,\text{dB}$. Kovalla soiva kannettava kaiutin kuulostaa muutaman metrin päässä suunnilleen vilkkaalta kadulta tai sitä kovemmalta.

## fy5-15-L2-02
**Annettu:** ruohonleikkuri yksinään $L_1 = 85\,\text{dB}$, lehtipuhallin yksinään $L_2 = 88\,\text{dB}$ ja kuulokynnys $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$
**Kysytty:** kuinka paljon suurempi yhteistaso $L$ on kuin $L_2$, eli $L - L_2$ desibeleinä
**Periaate:** Laitteet ovat toisistaan riippumattomia äänilähteitä, joten niiden intensiteetit lasketaan yhteen. Desibelejä ei voi laskea yhteen. Siksi tasot muutetaan ensin intensiteeteiksi.
**Kaava:** $L - L_2 = 10\,\text{dB} \cdot \lg \dfrac{I_1 + I_2}{I_0} - L_2$, missä intensiteetit ja yhteistaso lasketaan näin:
```latex
\begin{aligned}
&I_1 = I_0 \cdot 10^{\,L_1/(10\,\text{dB})} \\
&I_2 = I_0 \cdot 10^{\,L_2/(10\,\text{dB})} \\
&L = 10\,\text{dB} \cdot \lg \dfrac{I_1 + I_2}{I_0}
\end{aligned}
```
**Muunnokset:** Niitä ei tarvita. Kaikki tasot ovat desibeleinä ja intensiteetit yksikössä $\text{W/m}^2$.
**Sijoitus:** $I_1 = 10^{-12}\,\text{W/m}^2 \cdot 10^{8{,}5} = 3{,}16 \cdot 10^{-4}\,\text{W/m}^2$ ja $I_2 = 10^{-12}\,\text{W/m}^2 \cdot 10^{8{,}8} = 6{,}31 \cdot 10^{-4}\,\text{W/m}^2$, joten $L = 10\,\text{dB} \cdot \lg (9{,}47 \cdot 10^{8}) = 89{,}76\,\text{dB}$ ja $L - L_2 = 89{,}76\,\text{dB} - 88\,\text{dB} = 1{,}76\,\text{dB}$
**Vastaus:** $1{,}8\,\text{dB}$. Vastauksessa on kaksi merkitsevää numeroa, koska tasot on annettu kokonaisina desibeleinä.
**Järkevyys:** Jos ruohonleikkuri olisi yhtä kova kuin lehtipuhallin, taso nousisi $3\,\text{dB}$. Heikompi lähde lisää vähemmän. Hyvin heikko lähde ei lisäisi juuri mitään. Siksi $1{,}8\,\text{dB}$ on näiden välissä. Yhteistaso $89{,}8\,\text{dB}$ on paljon pienempi kuin virheellinen summa $173\,\text{dB}$.

## fy5-15-L2-03
**Annettu:** taso $L_1 = 85\,\text{dB}$ etäisyydellä $r_1 = 3{,}0\,\text{m}$ ja uusi etäisyys $r_2 = 12\,\text{m}$. Ääni leviää tasaisesti eikä heijastu.
**Kysytty:** taso $L_2$ etäisyydellä $r_2$ desibeleinä
**Periaate:** Pistemäisen lähteen intensiteetti on kääntäen verrannollinen etäisyyden neliöön, koska sama teho jakautuu pallopinnalle $4\pi r^2$. Tasojen erotus lasketaan intensiteettien suhteesta.
**Kaava:** $\dfrac{I_2}{I_1} = \dfrac{r_1^2}{r_2^2}$ ja $L_2 - L_1 = 10\,\text{dB} \cdot \lg \dfrac{I_2}{I_1}$, joten $L_2 = L_1 + 10\,\text{dB} \cdot \lg \dfrac{r_1^2}{r_2^2}$
**Muunnokset:** Niitä ei tarvita. Kumpikin etäisyys on metreinä, ja yksiköt supistuvat.
**Sijoitus:** $\dfrac{r_1^2}{r_2^2} = \dfrac{(3{,}0\,\text{m})^2}{(12\,\text{m})^2} = \dfrac{1}{16}$, joten $L_2 = 85\,\text{dB} + 10\,\text{dB} \cdot \lg \dfrac{1}{16} = 85\,\text{dB} - 12{,}04\,\text{dB} = 72{,}96\,\text{dB}$
**Vastaus:** $73\,\text{dB}$. Vastaus annetaan kokonaisina desibeleinä kuten lähtötaso $85\,\text{dB}$.
**Järkevyys:** Etäisyys kaksinkertaistuu kahdesti ($3\,\text{m} \to 6\,\text{m} \to 12\,\text{m}$). Kumpikin kaksinkertaistus pienentää tasoa noin $6\,\text{dB}$: $85\,\text{dB} - 6\,\text{dB} - 6\,\text{dB} = 73\,\text{dB}$. Taso pienenee, kuten pitääkin kauempana lähteestä.

## fy5-15-L2-04
**Annettu:** yksi saha $L_1 = 85\,\text{dB}$ ja kaikki sahat yhdessä $L = 91\,\text{dB}$. Sahat ovat samanlaisia ja yhtä kaukana mittarista.
**Kysytty:** sahojen lukumäärä $N$
**Periaate:** Riippumattomien lähteiden intensiteetit lasketaan yhteen. Kun $N$ samanlaista sahaa käy, intensiteetti on $N$-kertainen. Tasojen erotus kertoo siis intensiteettien suhteen $N$.
**Kaava:** $L - L_1 = 10\,\text{dB} \cdot \lg \dfrac{N I_1}{I_1} = 10\,\text{dB} \cdot \lg N$, joten $\lg N = \dfrac{L - L_1}{10\,\text{dB}}$ ja $N = 10^{\,(L - L_1)/(10\,\text{dB})}$
**Muunnokset:** Niitä ei tarvita. Tasot ovat desibeleinä, ja desibelit supistuvat.
**Sijoitus:** $N = 10^{\,(91\,\text{dB} - 85\,\text{dB})/(10\,\text{dB})} = 10^{0{,}6} = 3{,}98$
**Vastaus:** $4$ sahaa. Lukumäärä on kokonaisluku, ja $3{,}98$ pyöristyy siihen, koska tasot on annettu kokonaisina desibeleinä.
**Järkevyys:** Kaksi sahaa nostaisi tasoa $3\,\text{dB}$ ja neljä $6\,\text{dB}$, eli $85\,\text{dB} + 6\,\text{dB} = 91\,\text{dB}$. Tämä on annettu taso, joten neljä sahaa on oikea määrä.

## fy5-15-L3-01
**Annettu:** katsojia $N = 12\,000$, yhden huudon taso kentän keskellä $L_1 = 42\,\text{dB}$ ja kuulutusjärjestelmän taso yksinään $L_K = 80\,\text{dB}$. Huudot ovat yhtä voimakkaita, ja kaikki lähteet ovat toisistaan riippumattomia.
**Kysytty:** kaikkien äänien yhteistaso $L$ desibeleinä
**Periaate:** Riippumattomien lähteiden intensiteetit lasketaan yhteen. Desibelejä ei lasketa yhteen. Ensin lasketaan huutojen yhteistaso. Jokainen huuto tuottaa saman intensiteetin $I_1$, joten huutojen intensiteetti on $N I_1$. Sitten huutojen ja kuulutuksen intensiteetit lasketaan yhteen.
**Kaava:** huudot yhdessä $L_H = L_1 + 10\,\text{dB} \cdot \lg N$, ja koko ääni
```latex
\begin{aligned}
&L = 10\,\text{dB} \cdot \lg \frac{I_H + I_K}{I_0} \\
&I = I_0 \cdot 10^{\,L/(10\,\text{dB})}
\end{aligned}
```
**Muunnokset:** Niitä ei tarvita. Tasot ovat desibeleinä, $N$ on paljas luku ja intensiteetit ovat yksikössä $\text{W/m}^2$.
**Sijoitus:** $L_H = 42\,\text{dB} + 10\,\text{dB} \cdot \lg 12\,000 = 42\,\text{dB} + 40{,}79\,\text{dB} = 82{,}79\,\text{dB}$, joten $I_H = 10^{-12}\,\text{W/m}^2 \cdot 10^{8{,}279} = 1{,}90 \cdot 10^{-4}\,\text{W/m}^2$ ja $I_K = 10^{-12}\,\text{W/m}^2 \cdot 10^{8} = 1{,}0 \cdot 10^{-4}\,\text{W/m}^2$, joten $L = 10\,\text{dB} \cdot \lg \dfrac{2{,}90 \cdot 10^{-4}\,\text{W/m}^2}{1{,}0 \cdot 10^{-12}\,\text{W/m}^2} = 84{,}63\,\text{dB}$
**Vastaus:** $85\,\text{dB}$. Vastaus annetaan kokonaisina desibeleinä, koska tasot on annettu kokonaisina desibeleinä.
**Järkevyys:** Jos lähteitä on $10\,000$, taso nousee tasan $40\,\text{dB}$. Huudot yksin ovat siis noin $83\,\text{dB}$. Kuulutus on huutoja hiljaisempi, joten se nostaa yhteistasoa alle $3\,\text{dB}$. Nousu $2\,\text{dB}$ sopii tähän. Desibelien summa $12\,000 \cdot 42\,\text{dB} + 80\,\text{dB}$ olisi järjetön. Oikeassa hallissa heijastukset nostavat tasoa vielä lisää.

## fy5-15-L3-02
**Annettu:** taso $L_1 = 30\,\text{dB}$ etäisyydellä $r_1 = 0{,}50\,\text{m}$ ja kuulokynnyksen taso $L_2 = 0\,\text{dB}$. Lähde on pistemäinen ja ääni leviää tasaisesti. Heijastuksia, vaimenemista tai taustaääniä ei ole.
**Kysytty:** etäisyys $r_2$, jolla taso on $0\,\text{dB}$, metreinä
**Periaate:** Pistemäisen lähteen intensiteetti on kääntäen verrannollinen etäisyyden neliöön. Tasojen erotus kertoo, kuinka moninkertaisesti intensiteetin pitää pienentyä. Siitä saadaan etäisyyksien suhde.
**Kaava:** $L_1 - L_2 = 10\,\text{dB} \cdot \lg \dfrac{I_1}{I_2} = 10\,\text{dB} \cdot \lg \dfrac{r_2^2}{r_1^2}$, joten $\dfrac{r_2^2}{r_1^2} = 10^{\,(L_1 - L_2)/(10\,\text{dB})}$ ja $r_2 = r_1 \sqrt{10^{\,(L_1 - L_2)/(10\,\text{dB})}}$
**Muunnokset:** Niitä ei tarvita. Etäisyys on metreinä, ja desibelit supistuvat.
**Sijoitus:** $r_2 = 0{,}50\,\text{m} \cdot \sqrt{10^{\,(30\,\text{dB} - 0\,\text{dB})/(10\,\text{dB})}} = 0{,}50\,\text{m} \cdot \sqrt{1000} = 0{,}50\,\text{m} \cdot 31{,}6 = 15{,}8\,\text{m}$
**Vastaus:** $16\,\text{m}$. Vastauksessa on kaksi merkitsevää numeroa kuten etäisyydessä $0{,}50\,\text{m}$.
**Järkevyys:** Pudotus $30\,\text{dB}$ tarkoittaa, että intensiteetti pienenee tuhannesosaan. Sen aiheuttaa $\sqrt{1000} \approx 32$-kertainen etäisyys. Todellisuudessa ininää ei kuule näin kaukaa. Taustaäänet peittävät sen, ja oma kuulokynnys voi olla korkeampi. Tulos on ihanteellisen tilanteen yläraja.

## fy5-15-L3-03
**Kysytty:** onko negatiivinen intensiteettitaso mahdoton, mitä se tarkoittaa ja voiko tuulettimen kuulla
**Periaate:** Intensiteettitaso $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$ ei ole intensiteetti. Se on vertailu kuulokynnykseen $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$. Logaritmi on negatiivinen, kun sen sisällä oleva luku on positiivinen mutta pienempi kuin yksi.
**Mallivastaus:** Opiskelija ei ole oikeassa. Negatiivinen taso ei tarkoita negatiivista intensiteettiä. Se tarkoittaa, että intensiteetti on pienempi kuin kuulokynnys. Tässä $\lg \dfrac{I}{I_0} = -0{,}5$, joten
```latex
I = I_0 \cdot 10^{-0{,}5} \approx 3{,}2 \cdot 10^{-13}\,\text{W/m}^2
```
Intensiteetti on positiivinen, noin kolmasosa kuulokynnyksestä. Aina kun intensiteetti pienenee kymmenesosaan, taso laskee $10\,\text{dB}$. Siksi kuulokynnystä heikommilla äänillä taso on negatiivinen, vaikka intensiteetti on aina positiivinen. Keskimääräinen kuulija ei kuule tuuletinta, koska ääni on kuulokynnyksen alapuolella. Kuulokynnys $I_0$ on kuitenkin sovittu vertailuarvo. Kuulokynnys vaihtelee ihmisestä ja taajuudesta toiseen. Nuoret herkkäkuuloiset ihmiset voivat kuulla herkimmillä taajuuksilla, noin $3000\,\text{Hz}$:n tienoilla, ääniä, joiden taso on hieman alle $0\,\text{dB}$. Hiljaisessa kaiuttomassa huoneessa mittaus on siis aivan mahdollinen.

**Itsearviointi:** Vastauksessani

- sanon, että intensiteetti on aina positiivinen ja että negatiivinen taso tarkoittaa intensiteettiä, joka on pienempi kuin kuulokynnys $I_0$
- lasken tai arvioin intensiteetin tasosta $-5\,\text{dB}$ potenssina $10^{-0{,}5}$
- sanon, että kuulokynnys riippuu ihmisestä ja taajuudesta. Siksi tuulettimen voivat kuulla vain herkimmät kuulijat herkimmillä taajuuksilla.


## fy5-15-L1-06
**Kysytty:** mitä intensiteettitaso $0\,\text{dB}$ tarkoittaa
**Periaate:** Intensiteettitaso on $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$. Se vertaa intensiteettiä kuulokynnykseen $I_0$. Taso on nolla, kun logaritmin sisällä on luku $1$.
**Mallivastaus:** Oikea vaihtoehto on se, jonka mukaan intensiteetti on $I_0$, koska silloin $\lg(I/I_0) = \lg 1 = 0$. Taso $0\,\text{dB}$ on siis kuulokynnys. Se on heikoin ääni, jonka kuulija vielä juuri havaitsee. Se ei ole hiljaisuus. Vaihtoehto, jonka mukaan ääntä ei ole, on väärin. Nollan logaritmia ei ole olemassa, eikä intensiteetti $I = 0$ anna mitään tasoa. Vaihtoehto kipukynnyksestä on väärin. Kipukynnys on moninkertainen kuulokynnykseen verrattuna, eli se on asteikon yläpäässä. Vaihtoehto, jonka mukaan nolla on asteikon alaraja, on väärin. Heikommilla äänillä osamäärä $I/I_0$ on pienempi kuin $1$, ja taso on negatiivinen.

## fy5-15-L1-07
**Kysytty:** mikä on virhe laskussa, jossa kahden $64\,\text{dB}$:n koneen yhteistasoksi saadaan $128\,\text{dB}$
**Periaate:** Toisistaan riippumattomien äänilähteiden intensiteetit lasketaan yhteen. Yhteistaso lasketaan summaintensiteetistä. Desibelit ovat logaritminen asteikko, joten niitä ei voi laskea yhteen.
**Mallivastaus:** Virhe on se, että opiskelija laskee desibelit yhteen. Kaksi samanlaista konetta kaksinkertaistaa intensiteetin. Kaksinkertainen intensiteetti lisää tasoa vain $10\,\text{dB} \cdot \lg 2 \approx 3{,}0\,\text{dB}$. Siksi yhteistaso on noin $67\,\text{dB}$. Väite, että kumpikin kone lisäisi kolme desibeliä ja taso olisi $70\,\text{dB}$, on väärin. Kolmen desibelin lisäys tulee koko yhteistasoon vain kerran. Väite keskiarvosta $64\,\text{dB}$ on väärin, koska toinen kone lisää ääntä. Väite kymmenkertaisesta intensiteetistä ja tasosta $74\,\text{dB}$ on väärin, koska kaksi konetta antaa vain kaksinkertaisen intensiteetin. Lisäys $10\,\text{dB}$ vaatisi kymmenen konetta.

## fy5-15-L1-08
**Annettu:** kipukynnyksen intensiteetti $I = 1{,}0\,\text{W/m}^2$ ja kuulokynnys $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$
**Kysytty:** intensiteettitaso $L$ desibeleinä
**Periaate:** Intensiteettitaso saadaan vertaamalla intensiteettiä kuulokynnykseen $I_0$ logaritmisella asteikolla.
**Kaava:** $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$
**Muunnokset:** Niitä ei tarvita. Kumpikin intensiteetti on yksikössä $\text{W/m}^2$, joten yksiköt supistuvat osamäärässä.
**Sijoitus:** osamäärä on $I/I_0 = 10^{12}$, joten
```latex
\begin{aligned}
L &= 10\,\text{dB} \cdot \lg \dfrac{1{,}0\,\text{W/m}^2}{1{,}0 \cdot 10^{-12}\,\text{W/m}^2} \\
&= 10\,\text{dB} \cdot \lg 10^{12} \\
&= 120\,\text{dB}
\end{aligned}
```
**Vastaus:** $120\,\text{dB}$. Vastauksessa on kaksi merkitsevää numeroa kuten kipukynnyksessä $1{,}0\,\text{W/m}^2$.
**Järkevyys:** Intensiteettien suhde on $10^{12}$. Jokainen kymmenkertaistuminen lisää tasoa $10\,\text{dB}$, joten $12 \cdot 10\,\text{dB} = 120\,\text{dB}$. Tämä sopii yleiseen tietoon: $120\,\text{dB}$ on suihkukoneen lähellä oleva taso, ja se sattuu korvaan.

## fy5-15-L2-05
**Annettu:** taulukosta etäisyydet $1{,}0\,\text{m}$, $2{,}0\,\text{m}$, $4{,}0\,\text{m}$, $8{,}0\,\text{m}$ ja $16\,\text{m}$ sekä tasot $84{,}2\,\text{dB}$, $78{,}1\,\text{dB}$, $72{,}3\,\text{dB}$, $66{,}2\,\text{dB}$ ja $60{,}1\,\text{dB}$
**Kysytty:** tason keskimääräinen lasku $\Delta L_1$ yhtä etäisyyden kaksinkertaistumista kohti desibeleinä
**Periaate:** Jokainen mittauspiste on edellisen kaksinkertainen. Etäisyydet ovat $1{,}0\,\text{m} \to 2{,}0\,\text{m} \to 4{,}0\,\text{m} \to 8{,}0\,\text{m} \to 16\,\text{m}$, joten kaksinkertaistumisia on $n = 4$. Keskimääräinen lasku saadaan jakamalla tason kokonaismuutos luvulla $n$.
**Kaava:** $\Delta L_1 = \dfrac{L(1{,}0\,\text{m}) - L(16\,\text{m})}{n}$
**Muunnokset:** Niitä ei tarvita. Tasot ovat desibeleinä, ja $n$ on paljas luku.
**Sijoitus:** kaksinkertaistumisia on $n = 4$, joten
```latex
\begin{aligned}
\Delta L_1 &= \dfrac{84{,}2\,\text{dB} - 60{,}1\,\text{dB}}{4} \\
&= \dfrac{24{,}1\,\text{dB}}{4} \\
&= 6{,}025\,\text{dB}
\end{aligned}
```
**Vastaus:** $6{,}03\,\text{dB}$. Vastauksessa on kolme merkitsevää numeroa kuten mittarin lukemissa. Jako luvulla $4$ on tarkka.
**Järkevyys:** Pistemäisen lähteen malli ennustaa, että kaksinkertainen etäisyys pienentää intensiteetin neljäsosaan. Silloin taso laskee $10\,\text{dB} \cdot \lg 4 = 6{,}02\,\text{dB}$. Mitattu keskimääräinen lasku $6{,}03\,\text{dB}$ on käytännössä sama. Yksittäiset laskut $6{,}1\,\text{dB}$, $5{,}8\,\text{dB}$, $6{,}1\,\text{dB}$ ja $6{,}1\,\text{dB}$ vaihtelevat vain mittausvirheen verran. Avoin kenttä toimii siis pistemäisen lähteen mallina.

## fy5-15-L2-06
**Annettu:** taulukosta $L(1{,}0\,\text{m}) = 86{,}0\,\text{dB}$ ja $L(8{,}0\,\text{m}) = 71{,}9\,\text{dB}$. Etäisyys kasvaa kertoimella $\dfrac{8{,}0\,\text{m}}{1{,}0\,\text{m}} = 8{,}0$.
**Kysytty:** mitatun tason $L_\text{mit}$ ja pistemäisen lähteen mallin ennusteen $L_\text{malli}$ erotus $L_\text{mit} - L_\text{malli}$ desibeleinä
**Periaate:** Jos ääni etenisi pistemäisestä lähteestä ilman heijastuksia, intensiteetti olisi kääntäen verrannollinen etäisyyden neliöön. Silloin tasojen erotus riippuisi vain etäisyyksien suhteesta. Ennuste lasketaan $1{,}0\,\text{m}$:n lukemasta, ja sitä verrataan mittaukseen.
**Kaava:** $\Delta L = L_\text{mit} - L_\text{malli}$, missä ennuste on
```latex
L_\text{malli} = L_1 - 10\,\text{dB} \cdot \lg \left[\left(\dfrac{r_2}{r_1}\right)^{2}\right]
```
**Muunnokset:** Niitä ei tarvita. Etäisyydet ovat metreinä, ja suhde on yksikötön.
**Sijoitus:** etäisyyksien suhde on $8{,}0$, joten
```latex
\begin{aligned}
L_\text{malli} &= 86{,}0\,\text{dB} - 10\,\text{dB} \cdot \lg 64 \\
&= 86{,}0\,\text{dB} - 18{,}06\,\text{dB} \\
&= 67{,}94\,\text{dB} \\
L_\text{mit} - L_\text{malli} &= 71{,}9\,\text{dB} - 67{,}94\,\text{dB} \\
&= 3{,}96\,\text{dB}
\end{aligned}
```
**Vastaus:** $4{,}0\,\text{dB}$. Vastauksessa on kaksi merkitsevää numeroa, koska lukemat on annettu kymmenesosadesibelin tarkkuudella ja ennuste on pyöristetty. Kohdan a) ennuste on noin $67{,}9\,\text{dB}$.
**Järkevyys:** Taso $3{,}96\,\text{dB}$ suurempi tarkoittaa, että mitattu intensiteetti on noin $10^{0{,}396} = 2{,}5$-kertainen malliin verrattuna. Selitys: salin seinät, katto ja lattia heijastavat ääntä. Kuuntelupaikkaan tulee siis suoran äänen lisäksi heijastunutta ääntä. Suora ääni heikkenee etäisyyden mukana, mutta heijastunut ääni ei läheskään yhtä paljon. Siksi ero kasvaa kauempana. Mitatut laskut $5{,}9\,\text{dB}$, $5{,}1\,\text{dB}$ ja $3{,}1\,\text{dB}$ jäävät pienemmiksi kuin pistemäisen lähteen $6{,}0\,\text{dB}$.

## fy5-15-L2-07
**Annettu:** taulukosta vertailumittarin tasot $50{,}0\,\text{dB}$, $60{,}0\,\text{dB}$, $70{,}0\,\text{dB}$ ja $80{,}0\,\text{dB}$ sekä puhelimen lukemat $54{,}1\,\text{dB}$, $63{,}8\,\text{dB}$, $74{,}2\,\text{dB}$ ja $83{,}9\,\text{dB}$. Lisäksi $90{,}0\,\text{dB}$ ja $88{,}6\,\text{dB}$.
**Kysytty:** kerroin $k = \dfrac{I_\text{puh}}{I_\text{ref}}$ eli kuinka moninkertaiseksi puhelin arvioi intensiteetin
**Periaate:** Puhelimen virhe $\Delta L = L_\text{puh} - L_\text{ref}$ on neljällä pienimmällä tasolla lähes sama. Se on siis systemaattinen virhe eli aina samansuuntainen virhe. Tasojen erotus riippuu vain intensiteettien suhteesta. Siksi keskimääräisestä virheestä saadaan intensiteettien suhde.
**Kaava:** $\Delta L_\text{ka} = \dfrac{\Sigma \Delta L}{4}$ ja $\Delta L_\text{ka} = 10\,\text{dB} \cdot \lg k$, joten
```latex
k = 10^{\,\Delta L_\text{ka}/(10\,\text{dB})}
```
**Muunnokset:** Niitä ei tarvita. Kaikki tasot ovat desibeleinä, ja suhde $k$ on yksikötön.
**Sijoitus:** Virheet ovat $4{,}1\,\text{dB}$, $3{,}8\,\text{dB}$, $4{,}2\,\text{dB}$ ja $3{,}9\,\text{dB}$. Niiden summa on $16{,}0\,\text{dB}$, joten
```latex
\begin{aligned}
\Delta L_\text{ka} &= \dfrac{16{,}0\,\text{dB}}{4} \\
&= 4{,}0\,\text{dB} \\
k &= 10^{\,4{,}0\,\text{dB}/(10\,\text{dB})} \\
&= 2{,}51
\end{aligned}
```
**Vastaus:** $2{,}5$. Vastauksessa on kaksi merkitsevää numeroa kuten keskimääräisessä virheessä $4{,}0\,\text{dB}$. Puhelin näyttää tason keskimäärin $4{,}0\,\text{dB}$ liian suureksi. Se arvioi intensiteetin noin $2{,}5$-kertaiseksi. Kohdan c) tulos: tasolla $90{,}0\,\text{dB}$ virheen odottaisi olevan $+4\,\text{dB}$. Puhelin näyttää kuitenkin $1{,}4\,\text{dB}$ liian vähän, joten lukema ei seuraa muita. Mikrofoni todennäköisesti kyllästyy eli ylikuormittuu kovalla äänellä.
**Järkevyys:** Kolme desibeliä vastaisi kaksinkertaista intensiteettiä. Viisi desibeliä vastaisi intensiteettiä $10^{0{,}5} = 3{,}2$-kertaiseksi. Siksi $4{,}0\,\text{dB}$ antaa luvun $2$ ja $3{,}2$ väliltä, ja $2{,}5$ on sellainen. Systemaattinen virhe korjataan vähentämällä lukemista noin $4\,\text{dB}$. Korjaus pätee kuitenkin vain mitatulla alueella $50\,\text{dB}$–$80\,\text{dB}$.

## fy5-15-L3-04
**Annettu:** taulukosta etäisyydet $5{,}0\,\text{m}$, $10{,}0\,\text{m}$, $20{,}0\,\text{m}$ ja $40{,}0\,\text{m}$ sekä tasot $91{,}1\,\text{dB}$, $84{,}8\,\text{dB}$, $79{,}3\,\text{dB}$ ja $72{,}6\,\text{dB}$. Raja-arvo on $L_\text{raja} = 55\,\text{dB}$ ja kuulokynnys $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$. Lähde on pistemäinen, ääni leviää tasaisesti, eikä heijastuksia tai vaimenemista ole.
**Kysytty:** a) kaiuttimen ääniteho $P$ ja b) etäisyys $r$, jolla taso on $55\,\text{dB}$, metreinä
**Periaate:** Jokaisesta lukemasta lasketaan intensiteetti tasoyhtälöllä. Pistemäiselle lähteelle $I = \dfrac{P}{4\pi r^2}$ antaa tehon $P = I \cdot 4\pi r^2$. Lukemissa on mittausvirhettä, joten teho on kaikkien arvojen keskiarvo. Kun teho tunnetaan, sama kaava ratkaistaan etäisyydelle, jolla intensiteetti vastaa rajatasoa.
**Kaava:** $r = \sqrt{\dfrac{P}{4\pi I_\text{raja}}}$, missä teho ja intensiteetit lasketaan näin:
```latex
\begin{aligned}
&I = I_0 \cdot 10^{\,L/(10\,\text{dB})} \\
&P = I \cdot 4\pi r^2
\end{aligned}
```
**Muunnokset:** Niitä ei tarvita. Etäisyydet ovat metreinä ja intensiteetit yksikössä $\text{W/m}^2$.
**Sijoitus:** Lukemista saadaan intensiteetit $1{,}288 \cdot 10^{-3}\,\text{W/m}^2$, $3{,}020 \cdot 10^{-4}\,\text{W/m}^2$, $8{,}51 \cdot 10^{-5}\,\text{W/m}^2$ ja $1{,}820 \cdot 10^{-5}\,\text{W/m}^2$. Tehot ovat $0{,}4047\,\text{W}$, $0{,}3795\,\text{W}$, $0{,}4278\,\text{W}$ ja $0{,}3659\,\text{W}$. Tehojen summa on $1{,}578\,\text{W}$, joten keskiarvo on $P = 0{,}3945\,\text{W}$. Rajatason intensiteetti on $I_\text{raja} = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2 \cdot 10^{5{,}5} = 3{,}162 \cdot 10^{-7}\,\text{W/m}^2$, ja
```latex
\begin{aligned}
r &= \sqrt{\dfrac{0{,}3945\,\text{W}}{4\pi \cdot 3{,}162 \cdot 10^{-7}\,\text{W/m}^2}} \\
&= \sqrt{9{,}93 \cdot 10^{4}\,\text{m}^2} \\
&= 315\,\text{m} \approx 3{,}2 \cdot 10^{2}\,\text{m}
\end{aligned}
```
**Vastaus:** Kohdan b) tulos on $3{,}2 \cdot 10^{2}\,\text{m}$. Vastauksessa on kaksi merkitsevää numeroa, koska raja-arvo $55\,\text{dB}$ on annettu täysinä desibeleinä. Muutos $\pm 0{,}5\,\text{dB}$ muuttaa etäisyyttä välillä $297\,\text{m}$–$334\,\text{m}$. Kohdan a) ääniteho on noin $0{,}39\,\text{W}$.
**Järkevyys:** Taso laskee $6{,}0\,\text{dB}$ jokaisella etäisyyden kaksinkertaistumisella. Tasosta $72{,}6\,\text{dB}$ kohdassa $40\,\text{m}$ tasoon $55\,\text{dB}$ on noin $17{,}6\,\text{dB}$. Se on noin $2{,}9$ kaksinkertaistumista, joten etäisyys on noin $40\,\text{m} \cdot 2^{2{,}9} \approx 300\,\text{m}$. Se sopii tulokseen $3{,}2 \cdot 10^{2}\,\text{m}$. **Perustelu (kohta c):** Yksittäinen lukema sisältää mittausvirhettä. Tehoarviot vaihtelevat välillä $0{,}366\,\text{W}$–$0{,}428\,\text{W}$, joten keskiarvo tasoittaa virheen. Pitkällä matkalla ilman aiheuttama vaimennus, maan ja kasvillisuuden vaimennus, tuuli, lämpötilakerrokset ja rakennusten heijastukset voivat poiketa mallista, koska malli ei sisällä niitä. Todellinen taso voi olla pienempi tai suurempi kuin malli ennustaa. Ilman ja maan vaimennus pienentää sitä yleensä, ja heijastukset suurentavat sitä. Siksi tulos $3{,}2 \cdot 10^{2}\,\text{m}$ on arvio.

## fy5-15-L3-05
**Annettu:** kitaravahvistimen teho $P_1 = 0{,}20\,\text{W}$, rumpusetin taso $L_2 = 90\,\text{dB}$ etäisyydellä $r_2 = 2{,}0\,\text{m}$, kuuntelijan etäisyys $r = 8{,}0\,\text{m}$, tavoitetaso $L_\text{raja} = 70\,\text{dB}$ ja $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$. Lähteet ovat samassa paikassa, riippumattomia ja pistemäisiä.
**Kysytty:** a) yhteistaso $L$ etäisyydellä $8{,}0\,\text{m}$ ja b) etäisyys $r_\text{raja}$, jolla yhteistaso on $70\,\text{dB}$, metreinä
**Periaate:** Lähteet ovat toisistaan riippumattomia, joten niiden intensiteetit lasketaan yhteen. Vahvistimen intensiteetti saadaan tehosta kaavalla $I = \dfrac{P}{4\pi r^2}$. Rumpujen intensiteetti saadaan tasosta tasoyhtälöllä ja etäisyyden kaksinkertaistumisen vaikutuksella. Molemmat intensiteetit pienenevät kuten $\dfrac{1}{r^2}$, joten myös summaintensiteetti pienenee niin. Etäisyys saadaan suhteesta.
**Kaava:** $r_\text{raja} = r \sqrt{\dfrac{I}{I_\text{raja}}}$, missä summaintensiteetti ja taso lasketaan näin:
```latex
\begin{aligned}
&I = I_1 + I_2 \\
&L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}
\end{aligned}
```
**Muunnokset:** Niitä ei tarvita. Etäisyydet ovat metreinä ja tasot desibeleinä.
**Sijoitus:** Vahvistin: $I_1 = \dfrac{0{,}20\,\text{W}}{4\pi \cdot (8{,}0\,\text{m})^2} = 2{,}487 \cdot 10^{-4}\,\text{W/m}^2$. Rummut: tasosta $90\,\text{dB}$ lähellä saadaan $I = 10^{-12}\,\text{W/m}^2 \cdot 10^{9} = 1{,}0 \cdot 10^{-3}\,\text{W/m}^2$ etäisyydellä $2{,}0\,\text{m}$. Etäisyydellä $8{,}0\,\text{m}$ intensiteetti on $\left(\dfrac{2{,}0}{8{,}0}\right)^2 = \dfrac{1}{16}$ siitä, eli $I_2 = 6{,}25 \cdot 10^{-5}\,\text{W/m}^2$. Siten
```latex
\begin{aligned}
I &= 2{,}487 \cdot 10^{-4}\,\text{W/m}^2 \\
&\quad + 6{,}25 \cdot 10^{-5}\,\text{W/m}^2 \\
&= 3{,}112 \cdot 10^{-4}\,\text{W/m}^2 \\
L &= 10\,\text{dB} \cdot \lg \dfrac{3{,}112 \cdot 10^{-4}}{10^{-12}} \\
&= 84{,}93\,\text{dB}
\end{aligned}
```
Tasoa $70\,\text{dB}$ vastaa $I_\text{raja} = 10^{-12}\,\text{W/m}^2 \cdot 10^{7} = 1{,}0 \cdot 10^{-5}\,\text{W/m}^2$, joten
```latex
\begin{aligned}
r_\text{raja} &= 8{,}0\,\text{m} \cdot \sqrt{\dfrac{3{,}112 \cdot 10^{-4}}{1{,}0 \cdot 10^{-5}}} \\
&= 8{,}0\,\text{m} \cdot 5{,}579 \\
&= 44{,}6\,\text{m}
\end{aligned}
```
**Vastaus:** Kohdan b) tulos on $45\,\text{m}$. Vastauksessa on kaksi merkitsevää numeroa kuten tehossa $0{,}20\,\text{W}$ ja etäisyydessä $8{,}0\,\text{m}$. Kohdan a) yhteistaso on noin $85\,\text{dB}$.
**Järkevyys:** Taso laskee yhteistasosta $84{,}9\,\text{dB}$ tasoon $70\,\text{dB}$, eli $14{,}9\,\text{dB}$. Se on noin $2{,}5$ etäisyyden kaksinkertaistumista ($6{,}0\,\text{dB}$ kutakin kohti), ja $8{,}0\,\text{m} \cdot 2^{2{,}5} \approx 45\,\text{m}$. Yhteistaso on suurempi kuin kumpikaan lähde yksin ($84{,}0\,\text{dB}$ ja $78{,}0\,\text{dB}$), mutta pienempi kuin niiden desibelien summa. **Perustelu (kohta c):** Kuulon intensiteettialue on valtava. Kuulokynnyksestä kipukynnykseen intensiteetti kasvaa kertoimella $10^{12}$. Logaritminen asteikko pakkaa tämän alueen lukuihin $0\,\text{dB}$–$120\,\text{dB}$. Kuulo erottaa likimain suhteellisia eroja. Siksi sama intensiteetin kerroin, esimerkiksi kaksinkertaistuminen, tuntuu suunnilleen samalta muutokselta (noin $3\,\text{dB}$) hiljaisella ja kovalla äänellä.
