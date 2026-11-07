## fy6-16-L1-01
**Annettu:** akun energia täyteen ladattuna $W = 64\,\text{kWh}$, varaustaso nousee $15\,\%$:sta $80\,\%$:iin
**Kysytty:** akkuun varastoitava energia $W_\text{akku}$ kilowattitunteina
**Periaate:** Varaustaso kertoo, kuinka suuri osa akun täydestä energiasta on akkuun varastoitunut. Akkuun pitää siis siirtää se osa täydestä energiasta, jonka varaustasojen erotus kertoo.
**Kaava:** $W_\text{akku} = (s_2 - s_1) W$, missä $s_1$ ja $s_2$ ovat varaustasot desimaalilukuina
**Muunnokset:** $s_1 = 15\,\% = 0{,}15$ ja $s_2 = 80\,\% = 0{,}80$
**Sijoitus:** $W_\text{akku} = (0{,}80 - 0{,}15) \cdot 64\,\text{kWh} = 0{,}65 \cdot 64\,\text{kWh} = 41{,}6\,\text{kWh}$
**Vastaus:** $42\,\text{kWh}$. Vastauksessa on kaksi merkitsevää numeroa, kuten akun energiassa $64\,\text{kWh}$.
**Järkevyys:** Kaksi kolmasosaa akusta on noin $\tfrac{2}{3} \cdot 64\,\text{kWh} \approx 43\,\text{kWh}$, ja $65\,\%$ on vähän alle kahden kolmasosan. Tulos on pienempi kuin koko akku, kuten pitää.

## fy6-16-L1-02
**Annettu:** jännite $U = 230\,\text{V}$, latausvirta $I = 8{,}0\,\text{A}$
**Kysytty:** verkosta otettu latausteho $P$ kilowatteina
**Periaate:** Pistorasia käyttää yhtä vaihetta, joten teho on jännite kertaa virta. Niin lasketaan minkä tahansa yksivaiheisen laitteen teho. Verkkojännite $230\,\text{V}$ on vaihtojännitteen tehollinen arvo. Oletetaan, että latauslaitteen tehokerroin on likimain yksi. Silloin teho lasketaan samalla tavalla kuin tasajännitteellä.
**Kaava:** $P = UI$
**Muunnokset:** Tulos watteina muunnetaan kilowateiksi: $1\,\text{W} = 0{,}001\,\text{kW}$.
**Sijoitus:** $P = 230\,\text{V} \cdot 8{,}0\,\text{A} = 1840\,\text{W} \approx 1{,}8\,\text{kW}$
**Vastaus:** $1{,}8\,\text{kW}$. Vastauksessa on kaksi merkitsevää numeroa, kuten virrassa $8{,}0\,\text{A}$.
**Järkevyys:** Teho on suunnilleen sama kuin vedenkeittimen teho, mutta lataus kestää tunteja. Lataus $40\,\text{kWh}$ kestäisi tällä teholla yli $21\,\text{h}$. Pistorasialataus sopii siis lähinnä satunnaiseen käyttöön, esimerkiksi mökille. Tavallisesta pistorasiasta ladataan enintään $8\,\text{A}$:n virralla. Pistorasian on oltava hyväkuntoinen, koska pitkään kulkeva suuri virta lämmittää liitoksia.

## fy6-16-L1-03
**Annettu:** teho $P = 11\,\text{kW}$, kolme vaihetta, vaihejännite $U = 230\,\text{V}$
**Kysytty:** yhden vaihejohtimen virta $I$ ampeereina
**Periaate:** Asema ottaa jokaisesta kolmesta vaihejohtimesta saman virran. Jokainen vaihe siirtää tehon $UI$. Kokonaisteho on siis kolme kertaa yhden vaiheen teho.
**Kaava:** $P = 3UI$, josta $I = \dfrac{P}{3U}$
**Muunnokset:** $P = 11\,\text{kW} = 11\,000\,\text{W}$
**Sijoitus:** $I = \dfrac{11\,000\,\text{W}}{3 \cdot 230\,\text{V}} = \dfrac{11\,000\,\text{W}}{690\,\text{V}} = 15{,}94\,\text{A}$
**Vastaus:** $16\,\text{A}$. Vastauksessa on kaksi merkitsevää numeroa, kuten tehossa $11\,\text{kW}$.
**Järkevyys:** Jos koko teho kulkisi yhdessä vaiheessa, virta olisi $11\,000\,\text{W} : 230\,\text{V} \approx 48\,\text{A}$. Kolmeen vaiheeseen jaettuna virta on kolmasosa siitä. Arvo $16\,\text{A}$ on tavallinen latausaseman ryhmän sulakkeen koko.

## fy6-16-L1-04
**Annettu:** verkosta otettu energia $W_\text{verkko} = 45\,\text{kWh}$, hinta $a = 14\,\text{snt/kWh}$
**Kysytty:** kustannus $K$ euroina
**Periaate:** Lataus maksetaan verkosta otetusta energiasta. Jokainen kilowattitunti maksaa saman hinnan. Kustannus on siis hinta kertaa energia.
**Kaava:** $K = a W_\text{verkko}$
**Muunnokset:** $a = 14\,\text{snt/kWh} = 14 \cdot 0{,}01\,\text{€/kWh} = 0{,}14\,\text{€/kWh}$
**Sijoitus:** $K = 0{,}14\,\text{€/kWh} \cdot 45\,\text{kWh} = 6{,}30\,\text{€}$
**Vastaus:** $6{,}3\,\text{€}$. Vastauksessa on kaksi merkitsevää numeroa, kuten energiassa $45\,\text{kWh}$ ja hinnassa $14\,\text{snt/kWh}$.
**Järkevyys:** Sentteinä $45 \cdot 14\,\text{snt} = 630\,\text{snt}$. Kymmenen sentin hinnalla kustannus olisi $4{,}50\,\text{€}$ ja viidentoista sentin hinnalla $6{,}75\,\text{€}$. Tulos on niiden välissä, lähempänä jälkimmäistä.

## fy6-16-L1-05
**Annettu:** verkosta otettu energia $W_\text{verkko} = 50\,\text{kWh}$, akkuun varastoitunut energia $W_\text{akku} = 44\,\text{kWh}$
**Kysytty:** latauksen hyötysuhde $\eta$ prosentteina
**Periaate:** Hyödyllinen energia on akkuun varastoitunut energia. Otettu energia on verkosta otettu energia. Hyötysuhde on näiden energioiden suhde.
**Kaava:** $\eta = \dfrac{W_\text{akku}}{W_\text{verkko}}$
**Muunnokset:** Ei tarvita. Kumpikin energia on kilowattitunteina, joten yksikkö supistuu. Desimaaliluku muunnetaan prosenteiksi kertomalla se sadalla.
**Sijoitus:** $\eta = \dfrac{44\,\text{kWh}}{50\,\text{kWh}} = 0{,}88 = 88\,\%$
**Vastaus:** $88\,\%$. Vastauksessa on kaksi merkitsevää numeroa, kuten energioissa $44\,\text{kWh}$ ja $50\,\text{kWh}$.
**Järkevyys:** Häviöihin meni $50\,\text{kWh} - 44\,\text{kWh} = 6\,\text{kWh}$ eli $12\,\%$ otetusta energiasta. Yhteensä $88\,\% + 12\,\% = 100\,\%$. Hyötysuhde on alle $100\,\%$, ja se on tyypillisen kotilatauksen suuruinen.

## fy6-16-L2-01
**Annettu:** kuvaajasta luetut tehot ja ajat
**Kysytty:** verkosta otettu energia $W_\text{verkko}$ kilowattitunteina
**Periaate:** Kun teho pysyy samana, energia on teho kertaa aika. Kuvaajassa on kaksi jaksoa, joissa teho on vakio. Energia on siis kahden suorakulmion pinta-alojen summa.
**Kuvaajan lukeminen:** Ensimmäisessä jaksossa teho on $P_1 = 11\,\text{kW}$ ajan $0\text{–}2{,}0\,\text{h}$, joten $t_1 = 2{,}0\,\text{h}$. Toisessa jaksossa teho on $P_2 = 5{,}5\,\text{kW}$ ajan $2{,}0\text{–}3{,}0\,\text{h}$, joten $t_2 = 1{,}0\,\text{h}$. Sen jälkeen teho on nolla.
**Kaava:** $W_\text{verkko} = P_1 t_1 + P_2 t_2$
**Muunnokset:** Ei tarvita. Kun teho on kilowatteina ja aika tunteina, energia tulee suoraan kilowattitunteina.
**Sijoitus:** $W_\text{verkko} = 11\,\text{kW} \cdot 2{,}0\,\text{h} + 5{,}5\,\text{kW} \cdot 1{,}0\,\text{h} = 22\,\text{kWh} + 5{,}5\,\text{kWh} = 27{,}5\,\text{kWh}$
**Vastaus:** $28\,\text{kWh}$. Vastauksessa on kaksi merkitsevää numeroa, kuten kuvaajasta luetuissa arvoissa.
**Järkevyys:** Jos teho olisi ollut koko kolme tuntia $11\,\text{kW}$, energiaa olisi otettu $33\,\text{kWh}$. Viimeisen tunnin puolittunut teho vähentää tästä $5{,}5\,\text{kWh}$. Siis $33\,\text{kWh} - 5{,}5\,\text{kWh} = 27{,}5\,\text{kWh}$.

## fy6-16-L2-02
**Annettu:** $U = 230\,\text{V}$, $I = 16\,\text{A}$, yksi vaihe, akun energia $60\,\text{kWh}$, varaustaso $20\,\% \to 80\,\%$, $\eta = 90\,\%$
**Kysytty:** latausaika $t$ tunteina
**Periaate:** Akkuun pitää siirtää $60\,\%$ sen energiasta. Teho pysyy samana, joten verkosta otettu energia on teho kertaa aika. Siitä akkuun varastoituu hyötysuhteen osuus. Yksivaiheisen aseman teho on jännite kertaa virta.
**Kaava:** $\eta P t = W_\text{akku}$ ja $P = UI$, joten $t = \dfrac{W_\text{akku}}{\eta U I}$
**Muunnokset:** $W_\text{akku} = (0{,}80 - 0{,}20) \cdot 60\,\text{kWh} = 36\,\text{kWh}$; $UI = 230\,\text{V} \cdot 16\,\text{A} = 3680\,\text{W} = 3{,}68\,\text{kW}$; $\eta = 0{,}90$
**Sijoitus:** $t = \dfrac{36\,\text{kWh}}{0{,}90 \cdot 3{,}68\,\text{kW}} = \dfrac{36\,\text{kWh}}{3{,}312\,\text{kW}} = 10{,}87\,\text{h}$
**Vastaus:** $11\,\text{h}$. Vastauksessa on kaksi merkitsevää numeroa, kuten hyötysuhteessa $90\,\%$.
**Järkevyys:** Arvio: akkuun menee noin $3{,}3\,\text{kW}$, ja $33\,\text{kWh}$ veisi $10\,\text{h}$. Energia $36\,\text{kWh}$ vie vähän enemmän. Kolmivaiheisella $16\,\text{A}$:n asemalla sama lataus kestäisi kolmasosan, noin $3{,}6\,\text{h}$.

## fy6-16-L2-03
**Annettu:** pääsulakkeet $3 \cdot 25\,\text{A}$, kiukaan teho $P_\text{k} = 9{,}0\,\text{kW}$ kolmessa vaiheessa, $U = 230\,\text{V}$
**Kysytty:** latausaseman suurin sallittu virta $I_\text{a}$ yhdessä vaihejohtimessa
**Periaate:** Pääsulake on jokaisessa vaihejohtimessa. Saman vaihejohtimen kautta kulkevat virrat lasketaan yhteen (luku *Kirchhoffin lait ja potentiaali virtapiirissä*). Kiuas ottaa jokaisesta vaiheesta saman virran, joten sen virta saadaan kaavasta $P = 3UI$. Autolle jää se osa, joka jää jäljelle $25\,\text{A}$:sta.
**Kaava:** $I_\text{k} + I_\text{a} = I_\text{p}$ ja $I_\text{k} = \dfrac{P_\text{k}}{3U}$, joten $I_\text{a} = I_\text{p} - \dfrac{P_\text{k}}{3U}$, missä $I_\text{p} = 25\,\text{A}$
**Muunnokset:** $P_\text{k} = 9{,}0\,\text{kW} = 9000\,\text{W}$
**Sijoitus:** $I_\text{a} = 25\,\text{A} - \dfrac{9000\,\text{W}}{3 \cdot 230\,\text{V}} = 25\,\text{A} - 13{,}04\,\text{A} = 11{,}96\,\text{A}$
**Vastaus:** $12\,\text{A}$. Vastauksessa on kaksi merkitsevää numeroa, kuten pääsulakkeen virrassa $25\,\text{A}$.
**Järkevyys:** Kiuas ja auto ottavat silloin yhdessä $13\,\text{A} + 12\,\text{A} = 25\,\text{A}$ jokaisesta vaiheesta. Auton teho on noin $3 \cdot 230\,\text{V} \cdot 12\,\text{A} \approx 8{,}3\,\text{kW}$. Se on vähemmän kuin aseman $11\,\text{kW}$. Kuormanhallinnan pitää siis pienentää latausta saunan ajaksi.

## fy6-16-L2-04
**Annettu:** kaapelin pituus $l = 30\,\text{m}$, poikkipinta-ala $A = 2{,}5\,\text{mm}^2$, virta $I = 16\,\text{A}$, $\rho = 1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m}$
**Kysytty:** kaapelissa häviävä jännite $U_\text{h}$ voltteina
**Periaate:** Kaapelin kuparijohtimet ovat vastus, jonka läpi kulkee latausvirta. Virta kulkee vaihejohdinta pitkin asemalle ja nollajohdinta pitkin takaisin, joten kuparin pituus on $2l$. Ohmin lain mukaan vastuksen jännite on resistanssi kertaa virta.
**Kaava:** $U_\text{h} = RI$ ja $R = \rho \dfrac{2l}{A}$, joten $U_\text{h} = \rho \dfrac{2l}{A} I$
**Muunnokset:** $A = 2{,}5\,\text{mm}^2 = 2{,}5 \cdot (10^{-3}\,\text{m})^2 = 2{,}5 \cdot 10^{-6}\,\text{m}^2$
**Sijoitus:** $U_\text{h} = 1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot \dfrac{2 \cdot 30\,\text{m}}{2{,}5 \cdot 10^{-6}\,\text{m}^2} \cdot 16\,\text{A} = 0{,}408\,\Omega \cdot 16\,\text{A} = 6{,}53\,\text{V}$
**Vastaus:** $6{,}5\,\text{V}$. Vastauksessa on kaksi merkitsevää numeroa, kuten resistiivisyydessä $1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m}$ ja poikkipinta-alassa $2{,}5\,\text{mm}^2$.
**Järkevyys:** Häviö on $6{,}5\,\text{V} : 230\,\text{V} \approx 3\,\%$ verkkojännitteestä, joten asema saa yhä lähes koko jännitteen. Kaapeliin tulee teho $6{,}5\,\text{V} \cdot 16\,\text{A} \approx 100\,\text{W}$ eli noin $3{,}5\,\text{W}$ metriä kohti. Teho jakautuu pitkälle matkalle.

## fy6-16-L3-01
**Annettu:** akkuun vuodessa $W_\text{akku} = 3000\,\text{kWh}$, hyötysuhteet $\eta_1 = 82\,\%$ (pistorasia) ja $\eta_2 = 92\,\%$ (latausasema), hinta $a = 15\,\text{snt/kWh}$
**Kysytty:** vuoden säästö $\Delta K$ euroina
**Periaate:** Akkuun menee kummallakin tavalla sama energia. Verkosta otetaan akkuun menevä energia jaettuna hyötysuhteella. Säästö syntyy siitä, että latausasemalla verkosta otetaan vähemmän energiaa. Energia maksetaan samalla hinnalla.
**Kaava:** $W_\text{verkko} = \dfrac{W_\text{akku}}{\eta}$ ja $K = a W_\text{verkko}$, joten $\Delta K = a \left(\dfrac{W_\text{akku}}{\eta_1} - \dfrac{W_\text{akku}}{\eta_2}\right)$
**Muunnokset:** $\eta_1 = 0{,}82$, $\eta_2 = 0{,}92$ ja $a = 15\,\text{snt/kWh} = 0{,}15\,\text{€/kWh}$
**Sijoitus:** $\Delta K = 0{,}15\,\text{€/kWh} \cdot \left(\dfrac{3000\,\text{kWh}}{0{,}82} - \dfrac{3000\,\text{kWh}}{0{,}92}\right) = 0{,}15\,\text{€/kWh} \cdot (3658{,}5\,\text{kWh} - 3260{,}9\,\text{kWh}) = 0{,}15\,\text{€/kWh} \cdot 397{,}7\,\text{kWh} = 59{,}7\,\text{€}$
**Vastaus:** $60\,\text{€}$. Vastauksessa on kaksi merkitsevää numeroa, kuten hyötysuhteissa $82\,\%$ ja $92\,\%$.
**Järkevyys:** Hyötysuhteiden ero on kymmenen prosenttiyksikköä. Verkosta otettu energia eroaa siksi noin $10\text{–}12\,\%$ vuoden kulutuksesta ($3260\,\text{kWh}$ tai $3660\,\text{kWh}$) eli noin $400\,\text{kWh}$. Silloin $400\,\text{kWh} \cdot 0{,}15\,\text{€/kWh} = 60\,\text{€}$. Säästö on pieni verrattuna latausaseman hintaan. Tärkeämpi syy latausasemaan on turvallisuus.

## fy6-16-L3-02
**Annettu:** virta kasvaa $I_1 = 10\,\text{A}$:sta $I_2 = 16\,\text{A}$:iin, kaapelin resistanssi $R$ pysyy samana
**Kysytty:** lämpenemistehon kasvu prosentteina
**Periaate:** Joulen lain mukaan kaapeliin tuleva teho on $RI^2$. Kun $R$ pysyy samana, teho on verrannollinen virran neliöön. Verrannollinen tarkoittaa, että teho muuttuu samassa suhteessa kuin virran neliö. Tehojen suhde on siis virtojen suhteen neliö.
**Kaava:** $P = RI^2$, joten $\dfrac{P_2}{P_1} = \dfrac{R I_2^2}{R I_1^2} = \left(\dfrac{I_2}{I_1}\right)^2$ ja kasvu on $\dfrac{P_2}{P_1} - 1$
**Muunnokset:** Ei tarvita. Ampeerit supistuvat. Kasvu muunnetaan prosenteiksi kertomalla se sadalla.
**Sijoitus:** $\dfrac{P_2}{P_1} = \left(\dfrac{16\,\text{A}}{10\,\text{A}}\right)^2 = 1{,}6^2 = 2{,}56$, joten kasvu on $2{,}56 - 1 = 1{,}56 = 156\,\%$
**Vastaus:** $156\,\%$. Virrat $10\,\text{A}$ ja $16\,\text{A}$ ovat latauslaitteen tarkat asetukset, joten $156\,\%$ annetaan sellaisena kuin se laskettiin.
**Järkevyys:** Virta kasvaa $60\,\%$, mutta teho yli kaksinkertaistuu, koska virta on neliössä. Jos virta kaksinkertaistuisi, teho nelinkertaistuisi eli kasvaisi $300\,\%$. Tulos $156\,\%$ on sopivasti $60\,\%$:n ja $300\,\%$:n välissä.

## fy6-16-L3-03
**Annettu:** akkuun varastoitava energia $W_\text{akku} = 40\,\text{kWh}$, aika kello $22.00\text{–}7.00$, $\eta = 90\,\%$, kolme vaihetta, $U = 230\,\text{V}$
**Kysytty:** pienin vakiovirta $I$ yhdessä vaihejohtimessa
**Periaate:** Verkosta pitää ottaa akkuun menevä energia jaettuna hyötysuhteella. Energia pitää ottaa käytettävissä olevassa ajassa. Teho on siis vähintään energia jaettuna ajalla. Kolmivaiheisen aseman teho on $P = 3UI$, kun jokaisessa vaiheessa on sama virta.
**Kaava:** $\eta \cdot 3UI \cdot t = W_\text{akku}$, joten $I = \dfrac{W_\text{akku}}{3 \eta U t}$
**Muunnokset:** $t = 7.00 - 22.00 = 9{,}0\,\text{h}$; $W_\text{akku} = 40\,\text{kWh} = 40\,000\,\text{Wh}$, jotta tulos saadaan ampeereina; $\eta = 0{,}90$
**Sijoitus:** $I = \dfrac{40\,000\,\text{Wh}}{3 \cdot 0{,}90 \cdot 230\,\text{V} \cdot 9{,}0\,\text{h}} = \dfrac{40\,000\,\text{Wh}}{5589\,\text{Vh}} = 7{,}157\,\text{A}$
**Vastaus:** $7{,}2\,\text{A}$. Vastauksessa on kaksi merkitsevää numeroa, kuten energiassa $40\,\text{kWh}$ ja hyötysuhteessa $90\,\%$.
**Järkevyys:** Verkosta otetaan $40\,\text{kWh} : 0{,}90 \approx 44\,\text{kWh}$. Yhdeksässä tunnissa se vaatii noin $4{,}9\,\text{kW}$, ja $4900\,\text{W} : 690\,\text{V} \approx 7\,\text{A}$. Virta on alle puolet aseman $16\,\text{A}$:stä. Hidas yölataus jättää siis tilaa saunalle ja muille kuormille.

## fy6-16-L1-06
**Kysytty:** mitä aseman kilowattiluku ja akun kilowattituntiluku kertovat.
**Periaate:** Teho kertoo, kuinka nopeasti energiaa siirtyy. Tehon yksikkö on kilowatti. Energia saadaan, kun teho kerrotaan ajalla, $W = Pt$. Siksi energian yksikkö on kilowatti kertaa tunti eli kilowattitunti. Latausnopeus on siis tehoa, ja akun koko on energiaa.
**Mallivastaus:** Aseman kilowattiluku kertoo latausnopeuden eli tehon. Akun kilowattituntiluku kertoo, kuinka paljon energiaa akkuun mahtuu. Väite, jonka mukaan luvut ovat toisinpäin, on väärä. Kilowattitunti on energian yksikkö, eikä nopeutta voi mitata sillä. Väite, jonka mukaan yksiköt ovat sama asia, on väärä. Kilowattitunti saadaan, kun kilowatti kerrotaan ajalla. Väite, jonka mukaan kilowatti on jännite ja kilowattitunti virta, on väärä. Jännite mitataan voltteina ja virta ampeereina. Esimerkiksi $11\,\text{kW}$:n asema siirtää tunnissa $11\,\text{kWh}$.

## fy6-16-L1-07
**Annettu:** teho $P = 7{,}4\,\text{kW}$, latausaika $t = 5{,}5\,\text{h}$
**Kysytty:** verkosta otettu energia $W_\text{verkko}$ kilowattitunteina
**Periaate:** Teho on vakio, joten energia on teho kertaa aika (luku *Sähköenergia kotona*). Tehtävässä lasketaan verkosta otettu energia. Hyötysuhdetta ei siis tarvita.
**Kaava:** $W_\text{verkko} = Pt$
**Muunnokset:** Ei tarvita. Kun kilowatit kerrotaan tunneilla, tulos on suoraan kilowattitunteina.
**Sijoitus:** $W_\text{verkko} = 7{,}4\,\text{kW} \cdot 5{,}5\,\text{h} = 40{,}7\,\text{kWh}$
**Vastaus:** $41\,\text{kWh}$. Vastauksessa on kaksi merkitsevää numeroa, kuten tehossa $7{,}4\,\text{kW}$ ja ajassa $5{,}5\,\text{h}$.
**Järkevyys:** Arvio: teho $7\,\text{kW}$ kuuden tunnin ajan on $42\,\text{kWh}$. Tulos on vähän pienempi, koska teho ja aika ovat vähän pienemmät. Tulos on suunnilleen yhtä suuri kuin tavallisen sähköauton akun energia.

## fy6-16-L1-08
**Annettu:** resistanssi $R = 0{,}25\,\Omega$, virta $I = 16\,\text{A}$
**Kysytty:** kaapelin lämpenemisteho $P$ watteina
**Periaate:** Kun virta kulkee resistanssin läpi, sähköenergiaa muuttuu sisäenergiaksi. Teho saadaan Joulen laista. Teho riippuu virran neliöstä ja resistanssista.
**Kaava:** $P = RI^2$
**Muunnokset:** Ei tarvita. Kun ohmit ja ampeerit sijoitetaan kaavaan, tulos on suoraan watteina.
**Sijoitus:** $P = 0{,}25\,\Omega \cdot (16\,\text{A})^2 = 0{,}25\,\Omega \cdot 256\,\text{A}^2 = 64\,\text{W}$
**Vastaus:** $64\,\text{W}$. Vastauksessa on kaksi merkitsevää numeroa, kuten resistanssissa $0{,}25\,\Omega$.
**Järkevyys:** Jännitehäviö on $RI = 0{,}25\,\Omega \cdot 16\,\text{A} = 4{,}0\,\text{V}$. Teho on jännitehäviö kertaa virta, $4{,}0\,\text{V} \cdot 16\,\text{A} = 64\,\text{W}$. Tulos on pieni aseman tehoon verrattuna. Kaapelin lämmittämiseen se kuitenkin riittää.

## fy6-16-L2-05
**Annettu:** talon teho tunneittain taulukosta, pääsulakkeet $3 \cdot 25\,\text{A}$, $U = 230\,\text{V}$, kolmivaiheinen asema
**Kysytty:** a) huipputeho ja sen aika, b) aseman suurin latausteho $P_\text{a}$ huipun aikana kilowatteina, c) milloin $11\,\text{kW}$ sallitaan
**Periaate:** Pääsulake rajoittaa jokaisen vaihejohtimen virtaa. Kuormat jakautuvat tasan vaiheille, joten koko talon teho voi olla enintään $3UI_\text{p}$. Talon ja aseman tehot lasketaan yhteen. Asemalle jää se teho, jota talo ei käytä.
**Kuvaajan lukeminen:** Taulukossa suurin teho on $6{,}8\,\text{kW}$ kello $19\text{–}20$.
**Kaava:** $P_\text{max} = 3UI_\text{p}$ ja $P_\text{talo} + P_\text{a} \le P_\text{max}$, joten $P_\text{a} = 3UI_\text{p} - P_\text{talo}$, missä $I_\text{p} = 25\,\text{A}$
**Muunnokset:** $3UI_\text{p}$ lasketaan watteina ja muunnetaan kilowateiksi: $17\,250\,\text{W} = 17{,}25\,\text{kW}$.
**Sijoitus:** $P_\text{max} = 3 \cdot 230\,\text{V} \cdot 25\,\text{A} = 17\,250\,\text{W} = 17{,}25\,\text{kW}$, joten $P_\text{a} = 17{,}25\,\text{kW} - 6{,}8\,\text{kW} = 10{,}45\,\text{kW}$
**Vastaus:** Vastauslaatikkoon $10{,}5\,\text{kW}$. Vastauksessa on yksi desimaali, kuten taulukon tehoissa. a) Huipputeho on kello $19\text{–}20$.

b) Aseman teho saa olla huipun aikana enintään $10{,}5\,\text{kW}$.

c) Asema saa käyttää täyttä tehoa $11\,\text{kW}$, kun talon teho on enintään $17{,}25\,\text{kW} - 11\,\text{kW} = 6{,}25\,\text{kW}$. Taulukossa vain kello $19\text{–}20$ ylittää tämän ($6{,}8\,\text{kW}$). Muina tunteina kuormanhallintaa ei tarvita, kun oletetaan, että talon teho pysyy tunnin ajan taulukon arvossa. Kello $19\text{–}20$ asemaa pitää rajoittaa. Oikeassa elämässä tunnin sisällä voi olla lyhyitä huippuja, ja silloin kuormanhallintaa voidaan tarvita.
**Järkevyys:** Virta huipun aikana jokaisessa vaiheessa: talo $6800\,\text{W} : 690\,\text{V} \approx 9{,}9\,\text{A}$ ja asema $10\,450\,\text{W} : 690\,\text{V} \approx 15{,}1\,\text{A}$. Yhteensä virta on $25{,}0\,\text{A}$ eli täsmälleen pääsulakkeen raja. Tulos on pienempi kuin aseman $11\,\text{kW}$, kuten huipun aikana pitääkin.

## fy6-16-L2-06
**Annettu:** akun energia $60\,\text{kWh}$, varaustaso $20\,\% \to 80\,\%$, verkosta otettu teho $P = 7{,}4\,\text{kW}$, $\eta = 92\,\%$
**Kysytty:** a) kaksi virhettä opiskelijan ratkaisussa, b) oikea latausaika $t$ tunteina
**Periaate:** Latauksessa akkuun siirretään vain se osa akun energiasta, jonka varaustasojen erotus kertoo. Koko akkua ei ladata. Verkosta otetusta energiasta vain hyötysuhteen osuus varastoituu akkuun. Latausaika lasketaan siis jakamalla akkuun menevä energia hyötysuhteen ja tehon tulolla.
**Kaava:** $\eta P t = W_\text{akku}$, joten $t = \dfrac{W_\text{akku}}{\eta P}$
**Muunnokset:** $W_\text{akku} = (0{,}80 - 0{,}20) \cdot 60\,\text{kWh} = 36\,\text{kWh}$ ja $\eta = 0{,}92$
**Sijoitus:** $t = \dfrac{36\,\text{kWh}}{0{,}92 \cdot 7{,}4\,\text{kW}} = \dfrac{36\,\text{kWh}}{6{,}808\,\text{kW}} = 5{,}288\,\text{h}$
**Vastaus:** Vastauslaatikkoon $5{,}3\,\text{h}$. Vastauksessa on kaksi merkitsevää numeroa, kuten hyötysuhteessa $92\,\%$. a) Ensimmäinen virhe: opiskelija käyttää koko akun energiaa $60\,\text{kWh}$. Akkuun siirretään kuitenkin vain $60\,\%$ siitä eli $36\,\text{kWh}$.

Toinen virhe: opiskelija ei ota huomioon hyötysuhdetta. Hän jakaa pelkällä teholla eikä tulolla $\eta P$.

b) Oikea latausaika on $5{,}3\,\text{h}$.
**Järkevyys:** Jos vain hyötysuhde unohdetaan, tulos on $36\,\text{kWh} : 7{,}4\,\text{kW} \approx 4{,}9\,\text{h}$. Hyötysuhde pidentää aikaa tästä, kuten pitääkin. Opiskelijan $8{,}1\,\text{h}$ on liian pitkä, koska se kuvaa koko akun täyttöä tyhjästä täyteen.

## fy6-16-L2-07
**Annettu:** verkosta otettu teho $P$ ajan $t$ funktiona taulukosta, mittausväli $0{,}5\,\text{h}$, $t = 0\text{–}3{,}0\,\text{h}$
**Kysytty:** a) verkosta otettu energia $W_\text{verkko}$ kilowattitunteina, b) keskiteho $P_\text{ka}$ kilowatteina
**Periaate:** Teho muuttuu ajan mukana, joten energia ei ole teho kertaa aika. Energia on $(t, P)$-kuvaajan alle jäävä pinta-ala. Se saadaan laskemalla yhteen puolen tunnin mittaisten puolisuunnikkaiden pinta-alat. Keskiteho on energia jaettuna kokonaisajalla.
**Kuvaajan lukeminen:** Pisteet yhdistetään suorilla. Jokaisen puolen tunnin välin pinta-ala on välin päätepisteiden tehojen keskiarvo kertaa $\Delta t = 0{,}5\,\text{h}$. Ensimmäinen ja viimeinen teho ovat $11{,}0\,\text{kW}$ ja $1{,}4\,\text{kW}$. Välissä ovat $11{,}0$, $10{,}8$, $8{,}7$, $5{,}9$ ja $3{,}1\,\text{kW}$.
**Kaava:** väli kerrallaan $W_i = \Delta t \cdot \dfrac{P_i + P_{i+1}}{2}$, kaikkien välien summa $W_\text{verkko} = \sum W_i$, ja $P_\text{ka} = \dfrac{W_\text{verkko}}{t}$
**Muunnokset:** Ei tarvita. Kun kilowatit kerrotaan tunneilla, tulos on kilowattitunteina.
**Sijoitus:** Välitehojen summa on $11{,}0 + 10{,}8 + 8{,}7 + 5{,}9 + 3{,}1 = 39{,}5\,\text{kW}$. Päätepisteiden keskiarvo on $(11{,}0 + 1{,}4) : 2 = 6{,}2\,\text{kW}$. Siis $W_\text{verkko} = 0{,}5\,\text{h} \cdot (6{,}2\,\text{kW} + 39{,}5\,\text{kW}) = 22{,}85\,\text{kWh}$ ja $P_\text{ka} = \dfrac{22{,}85\,\text{kWh}}{3{,}0\,\text{h}} = 7{,}617\,\text{kW}$
**Vastaus:** Vastauslaatikkoon $23\,\text{kWh}$. Vastauksessa on kaksi merkitsevää numeroa, kuten tehoissa. a) Verkosta otettu energia on $23\,\text{kWh}$.

b) Keskiteho on $7{,}6\,\text{kW}$.
**Järkevyys:** Jos teho olisi pysynyt koko ajan arvossa $11\,\text{kW}$, energiaa olisi otettu $3{,}0\,\text{h}$ aikana $33\,\text{kWh}$. Tulos on pienempi, koska teho laskee latauksen loppua kohti. Keskiteho $7{,}6\,\text{kW}$ on huipputehon $11\,\text{kW}$ ja loppuarvon $1{,}4\,\text{kW}$ välissä.

## fy6-16-L2-08
**Kysytty:** latausaika $t$, kun akkuun varastoidaan $24\,\text{kWh}$ pistorasiasta virralla $8{,}0\,\text{A}$.
**Periaate:** Yksivaiheisen latauksen teho on $P = UI$. Häviöiden vuoksi verkosta otetaan enemmän energiaa kuin akkuun varastoituu. Siksi akkuun menevä energia jaetaan hyötysuhteella, ja latausaika on $t = W_\text{akku} : (\eta P)$. Energia ja teho sijoitetaan samassa kerrannaisyksikössä, kilowattitunteina ja kilowatteina. Silloin aika saadaan tunteina. Hyötysuhde sijoitetaan desimaalilukuna.
**Mallivastaus:** Latausteho on

$P = UI = 230\,\text{V} \cdot 8{,}0\,\text{A}$

$P = 1840\,\text{W} = 1{,}84\,\text{kW}$

ja hyötysuhde on $\eta = 85\,\% = 0{,}85$. Latausaika on

$$\begin{aligned}
t &= \frac{W_\text{akku}}{\eta P} \\
&= \frac{24\,\text{kWh}}{0{,}85 \cdot 1{,}84\,\text{kW}} \\
&\approx 15\,\text{h}
\end{aligned}$$

Oikea vaihtoehto on noin $15\,\text{h}$.

Tulos on järkevä: verkosta otetaan noin $1{,}8\,\text{kWh}$ tunnissa, ja akkuun siitä menee noin $1{,}6\,\text{kWh}$. Siksi $24\,\text{kWh}$ vie noin $15$ tuntia. Lataus ei mahdu yhteen yöhön, mutta vuorokaudessa se ehtii.

Muut vaihtoehdot syntyvät tyypillisistä virheistä. Ilman hyötysuhdetta saadaan häviöttömän latauksen aika:

$t = 24\,\text{kWh} : 1{,}84\,\text{kW} \approx 13\,\text{h}$

Kun energia kerrotaan hyötysuhteella eikä jaeta sillä, aika lyhenee entisestään:

$t = 0{,}85 \cdot 24\,\text{kWh} : 1{,}84\,\text{kW}$

eli $t \approx 11\,\text{h}$. Häviöt pidentävät latausta, joten kumpikin on liian lyhyt. Kolmivaiheisen laitteen kaava $P = 3UI$ antaa kolme kertaa liian suuren tehon, vaikka pistorasia on yksivaiheinen. Silloin aika jää noin arvoon $5{,}1\,\text{h}$.

## fy6-16-L3-04
**Annettu:** kuukausimatkat taulukosta, sähköauto $16{,}0\,\text{kWh}$ akusta sadalla kilometrillä, $\eta = 90{,}0\,\%$, $a_\text{koti} = 15\,\text{snt/kWh}$, $a_\text{julk} = 0{,}45\,\text{€/kWh}$, bensiiniauto $6{,}50\,\textsf{l}$ sadalla kilometrillä, bensiinin hinta $b = 1{,}85\,\text{€/}\textsf{l}$
**Kysytty:** b) bensiiniauton ja sähköauton kotilatauksen vuosikustannusten erotus $\Delta K$ euroina
**Periaate:** Vuosikustannus on kulutettu määrä kertaa hinta. Sähköautolla maksetaan verkosta otetusta energiasta. Siksi akusta kulutettu energia jaetaan hyötysuhteella. Bensiiniautolla maksetaan ostetuista litroista. Kulutus on molemmilla suoraan verrannollinen ajettuun matkaan. Siksi $100\,\text{km}$:n kulutus kerrotaan luvulla $s : 100\,\text{km}$.
**Kaava:** $W_\text{verkko} = \dfrac{s}{100\,\text{km}} \cdot \dfrac{w}{\eta}$, $K_\text{s} = a W_\text{verkko}$, $K_\text{b} = \dfrac{s}{100\,\text{km}} \cdot v b$ ja $\Delta K = K_\text{b} - K_\text{s}$, missä $w = 16{,}0\,\text{kWh}$ ja $v = 6{,}50\,\textsf{l}$
**Muunnokset:** $a_\text{koti} = 15\,\text{snt/kWh} = 0{,}15\,\text{€/kWh}$ ja $\eta = 0{,}900$
**Sijoitus:** Kuukausimatkojen summa on $s = 14\,640\,\text{km}$, joten $s : 100\,\text{km} = 146{,}4$. Sähköauto: $W_\text{verkko} = 146{,}4 \cdot 16{,}0\,\text{kWh} : 0{,}900 = 2602{,}7\,\text{kWh}$ ja $K_\text{s} = 0{,}15\,\text{€/kWh} \cdot 2602{,}7\,\text{kWh} = 390{,}4\,\text{€}$. Bensiiniauto: $K_\text{b} = 146{,}4 \cdot 6{,}50\,\textsf{l} \cdot 1{,}85\,\text{€/}\textsf{l} = 1760{,}5\,\text{€}$. Erotus on $\Delta K = 1760{,}5\,\text{€} - 390{,}4\,\text{€} = 1370{,}1\,\text{€}$.
**Vastaus:** Vastauslaatikkoon $1370\,\text{€}$ eli pyöristettynä kymmeneen euroon. Sähkön kustannus $390\,\text{€}$ on annettu kahdella merkitsevällä numerolla. a) Vuosittainen ajomatka on $14\,640\,\text{km}$.

b) Bensiiniauto maksaa vuodessa noin $1370\,\text{€}$ enemmän.

c) Julkisella latauksella $K_\text{s} = 0{,}45\,\text{€/kWh} \cdot 2602{,}7\,\text{kWh} = 1171{,}2\,\text{€}$. Se on edelleen pienempi kuin bensiiniauton $1760{,}5\,\text{€}$. Säästö pienenee arvoon $1760{,}5\,\text{€} - 1171{,}2\,\text{€} = 589{,}3\,\text{€}$ eli noin $780\,\text{€}$ pienemmäksi. Sähköauto on silti edullisempi, koska sen energiankulutus on pieni. Sen kustannus on noin kaksi kolmasosaa bensiiniauton kustannuksesta.
**Järkevyys:** Arvio: $15\,000\,\text{km}$ on $150$ kertaa $100\,\text{km}$. Sähköauto maksaa noin $150 \cdot 2{,}7\,\text{€} \approx 400\,\text{€}$ ($100\,\text{km}$ maksaa $17{,}8\,\text{kWh} \cdot 0{,}15\,\text{€/kWh} \approx 2{,}7\,\text{€}$). Bensiiniauto maksaa $150 \cdot 12\,\text{€} = 1800\,\text{€}$ ($100\,\text{km}$ maksaa $6{,}5\,\textsf{l} \cdot 1{,}85\,\text{€/}\textsf{l} \approx 12\,\text{€}$). Erotus on siis noin $1400\,\text{€}$. Verkosta otettu energia $17{,}8\,\text{kWh}$ sadalla kilometrillä on suurempi kuin akusta kulutettu $16{,}0\,\text{kWh}$. Niin pitääkin olla, koska latauksessa on häviöitä.

## fy6-16-L3-05
**Annettu:** pääsulakkeet $3 \cdot 25\,\text{A}$, $U = 230\,\text{V}$, kuormat $6{,}0\,\text{kW}$, $3{,}3\,\text{kW}$, $1{,}8\,\text{kW}$ ja $0{,}90\,\text{kW}$ jaettuna tasan kolmelle vaiheelle, kaapeli $l = 30\,\text{m}$, $A = 2{,}5\,\text{mm}^2$, $\rho = 1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m}$
**Kysytty:** b) suurin latausvirta $I_\text{a}$ ampeereina ja c) kaapelin lämpenemisteho $P_\text{johto}$ kahdella virralla
**Periaate:** Saman vaihejohtimen kautta kulkevat virrat lasketaan yhteen. Summa saa olla enintään pääsulakkeen virta. Talon kuormat jakautuvat tasan vaiheille, joten talon virta yhdessä vaiheessa saadaan kolmivaiheisen tehon kaavasta. Yksivaiheinen asema kuormittaa vain yhtä vaihetta. Sille jää se virta, joka sillä vaiheella on jäljellä. Kaapelin kuparijohtimet ovat vastus. Sen lämpenemisteho on Joulen lain mukaan $RI^2$.
**Kaava:** $P_\text{talo} = 3UI_\text{talo}$, joten $I_\text{talo} = \dfrac{P_\text{talo}}{3U}$; $I_\text{talo} + I_\text{a} \le I_\text{p}$, joten $I_\text{a} = I_\text{p} - I_\text{talo}$; $P_\text{johto} = \rho \dfrac{2l}{A} I^2$
**Muunnokset:** $P_\text{talo} = 6{,}0\,\text{kW} + 3{,}3\,\text{kW} + 1{,}8\,\text{kW} + 0{,}90\,\text{kW} = 12{,}0\,\text{kW} = 12\,000\,\text{W}$ ja $A = 2{,}5\,\text{mm}^2 = 2{,}5 \cdot 10^{-6}\,\text{m}^2$
**Sijoitus:** $I_\text{talo} = \dfrac{12\,000\,\text{W}}{3 \cdot 230\,\text{V}} = 17{,}39\,\text{A}$ ja $I_\text{a} = 25\,\text{A} - 17{,}39\,\text{A} = 7{,}609\,\text{A}$. Kaapelin resistanssi on $R = 1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot \dfrac{2 \cdot 30\,\text{m}}{2{,}5 \cdot 10^{-6}\,\text{m}^2} = 0{,}408\,\Omega$. Siis $P_\text{johto} = 0{,}408\,\Omega \cdot (7{,}609\,\text{A})^2 = 23{,}6\,\text{W}$ ja virralla $16\,\text{A}$ $P_\text{johto} = 0{,}408\,\Omega \cdot (16\,\text{A})^2 = 104{,}4\,\text{W}$.
**Vastaus:** Vastauslaatikkoon $7{,}6\,\text{A}$. Vastauksessa on kaksi merkitsevää numeroa, kuten kuormien tehoissa. a) Talon virta on $17\,\text{A}$ jokaisessa vaihejohtimessa.

b) Asema saa ottaa enintään $7{,}6\,\text{A}$.

c) Kaapelin lämpenemisteho on $24\,\text{W}$ virralla $7{,}6\,\text{A}$ ja $104\,\text{W}$ virralla $16\,\text{A}$. Virta kasvaa kertoimella $16 : 7{,}609 \approx 2{,}1$. Teho kasvaa kertoimen neliön verran eli noin $4{,}4$-kertaiseksi. Illalla pääsulake on jo lähes täynnä. Virta $16\,\text{A}$ ylittäisi sen ($17{,}4\,\text{A} + 16\,\text{A} = 33{,}4\,\text{A}$). Kuormanhallinnan pitää siis rajoittaa latausvirta ruuhka-ajaksi. Pienempi virta pitää myös kaapelin viileämpänä.
**Järkevyys:** Talon virta ja aseman virta ovat yhteensä $17{,}39\,\text{A} + 7{,}609\,\text{A} = 25{,}0\,\text{A}$ eli täsmälleen pääsulakkeen raja. Aseman teho olisi vain $230\,\text{V} \cdot 7{,}609\,\text{A} \approx 1{,}75\,\text{kW}$. Hidas lataus on siis järkevä ruuhka-aikaan. Yöllä kiuas ja liesi ovat pois päältä, ja silloin virtaa voi taas lisätä.
