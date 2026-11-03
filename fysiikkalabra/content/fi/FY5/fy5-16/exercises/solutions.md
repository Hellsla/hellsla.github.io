## fy5-16-L1-01
**Annettu:** melutaso $L = 91\,\text{dB}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** sallittu päivittäinen aika $t_\text{sall}$ tunteina
**Periaate:** Melualtistus lasketaan energian keskiarvona: jokainen $3\,\text{dB}$:n nousu kaksinkertaistaa intensiteetin, joten sama annos täyttyy puolessa ajassa.
**Kaava:** $t_\text{sall} = \dfrac{t_0}{2^{\,n}}$, missä $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Muunnokset:** Ei tarvita: tasot ovat desibeleinä ja aika saadaan tunteina.
**Sijoitus:** $n = \dfrac{91\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 2$, $t_\text{sall} = \dfrac{8\,\text{h}}{2^2} = 2{,}0\,\text{h}$
**Vastaus:** $2{,}0\,\text{h}$. Tasot ovat kokonaisia desibelejä ja sääntö on arvio, joten kaksi merkitsevää numeroa riittää.
**Järkevyys:** Kaksi puolitusta: $8\,\text{h} \to 4\,\text{h} \to 2\,\text{h}$. Intensiteetti on nelinkertainen, ja $4 \cdot 2\,\text{h} = 8\,\text{h}$, joten annos on sama kuin vertailussa.

## fy5-16-L1-02
**Annettu:** yhden puhaltimen taso $L_1 = 70\,\text{dB}$; kaksi samanlaista puhallinta
**Kysytty:** yhteinen taso $L$ desibeleinä
**Periaate:** Kahden lähteen intensiteetit summautuvat, eivät tasot. Kaksi yhtä voimakasta lähdettä kaksinkertaistaa intensiteetin (luku *Äänen voimakkuus*).
**Kaava:** $L = L_1 + 10\,\text{dB} \cdot \lg \dfrac{2 I_1}{I_1} = L_1 + 10\,\text{dB} \cdot \lg 2$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $L = 70\,\text{dB} + 10\,\text{dB} \cdot \lg 2 = 70\,\text{dB} + 3{,}01\,\text{dB} = 73{,}01\,\text{dB}$
**Vastaus:** $73\,\text{dB}$, kokonaisina desibeleinä kuten lähtötieto.
**Järkevyys:** Taso nousee vain vähän, vaikka melua tuottava laite kaksinkertaistuu. Tulos $140\,\text{dB}$ olisi kipukynnyksen yläpuolella, mikä ei sovi kahdelle puhaltimelle.

## fy5-16-L1-03
**Annettu:** $L_1 = 88\,\text{dB}$ etäisyydellä $r_1 = 4{,}0\,\text{m}$, uusi etäisyys $r_2 = 8{,}0\,\text{m}$; pistemäinen lähde avoimessa tilassa
**Kysytty:** taso $L_2$ etäisyydellä $r_2$
**Periaate:** Pistemäisen lähteen intensiteetti on kääntäen verrannollinen etäisyyden neliöön, joten kaksinkertainen etäisyys antaa neljäsosan intensiteetistä. Se laskee tasoa $10\,\text{dB} \cdot \lg 4 \approx 6\,\text{dB}$ (luku *Äänen voimakkuus*).
**Kaava:** $L_2 = L_1 - 6\,\text{dB}$, kun $r_2 = 2 r_1$
**Muunnokset:** Ei tarvita: $r_2 : r_1 = 8{,}0\,\text{m} : 4{,}0\,\text{m} = 2$.
**Sijoitus:** $L_2 = 88\,\text{dB} - 6\,\text{dB} = 82\,\text{dB}$
**Vastaus:** $82\,\text{dB}$, kokonaisina desibeleinä kuten lähtötieto.
**Järkevyys:** Taso pienenee mutta pysyy samaa suuruusluokkaa: neljäsosa intensiteetistä ei ole neljäsosa desibeliluvusta. Heijastavassa tilassa pudotus olisi pienempi.

## fy5-16-L1-04
**Annettu:** melutaso $L_\text{m} = 106\,\text{dB}$, suojainten vaimennus $\Delta L = 23\,\text{dB}$
**Kysytty:** korvaan pääsevä taso $L$
**Periaate:** Kuulonsuojaimen vaimennus kertoo, kuinka monta desibeliä se pienentää korvaan pääsevää tasoa, joten vaimennus vähennetään melutasosta.
**Kaava:** $L = L_\text{m} - \Delta L$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $L = 106\,\text{dB} - 23\,\text{dB} = 83\,\text{dB}$
**Vastaus:** $83\,\text{dB}$, kokonaisina desibeleinä kuten lähtötiedot.
**Järkevyys:** Taso jää ylemmän toiminta-arvon $85\,\text{dB}$ alle, joten suojaimet riittävät koko työpäiväksi, jos ne ovat hyvin paikallaan ja niitä pidetään koko ajan. Ilman suojaimia sallittu aika olisi noin $4\,\text{min}$.

## fy5-16-L1-05
**Kysytty:** kuuluuko kukin keino lähteeseen, kulkutiehen vai korvaan
**Periaate:** Lähteessä vähennetään syntyvää ääntä, kulkutiellä estetään tai vaimennetaan äänen eteneminen lähteestä kuulijaan, ja korvalla vähennetään korvaan pääsevää ääntä.
**Mallivastaus:** a) Meluseinä pysäyttää suoran äänen tien ja asuntojen välissä, joten se on kulkutien keino. b) Kotelo sulkee äänen heti koneen ympärille, joten se torjuu melua lähteessä. c) Korvatulpat vaimentavat ääntä vasta korvalla. d) Kattoon asennetut levyt eivät hiljennä konetta, mutta ne vaimentavat heijastuksia, joiden kautta ääni kulkee työntekijälle, joten ne ovat kulkutien keino.

## fy5-16-L2-01
**Annettu:** kaksi samanlaista konetta, kumpikin $L_1 = 85\,\text{dB}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** sallittu päivittäinen aika $t_\text{sall}$ tunteina
**Periaate:** Kahden yhtä voimakkaan lähteen intensiteetit summautuvat, joten intensiteetti kaksinkertaistuu ja taso nousee noin $3\,\text{dB}$. Sitten jokainen $3\,\text{dB}$ toiminta-arvon yli puolittaa sallitun ajan.
**Kaava:** $L = L_1 + 3\,\text{dB}$ ja $t_\text{sall} = \dfrac{t_0}{2^{\,n}}$, missä $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $L = 85\,\text{dB} + 3\,\text{dB} = 88\,\text{dB}$, $n = \dfrac{88\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 1$, $t_\text{sall} = \dfrac{8\,\text{h}}{2^1} = 4{,}0\,\text{h}$
**Vastaus:** $4{,}0\,\text{h}$. Sääntö on arvio, joten kaksi merkitsevää numeroa riittää.
**Järkevyys:** Toinen kone tuo saman energian lisää, joten kokonaisenergia kertyy kaksi kertaa nopeammin, ja annos täyttyy puolessa ajassa. Tulos on johdonmukainen: $2 \cdot 4\,\text{h} = 8\,\text{h}$.

## fy5-16-L2-02
**Annettu:** taso korvassa $L = 94\,\text{dB}$, kuunteluaika $t = 1{,}5\,\text{h}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** annos prosentteina vertailuannoksesta
**Periaate:** Lasketaan ensin sallittu aika tasolla $94\,\text{dB}$: siinä ajassa kertyy täsmälleen vertailuannos. Annoksen osuus on kuunteluajan ja sallitun ajan suhde, koska taso on koko ajan sama.
**Kaava:** $t_\text{sall} = \dfrac{t_0}{2^{\,n}}$, missä $n = \dfrac{L - L_0}{3\,\text{dB}}$, ja osuus $= \dfrac{t}{t_\text{sall}} \cdot 100\,\%$
**Muunnokset:** Ei tarvita: ajat ovat tunteina, ja yksikkö supistuu.
**Sijoitus:** $n = \dfrac{94\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 3$, $t_\text{sall} = \dfrac{8\,\text{h}}{2^3} = 1{,}0\,\text{h}$, osuus $= \dfrac{1{,}5\,\text{h}}{1{,}0\,\text{h}} \cdot 100\,\% = 150\,\%$
**Vastaus:** $150\,\%$, kaksi merkitsevää numeroa kuten ajassa $1{,}5\,\text{h}$.
**Järkevyys:** Kuunteluaika on pidempi kuin sallittu aika, joten annos ylittää vertailun, eli yli $100\,\%$ on odotettu. Jos ääntä pienennettäisiin $3\,\text{dB}$, annos puolittuisi $75\,\%$:iin.

## fy5-16-L2-03
**Annettu:** $L_1 = 78\,\text{dB}$ etäisyydellä $r_1 = 2{,}0\,\text{m}$, toivottu taso $L_2 = 60\,\text{dB}$; pistemäinen lähde avoimessa tilassa
**Kysytty:** etäisyys $r_2$ metreinä
**Periaate:** Avoimessa tilassa jokainen etäisyyden kaksinkertaistuminen laskee tasoa $6\,\text{dB}$, koska intensiteetti pienenee neljäsosaan (luku *Äänen voimakkuus*). Lasketaan, montako kaksinkertaistumista tarvitaan.
**Kaava:** $k = \dfrac{L_1 - L_2}{6\,\text{dB}}$ ja $r_2 = 2^{\,k} \cdot r_1$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $k = \dfrac{78\,\text{dB} - 60\,\text{dB}}{6\,\text{dB}} = 3$, $r_2 = 2^3 \cdot 2{,}0\,\text{m} = 16\,\text{m}$
**Vastaus:** $16\,\text{m}$, kaksi merkitsevää numeroa kuten etäisyydessä $2{,}0\,\text{m}$.
**Järkevyys:** Etäisyydet $2\,\text{m}$, $4\,\text{m}$, $8\,\text{m}$ ja $16\,\text{m}$ antavat tasot $78\,\text{dB}$, $72\,\text{dB}$, $66\,\text{dB}$ ja $60\,\text{dB}$. Pihalla talojen seinät heijastavat ääntä, joten todellisuudessa tarvittaisiin hieman pidempi matka.

## fy5-16-L2-04
**Annettu:** taso laskee $L_1 = 92\,\text{dB}$:stä $L_2 = 62\,\text{dB}$:iin ajassa $\Delta t = 0{,}45\,\text{s}$; lasku on tasainen
**Kysytty:** jälkikaiunta-aika $T$ eli aika, jossa taso laskee $60\,\text{dB}$
**Periaate:** Kun taso laskee tasaisesti, se laskee yhtä monta desibeliä jokaisessa sekunnissa. Jälkikaiunta-aika saadaan laskunopeudesta: $60\,\text{dB}$ vaatii yhtä monta kertaa pidemmän ajan kuin mitattu lasku on pienempi. Mittaus tehdään usein näin, koska huoneen taustamelu peittää täyden $60\,\text{dB}$:n pudotuksen.
**Kaava:** $T = \dfrac{60\,\text{dB}}{L_1 - L_2} \cdot \Delta t$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $T = \dfrac{60\,\text{dB}}{92\,\text{dB} - 62\,\text{dB}} \cdot 0{,}45\,\text{s} = 2 \cdot 0{,}45\,\text{s} = 0{,}90\,\text{s}$
**Vastaus:** $0{,}90\,\text{s}$, kaksi merkitsevää numeroa kuten ajassa $0{,}45\,\text{s}$.
**Järkevyys:** Mitattu lasku $30\,\text{dB}$ on puolet $60\,\text{dB}$:stä, joten aika kaksinkertaistuu. Tulos on pidempi kuin luokille tavoiteltu noin puoli sekuntia, mikä sopii tyhjään, kovapintaiseen luokkaan.

## fy5-16-L3-01
**Annettu:** $t_1 = 4{,}0\,\text{h}$ tasolla $L_1 = 88\,\text{dB}$, $t_2 = 4{,}0\,\text{h}$ tasolla $L_2 = 82\,\text{dB}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** päivän annos prosentteina vertailuannoksesta
**Periaate:** Annos on korvaan kertynyt energia, joten eri jaksojen osuudet lasketaan yhteen. Kunkin jakson osuus on sen keston ja kyseisen tason sallitun ajan suhde.
**Kaava:** $t_{\text{sall},i} = \dfrac{t_0}{2^{\,n_i}}$, missä $n_i = \dfrac{L_i - L_0}{3\,\text{dB}}$, ja annos $= \left(\dfrac{t_1}{t_{\text{sall},1}} + \dfrac{t_2}{t_{\text{sall},2}}\right) \cdot 100\,\%$
**Muunnokset:** Ei tarvita: ajat ovat tunteina, ja yksikkö supistuu.
**Sijoitus:** $n_1 = 1$, joten $t_{\text{sall},1} = 8\,\text{h} : 2 = 4{,}0\,\text{h}$. $n_2 = \dfrac{82\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = -1$, joten $t_{\text{sall},2} = 8\,\text{h} \cdot 2 = 16\,\text{h}$. Annos $= \left(\dfrac{4{,}0\,\text{h}}{4{,}0\,\text{h}} + \dfrac{4{,}0\,\text{h}}{16\,\text{h}}\right) \cdot 100\,\% = (1 + 0{,}25) \cdot 100\,\% = 125\,\%$
**Vastaus:** $125\,\%$. Ajat on annettu kahden numeron tarkkuudella, joten tulos on arvio, noin $1{,}3$-kertainen annos. Ylempi toiminta-arvo ylittyy, joten suojaimia on käytettävä.
**Järkevyys:** Jo lastauslaiturin $4\,\text{h}$ täyttää koko annoksen, joten tuloksen täytyy olla yli $100\,\%$. Pakkaamon osuus on pieni, koska siellä intensiteetti on vain neljäsosa laiturin intensiteetistä.

## fy5-16-L3-02
**Annettu:** kaksi samanlaista yksikköä, kumpikin $L_1 = 55\,\text{dB}$ etäisyydellä $r_1 = 3{,}0\,\text{m}$; ikkunan etäisyys kummastakin $r_2 = 12\,\text{m}$; pistemäiset lähteet avoimessa tilassa
**Kysytty:** taso $L$ ikkunan kohdalla, kun molemmat käyvät
**Periaate:** Lasketaan ensin yhden yksikön taso ikkunalla: jokainen etäisyyden kaksinkertaistuminen laskee tasoa $6\,\text{dB}$. Kahden yhtä voimakkaan lähteen intensiteetit summautuvat, joten yhteinen taso on $3\,\text{dB}$ suurempi.
**Kaava:** $L_\text{yksi} = L_1 - k \cdot 6\,\text{dB}$, missä $2^{\,k} = \dfrac{r_2}{r_1}$, ja $L = L_\text{yksi} + 3\,\text{dB}$
**Muunnokset:** Ei tarvita: $r_2 : r_1 = 12\,\text{m} : 3{,}0\,\text{m} = 4$, joten $2^{\,k} = 4$ ja $k = 2$.
**Sijoitus:** $L_\text{yksi} = 55\,\text{dB} - 2 \cdot 6\,\text{dB} = 43\,\text{dB}$. $L = 43\,\text{dB} + 3\,\text{dB} = 46\,\text{dB}$
**Vastaus:** $46\,\text{dB}$, kokonaisina desibeleinä kuten lähtötieto.
**Järkevyys:** Yhden yksikön taso on etäisyyden vuoksi selvästi pienempi kuin lähellä, ja toinen yksikkö nostaa sitä vain vähän. Tulos on hiljaisen keskustelun alapuolella, mutta makuuhuoneessa tasainen humina voi silti häiritä unta.

## fy5-16-L3-03
**Kysytty:** miksi vastamelu vaimentaa matalaa huminaa paremmin kuin puhetta
**Periaate:** Vastamelu kumoaa melun heikentävällä interferenssillä vain, jos se on korvan kohdalla vastakkaisessa vaiheessa. Aallonpituus $\lambda = \dfrac{v}{f}$ ja jaksonaika $T = \dfrac{1}{f}$ kertovat, kuinka tarkasti ajoituksen ja paikan on osuttava.
**Mallivastaus:** Huminan aallonpituus on $\lambda = \dfrac{343\,\text{m/s}}{100\,\text{Hz}} \approx 3{,}4\,\text{m}$ ja jaksonaika $10\,\text{ms}$. Koko korvakäytävä ja kuvun sisus ovat pieniä aallonpituuteen verrattuna, ja elektroniikalla on aikaa muodostaa vastakkainen signaali, joten vastamelu pysyy korvan kohdalla vastakkaisessa vaiheessa. Puheen aallonpituudet ovat $\dfrac{343\,\text{m/s}}{3000\,\text{Hz}} \approx 11\,\text{cm}$ ja $\dfrac{343\,\text{m/s}}{1000\,\text{Hz}} \approx 34\,\text{cm}$, ja jaksonaika on enintään $1\,\text{ms}$. Pienikin ajoitusvirhe tai muutaman senttimetrin paikkaero siirtää vaihetta paljon, jolloin aallot eivät enää kumoa toisiaan. Lisäksi puhe vaihtelee nopeasti, kun taas humina on tasaista. Korkeita ääniä vaimentavat lähinnä kuulokkeiden kuvut.
