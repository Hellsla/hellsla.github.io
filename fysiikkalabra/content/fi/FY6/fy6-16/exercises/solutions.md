## fy6-16-L1-01
**Annettu:** akun energia täyteen ladattuna $W = 64\,\text{kWh}$, varaustaso nousee $15\,\%$:sta $80\,\%$:iin
**Kysytty:** akkuun varastoitava energia $W_\text{akku}$ kilowattitunteina
**Periaate:** Varaustaso kertoo, kuinka suuri osa akun täydestä energiasta siihen on varastoitunut. Akkuun pitää siis siirtää varaustasojen erotuksen osuus täydestä energiasta.
**Kaava:** $W_\text{akku} = (s_2 - s_1) W$, missä $s_1$ ja $s_2$ ovat varaustasot desimaalilukuina
**Muunnokset:** $s_1 = 15\,\% = 0{,}15$ ja $s_2 = 80\,\% = 0{,}80$
**Sijoitus:** $W_\text{akku} = (0{,}80 - 0{,}15) \cdot 64\,\text{kWh} = 0{,}65 \cdot 64\,\text{kWh} = 41{,}6\,\text{kWh}$
**Vastaus:** $42\,\text{kWh}$, kaksi merkitsevää numeroa kuten akun energiassa $64\,\text{kWh}$.
**Järkevyys:** Kaksi kolmasosaa akusta on noin $\tfrac{2}{3} \cdot 64\,\text{kWh} \approx 43\,\text{kWh}$, ja $65\,\%$ on vähän alle kahden kolmasosan. Tulos on pienempi kuin koko akku, kuten pitää.

## fy6-16-L1-02
**Annettu:** jännite $U = 230\,\text{V}$, latausvirta $I = 10\,\text{A}$
**Kysytty:** latausteho $P$ kilowatteina
**Periaate:** Pistorasia käyttää yhtä vaihetta, joten teho on jännite kertaa virta kuten minkä tahansa yksivaiheisen laitteen teho. Verkkojännite $230\,\text{V}$ on vaihtojännitteen tehollinen arvo, joten sillä lasketaan kuten tasajännitteellä.
**Kaava:** $P = UI$
**Muunnokset:** Tulos watteina muunnetaan kilowateiksi: $1\,\text{W} = 0{,}001\,\text{kW}$.
**Sijoitus:** $P = 230\,\text{V} \cdot 10\,\text{A} = 2300\,\text{W} = 2{,}3\,\text{kW}$
**Vastaus:** $2{,}3\,\text{kW}$, kaksi merkitsevää numeroa kuten virrassa $10\,\text{A}$.
**Järkevyys:** Teho on samaa suuruusluokkaa kuin vedenkeittimen teho, mutta lataus kestää tunteja. $40\,\text{kWh}$:n lataukseen kuluisi tällä teholla yli $17\,\text{h}$, joten pistorasialataus sopii lähinnä hätätilanteisiin tai mökille.

## fy6-16-L1-03
**Annettu:** teho $P = 11\,\text{kW}$, kolme vaihetta, vaihejännite $U = 230\,\text{V}$
**Kysytty:** yhden vaihejohtimen virta $I$ ampeereina
**Periaate:** Asema ottaa jokaisesta kolmesta vaihejohtimesta saman virran, ja jokainen vaihe siirtää tehon $UI$. Kokonaisteho on siis kolme kertaa yhden vaiheen teho.
**Kaava:** $P = 3UI$, josta $I = \dfrac{P}{3U}$
**Muunnokset:** $P = 11\,\text{kW} = 11\,000\,\text{W}$
**Sijoitus:** $I = \dfrac{11\,000\,\text{W}}{3 \cdot 230\,\text{V}} = \dfrac{11\,000\,\text{W}}{690\,\text{V}} = 15{,}94\,\text{A}$
**Vastaus:** $16\,\text{A}$, kaksi merkitsevää numeroa kuten tehossa $11\,\text{kW}$.
**Järkevyys:** Jos koko teho kulkisi yhdessä vaiheessa, virta olisi $11\,000\,\text{W} : 230\,\text{V} \approx 48\,\text{A}$; kolmeen vaiheeseen jaettuna se on kolmasosa siitä. $16\,\text{A}$ on tavallinen latausaseman ryhmän sulakkeen koko.

## fy6-16-L1-04
**Annettu:** verkosta otettu energia $W_\text{verkko} = 45\,\text{kWh}$, hinta $a = 14\,\text{snt/kWh}$
**Kysytty:** kustannus $K$ euroina
**Periaate:** Lataus maksetaan verkosta otetusta energiasta, ja jokainen kilowattitunti maksaa saman hinnan. Kustannus on siis hinta kertaa energia.
**Kaava:** $K = a W_\text{verkko}$
**Muunnokset:** $a = 14\,\text{snt/kWh} = 14 \cdot 0{,}01\,\text{€/kWh} = 0{,}14\,\text{€/kWh}$
**Sijoitus:** $K = 0{,}14\,\tfrac{\text{€}}{\text{kWh}} \cdot 45\,\text{kWh} = 6{,}30\,\text{€}$
**Vastaus:** $6{,}3\,\text{€}$, kaksi merkitsevää numeroa kuten energiassa $45\,\text{kWh}$ ja hinnassa $14\,\text{snt/kWh}$.
**Järkevyys:** Sentteinä $45 \cdot 14\,\text{snt} = 630\,\text{snt}$. Kymmenellä sentillä hinta olisi $4{,}50\,\text{€}$ ja viidellätoista $6{,}75\,\text{€}$, joten tulos on niiden välissä lähellä jälkimmäistä.

## fy6-16-L1-05
**Annettu:** verkosta otettu energia $W_\text{verkko} = 50\,\text{kWh}$, akkuun varastoitunut energia $W_\text{akku} = 44\,\text{kWh}$
**Kysytty:** latauksen hyötysuhde $\eta$ prosentteina
**Periaate:** Hyödyllinen energia on akkuun varastoitunut energia, ja otettu energia on verkosta otettu energia. Hyötysuhde on niiden suhde.
**Kaava:** $\eta = \dfrac{W_\text{akku}}{W_\text{verkko}}$
**Muunnokset:** Ei tarvita: kumpikin energia on kilowattitunteina, joten yksikkö supistuu. Desimaaliluku muunnetaan prosenteiksi kertomalla sadalla.
**Sijoitus:** $\eta = \dfrac{44\,\text{kWh}}{50\,\text{kWh}} = 0{,}88 = 88\,\%$
**Vastaus:** $88\,\%$, kaksi merkitsevää numeroa kuten energioissa $44\,\text{kWh}$ ja $50\,\text{kWh}$.
**Järkevyys:** Häviöihin meni $50\,\text{kWh} - 44\,\text{kWh} = 6\,\text{kWh}$, eli $12\,\%$ otetusta energiasta; $88\,\% + 12\,\% = 100\,\%$. Hyötysuhde on alle $100\,\%$ ja tyypillisen kotilatauksen suuruinen.

## fy6-16-L2-01
**Annettu:** kuvaajasta luetut tehot ja ajat
**Kysytty:** verkosta otettu energia $W_\text{verkko}$ kilowattitunteina
**Periaate:** Kun teho on vakio, energia on teho kertaa aika. Kuvaajassa teho on kahdessa vakiotehoisessa jaksossa, joten energia on kahden suorakulmion pinta-alojen summa.
**Kuvaajan lukeminen:** Ensimmäisessä jaksossa teho on $P_1 = 11\,\text{kW}$ ajan $0\text{–}2{,}0\,\text{h}$, joten $t_1 = 2{,}0\,\text{h}$. Toisessa jaksossa teho on $P_2 = 5{,}5\,\text{kW}$ ajan $2{,}0\text{–}3{,}0\,\text{h}$, joten $t_2 = 1{,}0\,\text{h}$. Sen jälkeen teho on nolla.
**Kaava:** $W_\text{verkko} = P_1 t_1 + P_2 t_2$
**Muunnokset:** Ei tarvita: kilowateilla ja tunneilla energia saadaan suoraan kilowattitunteina.
**Sijoitus:** $W_\text{verkko} = 11\,\text{kW} \cdot 2{,}0\,\text{h} + 5{,}5\,\text{kW} \cdot 1{,}0\,\text{h} = 22\,\text{kWh} + 5{,}5\,\text{kWh} = 27{,}5\,\text{kWh}$
**Vastaus:** $28\,\text{kWh}$, kaksi merkitsevää numeroa kuten kuvaajasta luetuissa arvoissa.
**Järkevyys:** Jos teho olisi ollut koko kolme tuntia $11\,\text{kW}$, energiaa olisi otettu $33\,\text{kWh}$; viimeisen tunnin puolittunut teho vähentää tästä $5{,}5\,\text{kWh}$, joten $33\,\text{kWh} - 5{,}5\,\text{kWh} = 27{,}5\,\text{kWh}$.

## fy6-16-L2-02
**Annettu:** $U = 230\,\text{V}$, $I = 16\,\text{A}$, yksi vaihe, akun energia $60\,\text{kWh}$, varaustaso $20\,\% \to 80\,\%$, $\eta = 90\,\%$
**Kysytty:** latausaika $t$ tunteina
**Periaate:** Akkuun pitää siirtää $60\,\%$ sen energiasta. Teho on vakio, joten verkosta otettu energia on teho kertaa aika, ja akkuun siitä varastoituu hyötysuhteen osuus. Yksivaiheisen aseman teho on jännite kertaa virta.
**Kaava:** $\eta P t = W_\text{akku}$ ja $P = UI$, joten $t = \dfrac{W_\text{akku}}{\eta U I}$
**Muunnokset:** $W_\text{akku} = (0{,}80 - 0{,}20) \cdot 60\,\text{kWh} = 36\,\text{kWh}$; $UI = 230\,\text{V} \cdot 16\,\text{A} = 3680\,\text{W} = 3{,}68\,\text{kW}$; $\eta = 0{,}90$
**Sijoitus:** $t = \dfrac{36\,\text{kWh}}{0{,}90 \cdot 3{,}68\,\text{kW}} = \dfrac{36\,\text{kWh}}{3{,}312\,\text{kW}} = 10{,}87\,\text{h}$
**Vastaus:** $11\,\text{h}$, kaksi merkitsevää numeroa kuten hyötysuhteessa $90\,\%$.
**Järkevyys:** Arvio: akkuun menee noin $3{,}3\,\text{kW}$, ja $33\,\text{kWh}$ veisi $10\,\text{h}$; $36\,\text{kWh}$ vie vähän enemmän. Kolmivaiheisella $16\,\text{A}$:n asemalla sama lataus kestäisi kolmasosan, noin $3{,}6\,\text{h}$.

## fy6-16-L2-03
**Annettu:** pääsulakkeet $3 \cdot 25\,\text{A}$, kiukaan teho $P_\text{k} = 9{,}0\,\text{kW}$ kolmessa vaiheessa, $U = 230\,\text{V}$
**Kysytty:** latausaseman suurin sallittu virta $I_\text{a}$ yhdessä vaihejohtimessa
**Periaate:** Pääsulake on jokaisessa vaihejohtimessa, ja saman vaihejohtimen kautta kulkevat virrat lasketaan yhteen (luku *Kirchhoffin lait ja potentiaali virtapiirissä*). Kiuas ottaa jokaisesta vaiheesta saman virran, joten sen virta saadaan kaavasta $P = 3UI$. Autolle jää se, mikä jää jäljelle $25\,\text{A}$:sta.
**Kaava:** $I_\text{k} + I_\text{a} = I_\text{p}$ ja $I_\text{k} = \dfrac{P_\text{k}}{3U}$, joten $I_\text{a} = I_\text{p} - \dfrac{P_\text{k}}{3U}$, missä $I_\text{p} = 25\,\text{A}$
**Muunnokset:** $P_\text{k} = 9{,}0\,\text{kW} = 9000\,\text{W}$
**Sijoitus:** $I_\text{a} = 25\,\text{A} - \dfrac{9000\,\text{W}}{3 \cdot 230\,\text{V}} = 25\,\text{A} - 13{,}04\,\text{A} = 11{,}96\,\text{A}$
**Vastaus:** $12\,\text{A}$, kaksi merkitsevää numeroa kuten pääsulakkeen virrassa $25\,\text{A}$.
**Järkevyys:** Kiuas ja auto yhdessä ottavat silloin $13\,\text{A} + 12\,\text{A} = 25\,\text{A}$ jokaisesta vaiheesta. Auton teho on noin $3 \cdot 230\,\text{V} \cdot 12\,\text{A} \approx 8{,}3\,\text{kW}$, vähemmän kuin aseman $11\,\text{kW}$, joten kuormanhallinnan pitää pienentää latausta saunan ajaksi.

## fy6-16-L2-04
**Annettu:** kaapelin pituus $l = 30\,\text{m}$, poikkipinta-ala $A = 2{,}5\,\text{mm}^2$, virta $I = 16\,\text{A}$, $\rho = 1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m}$
**Kysytty:** kaapelissa häviävä jännite $U_\text{h}$ voltteina
**Periaate:** Kaapelin kuparijohtimet ovat vastus, jonka läpi kulkee latausvirta. Virta kulkee vaihejohdinta pitkin asemalle ja nollajohdinta pitkin takaisin, joten kuparin pituus on $2l$. Ohmin lain mukaan resistanssin yli oleva jännite on resistanssi kertaa virta.
**Kaava:** $U_\text{h} = RI$ ja $R = \rho \dfrac{2l}{A}$, joten $U_\text{h} = \rho \dfrac{2l}{A} I$
**Muunnokset:** $A = 2{,}5\,\text{mm}^2 = 2{,}5 \cdot (10^{-3}\,\text{m})^2 = 2{,}5 \cdot 10^{-6}\,\text{m}^2$
**Sijoitus:** $U_\text{h} = 1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot \dfrac{2 \cdot 30\,\text{m}}{2{,}5 \cdot 10^{-6}\,\text{m}^2} \cdot 16\,\text{A} = 0{,}408\,\Omega \cdot 16\,\text{A} = 6{,}53\,\text{V}$
**Vastaus:** $6{,}5\,\text{V}$, kaksi merkitsevää numeroa kuten resistiivisyydessä $1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m}$ ja poikkipinta-alassa $2{,}5\,\text{mm}^2$.
**Järkevyys:** Häviö on $6{,}5\,\text{V} : 230\,\text{V} \approx 3\,\%$ verkkojännitteestä, joten asema saa yhä lähes koko jännitteen. Kaapeliin tulee teho $6{,}5\,\text{V} \cdot 16\,\text{A} \approx 100\,\text{W}$, eli noin $3{,}5\,\text{W}$ metriä kohti, mikä jakautuu pitkälle matkalle.

## fy6-16-L3-01
**Annettu:** akkuun vuodessa $W_\text{akku} = 3000\,\text{kWh}$, hyötysuhteet $\eta_1 = 82\,\%$ (pistorasia) ja $\eta_2 = 92\,\%$ (latausasema), hinta $a = 15\,\text{snt/kWh}$
**Kysytty:** vuoden säästö $\Delta K$ euroina
**Periaate:** Akkuun menee kummallakin tavalla sama energia, mutta verkosta otetaan akkuun menevä energia jaettuna hyötysuhteella. Säästö syntyy siitä, että latausasemalla verkosta otetaan vähemmän, ja se maksetaan samalla hinnalla.
**Kaava:** $W_\text{verkko} = \dfrac{W_\text{akku}}{\eta}$ ja $K = a W_\text{verkko}$, joten $\Delta K = a \left(\dfrac{W_\text{akku}}{\eta_1} - \dfrac{W_\text{akku}}{\eta_2}\right)$
**Muunnokset:** $\eta_1 = 0{,}82$, $\eta_2 = 0{,}92$ ja $a = 15\,\text{snt/kWh} = 0{,}15\,\text{€/kWh}$
**Sijoitus:** $\Delta K = 0{,}15\,\tfrac{\text{€}}{\text{kWh}} \cdot \left(\dfrac{3000\,\text{kWh}}{0{,}82} - \dfrac{3000\,\text{kWh}}{0{,}92}\right) = 0{,}15\,\tfrac{\text{€}}{\text{kWh}} \cdot (3658{,}5\,\text{kWh} - 3260{,}9\,\text{kWh}) = 0{,}15\,\tfrac{\text{€}}{\text{kWh}} \cdot 397{,}7\,\text{kWh} = 59{,}7\,\text{€}$
**Vastaus:** $60\,\text{€}$, kaksi merkitsevää numeroa kuten hyötysuhteissa $82\,\%$ ja $92\,\%$.
**Järkevyys:** Hyötysuhteiden ero on kymmenen prosenttiyksikköä, joten verkosta otettu energia eroaa noin $10\text{–}12\,\%$, eli noin $400\,\text{kWh}$. $400\,\text{kWh} \cdot 0{,}15\,\text{€/kWh} = 60\,\text{€}$. Säästö on pieni verrattuna latausaseman hintaan; tärkeämpi syy latausasemaan on turvallisuus.

## fy6-16-L3-02
**Annettu:** virta kasvaa $I_1 = 10\,\text{A}$:sta $I_2 = 16\,\text{A}$:iin, kaapelin resistanssi $R$ pysyy samana
**Kysytty:** lämpenemistehon kasvu prosentteina
**Periaate:** Joulen lain mukaan kaapeliin tuleva teho on $RI^2$. Kun $R$ pysyy samana, teho on verrannollinen virran neliöön, joten tehojen suhde on virtojen suhteen neliö.
**Kaava:** $P = RI^2$, joten $\dfrac{P_2}{P_1} = \dfrac{R I_2^2}{R I_1^2} = \left(\dfrac{I_2}{I_1}\right)^2$ ja kasvu on $\dfrac{P_2}{P_1} - 1$
**Muunnokset:** Ei tarvita: ampeerit supistuvat. Kasvu muunnetaan prosenteiksi kertomalla sadalla.
**Sijoitus:** $\dfrac{P_2}{P_1} = \left(\dfrac{16\,\text{A}}{10\,\text{A}}\right)^2 = 1{,}6^2 = 2{,}56$, joten kasvu on $2{,}56 - 1 = 1{,}56 = 156\,\%$
**Vastaus:** $156\,\%$; virrat on annettu kokonaislukuina, joten tulos lasketaan tarkasti.
**Järkevyys:** Virta kasvaa $60\,\%$, mutta teho yli kaksinkertaistuu, koska virta on neliössä. Jos virta kaksinkertaistuisi, teho nelinkertaistuisi eli kasvaisi $300\,\%$; $156\,\%$ on sopivasti $60\,\%$:n ja $300\,\%$:n välissä.

## fy6-16-L3-03
**Annettu:** akkuun varastoitava energia $W_\text{akku} = 40\,\text{kWh}$, aika kello $22.00\text{–}7.00$, $\eta = 90\,\%$, kolme vaihetta, $U = 230\,\text{V}$
**Kysytty:** pienin vakiovirta $I$ yhdessä vaihejohtimessa
**Periaate:** Verkosta pitää ottaa akkuun menevä energia jaettuna hyötysuhteella, ja se pitää ottaa käytettävissä olevassa ajassa, joten teho on vähintään energia jaettuna ajalla. Kolmivaiheisen aseman teho on $P = 3UI$, kun jokaisessa vaiheessa on sama virta.
**Kaava:** $\eta \cdot 3UI \cdot t = W_\text{akku}$, joten $I = \dfrac{W_\text{akku}}{3 \eta U t}$
**Muunnokset:** $t = 7.00 - 22.00 = 9{,}0\,\text{h}$; $W_\text{akku} = 40\,\text{kWh} = 40\,000\,\text{Wh}$, jotta tulos saadaan ampeereina; $\eta = 0{,}90$
**Sijoitus:** $I = \dfrac{40\,000\,\text{Wh}}{3 \cdot 0{,}90 \cdot 230\,\text{V} \cdot 9{,}0\,\text{h}} = \dfrac{40\,000\,\text{Wh}}{5589\,\text{Vh}} = 7{,}157\,\text{A}$
**Vastaus:** $7{,}2\,\text{A}$, kaksi merkitsevää numeroa kuten energiassa $40\,\text{kWh}$ ja hyötysuhteessa $90\,\%$.
**Järkevyys:** Verkosta otetaan $40\,\text{kWh} : 0{,}90 \approx 44\,\text{kWh}$, mikä yhdeksässä tunnissa vaatii noin $4{,}9\,\text{kW}$; $4900\,\text{W} : 690\,\text{V} \approx 7\,\text{A}$. Virta on alle puolet aseman $16\,\text{A}$:stä, joten hidas yölataus jättää tilaa saunalle ja muille kuormille.
