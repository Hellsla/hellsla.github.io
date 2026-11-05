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
**Periaate:** Kahden lähteen intensiteetit summautuvat, eivät tasot. Kaksi yhtä voimakasta lähdettä kaksinkertaistaa intensiteetin (luku *Intensiteetti ja desibeliasteikko*).
**Kaava:** $L = L_1 + 10\,\text{dB} \cdot \lg \dfrac{2 I_1}{I_1} = L_1 + 10\,\text{dB} \cdot \lg 2$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $L = 70\,\text{dB} + 10\,\text{dB} \cdot \lg 2 = 70\,\text{dB} + 3{,}01\,\text{dB} = 73{,}01\,\text{dB}$
**Vastaus:** $73\,\text{dB}$, kokonaisina desibeleinä kuten lähtötieto.
**Järkevyys:** Taso nousee vain vähän, vaikka melua tuottava laite kaksinkertaistuu. Tulos $140\,\text{dB}$ olisi kipukynnyksen yläpuolella, mikä ei sovi kahdelle puhaltimelle.

## fy5-16-L1-03
**Annettu:** $L_1 = 88\,\text{dB}$ etäisyydellä $r_1 = 4{,}0\,\text{m}$, uusi etäisyys $r_2 = 8{,}0\,\text{m}$; pistemäinen lähde avoimessa tilassa
**Kysytty:** taso $L_2$ etäisyydellä $r_2$
**Periaate:** Pistemäisen lähteen intensiteetti on kääntäen verrannollinen etäisyyden neliöön, joten kaksinkertainen etäisyys antaa neljäsosan intensiteetistä. Se laskee tasoa $10\,\text{dB} \cdot \lg 4 \approx 6\,\text{dB}$ (luku *Intensiteetti ja desibeliasteikko*).
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
**Periaate:** Avoimessa tilassa jokainen etäisyyden kaksinkertaistuminen laskee tasoa $6\,\text{dB}$, koska intensiteetti pienenee neljäsosaan (luku *Intensiteetti ja desibeliasteikko*). Lasketaan, montako kaksinkertaistumista tarvitaan.
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

## fy5-16-L1-06
**Kysytty:** mikä toimenpide lyhentää luokan jälkikaiunta-aikaa
**Periaate:** Jälkikaiunta-aika on aika, jossa taso laskee $60\,\text{dB}$ äänilähteen vaiettua. Kovat pinnat heijastavat ääntä ja pitävät sen huoneessa, pehmeät ja huokoiset pinnat vaimentavat heijastuksia, joten taso laskee nopeammin.
**Mallivastaus:** Jälkikaiunta-aikaa lyhentää se, että kattoon asennetaan huokoisia vaimennuslevyjä, jotka imevät osan niihin osuvasta äänestä. Kiiltävät laatat ja lasipinnat ovat kovia pintoja, jotka heijastavat ääntä takaisin huoneeseen ja pidentäisivät aikaa. Äänen voimakkuuden pienentäminen ei auta, koska jälkikaiunta-aika mitataan $60\,\text{dB}$:n pudotuksena eikä se riipu alkutasosta.

## fy5-16-L1-07
**Annettu:** ulkotaso $L_\text{ulko} = 68\,\text{dB}$, sisätaso $L_\text{sisä} = 41\,\text{dB}$
**Kysytty:** seinän ja ikkunoiden vaimennus $\Delta L$
**Periaate:** Vaimennus kertoo, kuinka monta desibeliä rakenne pienentää tasoa, joten se on ulko- ja sisätason erotus.
**Kaava:** $\Delta L = L_\text{ulko} - L_\text{sisä}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $\Delta L = 68\,\text{dB} - 41\,\text{dB} = 27\,\text{dB}$
**Vastaus:** $27\,\text{dB}$, kokonaisina desibeleinä kuten lähtötiedot.
**Järkevyys:** Vaimennus lisättynä sisätasoon antaa ulkotason: $41\,\text{dB} + 27\,\text{dB} = 68\,\text{dB}$. Sisällä on hiljaisempaa kuin ulkona, kuten pitääkin.

## fy5-16-L1-08
**Kysytty:** miten kaiutin tuottaa äänen sähköisestä signaalista
**Periaate:** Kaiuttimessa signaali on vaihtovirta, joka kulkee magneetin kentässä olevassa kelassa. Magneettikenttä kohdistaa virtaan vaihtuvan voiman, joten kela ja siihen kiinnitetty kartio värähtelevät, ja kartio synnyttää ilmaan ääniaallon.
**Mallivastaus:** Kelan vaihtovirta ja magneetti saavat kartion värähtelemään signaalin tahdissa, ja kartio työntää ilmaa edestakaisin. Ääni, joka liikuttaa kalvoa ja synnyttää jännitteen, on mikrofonin toimintaa eikä kaiuttimen. Magneetti on kaiuttimessa paikallaan, eikä äänen synty perustu ilman lämpenemiseen.

## fy5-16-L2-05
**Annettu:** ennen levyjä taso laskee $90{,}3\,\text{dB}$:stä $74{,}4\,\text{dB}$:iin ja levyjen jälkeen $90{,}2\,\text{dB}$:stä $50{,}1\,\text{dB}$:iin ajassa $\Delta t = 0{,}40\,\text{s}$; lasku on tasainen
**Kysytty:** jälkikaiunta-ajan lyhenemä prosentteina
**Periaate:** Kun taso laskee tasaisesti, jälkikaiunta-aika on aika, jossa lasku on $60\,\text{dB}$. Lasketaan se kummallekin mittaukselle mitatun pudotuksen ja ajan avulla ja verrataan aikoja.
**Taulukon lukeminen:** Pudotus ennen levyjä on $\Delta L_1 = 90{,}3\,\text{dB} - 74{,}4\,\text{dB} = 15{,}9\,\text{dB}$ ja levyjen jälkeen $\Delta L_2 = 90{,}2\,\text{dB} - 50{,}1\,\text{dB} = 40{,}1\,\text{dB}$.
**Kaava:** $T = \dfrac{60\,\text{dB}}{\Delta L} \cdot \Delta t$ ja lyhenemä $= \dfrac{T_1 - T_2}{T_1} \cdot 100\,\%$
**Muunnokset:** Ei tarvita.
**Sijoitus:**
$$\begin{aligned}
T_1 &= \frac{60\,\text{dB}}{15{,}9\,\text{dB}} \cdot 0{,}40\,\text{s} \\
&= 1{,}51\,\text{s} \\
T_2 &= \frac{60\,\text{dB}}{40{,}1\,\text{dB}} \cdot 0{,}40\,\text{s} \\
&= 0{,}599\,\text{s} \\
\text{lyhenemä} &= \frac{1{,}51 - 0{,}599}{1{,}51} \cdot 100\,\% \\
&= 60{,}3\,\%
\end{aligned}$$
**Vastaus:** $60{,}3\,\%$. Lähtötiedoissa on kolme merkitsevää numeroa, joten tulos annetaan kolmella.
**Järkevyys:** Jälkikaiunta-aika lyheni noin $1{,}5\,\text{s}$:sta noin $0{,}6\,\text{s}$:iin, eli se on noin $0{,}4$-kertainen. Levyjen jälkeen taso laskee $40{,}1\,\text{dB} : 15{,}9\,\text{dB} \approx 2{,}5$ kertaa nopeammin, ja $1 - 1 : 2{,}5 = 0{,}6$ vastaa tulosta. Aika $0{,}6\,\text{s}$ sopii puheluokkaan.

## fy5-16-L2-06
**Annettu:** vaimennus $\Delta L = L_\text{ilman} - L_\text{este}$ taajuuksilla $125$, $500$, $2000$ ja $4000\,\text{Hz}$ taulukon arvoista; äänen nopeus $v = 343\,\text{m/s}$
**Kysytty:** a) ero vaimennuksessa taajuuksilla $4000\,\text{Hz}$ ja $500\,\text{Hz}$; b) miksi matala ääni vaimenee huonommin
**Periaate:** Esteen vaimennus on tason pudotus esteen takana. Aalto kiertyy esteen ohi sitä paremmin, mitä pidempi sen aallonpituus $\lambda = \dfrac{v}{f}$ on esteen kokoon verrattuna.
**Taulukon lukeminen:** Taulukosta vaimennukset ovat $125\,\text{Hz}$: $8{,}1\,\text{dB}$, $500\,\text{Hz}$: $13{,}4\,\text{dB}$, $2000\,\text{Hz}$: $22{,}2\,\text{dB}$ ja $4000\,\text{Hz}$: $25{,}2\,\text{dB}$.
**Kaava:** $\Delta L = L_\text{ilman} - L_\text{este}$ ja $\lambda = \dfrac{v}{f}$
**Muunnokset:** Ei tarvita.
**Sijoitus:**
$$\begin{aligned}
\Delta L_{500} &= 68{,}4\,\text{dB} - 55{,}0\,\text{dB} \\
&= 13{,}4\,\text{dB} \\
\Delta L_{4000} &= 60{,}3\,\text{dB} - 35{,}1\,\text{dB} \\
&= 25{,}2\,\text{dB} \\
\Delta L_{4000} - \Delta L_{500} &= 11{,}8\,\text{dB}
\end{aligned}$$
Aallonpituudet ovat $\lambda_{125} = \dfrac{343\,\text{m/s}}{125\,\text{Hz}} = 2{,}7\,\text{m}$ ja $\lambda_{4000} = \dfrac{343\,\text{m/s}}{4000\,\text{Hz}} = 0{,}086\,\text{m}$.
**Vastaus:** a) $11{,}8\,\text{dB}$. b) Matalan äänen aallonpituus $2{,}7\,\text{m}$ on esteen korkeuden luokkaa, joten aalto taipuu esteen yli ja äänen taso esteen takana pysyy suurempana. Korkean äänen aallonpituus $0{,}086\,\text{m}$ on paljon esteen kokoa pienempi, joten este jättää sen varjoonsa.
**Järkevyys:** Vaimennus kasvaa taajuuden mukana joka rivillä: $8{,}1 < 13{,}4 < 22{,}2 < 25{,}2\,\text{dB}$. Siksi tulos on positiivinen, ja ero on pienempi kuin suurin vaimennus $25{,}2\,\text{dB}$.

## fy5-16-L2-07
**Annettu:** työpisteen taso $L = 100\,\text{dB}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$; oppilaan tulos $1{,}6\,\text{h}$
**Kysytty:** a) mikä oppilaan päättelyssä on väärin; b) oikea sallittu aika $t_\text{sall}$ minuutteina
**Periaate:** Jokainen $3\,\text{dB}$ toiminta-arvon yli puolittaa sallitun ajan, joten aika jaetaan kahdella jokaista $3\,\text{dB}$:n askelta kohti. Askeleet kertautuvat: aika jaetaan luvulla $2^{\,n}$, ei luvulla $n$.
**Kaava:** $n = \dfrac{L - L_0}{3\,\text{dB}}$ ja $t_\text{sall} = \dfrac{t_0}{2^{\,n}}$
**Muunnokset:** $1\,\text{h} = 60\,\text{min}$.
**Sijoitus:**
$$\begin{aligned}
n &= \frac{100\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} \\
&= 5 \\
t_\text{sall} &= \frac{8\,\text{h}}{2^{\,5}} \\
&= \frac{8\,\text{h}}{32} \\
&= 0{,}25\,\text{h} \\
&= 15\,\text{min}
\end{aligned}$$
**Vastaus:** a) Oppilas laski askelten määrän $n = 5$ oikein mutta jakoi ajan luvulla $5$. Jokainen askel puolittaa jäljellä olevan ajan, joten ajan pitää jakaa luvulla $2^{\,5} = 32$. b) Sallittu aika on $15\,\text{min}$.
**Järkevyys:** Oppilaan $1{,}6\,\text{h}$ eli $96\,\text{min}$ on yli kuusinkertainen oikeaan nähden, vaikka taso on selvästi toiminta-arvon yli. Tarkistus askel kerrallaan: $8\,\text{h} \to 4\,\text{h} \to 2\,\text{h} \to 1\,\text{h} \to 30\,\text{min} \to 15\,\text{min}$ on viisi puolitusta.

## fy5-16-L3-04
**Annettu:** sahaus $L_1 = 97\,\text{dB}$, $t_1 = 1{,}0\,\text{h}$; höyläys $L_2 = 91\,\text{dB}$, $t_2 = 2{,}0\,\text{h}$; kokoaminen $L_3 = 85\,\text{dB}$, $t_3 = 3{,}0\,\text{h}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** a) päivän annos prosentteina; b) kuulonsuojainten pienin vaimennus $\Delta L$; c) riittääkö sahan koteloiminen
**Periaate:** Annos on korvaan kertynyt energia, joten vaiheiden osuudet lasketaan yhteen. Osuus on keston ja kyseisen tason sallitun ajan suhde. Kuulonsuojain pienentää kaikkien vaiheiden intensiteettiä samalla kertoimella, joten annos jaetaan luvulla $2^{\,\Delta L / (3\,\text{dB})}$.
**Kaava:** $t_{\text{sall},i} = \dfrac{t_0}{2^{\,n_i}}$, missä $n_i = \dfrac{L_i - L_0}{3\,\text{dB}}$; annos $D = \sum \dfrac{t_i}{t_{\text{sall},i}}$; ehto $\dfrac{D}{2^{\,\Delta L / (3\,\text{dB})}} \le 1$
**Muunnokset:** Ei tarvita: ajat ovat tunteina, ja yksikkö supistuu.
**Sijoitus:**
Sahaus: $n_1 = \dfrac{97 - 85}{3} = 4$, joten $t_{\text{sall},1} = 8\,\text{h} : 16 = 0{,}50\,\text{h}$ ja osuus on $1{,}0\,\text{h} : 0{,}50\,\text{h} = 2{,}0$. Höyläys: $n_2 = 2$, $t_{\text{sall},2} = 2{,}0\,\text{h}$ ja osuus $1{,}0$. Kokoaminen: $n_3 = 0$, $t_{\text{sall},3} = 8\,\text{h}$ ja osuus $0{,}375$.
$$\begin{aligned}
D &= 2{,}0 + 1{,}0 + 0{,}375 \\
&= 3{,}375
\end{aligned}$$
Kohta b:
$$\begin{aligned}
2^{\,\Delta L / (3\,\text{dB})} &\ge 3{,}375 \\
\Delta L &\ge 3\,\text{dB} \cdot \frac{\lg 3{,}375}{\lg 2} \\
&= 3\,\text{dB} \cdot 1{,}755 \\
&= 5{,}26\,\text{dB}
\end{aligned}$$
Kohta c: kotelo laskee sahauksen tason arvoon $87\,\text{dB}$, jolloin $n_1 = \dfrac{2}{3}$ ja $t_{\text{sall},1} = \dfrac{8\,\text{h}}{2^{2/3}} = 5{,}04\,\text{h}$, osuus $1{,}0 : 5{,}04 = 0{,}198$. Uusi annos on $D = 0{,}198 + 1{,}0 + 0{,}375 = 1{,}57$.
**Vastaus:** a) noin $340\,\%$. b) vähintään $5{,}3\,\text{dB}$. c) Ei riitä yksin, koska annos on edelleen noin $160\,\%$ vertailuannoksesta. Kotelon lisäksi tarvitaan esimerkiksi kuulonsuojaimet, joiden vaimennus on vähintään $\dfrac{3\,\text{dB} \cdot \lg 1{,}57}{\lg 2} = 2{,}0\,\text{dB}$, tai höyläyskoneen sijoittaminen erilleen työpisteestä.
**Järkevyys:** Sahaus ja höyläys ovat yli toiminta-arvon, joten annoksen täytyy olla yli $100\,\%$. Tavalliset suojaimet vaimentavat $20$–$30\,\text{dB}$, joten $5{,}3\,\text{dB}$ täyttyy helposti.

## fy5-16-L3-05
**Annettu:** $L_1 = 112\,\text{dB}$ etäisyydellä $r_1 = 2{,}0\,\text{m}$, kuulija etäisyydellä $r_2 = 8{,}0\,\text{m}$; tulppien vaimennus $\Delta L = 8\,\text{dB}$; konsertin kesto $t = 3{,}0\,\text{h}$; vertailu $L_0 = 85\,\text{dB}$ ja $t_0 = 8\,\text{h}$
**Kysytty:** a) taso ilman tulppia; b) sallittu aika tulppien kanssa; c) annos prosentteina ja riittääkö siirtyminen etäisyydelle $16\,\text{m}$
**Periaate:** Pistemäisen lähteen taso laskee $6\,\text{dB}$ jokaisella etäisyyden kaksinkertaistumisella. Tulpat vähentävät korvaan pääsevää tasoa vaimennuksensa verran, ja sallittu aika saadaan säännöstä, jossa jokainen $3\,\text{dB}$ toiminta-arvon yli puolittaa ajan. Annos on kuunteluajan ja sallitun ajan suhde.
**Kaava:** $L_2 = L_1 - k \cdot 6\,\text{dB}$, missä $2^{\,k} = \dfrac{r_2}{r_1}$; $L = L_2 - \Delta L$; $t_\text{sall} = \dfrac{t_0}{2^{\,n}}$, missä $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Muunnokset:** Ei tarvita: $r_2 : r_1 = 8{,}0\,\text{m} : 2{,}0\,\text{m} = 4$, joten $k = 2$.
**Sijoitus:**
Kohta a: $L_2 = 112\,\text{dB} - 2 \cdot 6\,\text{dB} = 100\,\text{dB}$.
Kohta b: tulppien kanssa taso on $L = 100\,\text{dB} - 8\,\text{dB} = 92\,\text{dB}$.
$$\begin{aligned}
n &= \frac{92\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} \\
&= 2{,}33 \\
t_\text{sall} &= \frac{8\,\text{h}}{2^{\,2{,}33}} \\
&= 1{,}59\,\text{h}
\end{aligned}$$
Kohta c: annos on $\dfrac{3{,}0\,\text{h}}{1{,}59\,\text{h}} = 1{,}89$ eli $190\,\%$. Etäisyydellä $16\,\text{m}$ taso on $100\,\text{dB} - 6\,\text{dB} = 94\,\text{dB}$ ja tulpat korvissa $86\,\text{dB}$. Silloin $n = \dfrac{1}{3}$, $t_\text{sall} = \dfrac{8\,\text{h}}{2^{1/3}} = 6{,}35\,\text{h}$ ja annos on $\dfrac{3{,}0\,\text{h}}{6{,}35\,\text{h}} = 0{,}47$ eli $47\,\%$.
**Vastaus:** a) $100\,\text{dB}$. b) $1{,}6\,\text{h}$, kaksi merkitsevää numeroa kuten vaimennuksessa ja kestossa. c) Paikallaan etäisyydellä $8{,}0\,\text{m}$ annos on $190\,\%$ eli liian suuri. Jos kuulija pitää tulpat korvissa myös etäisyydellä $16\,\text{m}$, siirtyminen riittää, koska annos putoaa noin $47\,\%$:iin.
**Järkevyys:** Ilman tulppia sallittu aika olisi vain $8\,\text{h} : 2^5 = 0{,}25\,\text{h}$, joten $8\,\text{dB}$:n vaimennus pidentää sitä noin kuusinkertaiseksi, ja $1{,}59\,\text{h} : 0{,}25\,\text{h} = 6{,}3 \approx 2^{8/3} = 6{,}35$.
