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
