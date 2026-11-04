## fy6-15-L1-01
**Annettu:** teho $P = 1500\,\text{W}$, jännite $U = 230\,\text{V}$
**Kysytty:** virta $I$ ampeereina
**Periaate:** Sähköteho on jännite kertaa virta. Verkkojännite $230\,\text{V}$ on vaihtojännitteen tehollinen arvo eli arvo, jolla vaihtojännite lämmittää yhtä paljon kuin tasajännite. Siksi lämmittävän laitteen teho lasketaan sillä samoin kuin tasajännitteellä.
**Kaava:** $P = UI$, josta $I = \dfrac{P}{U}$
**Muunnokset:** Ei tarvita: $1\,\text{W} : 1\,\text{V} = 1\,\text{A}$.
**Sijoitus:** $I = \dfrac{1500\,\text{W}}{230\,\text{V}} = 6{,}522\,\text{A}$
**Vastaus:** $6{,}5\,\text{A}$, kaksi merkitsevää numeroa kuten tehossa $1500\,\text{W}$.
**Järkevyys:** Arvio $1500\,\text{W} : 200\,\text{V} = 7{,}5\,\text{A}$ on hieman suurempi, koska jakaja on pienempi. Virta on alle $10\,\text{A}$, joten puhallin mahtuu yksin $10\,\text{A}$:n ryhmään, mutta samaan ryhmään ei mahdu enää paljon muuta.

## fy6-15-L1-02
**Annettu:** sulakkeen nimellisvirta $I_\text{s} = 10\,\text{A}$, jännite $U = 230\,\text{V}$
**Kysytty:** suurin yhteisteho $P_\text{max}$ watteina
**Periaate:** Ryhmän laitteet ovat rinnan samassa jännitteessä. Siksi niiden virrat lasketaan yhteen, ja ryhmäjohdon virta on yhteisteho jaettuna jännitteellä. Nimellisvirta eli suurin sallittu virta ei ylity, kun tämä virta on enintään $I_\text{s}$.
**Kaava:** $I = \dfrac{P_1 + P_2 + \dots}{U} \le I_\text{s}$, josta $P_\text{max} = UI_\text{s}$
**Muunnokset:** Ei tarvita: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Sijoitus:** $P_\text{max} = 230\,\text{V} \cdot 10\,\text{A} = 2300\,\text{W}$
**Vastaus:** $2300\,\text{W}$ eli $2{,}3\,\text{kW}$, kaksi merkitsevää numeroa kuten nimellisvirrassa $10\,\text{A}$.
**Järkevyys:** Yksi $2000\,\text{W}$:n vedenkeitin mahtuu ryhmään, mutta keitin ja $900\,\text{W}$:n leivänpaahdin yhdessä eivät mahdu. Tämä sopii arjen kokemukseen: vanhan keittiön sulake laukeaa, kun liian monta lämmittävää laitetta on päällä yhtä aikaa.

## fy6-15-L1-03
**Annettu:** kosketusjännite $U = 230\,\text{V}$, virtatien resistanssi $R = 2{,}3\,\text{k}\Omega$
**Kysytty:** kehon läpi kulkeva virta $I$ milliampeereina
**Periaate:** Keho on osa virtapiiriä kosketuskohdan ja maan välillä. Sen läpi kulkeva virta saadaan siksi Ohmin laista, kun käytetään koko virtatien resistanssia.
**Kaava:** $U = RI$, josta $I = \dfrac{U}{R}$
**Muunnokset:** $R = 2{,}3\,\text{k}\Omega = 2{,}3 \cdot 1000\,\Omega = 2300\,\Omega$; tulos ampeereista milliampeereiksi: $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $I = \dfrac{230\,\text{V}}{2300\,\Omega} = 0{,}100\,\text{A} = 100\,\text{mA}$
**Vastaus:** $100\,\text{mA}$, kaksi merkitsevää numeroa kuten resistanssissa $2{,}3\,\text{k}\Omega$.
**Järkevyys:** Resistanssin $2300\,\Omega$ lukuarvo on kymmenkertainen jännitteen $230\,\text{V}$ lukuarvoon verrattuna. Siksi virran lukuarvo ampeereina on kymmenesosa eli noin $0{,}1\,\text{A}$. Virta on kaksinkertainen kammiovärinän vaaran rajaan noin $50\,\text{mA}$ verrattuna. Märin käsin kosketus on siis hengenvaarallinen.

## fy6-15-L1-04
**Annettu:** kosketusjännite $U = 230\,\text{V}$, virtatien resistanssi $R = 50\,\text{k}\Omega$
**Kysytty:** kehon läpi kulkeva virta $I$ milliampeereina
**Periaate:** Keho, kengät ja lattia ovat samassa virtatiessä, ja niiden yhteinen resistanssi on annettu. Virta saadaan siksi suoraan Ohmin laista.
**Kaava:** $U = RI$, josta $I = \dfrac{U}{R}$
**Muunnokset:** $R = 50\,\text{k}\Omega = 50 \cdot 1000\,\Omega = 50\,000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $I = \dfrac{230\,\text{V}}{50\,000\,\Omega} = 0{,}0046\,\text{A} = 4{,}6\,\text{mA}$
**Vastaus:** $4{,}6\,\text{mA}$, kaksi merkitsevää numeroa kuten resistanssissa $50\,\text{k}\Omega$.
**Järkevyys:** Virta tuntuu selvästi, koska se on lähes kymmenkertainen tuntokynnykseen $0{,}5\,\text{mA}$ verrattuna. Se jää kuitenkin alle irrottamiskynnyksen $10\,\text{mA}$. Märin käsin resistanssi voi olla kymmenesosa tai vähemmän, ja silloin virta on kymmenkertainen. Tulos pätee vain ehjillä, kuivilla kengillä ja kuivalla lattialla. Lisäksi ihminen ei saa koskea samalla mihinkään maadoitettuun, kuten hanaan. Muuten virta kulkee kenkien ohi. Kenkiä ei pidä pitää suojana.

## fy6-15-L1-05
**Annettu:** johtimien resistanssi $R = 0{,}20\,\Omega$, virta $I = 16\,\text{A}$
**Kysytty:** jatkojohdossa kehittyvä lämpöteho $P$
**Periaate:** Johtimen resistanssissa sähköenergia muuttuu johtimen sisäenergiaksi, joka siirtyy lämpönä ympäristöön. Kun johtimen resistanssi ja virta tunnetaan, teho saadaan Joulen laista.
**Kaava:** $P = RI^2$
**Muunnokset:** Ei tarvita: $1\,\Omega \cdot (1\,\text{A})^2 = 1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Sijoitus:** $P = 0{,}20\,\Omega \cdot (16\,\text{A})^2 = 0{,}20\,\Omega \cdot 256\,\text{A}^2 = 51{,}2\,\text{W}$
**Vastaus:** $51\,\text{W}$, kaksi merkitsevää numeroa kuten resistanssissa ja virrassa.
**Järkevyys:** Teho on kuin pienen hehkulampun. Se jakautuu koko johdon pituudelle, joten ehjä johto lämpenee vain vähän. Jos johto on kelalla tiukasti rullattuna, lämpö ei pääse pois, ja johto voi kuumeta vaarallisesti.

## fy6-15-L2-01
**Annettu:** nimellisvirta $I_\text{s} = 16\,\text{A}$, jännite $U = 230\,\text{V}$, päällä olevat tehot $P_1 = 2000\,\text{W}$ ja $P_2 = 1200\,\text{W}$
**Kysytty:** teho $P_\text{lisä}$, jonka ryhmään voi vielä kytkeä
**Periaate:** Ryhmän laitteet ovat rinnan, joten virrat lasketaan yhteen. Kokonaisvirta on yhteisteho jaettuna jännitteellä. Nimellisvirta ei ylity, kun yhteisteho on enintään $UI_\text{s}$. Lisätehoksi jää tämän ja käytössä olevan tehon erotus.
**Kaava:** $\dfrac{P_1 + P_2 + P_\text{lisä}}{U} = I_\text{s}$, josta $P_\text{lisä} = UI_\text{s} - (P_1 + P_2)$
**Muunnokset:** Ei tarvita: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Sijoitus:** $P_\text{lisä} = 230\,\text{V} \cdot 16\,\text{A} - (2000\,\text{W} + 1200\,\text{W}) = 3680\,\text{W} - 3200\,\text{W} = 480\,\text{W}$
**Vastaus:** noin $480\,\text{W}$. Erotus on laskettu suurista luvuista, joten se on vain suuntaa antava. Nimellisvirta $16\,\text{A}$ on annettu kahden merkitsevän numeron tarkkuudella.
**Järkevyys:** Tarkista virtoina. Keitin ottaa $8{,}7\,\text{A}$ ja mikroaaltouuni $5{,}2\,\text{A}$, yhteensä $13{,}9\,\text{A}$. Jäljellä on siis noin $2{,}1\,\text{A}$ eli $230\,\text{V} \cdot 2{,}1\,\text{A} \approx 480\,\text{W}$. Leivänpaahdin ($900\,\text{W}$) ei mahdu, mutta jääkaappi mahtuu.

## fy6-15-L2-02
**Annettu:** patterin teho $P = 2000\,\text{W}$, jännite $U = 230\,\text{V}$, johtimien resistanssi $R = 0{,}30\,\Omega$
**Kysytty:** jatkojohdossa kehittyvä lämpöteho $P_\text{j}$
**Periaate:** Jatkojohto on sarjassa patterin kanssa, joten sen läpi kulkee patterin virta. Virta saadaan patterin tehosta. Johdossa sähköenergia muuttuu sisäenergiaksi teholla $RI^2$. Oletus: johdon jännitehäviö on niin pieni, että patterin virta on sama kuin ilman jatkojohtoa.
**Kaava:** $P = UI$, josta $I = \dfrac{P}{U}$; johdossa $P_\text{j} = RI^2$, joten $P_\text{j} = R\left(\dfrac{P}{U}\right)^2$
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä.
**Sijoitus:** $I = \dfrac{2000\,\text{W}}{230\,\text{V}} = 8{,}696\,\text{A}$ ja $P_\text{j} = 0{,}30\,\Omega \cdot (8{,}696\,\text{A})^2 = 22{,}68\,\text{W}$
**Vastaus:** $23\,\text{W}$, kaksi merkitsevää numeroa kuten resistanssissa $0{,}30\,\Omega$.
**Järkevyys:** Johdon jännite on $RI = 0{,}30\,\Omega \cdot 8{,}7\,\text{A} \approx 2{,}6\,\text{V}$. Se on hyvin pieni verrattuna $230\,\text{V}$:iin, joten oletus pitää. Johdossa kuluu noin $1\,\%$ patterin tehosta. Se on vähän, mutta riittää lämmittämään kelalle rullattua johtoa.

## fy6-15-L2-03
**Annettu:** jännite $U = 90\,\text{kV}$, ilman läpilyöntilujuus $E_\text{max} = 3{,}0\,\text{MV/m}$, tasainen kenttä
**Kysytty:** pienin ilmaväli $d$ senttimetreinä
**Periaate:** Tasaisessa kentässä kentän voimakkuus on jännite jaettuna välin pituudella (luku *Kondensaattori ja sen energia*). Ilma ei lyö läpi eli ala johtaa, kun kenttä on enintään läpilyöntilujuus. Lyhin sallittu väli on siis se, jossa kenttä on täsmälleen $E_\text{max}$.
**Kaava:** $E = \dfrac{U}{d} \le E_\text{max}$, josta $d = \dfrac{U}{E_\text{max}}$
**Muunnokset:** $U = 90\,\text{kV} = 90 \cdot 1000\,\text{V} = 90\,000\,\text{V}$; $E_\text{max} = 3{,}0\,\text{MV/m} = 3{,}0 \cdot 1\,000\,000\,\text{V/m}$; $1\,\text{m} = 100\,\text{cm}$.
**Sijoitus:** $d = \dfrac{90\,000\,\text{V}}{3\,000\,000\,\text{V/m}} = 0{,}030\,\text{m} = 3{,}0\,\text{cm}$
**Vastaus:** $3{,}0\,\text{cm}$, kaksi merkitsevää numeroa kuten läpilyöntilujuudessa $3{,}0\,\text{MV/m}$.
**Järkevyys:** Yksi megavoltti metriä kohti on yksi kilovoltti millimetriä kohti. Ilma kestää siis noin $3\,\text{kV}$ millimetriltä, ja $90\,\text{kV}$ vaatii $30\,\text{mm}$. Todelliset turvaetäisyydet ovat metrejä. Ohuen johtimen lähellä kenttä on paljon tasaista voimakkaampi, kosteus ja lika heikentävät ilmaa, ja verkossa voi esiintyä ylijännitteitä. Laskettu väli on vain laskennallinen alaraja.

## fy6-15-L2-04
**Annettu:** virtatien resistanssi $R = 1{,}5\,\text{k}\Omega$, suurin sallittu virta $I = 10\,\text{mA}$
**Kysytty:** suurin kosketusjännite $U$ voltteina
**Periaate:** Kehon läpi kulkeva virta noudattaa Ohmin lakia. Kun resistanssi on annettu, virta kasvaa jännitteen mukana. Suurin sallittu jännite on se, joka antaa juuri $10\,\text{mA}$:n virran.
**Kaava:** $I = \dfrac{U}{R}$, josta $U = RI$
**Muunnokset:** $R = 1{,}5\,\text{k}\Omega = 1{,}5 \cdot 1000\,\Omega = 1500\,\Omega$; $I = 10\,\text{mA} = 10 \cdot 0{,}001\,\text{A} = 0{,}010\,\text{A}$.
**Sijoitus:** $U = 1500\,\Omega \cdot 0{,}010\,\text{A} = 15\,\text{V}$
**Vastaus:** $15\,\text{V}$, kaksi merkitsevää numeroa kuten resistanssissa $1{,}5\,\text{k}\Omega$.
**Järkevyys:** Tulos on paljon pienempi kuin verkkojännite $230\,\text{V}$ ja pienempi kuin suojajännitteen yläraja $50\,\text{V}$. Siksi märissä tiloissa käytetään vikavirtasuojaa ja erityisen pientä jännitettä. Kun iho on märkä, jo kymmenien volttien jännite voi olla vaarallinen.

## fy6-15-L3-01
**Annettu:** johtimien resistanssi $R = 0{,}50\,\Omega$, mitoitusvirta $I_1 = 10\,\text{A}$, todellinen virta $I_2 = 22\,\text{A}$
**Kysytty:** kuinka moninkertainen lämpöteho $P_2$ on tehoon $P_1$ verrattuna
**Periaate:** Johtimissa sähköenergia muuttuu sisäenergiaksi teholla $P = RI^2$. Resistanssi on molemmissa tilanteissa sama. Siksi tehojen suhde riippuu vain virtojen suhteesta toiseen potenssiin korotettuna. $25\,\text{A}$:n sulake ei katkaise $22\,\text{A}$:n virtaa, joten johto kuormittuu yli mitoituksensa.
**Kaava:** $P_1 = RI_1^2$ ja $P_2 = RI_2^2$, joten $\dfrac{P_2}{P_1} = \dfrac{I_2^2}{I_1^2}$
**Muunnokset:** Ei tarvita: virrat ovat samassa yksikössä, ja yksiköt supistuvat.
**Sijoitus:** $P_1 = 0{,}50\,\Omega \cdot (10\,\text{A})^2 = 50\,\text{W}$, $P_2 = 0{,}50\,\Omega \cdot (22\,\text{A})^2 = 242\,\text{W}$ ja $\dfrac{P_2}{P_1} = \dfrac{242\,\text{W}}{50\,\text{W}} = 4{,}84$
**Vastaus:** noin $4{,}8$-kertainen, kaksi merkitsevää numeroa kuten virrassa $22\,\text{A}$.
**Järkevyys:** Virta on vähän yli kaksinkertainen, joten teho on vähän yli nelinkertainen, sillä $2^2 = 4$. Johto kuumenee siis paljon enemmän kuin mitä sen on suunniteltu kestämään. Eriste voi sulaa ja syttyä palamaan. Tästä syystä sulaketta ei saa vaihtaa suurempaan.

## fy6-15-L3-02
**Annettu:** jännite $U = 230\,\text{V}$, kehon resistanssi $R_\text{keho} = 1{,}5\,\text{k}\Omega$, kenkien ja lattian resistanssi $R_\text{k} = 100\,\text{k}\Omega$
**Kysytty:** kehon läpi kulkeva virta $I$ milliampeereina
**Periaate:** Virta kulkee kehon, kenkien ja lattian läpi peräkkäin. Resistanssit ovat siis sarjassa, ja kokonaisresistanssi on niiden summa (luku *Vastusten sarja- ja rinnankytkennät*). Sama virta kulkee jokaisen läpi, ja se saadaan Ohmin laista kokonaisresistanssin avulla.
**Kaava:** $R = R_\text{keho} + R_\text{k}$ ja $I = \dfrac{U}{R}$, joten $I = \dfrac{U}{R_\text{keho} + R_\text{k}}$
**Muunnokset:** $R_\text{keho} = 1{,}5 \cdot 1000\,\Omega = 1500\,\Omega$ ja $R_\text{k} = 100 \cdot 1000\,\Omega = 100\,000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $I = \dfrac{230\,\text{V}}{1500\,\Omega + 100\,000\,\Omega} = \dfrac{230\,\text{V}}{101\,500\,\Omega} = 0{,}002266\,\text{A} = 2{,}3\,\text{mA}$
**Vastaus:** $2{,}3\,\text{mA}$, kaksi merkitsevää numeroa kuten kehon resistanssissa $1{,}5\,\text{k}\Omega$.
**Järkevyys:** Ilman kenkiä virta olisi $230\,\text{V} : 1500\,\Omega \approx 150\,\text{mA}$, joka on yli kammiovärinän vaaran rajan. Kengät ja kuiva lattia pienentävät virran alle irrottamiskynnyksen $10\,\text{mA}$. Virta kuitenkin tuntuu, koska se on yli tuntokynnyksen $0{,}5\,\text{mA}$. Märkä lattia, vahingoittunut kenkä tai samanaikainen kosketus esimerkiksi hanaan tai maadoitettuun laitteeseen ohittaisi kengät kokonaan. Kengät eivät siis ole suoja.

## fy6-15-L3-03
**Annettu:** kuvaajan $(r, V)$ maan potentiaali; jalat etäisyyksillä $r_1 = 2{,}0\,\text{m}$ ja $r_2 = 3{,}0\,\text{m}$; virtatien resistanssi $R = 4{,}0\,\text{k}\Omega$
**Kysytty:** jalasta toiseen kulkeva virta $I$ milliampeereina
**Periaate:** Jalkojen välinen jännite eli askeljännite on maan potentiaalien erotus jalkojen kohdilla. Potentiaali kertoo, kuinka suuri jännite paikassa on maahan verrattuna. Virta kulkee jalasta kehon kautta toiseen jalkaan, ja se saadaan Ohmin laista.
**Kuvaajan lukeminen:** Kohdassa $r = 2{,}0\,\text{m}$ käyrä kulkee ruudukon risteyksen kautta, ja arvo on $V_1 = 600\,\text{V}$. Kohdassa $r = 3{,}0\,\text{m}$ arvo on $V_2 = 400\,\text{V}$. Askeljännite on näiden arvojen erotus.
**Kaava:** $U = V_1 - V_2$ ja $I = \dfrac{U}{R}$, joten $I = \dfrac{V_1 - V_2}{R}$
**Muunnokset:** $R = 4{,}0\,\text{k}\Omega = 4{,}0 \cdot 1000\,\Omega = 4000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $I = \dfrac{600\,\text{V} - 400\,\text{V}}{4000\,\Omega} = \dfrac{200\,\text{V}}{4000\,\Omega} = 0{,}050\,\text{A} = 50\,\text{mA}$
**Vastaus:** $50\,\text{mA}$, kaksi merkitsevää numeroa kuten resistanssissa $4{,}0\,\text{k}\Omega$.
**Järkevyys:** Virta on kammiovärinän vaaran rajalla, vaikka ihminen ei koske johtimeen lainkaan. Jos jalat olisivat yhdessä, potentiaaliero ja virta olisivat lähes nolla. Jalasta toiseen kulkeva virta ei välttämättä kulje sydämen kautta, mutta kaatuminen voi tuoda sydämen virran reitille. Kauempana käyrä loivenee: kohtien $4{,}0\,\text{m}$ ja $6{,}0\,\text{m}$ välinen jännite on vain $100\,\text{V}$, vaikka väli on kaksi metriä. Pois kannattaa siis siirtyä lyhyin askelin.
