## fy4-15-L1-01
**Annettu:** putouskorkeus $h = 15{,}0\,\text{m}$, virtaama $Q = 120\,\text{m}^3\text{/s}$, hyötysuhde $\eta = 0{,}900$; veden tiheys $\rho = 1000\,\text{kg/m}^3$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** sähköteho $P$ yksikössä $\text{MW}$
**Periaate:** Turbiinien läpi putoava vesi menettää potentiaalienergiaa $mgh$, ja sekunnissa putoaa massa $\rho Q$. Voimala muuttaa tästä tehosta sähköksi osuuden $\eta$, joten käytetään vesivoimalan tehon kaavaa.
**Kaava:** $P = \eta\rho Q g h$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten teho saadaan watteina; lopuksi $1\,\text{MW} = 10^{6}\,\text{W}$.
**Sijoitus:** $P = 0{,}900 \cdot 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 120\,\tfrac{\text{m}^3}{\text{s}} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 15{,}0\,\text{m} = 15\,892\,200\,\text{W} \approx 15{,}9\,\text{MW}$
**Vastaus:** $15{,}9\,\text{MW}$, kolme merkitsevää numeroa kuten putouskorkeudessa $15{,}0\,\text{m}$, virtaamassa $120\,\text{m}^3\text{/s}$ ja hyötysuhteessa $0{,}900$.
**Järkevyys:** Kuutiometri vettä antaa $15\,\text{m}$:n pudotuksessa noin $1000\,\text{kg} \cdot 10\,\text{m/s}^2 \cdot 15\,\text{m} = 150\,\text{kJ}$, joten $120$ kuutiometriä sekunnissa antaa noin $18\,\text{MW}$, ja siitä $90\,\%$ on noin $16\,\text{MW}$. Teho on pienempi kuin Imatran $192\,\text{MW}$, koska sekä virtaama että putouskorkeus ovat pienempiä.

## fy4-15-L1-02
**Annettu:** veden massa $m = 1000\,\text{kg}$, korkeusero $h = 24{,}0\,\text{m}$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** potentiaalienergian pieneneminen $E_\text{p}$ yksikössä $\text{kJ}$
**Periaate:** Painovoiman potentiaalienergia on verrannollinen korkeuteen valitusta nollatasosta. Kun nollatasoksi valitaan alaveden pinta, yläaltaan veden potentiaalienergia on $mgh$, ja juuri sen verran se pienenee pudotessaan alaveteen.
**Kaava:** $E_\text{p} = mgh$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten energia saadaan jouleina; lopuksi $1\,\text{kJ} = 1000\,\text{J}$.
**Sijoitus:** $E_\text{p} = 1000\,\text{kg} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 24{,}0\,\text{m} = 235\,440\,\text{J} \approx 235\,\text{kJ}$
**Vastaus:** $235\,\text{kJ}$, kolme merkitsevää numeroa kuten korkeuserossa $24{,}0\,\text{m}$.
**Järkevyys:** Arvio $1000\,\text{kg} \cdot 10\,\text{m/s}^2 \cdot 24\,\text{m} = 240\,\text{kJ}$ on lähellä tulosta. Jos sekunnissa putoaa satoja kuutiometrejä, teho on satoja kertoja $235\,\text{kW}$ eli kymmeniä tai satoja megawatteja, kuten suurissa vesivoimaloissa.

## fy4-15-L1-03
**Annettu:** turbiiniin virtaavan veden teho $P_\text{o} = 50{,}0\,\text{MW}$, sähköteho $P_\text{s} = 46{,}0\,\text{MW}$
**Kysytty:** hyötysuhde $\eta$ prosentteina
**Periaate:** Hyötysuhde on hyödyksi saadun tehon ja laitteeseen otetun tehon suhde. Tässä hyödyllinen teho on sähköteho ja otettu teho on veden voimalaan tuoma teho.
**Kaava:** $\eta = \dfrac{P_\text{s}}{P_\text{o}}$
**Muunnokset:** Kumpikin teho on megawatteina, joten yksikkö supistuu. Desimaaliluku muutetaan prosenteiksi kertomalla sadalla.
**Sijoitus:** $\eta = \dfrac{46{,}0\,\text{MW}}{50{,}0\,\text{MW}} = 0{,}920 = 92{,}0\,\%$
**Vastaus:** $92{,}0\,\%$, kolme merkitsevää numeroa kuten tehoissa $46{,}0\,\text{MW}$ ja $50{,}0\,\text{MW}$.
**Järkevyys:** Hyötysuhde on alle $100\,\%$, kuten pitää, ja suuren vesivoimalan hyötysuhde on tyypillisesti noin $90\,\%$. Häviöt ovat $4{,}0\,\text{MW}$ eli $8\,\%$ otetusta tehosta.

## fy4-15-L1-04
**Annettu:** roottorin pyyhkäisemä pinta-ala $A = 1500\,\text{m}^2$, tuulen nopeus $v = 8{,}0\,\text{m/s}$, ilman tiheys $\rho = 1{,}25\,\text{kg/m}^3$
**Kysytty:** tuulen teho $P_\text{tuuli}$ yksikössä $\text{kW}$
**Periaate:** Ajassa $t$ roottorin läpi virtaa ilmalieriö, jonka massa on $m = \rho A v t$ ja liike-energia $\tfrac{1}{2}mv^2$. Tuulen teho on tämä liike-energia jaettuna ajalla. Hyötysuhdetta ei tarvita, koska kysytään tuulen tehoa, ei sähkötehoa.
**Kaava:** $P_\text{tuuli} = \dfrac{\tfrac{1}{2}mv^2}{t} = \dfrac{\tfrac{1}{2}\rho A v t\, v^2}{t}$, joten $P_\text{tuuli} = \tfrac{1}{2}\rho A v^3$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten teho saadaan watteina; lopuksi $1\,\text{kW} = 1000\,\text{W}$.
**Sijoitus:** $P_\text{tuuli} = \tfrac{1}{2} \cdot 1{,}25\,\tfrac{\text{kg}}{\text{m}^3} \cdot 1500\,\text{m}^2 \cdot \left(8{,}0\,\tfrac{\text{m}}{\text{s}}\right)^3 = 480\,000\,\text{W} = 480\,\text{kW}$
**Vastaus:** $480\,\text{kW}$ eli $4{,}8 \cdot 10^{2}\,\text{kW}$, kaksi merkitsevää numeroa kuten tuulen nopeudessa $8{,}0\,\text{m/s}$.
**Järkevyys:** Sekunnissa roottorin läpi virtaa $1{,}25 \cdot 1500 \cdot 8\,\text{kg} = 15\,000\,\text{kg}$ ilmaa, ja jokaisella kilogrammalla on liike-energiaa $\tfrac{1}{2}\cdot 8^2\,\text{J} = 32\,\text{J}$. Tulo on $480\,000\,\text{J}$ sekunnissa, sama tulos. Sähköksi saataisiin tästä alle puolet.

## fy4-15-L1-05
**Annettu:** sähköteho $P = 3{,}00\,\text{MW}$, aika $t = 6{,}00\,\text{h}$
**Kysytty:** sähköenergia $E$ yksikössä $\text{MWh}$
**Periaate:** Teho kertoo, kuinka paljon energiaa muuntuu aikayksikössä. Kun teho pysyy vakiona, energia on teho kertaa aika.
**Kaava:** $P = \dfrac{E}{t}$, joten $E = Pt$
**Muunnokset:** Kun teho on megawatteina ja aika tunteina, energia saadaan suoraan megawattitunteina, joten muunnoksia ei tarvita.
**Sijoitus:** $E = 3{,}00\,\text{MW} \cdot 6{,}00\,\text{h} = 18{,}0\,\text{MWh}$
**Vastaus:** $18{,}0\,\text{MWh}$, kolme merkitsevää numeroa kuten tehossa $3{,}00\,\text{MW}$ ja ajassa $6{,}00\,\text{h}$.
**Järkevyys:** Jouleina energia on $3{,}00 \cdot 10^{6}\,\text{W} \cdot 6{,}00 \cdot 3600\,\text{s} \approx 6{,}5 \cdot 10^{10}\,\text{J}$. Sähkölämmitteinen omakotitalo kuluttaa vuodessa noin $20\,\text{MWh}$, joten tämä vastaa lähes yhden talon vuoden kulutusta.

## fy4-15-L2-01
**Annettu:** sähköteho $P = 10{,}0\,\text{MW}$, putouskorkeus $h = 12{,}0\,\text{m}$, hyötysuhde $\eta = 0{,}880$; veden tiheys $\rho = 1000\,\text{kg/m}^3$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** virtaama $Q$ yksikössä $\text{m}^3\text{/s}$
**Periaate:** Vesi menettää pudotessaan potentiaalienergiaa, ja voimala muuttaa siitä sähköksi osuuden $\eta$. Vesivoimalan tehon kaavasta ratkaistaan virtaama, joka antaa halutun tehon.
**Kaava:** $P = \eta\rho Q g h$, joten $Q = \dfrac{P}{\eta\rho g h}$
**Muunnokset:** $P = 10{,}0\,\text{MW} = 10{,}0 \cdot 10^{6}\,\text{W}$
**Sijoitus:** Suureet ovat SI-yksiköissä, ja $\tfrac{\text{W}}{\text{kg/m}^3 \cdot \text{m/s}^2 \cdot \text{m}} = \tfrac{\text{m}^3}{\text{s}}$, joten $Q = \dfrac{10{,}0 \cdot 10^{6}}{0{,}880 \cdot 1000 \cdot 9{,}81 \cdot 12{,}0}\,\tfrac{\text{m}^3}{\text{s}} = 96{,}53\,\tfrac{\text{m}^3}{\text{s}}$
**Vastaus:** $96{,}5\,\text{m}^3\text{/s}$, kolme merkitsevää numeroa kuten tehossa $10{,}0\,\text{MW}$, putouskorkeudessa $12{,}0\,\text{m}$ ja hyötysuhteessa $0{,}880$.
**Järkevyys:** Kuutiometri vettä antaa $12\,\text{m}$:n pudotuksessa noin $120\,\text{kJ}$ ja sähköä noin $105\,\text{kJ}$. Tehoon $10\,\text{MW}$ tarvitaan siis noin $10\,000 : 105 \approx 95$ kuutiometriä sekunnissa.

## fy4-15-L2-02
**Annettu:** roottorin halkaisija $d = 82\,\text{m}$, tuulen nopeus $v = 8{,}0\,\text{m/s}$, sähköteho $P = 758\,\text{kW}$, ilman tiheys $\rho = 1{,}25\,\text{kg/m}^3$
**Kysytty:** sähköksi muuttuva osuus eli hyötysuhde $\eta$ prosentteina
**Periaate:** Roottorin läpi virtaavan tuulen teho on ilman liike-energia sekunnissa, $\tfrac{1}{2}\rho A v^3$. Voimala muuttaa siitä sähköksi osuuden $\eta$, joten osuus saadaan tuulivoimalan tehon kaavasta.
**Kaava:** $P = \tfrac{1}{2}\eta\rho A v^3$ ja $A = \pi r^2$, joten $\eta = \dfrac{2P}{\rho A v^3}$
**Muunnokset:** Säde $r = 82\,\text{m} : 2 = 41\,\text{m}$ ja $P = 758\,\text{kW} = 758\,000\,\text{W}$.
**Sijoitus:** $A = \pi \cdot (41\,\text{m})^2 = 5281{,}0\,\text{m}^2$ ja $\eta = \dfrac{2 \cdot 758\,000\,\text{W}}{1{,}25\,\tfrac{\text{kg}}{\text{m}^3} \cdot 5281{,}0\,\text{m}^2 \cdot \left(8{,}0\,\tfrac{\text{m}}{\text{s}}\right)^3} = 0{,}4485$
**Vastaus:** noin $45\,\%$, kaksi merkitsevää numeroa kuten halkaisijassa $82\,\text{m}$ ja tuulen nopeudessa $8{,}0\,\text{m/s}$.
**Järkevyys:** Osuus on alle teoreettisen ylärajan $59\,\%$, ja todellisen tuulivoimalan osuus on alle puolet, kuten pitääkin. Tuulen teho on noin $1{,}7\,\text{MW}$, ja sähköteho $0{,}76\,\text{MW}$ on vähän alle puolet siitä.

## fy4-15-L2-03
**Annettu:** virtaama $Q = 850\,\textsf{l}\text{/s}$, putouskorkeus $h = 6{,}5\,\text{m}$, hyötysuhde $\eta = 0{,}75$; veden tiheys $\rho = 1000\,\text{kg/m}^3$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** sähköteho $P$ yksikössä $\text{kW}$
**Periaate:** Turbiinin läpi putoava vesi menettää potentiaalienergiaa, ja sekunnissa putoaa massa $\rho Q$. Voimala muuttaa tästä tehosta sähköksi osuuden $\eta$, joten käytetään vesivoimalan tehon kaavaa.
**Kaava:** $P = \eta\rho Q g h$
**Muunnokset:** $850\,\textsf{l} = 850 \cdot 0{,}001\,\text{m}^3 = 0{,}850\,\text{m}^3$, joten $Q = 0{,}850\,\text{m}^3\text{/s}$; lopuksi $1\,\text{kW} = 1000\,\text{W}$.
**Sijoitus:** $P = 0{,}75 \cdot 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 0{,}850\,\tfrac{\text{m}^3}{\text{s}} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 6{,}5\,\text{m} = 40\,650\,\text{W} \approx 41\,\text{kW}$
**Vastaus:** $41\,\text{kW}$, kaksi merkitsevää numeroa kuten putouskorkeudessa $6{,}5\,\text{m}$ ja hyötysuhteessa $0{,}75$.
**Järkevyys:** Sekunnissa putoaa $850\,\text{kg}$ vettä, joka antaa $6{,}5\,\text{m}$:n pudotuksessa noin $850 \cdot 10 \cdot 6{,}5\,\text{J} \approx 55\,\text{kJ}$, ja siitä kolme neljäsosaa on noin $41\,\text{kJ}$ sekunnissa. Jos litroja ei muunnettaisi, tulos olisi tuhatkertainen, $41\,\text{MW}$, mikä on purolle aivan liikaa.

## fy4-15-L2-04
**Annettu:** putouskorkeus $h = 9{,}50\,\text{m}$, virtaama $Q = 3{,}20\,\text{m}^3\text{/s}$, hyötysuhde $\eta = 0{,}800$, aika $t = 24{,}0\,\text{h}$; veden tiheys $\rho = 1000\,\text{kg/m}^3$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** sähköenergia $E$ yksikössä $\text{MWh}$
**Periaate:** Ensin lasketaan sähköteho vesivoimalan tehon kaavasta, koska putoavan veden potentiaalienergiasta muuttuu sähköksi osuus $\eta$. Teho pysyy vakiona, kun virtaama pysyy samana, joten energia on teho kertaa aika.
**Kaava:** $P = \eta\rho Q g h$ ja $E = Pt$, joten $E = \eta\rho Q g h t$
**Muunnokset:** Teho lasketaan watteina ja muunnetaan megawateiksi, $1\,\text{MW} = 10^{6}\,\text{W}$; aika pidetään tunteina, jolloin energia saadaan megawattitunteina.
**Sijoitus:** $P = 0{,}800 \cdot 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 3{,}20\,\tfrac{\text{m}^3}{\text{s}} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 9{,}50\,\text{m} = 238\,579\,\text{W}$ ja $E = 0{,}238\,579\,\text{MW} \cdot 24{,}0\,\text{h} = 5{,}7259\,\text{MWh}$
**Vastaus:** $5{,}73\,\text{MWh}$, kolme merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Teho on noin $0{,}24\,\text{MW}$, ja vuorokaudessa on $24$ tuntia: $0{,}24 \cdot 24 \approx 5{,}8\,\text{MWh}$. Se vastaa noin kolmasosaa sähkölämmitteisen omakotitalon vuoden kulutuksesta, mikä sopii pienvoimalalle.

## fy4-15-L3-01
**Annettu:** tuulen nopeus ennen $v_1 = 6{,}0\,\text{m/s}$ ja jälkeen $v_2 = 9{,}0\,\text{m/s}$; roottori ja hyötysuhde ovat samat, eikä voimala saavuta nimellistehoaan
**Kysytty:** kuinka monta kertaa suurempi sähköteho $P_2$ on kuin $P_1$, suhdeluku $x$
**Periaate:** Sähköteho on osuus $\eta$ roottorin läpi virtaavan ilman liike-energiasta sekunnissa. Kun tuuli on nopeampi, ilmaa virtaa sekunnissa enemmän suhteessa $v$ ja jokaisella kilogrammalla on liike-energiaa enemmän suhteessa $v^2$, joten teho on verrannollinen kuutioon $v^3$, kun $\eta$, $\rho$ ja $A$ pysyvät samoina.
**Kaava:** $P = \tfrac{1}{2}\eta\rho A v^3$, joten $x = \dfrac{P_2}{P_1} = \dfrac{\tfrac{1}{2}\eta\rho A v_2^3}{\tfrac{1}{2}\eta\rho A v_1^3} = \left(\dfrac{v_2}{v_1}\right)^3$
**Muunnokset:** Kumpikin nopeus on samassa yksikössä, joten yksikkö supistuu eikä muunnoksia tarvita.
**Sijoitus:** $x = \left(\dfrac{9{,}0\,\text{m/s}}{6{,}0\,\text{m/s}}\right)^3 = 1{,}5^3 = 3{,}375$
**Vastaus:** noin $3{,}4$ kertaa suurempi, kaksi merkitsevää numeroa kuten tuulen nopeuksissa $6{,}0\,\text{m/s}$ ja $9{,}0\,\text{m/s}$.
**Järkevyys:** Ilmaa virtaa $1{,}5$ kertaa enemmän ja jokaisella kilogrammalla on $1{,}5^2 = 2{,}25$ kertaa enemmän liike-energiaa: $1{,}5 \cdot 2{,}25 \approx 3{,}4$. Kerroin on suurempi kuin nopeuksien suhde $1{,}5$, kuten kolmannesta potenssista seuraa.

## fy4-15-L3-02
**Annettu:** vanhan roottorin halkaisija $d_1 = 82\,\text{m}$, uuden $d_2 = 162\,\text{m}$; tuulen nopeus, ilman tiheys ja hyötysuhde ovat samat, eikä kumpikaan saavuta nimellistehoaan
**Kysytty:** kuinka monta kertaa suurempi uuden voimalan sähköteho $P_2$ on kuin vanhan $P_1$, suhdeluku $x$
**Periaate:** Samalla tuulen nopeudella jokaisen roottorin läpi virtaa sekunnissa ilmalieriö, jonka massa on verrannollinen roottorin pinta-alaan $A = \pi r^2$. Jokaisella ilmakilogrammalla on sama liike-energia, joten teho on verrannollinen pinta-alaan ja siten halkaisijan neliöön.
**Kaava:** $P = \tfrac{1}{2}\eta\rho A v^3$ ja $A = \pi\left(\tfrac{d}{2}\right)^2$, joten $x = \dfrac{P_2}{P_1} = \dfrac{A_2}{A_1} = \left(\dfrac{d_2}{d_1}\right)^2$
**Muunnokset:** Halkaisijat ovat samassa yksikössä, joten yksikkö supistuu eikä muunnoksia tarvita.
**Sijoitus:** $x = \left(\dfrac{162\,\text{m}}{82\,\text{m}}\right)^2 = 1{,}9756^2 = 3{,}903$
**Vastaus:** noin $3{,}9$ kertaa suurempi, kaksi merkitsevää numeroa kuten halkaisijassa $82\,\text{m}$.
**Järkevyys:** Halkaisija on noin kaksinkertainen, joten pinta-ala on noin $2^2 = 4$ -kertainen, ja tulos on vähän alle neljän. Siksi uusissa voimaloissa on yhä pidemmät lavat: pinta-ala kasvaa halkaisijan neliössä.

## fy4-15-L3-03
**Annettu:** tuulen nopeus $v = 10{,}0\,\text{m/s}$, massa $m = 1\,\text{kg}$ sekä ilmalle että vedelle; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** putouskorkeus $h$ yksikössä $\text{m}$
**Periaate:** Kilogramman ilmaa liike-energia on $\tfrac{1}{2}mv^2$, ja kilogramman vettä potentiaalienergia pienenee pudotuksessa $mgh$. Asetetaan nämä yhtä suuriksi. Massa supistuu, joten tulos ei riipu siitä, kuinka monta kilogrammaa verrataan.
**Kaava:** $mgh = \tfrac{1}{2}mv^2$, joten $h = \dfrac{v^2}{2 \cdot g}$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $h = \dfrac{\left(10{,}0\,\tfrac{\text{m}}{\text{s}}\right)^2}{2 \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2}} = 5{,}097\,\text{m}$
**Vastaus:** $5{,}10\,\text{m}$, kolme merkitsevää numeroa kuten tuulen nopeudessa $10{,}0\,\text{m/s}$.
**Järkevyys:** Kilogrammalla tuulta on liike-energiaa vain $50\,\text{J}$, kun Imatran $24\,\text{m}$:n putouksessa kilogramma vettä antaa noin $235\,\text{J}$. Tuulessa on siis vähän energiaa kilogrammaa kohden, ja ilma on lisäksi kevyttä, joten tuulivoimalan roottorin on oltava suuri. Yksikkö: $\tfrac{\text{m}^2/\text{s}^2}{\text{m}/\text{s}^2} = \text{m}$.


## fy4-15-L1-06
**Kysytty:** mikä selittää, miksi kaksinkertaisen putouskorkeuden voimalan teho on kaksinkertainen, kun virtaama ja hyötysuhde ovat samat
**Periaate:** Turbiinin läpi putoava vesi menettää potentiaalienergiaa $mgh$, joka on suoraan verrannollinen putouskorkeuteen $h$. Koska sekunnissa turbiinin läpi kulkeva massa $\rho Q$ on sama, veden tuoma teho $\rho Q g h$ on verrannollinen putouskorkeuteen, ja samalla hyötysuhteella sähköteho on sitä myös.
**Mallivastaus:** Jokainen turbiinin läpi virtaava vesikilogramma menettää pudotessaan kaksi kertaa enemmän potentiaalienergiaa. Massa sekunnissa ja hyötysuhde pysyvät samoina, joten teho kaksinkertaistuu, kun putouskorkeus kaksinkertaistuu. Muut selitykset eivät päde: virtaama on tehtävän mukaan sama, veden massa ei kasva pudotessa, eikä hyötysuhde muutu.

## fy4-15-L1-07
**Annettu:** virtaama $Q = 35{,}0\,\text{m}^3\text{/s}$, putouskorkeus $h = 8{,}50\,\text{m}$; veden tiheys $\rho = 1000\,\text{kg/m}^3$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** veden tuoma teho $P_\text{o}$ yksikössä $\text{MW}$
**Periaate:** Sekunnissa turbiinien läpi putoaa vesimassa $\rho Q$, ja jokainen kilogramma menettää potentiaalienergiaa $gh$. Hyötysuhdetta ei oteta huomioon, joten kysytty teho on potentiaalienergian pienenemisnopeus.
**Kaava:** $P_\text{o} = \rho Q g h$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten teho saadaan watteina; lopuksi $1\,\text{MW} = 10^{6}\,\text{W}$.
**Sijoitus:** $P_\text{o} = 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 35{,}0\,\tfrac{\text{m}^3}{\text{s}} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 8{,}50\,\text{m} = 2\,918\,475\,\text{W} \approx 2{,}92\,\text{MW}$
**Vastaus:** $2{,}92\,\text{MW}$, kolme merkitsevää numeroa kuten virtaamassa $35{,}0\,\text{m}^3\text{/s}$ ja putouskorkeudessa $8{,}50\,\text{m}$.
**Järkevyys:** Sekunnissa putoaa $35\,000\,\text{kg}$ vettä, ja kilogramma menettää $8{,}5\,\text{m}$:n pudotuksessa noin $10 \cdot 8{,}5\,\text{J} = 85\,\text{J}$. Tulo on noin $3{,}0\,\text{MW}$, joten tulos on oikean suuruinen. Sähkötehoa saataisiin hyötysuhteella vähemmän kuin $2{,}92\,\text{MW}$.

## fy4-15-L1-08
**Annettu:** ilman massa $m = 2{,}50 \cdot 10^{3}\,\text{kg}$, nopeus $v = 12{,}0\,\text{m/s}$
**Kysytty:** liike-energia $E_\text{k}$ yksikössä $\text{kJ}$
**Periaate:** Liikkuvan kappaleen liike-energia riippuu massasta ja nopeuden neliöstä. Ilmamassa lasketaan yhtenä kappaleena, jonka kaikki osat liikkuvat nopeudella $v$.
**Kaava:** $E_\text{k} = \tfrac{1}{2}mv^2$
**Muunnokset:** Suureet ovat SI-yksiköissä, joten energia saadaan jouleina; lopuksi $1\,\text{kJ} = 1000\,\text{J}$.
**Sijoitus:** $E_\text{k} = \tfrac{1}{2} \cdot 2{,}50 \cdot 10^{3}\,\text{kg} \cdot \left(12{,}0\,\tfrac{\text{m}}{\text{s}}\right)^2 = 180\,000\,\text{J} = 180\,\text{kJ}$
**Vastaus:** $180\,\text{kJ}$, kolme merkitsevää numeroa kuten massassa ja nopeudessa.
**Järkevyys:** Kilogramma ilmaa nopeudella $12\,\text{m/s}$ sisältää liike-energiaa $\tfrac{1}{2} \cdot 12^2\,\text{J} = 72\,\text{J}$, ja $2500$ kilogrammaa sisältää $2500 \cdot 72\,\text{J} = 180\,\text{kJ}$. Tulos täsmää.

## fy4-15-L2-05
**Annettu:** taulukko: teho $P$ ja aika $t$ vuodessa viidellä tuulen nopeudella (esimerkkiaineisto); muina aikoina teho on nolla
**Kysytty:** vuosienergia $E$ yksikössä $\text{GWh}$
**Periaate:** Teho kertoo energian muuntumisnopeuden, joten energia on teho kertaa aika. Kullakin nopeudella teho on vakio, joten jokaisen rivin energia on $P t$. Vuosienergia on rivien energioiden summa.
**Kaava:** $E = \sum P t$
**Muunnokset:** Kun teho on kilowatteina ja aika tunteina, energia saadaan kilowattitunteina. Lopuksi $1\,\text{GWh} = 10^{6}\,\text{kWh}$.
**Sijoitus:** Rivien energiat ovat $100\,\text{kW} \cdot 1500\,\text{h} = 150\,000\,\text{kWh}$, $340 \cdot 2200 = 748\,000\,\text{kWh}$, $850 \cdot 1800 = 1\,530\,000\,\text{kWh}$, $1650 \cdot 1000 = 1\,650\,000\,\text{kWh}$ ja $2000 \cdot 700 = 1\,400\,000\,\text{kWh}$. Summa on $5\,478\,000\,\text{kWh}$, joten $E = 5{,}478\,\text{GWh}$.
**Vastaus:** $5{,}5\,\text{GWh}$, kaksi merkitsevää numeroa, koska taulukon tehot ovat kahden tai kolmen merkitsevän numeron tarkkuudella.
**Järkevyys:** Jos voimala tuottaisi koko vuoden ($8760\,\text{h}$) nimellistehoa $2000\,\text{kW}$, energia olisi $17{,}5\,\text{GWh}$. Saatu $5{,}5\,\text{GWh}$ on noin $31\,\%$ siitä, mikä sopii sille, että tuulivoimalan keskiteho on selvästi nimellistehoa pienempi.

## fy4-15-L2-06
**Annettu:** virtaamat huhtikuusta syyskuuhun $85$, $120$, $45$, $30$, $28$ ja $40\,\text{m}^3\text{/s}$ (esimerkkiaineisto), putouskorkeus $h = 9{,}0\,\text{m}$, hyötysuhde $\eta = 0{,}85$, kuukauden pituus $30\,\text{vrk}$; $\rho = 1000\,\text{kg/m}^3$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** a) sähköenergia $E$ yksikössä $\text{GWh}$; b) toukokuun ja elokuun tehojen suhde sekä selitys vaihtelulle
**Periaate:** Vesivoimalan teho on kuukauden virtaamalla $P = \eta\rho Q g h$. Koska $\eta$, $\rho$ ja $h$ ovat vakioita, teho on verrannollinen virtaamaan. Energia on teho kertaa aika, ja kullakin kuukaudella on sama pituus, joten energia saadaan summaamalla kuukausien tehot ja kertomalla yhden kuukauden pituudella.
**Kaava:** $P = \eta\rho Q g h$ ja $E = Pt$, joten $E = \eta\rho g h\,\left(\sum Q\right) t$
**Muunnokset:** Kuukauden pituus on $t = 30 \cdot 24\,\text{h} = 720\,\text{h}$. Teho lasketaan watteina ja muunnetaan megawateiksi, $1\,\text{MW} = 10^{6}\,\text{W}$, jolloin energia saadaan megawattitunteina; lopuksi $1\,\text{GWh} = 1000\,\text{MWh}$.
**Sijoitus:** Virtaamien summa on $85 + 120 + 45 + 30 + 28 + 40 = 348\,\text{m}^3\text{/s}$. Kuukausitehojen summa on
$$\begin{aligned}\textstyle\sum P &= 0{,}85 \cdot 1000 \cdot 9{,}81 \cdot 9{,}0 \cdot 348\,\text{W} \\ &= 26{,}12\,\text{MW}\end{aligned}$$
ja energia
$$\begin{aligned}E &= 26{,}12\,\text{MW} \cdot 720\,\text{h} \\ &= 18\,804\,\text{MWh} \\ &= 18{,}8\,\text{GWh}\end{aligned}$$
**Vastaus:** $19\,\text{GWh}$, kaksi merkitsevää numeroa kuten putouskorkeudessa $9{,}0\,\text{m}$ ja hyötysuhteessa $0{,}85$.
**Mallivastaus kohtaan b:** Teho on verrannollinen virtaamaan, joten toukokuun ja elokuun tehojen suhde on sama kuin virtaamien suhde $120 : 28 = 4{,}3$. Toukokuussa teho on noin $9{,}0\,\text{MW}$ ja elokuussa noin $2{,}1\,\text{MW}$. Taulukossa virtaama on suurin keväällä ja pienin loppukesällä, joten tuotanto vaihtelee sen mukaan, kuinka paljon vettä joessa virtaa. Putouskorkeus ja hyötysuhde pysyvät vakioina, joten ne eivät selitä vaihtelua.
**Järkevyys:** Keskivirtaama on $348 : 6 = 58\,\text{m}^3\text{/s}$, ja sillä teho olisi $0{,}85 \cdot 1000 \cdot 58 \cdot 9{,}81 \cdot 9{,}0\,\text{W} \approx 4{,}35\,\text{MW}$. Kuuden kuukauden ($4320\,\text{h}$) aikana energia olisi $4{,}35\,\text{MW} \cdot 4320\,\text{h} \approx 18{,}8\,\text{GWh}$, sama tulos.

## fy4-15-L2-07
**Annettu:** halkaisija $d = 60\,\text{m}$, tuulen nopeus $v = 7{,}0\,\text{m/s}$, ilman tiheys $\rho = 1{,}25\,\text{kg/m}^3$, hyötysuhde $\eta = 0{,}40$; oppilaan tulos $4{,}9\,\text{kW}$
**Kysytty:** oppilaan virhe ja oikea sähköteho $P$ yksikössä $\text{kW}$
**Periaate:** Roottorin läpi virtaa sekunnissa ilmaa, jonka massa on verrannollinen nopeuteen $v$, ja jokaisen ilmakilogramman liike-energia on verrannollinen nopeuden neliöön $v^2$. Tuulen teho on siksi verrannollinen nopeuden kolmanteen potenssiin $v^3$. Oppilas käytti nopeutta ensimmäisessä potenssissa.
**Kaava:** $P = \tfrac{1}{2}\eta\rho A v^3$ ja $A = \pi r^2$
**Muunnokset:** Säde on $r = 60\,\text{m} : 2 = 30\,\text{m}$. Pinta-ala on $A = \pi \cdot (30\,\text{m})^2 = 2827\,\text{m}^2$, kuten oppilaalla. Lopuksi $1\,\text{kW} = 1000\,\text{W}$.
**Sijoitus:** Oikea teho on
$$\begin{aligned}P &= 0{,}5 \cdot 0{,}40 \cdot 1{,}25\,\tfrac{\text{kg}}{\text{m}^3} \\ &\quad \cdot 2827\,\text{m}^2 \cdot \left(7{,}0\,\tfrac{\text{m}}{\text{s}}\right)^3 \\ &= 242\,452\,\text{W}\end{aligned}$$
**Vastaus:** $240\,\text{kW}$ eli $2{,}4 \cdot 10^{2}\,\text{kW}$, kaksi merkitsevää numeroa kuten tuulen nopeudessa $7{,}0\,\text{m/s}$ ja hyötysuhteessa $0{,}40$.
**Mallivastaus virheestä:** Oppilaan kaavassa tuulen nopeus on ensimmäisessä potenssissa, vaikka sen pitää olla kolmannessa potenssissa. Virheen huomaa yksiköistä: $\tfrac{\text{kg}}{\text{m}^3} \cdot \text{m}^2 \cdot \tfrac{\text{m}}{\text{s}}$ on $\tfrac{\text{kg}}{\text{s}}$, ei watti $\tfrac{\text{kg} \cdot \text{m}^2}{\text{s}^3}$: tulosta puuttuu tekijä $v^2$ eli yksikkö $\tfrac{\text{m}^2}{\text{s}^2}$. Oikea teho on $7{,}0^2 = 49$ kertaa oppilaan tulos.
**Järkevyys:** Oppilaan tulos $4948\,\text{W}$ kerrottuna luvulla $49$ on $242\,452\,\text{W}$, sama kuin oikea tulos. Tuulen teho on $240 : 0{,}40 = 600\,\text{kW}$, ja sähköksi muuttuu sen $40\,\%$, kuten pitääkin.

## fy4-15-L3-04
**Annettu:** taulukko: nopeudet $v = 4$–$9\,\text{m/s}$ ja tehot $P = 80$–$905\,\text{kW}$ (esimerkkiaineisto), halkaisija $d = 80\,\text{m}$, ilman tiheys $\rho = 1{,}25\,\text{kg/m}^3$, nimellisteho $2{,}0\,\text{MW}$
**Kysytty:** a) onko $P \propto v^3$; b) hyötysuhde $\eta$ prosentteina; c) mallin teho nopeudella $13\,\text{m/s}$ ja sen vertaus nimellistehoon
**Periaate:** Jos teho noudattaa mallia $P = k v^3$, suhde $P/v^3 = k$ on vakio. Tuulivoimalan kaavassa $P = \tfrac{1}{2}\eta\rho A v^3$ vakio on $k = \tfrac{1}{2}\eta\rho A$, joten hyötysuhde saadaan vakiosta $k$, kun roottorin pinta-ala tunnetaan.
**Kaava:** $k = \dfrac{P}{v^3}$ ja $k = \tfrac{1}{2}\eta\rho A$, joten $\eta = \dfrac{2k}{\rho A}$ ja $A = \pi r^2$
**Muunnokset:** Säde on $r = 80\,\text{m} : 2 = 40\,\text{m}$, ja $A = \pi \cdot (40\,\text{m})^2 = 5027\,\text{m}^2$. Suhteet lasketaan yksikössä $\text{kW}/(\text{m/s})^3$; keskiarvo muunnetaan watteihin, $1\,\text{kW} = 1000\,\text{W}$.
**Sijoitus:** Suhteet $P/v^3$ nopeuksilla $4$–$9\,\text{m/s}$ ovat $1{,}250$, $1{,}240$, $1{,}273$, $1{,}239$, $1{,}270$ ja $1{,}241$ yksikössä $\tfrac{\text{kW}}{(\text{m/s})^3}$.
Suhteiden summa on $7{,}513$, joten keskiarvo on $k_\text{ka} = 7{,}513 : 6 = 1{,}252\,\tfrac{\text{kW}}{(\text{m/s})^3} = 1252\,\tfrac{\text{W}}{(\text{m/s})^3}$. Hyötysuhde on
$$\begin{aligned}\eta &= \frac{2 \cdot 1252}{1{,}25 \cdot 5027} \\ &= 0{,}3986\end{aligned}$$
**Vastaus:** $40\,\%$, kaksi merkitsevää numeroa, koska taulukon tehot ovat kahden tai kolmen merkitsevän numeron tarkkuudella.
**Mallivastaus kohtiin a ja c:** Nopeus kasvaa nopeudesta $4\,\text{m/s}$ nopeuteen $9\,\text{m/s}$ eli $2{,}25$-kertaiseksi, jolloin $v^3$ kasvaa yli $11$-kertaiseksi, ja teho kasvaa saman verran: $905 : 80 \approx 11{,}3$. Suhde $P/v^3$ pysyy välillä $1{,}24$–$1{,}27$, eli se vaihtelee vain noin $\pm 2\,\%$ koko nopeusalueella. Pisteiden satunnaishajonta selittää pienen vaihtelun, eikä suhde kasva tai pienene nopeuden mukana, joten malli $P = k v^3$ sopii aineistoon. Tuplaus tukee tulosta: nopeudesta $4\,\text{m/s}$ nopeuteen $8\,\text{m/s}$ teho kasvaa $650 : 80 \approx 8{,}1$-kertaiseksi, ja $2^3 = 8$. Mallin ennuste nopeudella $13\,\text{m/s}$ on $1{,}252 \cdot 13^3\,\text{kW} \approx 2750\,\text{kW} = 2{,}8\,\text{MW}$, mikä on suurempi kuin nimellisteho $2{,}0\,\text{MW}$. Voimala ei voi tuottaa nimellistehoaan enempää, vaan lapoja käännetään päästämään osa tuulesta ohi, joten malli $P = k v^3$ pätee vain nimellistehon alapuolella.
**Järkevyys:** Tuulen teho nopeudella $9\,\text{m/s}$ on $\tfrac{1}{2} \cdot 1{,}25 \cdot 5027 \cdot 9^3\,\text{W} \approx 2290\,\text{kW}$, ja $905\,\text{kW}$ on siitä $905 : 2290 \approx 0{,}40$, sama kuin saatu hyötysuhde. Tulos on alle teoreettisen ylärajan $59\,\%$ ja alle puolet, kuten tuulivoimalalla.

## fy4-15-L3-05
**Annettu:** ylijäämätehot $40$, $52$, $62$, $58$, $48$ ja $40\,\text{MW}$ kuuden tunnin ajan, kunkin tunnin keskiarvoina (esimerkkiaineisto); nostokorkeus $h = 85{,}0\,\text{m}$, pumppujen hyötysuhde $\eta = 0{,}800$, yläaltaan tilavuus $1{,}20 \cdot 10^{6}\,\text{m}^3$, kulutus $40{,}0\,\text{MW}$; $\rho = 1000\,\text{kg/m}^3$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** a) pumpatun veden tilavuus $V$ yksikössä $\text{m}^3$; b) mahtuuko vesi yläaltaaseen; c) varastoidun energian kestoaika kulutukselle $40{,}0\,\text{MW}$
**Periaate:** Ylijäämäsähköenergia on teho kertaa aika. Pumput muuttavat siitä osuuden $\eta$ veden potentiaalienergiaksi $mgh$, josta ratkaistaan nostetun veden massa ja edelleen tilavuus $V = m/\rho$.
**Kaava:** $E = \sum P t$, $\eta E = mgh$, joten $m = \dfrac{\eta E}{gh}$ ja $V = \dfrac{m}{\rho}$
**Muunnokset:** Jokaisen tunnin teho on vakio, joten $E$ saadaan megawattitunteina. Lopuksi $1\,\text{MWh} = 10^{6}\,\text{W} \cdot 3600\,\text{s} = 3{,}6 \cdot 10^{9}\,\text{J}$.
**Sijoitus:** Tehojen summa on $40 + 52 + 62 + 58 + 48 + 40 = 300\,\text{MW}$, ja jokainen teho kestää yhden tunnin, joten $E = 300\,\text{MWh} = 300 \cdot 3{,}6 \cdot 10^{9}\,\text{J} = 1{,}08 \cdot 10^{12}\,\text{J}$. Veteen siirtyy energiaa $\eta E = 0{,}800 \cdot 1{,}08 \cdot 10^{12}\,\text{J} = 8{,}64 \cdot 10^{11}\,\text{J}$. Massa ja tilavuus ovat
$$\begin{aligned}m &= \frac{8{,}64 \cdot 10^{11}\,\text{J}}{9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 85{,}0\,\text{m}} \\ &= 1{,}036 \cdot 10^{9}\,\text{kg} \\ V &= \frac{m}{\rho} = 1{,}036 \cdot 10^{6}\,\text{m}^3\end{aligned}$$
**Vastaus:** $1{,}04 \cdot 10^{6}\,\text{m}^3$, kolme merkitsevää numeroa kuten korkeudessa $85{,}0\,\text{m}$ ja hyötysuhteessa $0{,}800$.
**Mallivastaus kohtiin b ja c:** Pumpattu vesi $1{,}04 \cdot 10^{6}\,\text{m}^3$ on pienempi kuin yläaltaan tilavuus $1{,}20 \cdot 10^{6}\,\text{m}^3$, joten vesi mahtuu altaaseen ja allas täyttyy noin $86\,\%$:iin. Veteen varastoitunut energia on $0{,}800 \cdot 300\,\text{MWh} = 240\,\text{MWh}$. Teholla $40{,}0\,\text{MW}$ se riittäisi ajaksi $240\,\text{MWh} : 40{,}0\,\text{MW} = 6{,}00\,\text{h}$, jos turbiinin ja generaattorin häviöt jätetään huomiotta. Todellisuudessa häviöt lyhentävät aikaa. Pumppuvoimala sopii tuulivoiman rinnalle, koska tuulivoima on sääriippuvaa ja sen teho voi ylittää kulutuksen, kun taas vesivoima on hyvin säädettävää. Ylijäämäsähkö voidaan varastoida veden potentiaalienergiaksi ja muuttaa takaisin sähköksi, kun tuuli tyyntyy ja kulutus on suurempi kuin tuotanto.
**Järkevyys:** Tarkistetaan potentiaalienergia: $1{,}036 \cdot 10^{9}\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \cdot 85{,}0\,\text{m} = 8{,}64 \cdot 10^{11}\,\text{J}$, joka on $240\,\text{MWh}$. Kuutiometri vettä sitoo $85\,\text{m}$:n korkeudella noin $1000 \cdot 9{,}81 \cdot 85\,\text{J} = 0{,}83\,\text{MJ}$, joten $240\,\text{MWh} = 8{,}64 \cdot 10^{5}\,\text{MJ}$ vaatii noin $10^{6}$ kuutiometriä, kuten saatiin.

## fy4-15-L2-08
**Kysytty:** tuulivoimalan sähkötehon $P$ suuruusluokka.
**Periaate:** Roottorin läpi virtaa sekunnissa ilmaa, jonka liike-energia on tuulen teho $\tfrac{1}{2}\rho A v^3$, ja voimala muuttaa siitä sähköksi osuuden $\eta$. Voimala ei saavuta nimellistehoaan, joten kaava $P = \tfrac{1}{2}\eta\rho A v^3$ kuvaa sitä. Nopeus on muunnettava yksikköön $\text{m/s}$, koska se on kaavassa kolmannessa potenssissa.
**Mallivastaus:** Säde on $r = 100\,\text{m} : 2 = 50\,\text{m}$ ja $\eta = 0{,}40$. Tuulen nopeus muunnetaan yksikköön $\text{m/s}$, ja sitten lasketaan roottorin pyyhkäisemä pinta-ala ja sähköteho:

$$\begin{aligned}
&v = 36\,\text{km/h} \\
&\phantom{v} = \dfrac{36\,000\,\text{m}}{3600\,\text{s}} \\
&\phantom{v} = 10\,\text{m/s} \\
&A = \pi r^2 = \pi \cdot (50\,\text{m})^2 \\
&\phantom{A} \approx 7854\,\text{m}^2 \\
&P = \tfrac{1}{2}\eta\rho A v^3 \\
&\phantom{P} = 0{,}5 \cdot 0{,}40 \cdot 1{,}25\,\tfrac{\text{kg}}{\text{m}^3} \\
&\qquad \cdot 7854\,\text{m}^2 \cdot \left(10\,\tfrac{\text{m}}{\text{s}}\right)^3 \\
&\phantom{P} \approx 1{,}96 \cdot 10^{6}\,\text{W}
\end{aligned}$$

Sähköteho on suuruusluokaltaan $2\,\text{MW}$. Vääriin vaihtoehtoihin johtavat tyypilliset virheet: jos teho lasketaan verrannolliseksi nopeuteen $v$, tulos on noin $20\,\text{kW}$, ja nopeuden neliöllä $v^2$ noin $0{,}2\,\text{MW}$. Verrannollisuudessa $v$ unohtuvat molemmat nopeuden mukana kasvavat tekijät, ilmakilogramman liike-energia ja sekunnissa virtaavan ilman massa, neliössä $v^2$ vain sekunnissa virtaavan ilman massan kasvu. Jos nopeus sijoitetaan lukuna $36$ ilman muunnosta, tulos on noin $47$ kertaa liian suuri, noin $90\,\text{MW}$.

Tulos on järkevä: tuulen teho on $P : \eta \approx 4{,}9\,\text{MW}$, ja sähköksi saadaan alle puolet. Lisäksi luvun esimerkin $120\,\text{m}$:n roottori antoi tuulen nopeudella $9{,}0\,\text{m/s}$ noin $2{,}3\,\text{MW}$, mikä on samaa suuruusluokkaa.
