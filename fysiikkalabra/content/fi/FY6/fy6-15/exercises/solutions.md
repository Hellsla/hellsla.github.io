## fy6-15-L1-01
**Annettu:** teho $P = 1500\,\text{W}$, jännite $U = 230\,\text{V}$
**Kysytty:** virta $I$ ampeereina
**Periaate:** Sähköteho on jännite kertaa virta. Verkkojännite $230\,\text{V}$ on vaihtojännitteen tehollinen arvo, joten lämmittävän laitteen teho lasketaan sillä kuten tasajännitteellä.
**Kaava:** $P = UI$, josta $I = \dfrac{P}{U}$
**Muunnokset:** Ei tarvita: $1\,\text{W} : 1\,\text{V} = 1\,\text{A}$.
**Sijoitus:** $I = \dfrac{1500\,\text{W}}{230\,\text{V}} = 6{,}522\,\text{A}$
**Vastaus:** $6{,}5\,\text{A}$, kaksi merkitsevää numeroa kuten tehossa $1500\,\text{W}$.
**Järkevyys:** Arvio $1500\,\text{W} : 200\,\text{V} = 7{,}5\,\text{A}$ on hieman suurempi, koska jakaja on pienempi. Virta on alle $10\,\text{A}$, joten puhallin mahtuu yksin $10\,\text{A}$:n ryhmään, mutta samaan ryhmään ei mahdu enää paljon muuta.

## fy6-15-L1-02
**Annettu:** sulakkeen nimellisvirta $I_\text{s} = 10\,\text{A}$, jännite $U = 230\,\text{V}$
**Kysytty:** suurin yhteisteho $P_\text{max}$ watteina
**Periaate:** Ryhmän laitteet ovat rinnan samassa jännitteessä, joten niiden virrat summautuvat ja ryhmäjohdon virta on yhteisteho jaettuna jännitteellä. Nimellisvirta ei ylity, kun tämä virta on enintään $I_\text{s}$.
**Kaava:** $I = \dfrac{P_1 + P_2 + \dots}{U} \le I_\text{s}$, josta $P_\text{max} = UI_\text{s}$
**Muunnokset:** Ei tarvita: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Sijoitus:** $P_\text{max} = 230\,\text{V} \cdot 10\,\text{A} = 2300\,\text{W}$
**Vastaus:** $2300\,\text{W}$ eli $2{,}3\,\text{kW}$, kaksi merkitsevää numeroa kuten nimellisvirrassa $10\,\text{A}$.
**Järkevyys:** Yksi $2000\,\text{W}$:n vedenkeitin mahtuu ryhmään, mutta keitin ja $900\,\text{W}$:n leivänpaahdin yhdessä eivät. Tämä vastaa kokemusta siitä, että vanhan keittiön sulake laukeaa, kun liian monta lämmittävää laitetta on päällä yhtä aikaa.

## fy6-15-L1-03
**Annettu:** kosketusjännite $U = 230\,\text{V}$, virtatien resistanssi $R = 2{,}3\,\text{k}\Omega$
**Kysytty:** kehon läpi kulkeva virta $I$ milliampeereina
**Periaate:** Keho on osa virtapiiriä kosketuskohdan ja maan välillä, joten sen läpi kulkeva virta saadaan Ohmin laista koko virtatien resistanssin avulla.
**Kaava:** $U = RI$, josta $I = \dfrac{U}{R}$
**Muunnokset:** $R = 2{,}3\,\text{k}\Omega = 2{,}3 \cdot 1000\,\Omega = 2300\,\Omega$; tulos ampeereista milliampeereiksi: $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $I = \dfrac{230\,\text{V}}{2300\,\Omega} = 0{,}100\,\text{A} = 100\,\text{mA}$
**Vastaus:** $100\,\text{mA}$, kaksi merkitsevää numeroa kuten resistanssissa $2{,}3\,\text{k}\Omega$.
**Järkevyys:** Resistanssin $2300\,\Omega$ lukuarvo on kymmenkertainen jännitteen $230\,\text{V}$ lukuarvoon verrattuna, joten virran lukuarvo on kymmenesosa ampeereina eli noin $0{,}1\,\text{A}$. Virta on kaksinkertainen kammiovärinän vaaran rajaan noin $50\,\text{mA}$ verrattuna, joten märin käsin kosketus on hengenvaarallinen.

## fy6-15-L1-04
**Annettu:** kosketusjännite $U = 230\,\text{V}$, virtatien resistanssi $R = 50\,\text{k}\Omega$
**Kysytty:** kehon läpi kulkeva virta $I$ milliampeereina
**Periaate:** Keho, kengät ja lattia ovat samassa virtatiessä, ja niiden yhteinen resistanssi on annettu. Virta saadaan Ohmin laista.
**Kaava:** $U = RI$, josta $I = \dfrac{U}{R}$
**Muunnokset:** $R = 50\,\text{k}\Omega = 50 \cdot 1000\,\Omega = 50\,000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $I = \dfrac{230\,\text{V}}{50\,000\,\Omega} = 0{,}0046\,\text{A} = 4{,}6\,\text{mA}$
**Vastaus:** $4{,}6\,\text{mA}$, kaksi merkitsevää numeroa kuten resistanssissa $50\,\text{k}\Omega$.
**Järkevyys:** Virta tuntuu selvästi, koska se on lähes kymmenkertainen tuntokynnykseen $0{,}5\,\text{mA}$ verrattuna, mutta se jää alle irrottamiskynnyksen $10\,\text{mA}$. Märin käsin resistanssi voi olla kymmenesosa tai vähemmän, jolloin virta on kymmenkertainen. Tulos pätee vain ehjillä, kuivilla kengillä ja kuivalla lattialla, kun ihminen ei koske samalla mihinkään maadoitettuun, kuten hanaan; muuten virta ohittaa kengät. Kenkiä ei pidä pitää suojana.

## fy6-15-L1-05
**Annettu:** johtimien resistanssi $R = 0{,}20\,\Omega$, virta $I = 16\,\text{A}$
**Kysytty:** jatkojohdossa kehittyvä lämpöteho $P$
**Periaate:** Johtimen resistanssissa sähköenergia muuttuu johtimen sisäenergiaksi, joka siirtyy lämpönä ympäristöön. Kun johtimen resistanssi ja virta tunnetaan, teho saadaan Joulen laista.
**Kaava:** $P = RI^2$
**Muunnokset:** Ei tarvita: $1\,\Omega \cdot (1\,\text{A})^2 = 1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Sijoitus:** $P = 0{,}20\,\Omega \cdot (16\,\text{A})^2 = 0{,}20\,\Omega \cdot 256\,\text{A}^2 = 51{,}2\,\text{W}$
**Vastaus:** $51\,\text{W}$, kaksi merkitsevää numeroa kuten resistanssissa ja virrassa.
**Järkevyys:** Teho on kuin pienen hehkulampun, mutta se jakautuu koko johdon pituudelle, joten ehjä johto lämpenee vain vähän. Jos johto on kelalla tiukasti rullattuna, siitä siirtyy energiaa lämpönä ympäristöön huonosti, ja johto voi kuumeta vaarallisesti.

## fy6-15-L1-06
**Kysytty:** mikä väite suojamaadoituksen tehtävästä on oikein
**Periaate:** Suojamaadoitus yhdistää laitteen metallirungon maahan johtimella. Jos vaihejohdin koskettaa vian takia runkoa, suuri vikavirta kulkee tätä johdinta pitkin ja sulake tai vikavirtasuoja katkaisee virran, jolloin runko ei jää jännitteiseksi.
**Mallivastaus:** Oikea väite on se, jonka mukaan maadoitus ohjaa vikavirran johdinta pitkin maahan, jolloin sulake tai vikavirtasuoja katkaisee virran. Väite sähkönkulutuksen pienenemisestä on väärä, koska normaalikäytössä maadoitusjohtimessa ei kulje virtaa. Väite rungon eristämisestä maasta on väärä, koska maadoitus yhdistää rungon maahan, ei eristä sitä. Väite rungon jatkuvasta jännitteisyydestä on väärä, koska maadoituksen tarkoitus on estää runkoa jäämästä jännitteiseksi.

## fy6-15-L1-07
**Kysytty:** mikä väite suojausluokan II laitteesta on oikein
**Periaate:** Suojausluokka kertoo, miten laite suojaa käyttäjää sähköiskulta. Luokan I laitteen metallirunko on suojamaadoitettu, luokan II laitteessa on kaksinkertainen tai vahvistettu eristys ja luokan III laite toimii pienellä suojajännitteellä. Luokan II suoja on siis eristyksessä: yksi eristysvika ei vielä tuo verkkojännitettä kuoreen.
**Mallivastaus:** Oikea väite on se, jonka mukaan laitteessa on kaksinkertainen eristys, joten kuori ei tule jännitteiseksi yhden vian takia. Väite maadoitetusta metallirungosta on väärä, koska se kuvaa luokkaa I. Väite pienestä suojajännitteestä on väärä, koska se kuvaa luokkaa III. Väite vesitiiviistä kuoresta on väärä, koska suojausluokka kertoo suojasta sähköiskua vastaan eikä kosteudenkestosta.

## fy6-15-L1-08
**Annettu:** ilmaväli $d = 2{,}0\,\text{mm}$, tasainen kenttä, ilman läpilyöntilujuus $E_\text{max} = 3{,}0\,\text{MV/m}$
**Kysytty:** suurin sallittu jännite $U_\text{max}$ kilovoltteina
**Periaate:** Tasaisessa kentässä kentän voimakkuus on jännite jaettuna välin pituudella. Ilma ei lyö läpi, kun kenttä on enintään läpilyöntilujuus, joten suurin sallittu jännite on se, jolla kenttä on täsmälleen $E_\text{max}$.
**Kaava:** $E = \dfrac{U}{d} \le E_\text{max}$, josta $U_\text{max} = E_\text{max}\,d$
**Muunnokset:** $d = 2{,}0\,\text{mm} = 2{,}0 \cdot 0{,}001\,\text{m} = 0{,}0020\,\text{m}$; $E_\text{max} = 3{,}0\,\text{MV/m} = 3{,}0 \cdot 1\,000\,000\,\text{V/m}$; tulos $1\,\text{kV} = 1000\,\text{V}$.
**Sijoitus:** $U_\text{max} = 3\,000\,000\,\text{V/m} \cdot 0{,}0020\,\text{m} = 6000\,\text{V} = 6{,}0\,\text{kV}$
**Vastaus:** $6{,}0\,\text{kV}$, kaksi merkitsevää numeroa kuten läpilyöntilujuudessa $3{,}0\,\text{MV/m}$.
**Järkevyys:** Yksi megavoltti metriä kohti on yksi kilovoltti millimetriä kohti, joten ilma kestää noin $3\,\text{kV}$ millimetriltä ja kahden millimetrin väli $2 \cdot 3\,\text{kV} = 6\,\text{kV}$. Pistorasian $230\,\text{V}$ jää tästä kauas alle, mutta salaman tai suurjännitejohdon jännitteet ovat tuhansia kertoja suurempia.

## fy6-15-L1-09
**Kysytty:** tilanteiden A–D järjestys kehon läpi kulkevan virran $I$ mukaan pienimmästä suurimpaan.
**Periaate:** Vahingon tekee kehon läpi kulkeva virta, ja se riippuu sekä kosketusjännitteestä että virtatien resistanssista Ohmin lain mukaan, $I = U : R$. Suurin jännite ei siis välttämättä anna suurinta virtaa, eikä suurin resistanssi välttämättä pienintä. Lasketaan jokaisen tilanteen virta.
**Mallivastaus:** Virrat:

$I_\text{A} = 24\,\text{V} : 20\,\text{k}\Omega = 1{,}2\,\text{mA}$

$I_\text{B} = 230\,\text{V} : 46\,\text{k}\Omega = 5{,}0\,\text{mA}$

$I_\text{C} = 230\,\text{V} : 1{,}6\,\text{k}\Omega \approx 140\,\text{mA}$

$I_\text{D} = 1000\,\text{V} : 25\,\text{k}\Omega = 40\,\text{mA}$

Virta $I_\text{C}$ on ilmoitettu kahdella merkitsevällä numerolla kuten resistanssi $1{,}6\,\text{k}\Omega$. Virran mukaan pienimmästä suurimpaan järjestys on A, B, D, C.

Jännitteen mukaan järjestys olisi eri, A, B ja C, D: tilanteen D jännite $1000\,\text{V}$ on suurin, mutta märän käden pieni resistanssi tekee tilanteen C virrasta suurimman. Pelkkä resistanssikaan ei ratkaise: tilanteen A resistanssi on pienempi kuin tilanteiden B ja D, mutta sen jännite on niin pieni, että virta jää pienimmäksi.

Tilanteen A virta ylittää vain tuntokynnyksen. Tilanteen B virta jää näillä arvoilla alle irrottamiskynnyksen $10\,\text{mA}$, mutta kenkiä ei voi pitää sähköiskulta suojaavina: märkä lattia, vaurioitunut kenkä tai samanaikainen hanan kosketus ohittaa ne, eikä mitään virtaa voi pitää varmasti turvallisena. Tilanteen D virta ylittää hengityksen vaikeutumisen rajan $30\,\text{mA}$, ja tilanteen C virta ylittää kammiovärinän vaaran rajan $50\,\text{mA}$.

## fy6-15-L2-01
**Annettu:** nimellisvirta $I_\text{s} = 16\,\text{A}$, jännite $U = 230\,\text{V}$, päällä olevat tehot $P_1 = 2000\,\text{W}$ ja $P_2 = 1200\,\text{W}$
**Kysytty:** teho $P_\text{lisä}$, jonka ryhmään voi vielä kytkeä
**Periaate:** Ryhmän laitteet ovat rinnan, joten virrat summautuvat ja kokonaisvirta on yhteisteho jaettuna jännitteellä. Nimellisvirta ei ylity, kun yhteisteho on enintään $UI_\text{s}$; lisätehoksi jää tämän ja käytössä olevan tehon erotus.
**Kaava:** $\dfrac{P_1 + P_2 + P_\text{lisä}}{U} = I_\text{s}$, josta $P_\text{lisä} = UI_\text{s} - (P_1 + P_2)$
**Muunnokset:** Ei tarvita: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Sijoitus:** $P_\text{lisä} = 230\,\text{V} \cdot 16\,\text{A} - (2000\,\text{W} + 1200\,\text{W}) = 3680\,\text{W} - 3200\,\text{W} = 480\,\text{W}$
**Vastaus:** noin $480\,\text{W}$. Erotus on suurista luvuista laskettu, joten se on vain suuntaa antava: nimellisvirta $16\,\text{A}$ on kahden merkitsevän numeron tarkkuudella.
**Järkevyys:** Virtoina: keitin ottaa $8{,}7\,\text{A}$ ja mikroaaltouuni $5{,}2\,\text{A}$, yhteensä $13{,}9\,\text{A}$, joten jäljellä on noin $2{,}1\,\text{A}$ eli $230\,\text{V} \cdot 2{,}1\,\text{A} \approx 480\,\text{W}$. Leivänpaahdin ($900\,\text{W}$) ei siis mahdu, mutta jääkaappi mahtuu.

## fy6-15-L2-02
**Annettu:** patterin teho $P = 2000\,\text{W}$, jännite $U = 230\,\text{V}$, johtimien resistanssi $R = 0{,}30\,\Omega$
**Kysytty:** jatkojohdossa kehittyvä lämpöteho $P_\text{j}$
**Periaate:** Jatkojohto on sarjassa patterin kanssa, joten sen läpi kulkee patterin virta. Virta saadaan patterin tehosta, ja johdossa sähköenergia muuttuu sisäenergiaksi teholla $RI^2$. Oletus: johdon jännitehäviö on niin pieni, että patterin virta on sama kuin ilman jatkojohtoa.
**Kaava:** $P = UI$, josta $I = \dfrac{P}{U}$; johdossa $P_\text{j} = RI^2$, joten $P_\text{j} = R\left(\dfrac{P}{U}\right)^2$
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä.
**Sijoitus:** $I = \dfrac{2000\,\text{W}}{230\,\text{V}} = 8{,}696\,\text{A}$ ja $P_\text{j} = 0{,}30\,\Omega \cdot (8{,}696\,\text{A})^2 = 22{,}68\,\text{W}$
**Vastaus:** $23\,\text{W}$, kaksi merkitsevää numeroa kuten resistanssissa $0{,}30\,\Omega$.
**Järkevyys:** Johdon jännite on $RI = 0{,}30\,\Omega \cdot 8{,}7\,\text{A} \approx 2{,}6\,\text{V}$, hyvin pieni verrattuna $230\,\text{V}$:iin, joten oletus pitää. Johdossa kuluu noin $1\,\%$ patterin tehosta, mikä on vähän mutta riittää lämmittämään kelalle rullattua johtoa.

## fy6-15-L2-03
**Annettu:** jännite $U = 90\,\text{kV}$, ilman läpilyöntilujuus $E_\text{max} = 3{,}0\,\text{MV/m}$, tasainen kenttä
**Kysytty:** pienin ilmaväli $d$ senttimetreinä
**Periaate:** Tasaisessa kentässä kentän voimakkuus on jännite jaettuna välin pituudella (luku *Kondensaattori ja sen energia*). Ilma ei lyö läpi, kun kenttä on enintään läpilyöntilujuus, joten lyhin sallittu väli on se, jossa kenttä on täsmälleen $E_\text{max}$.
**Kaava:** $E = \dfrac{U}{d} \le E_\text{max}$, josta $d = \dfrac{U}{E_\text{max}}$
**Muunnokset:** $U = 90\,\text{kV} = 90 \cdot 1000\,\text{V} = 90\,000\,\text{V}$; $E_\text{max} = 3{,}0\,\text{MV/m} = 3{,}0 \cdot 1\,000\,000\,\text{V/m}$; $1\,\text{m} = 100\,\text{cm}$.
**Sijoitus:** $d = \dfrac{90\,000\,\text{V}}{3\,000\,000\,\text{V/m}} = 0{,}030\,\text{m} = 3{,}0\,\text{cm}$
**Vastaus:** $3{,}0\,\text{cm}$, kaksi merkitsevää numeroa kuten läpilyöntilujuudessa $3{,}0\,\text{MV/m}$.
**Järkevyys:** Yksi megavoltti metriä kohti on yksi kilovoltti millimetriä kohti, joten ilma kestää noin $3\,\text{kV}$ millimetriltä ja $90\,\text{kV}$ vaatii $30\,\text{mm}$. Todelliset turvaetäisyydet ovat metrejä, koska ohuen johtimen lähellä kenttä on paljon tasaista voimakkaampi, kosteus ja lika heikentävät ilmaa ja verkossa voi esiintyä ylijännitteitä; laskettu väli on vain laskennallinen alaraja.

## fy6-15-L2-04
**Annettu:** virtatien resistanssi $R = 1{,}5\,\text{k}\Omega$, suurin sallittu virta $I = 10\,\text{mA}$
**Kysytty:** suurin kosketusjännite $U$ voltteina
**Periaate:** Kehon läpi kulkeva virta noudattaa Ohmin lakia: kun resistanssi on annettu, virta kasvaa jännitteen mukana. Suurin sallittu jännite on se, joka antaa juuri $10\,\text{mA}$:n virran.
**Kaava:** $I = \dfrac{U}{R}$, josta $U = RI$
**Muunnokset:** $R = 1{,}5\,\text{k}\Omega = 1{,}5 \cdot 1000\,\Omega = 1500\,\Omega$; $I = 10\,\text{mA} = 10 \cdot 0{,}001\,\text{A} = 0{,}010\,\text{A}$.
**Sijoitus:** $U = 1500\,\Omega \cdot 0{,}010\,\text{A} = 15\,\text{V}$
**Vastaus:** $15\,\text{V}$, kaksi merkitsevää numeroa kuten resistanssissa $1{,}5\,\text{k}\Omega$.
**Järkevyys:** Tulos on paljon pienempi kuin verkkojännite $230\,\text{V}$ ja pienempi kuin suojajännitteen yläraja $50\,\text{V}$. Siksi märissä tiloissa käytetään vikavirtasuojaa ja erityisen pientä jännitettä: kun iho on märkä, jo kymmenien volttien jännite voi olla vaarallinen.

## fy6-15-L2-05
**Annettu:** kosketusjännite $U = 230\,\text{V}$; resistanssit taulukosta: $R_1 = 55\,\text{k}\Omega$ (kuiva iho, kumikengät), $R_2 = 12\,\text{k}\Omega$ (kuiva iho, paljaat jalat), $R_3 = 2{,}4\,\text{k}\Omega$ (märät kädet), $R_4 = 0{,}90\,\text{k}\Omega$ (kylpyammeessa)
**Kysytty:** a) virta $I$ jokaisessa tilanteessa ja sen vaikutus; b) kylpyammeen ja kumikenkien virtojen suhde $I_4 : I_1$
**Periaate:** Keho on osa virtapiiriä kosketuskohdan ja maan välillä, joten kehon läpi kulkeva virta saadaan Ohmin laista virtatien resistanssin avulla. Virran vaikutus luetaan sen suuruudesta kynnysarvojen mukaan. Jännite on joka tilanteessa sama, joten virrat ovat kääntäen verrannollisia resistansseihin.
**Kaava:** $I = \dfrac{U}{R}$ ja $\dfrac{I_4}{I_1} = \dfrac{U / R_4}{U / R_1} = \dfrac{R_1}{R_4}$
**Muunnokset:** $R_1 = 55\,\text{k}\Omega = 55 \cdot 1000\,\Omega = 55\,000\,\Omega$, vastaavasti $R_2 = 12\,000\,\Omega$, $R_3 = 2400\,\Omega$ ja $R_4 = 900\,\Omega$; virrat ampeereista milliampeereiksi: $1\,\text{A} = 1000\,\text{mA}$. Suhteessa kiloohmit supistuvat.
**Sijoitus:** $I_1 = \dfrac{230\,\text{V}}{55\,000\,\Omega} = 4{,}2\,\text{mA}$, $I_2 = \dfrac{230\,\text{V}}{12\,000\,\Omega} = 19{,}2\,\text{mA}$, $I_3 = \dfrac{230\,\text{V}}{2400\,\Omega} = 95{,}8\,\text{mA}$, $I_4 = \dfrac{230\,\text{V}}{900\,\Omega} = 255{,}6\,\text{mA}$ ja $\dfrac{I_4}{I_1} = \dfrac{55\,\text{k}\Omega}{0{,}90\,\text{k}\Omega} = 61{,}11$
**Vastaus:** noin $61$-kertainen, kaksi merkitsevää numeroa kuten resistanssissa $0{,}90\,\text{k}\Omega$. Kohta a): kumikengillä $4{,}2\,\text{mA}$ tuntuu mutta jää alle irrottamiskynnyksen; paljain jaloin $19\,\text{mA}$ ylittää irrottamiskynnyksen, joten ote ei välttämättä irtoa; märin käsin $96\,\text{mA}$ ja kylpyammeessa $256\,\text{mA}$ ylittävät kammiovärinän vaaran rajan.
**Järkevyys:** Arvio: $55 : 0{,}9 \approx 60$. Sama suhde saadaan virroista, $256\,\text{mA} : 4{,}2\,\text{mA} \approx 61$. Kaikki neljä virtaa ovat tuntokynnystä $0{,}5\,\text{mA}$ suurempia, ja virta kasvaa tilanteesta toiseen samassa järjestyksessä kuin resistanssi pienenee. Kosteus ja paljas iho kasvattavat samalla jännitteellä virran yli kuusikymmenkertaiseksi.

## fy6-15-L2-06
**Annettu:** sulakkeen nimellisvirta $I_\text{s} = 10\,\text{A}$, jännite $U = 230\,\text{V}$; tehot taulukosta: vedenkeitin $2000\,\text{W}$, pölynimuri $1400\,\text{W}$, silitysrauta $1100\,\text{W}$, leivänpaahdin $800\,\text{W}$, kahvinkeitin $600\,\text{W}$
**Kysytty:** a) parit, joiden yhteisvirta ylittää $I_\text{s}$; b) suurin yhteisteho, joka ei ylitä rajaa, ja sitä vastaava virta $I$ ampeereina
**Periaate:** Ryhmän laitteet ovat rinnan samassa jännitteessä, joten niiden virrat summautuvat ja ryhmäjohdon virta on yhteisteho jaettuna jännitteellä. Sulakkeen nimellisvirta ylittyy, kun yhteisteho on suurempi kuin $P_\text{max} = UI_\text{s}$.
**Kaava:** $P_\text{max} = UI_\text{s}$ ja $I = \dfrac{P_1 + P_2}{U}$
**Muunnokset:** Ei tarvita: $1\,\text{W} : 1\,\text{V} = 1\,\text{A}$.
**Sijoitus:** $P_\text{max} = 230\,\text{V} \cdot 10\,\text{A} = 2300\,\text{W}$. Parien yhteistehot: vedenkeitin ja pölynimuri $3400\,\text{W}$, vedenkeitin ja silitysrauta $3100\,\text{W}$, vedenkeitin ja leivänpaahdin $2800\,\text{W}$, vedenkeitin ja kahvinkeitin $2600\,\text{W}$, pölynimuri ja silitysrauta $2500\,\text{W}$; kaikki ovat yli $2300\,\text{W}$. Muut parit ovat alle: suurin niistä on pölynimuri ja leivänpaahdin, $1400\,\text{W} + 800\,\text{W} = 2200\,\text{W}$. Virta on $I = \dfrac{2200\,\text{W}}{230\,\text{V}} = 9{,}565\,\text{A}$
**Vastaus:** $9{,}6\,\text{A}$, kaksi merkitsevää numeroa kuten sulakkeen nimellisvirrassa. Kohta a): sulakkeen nimellisvirran ylittävät vedenkeittimen yhdistelmät kaikkien muiden laitteiden kanssa sekä pölynimurin ja silitysraudan pari.
**Järkevyys:** Virta $9{,}6\,\text{A}$ on vähän alle rajan $10\,\text{A}$, joten pari mahtuu ryhmään mutta ei jätä juuri varaa: seuraavaksi suurin pari, pölynimuri ja kahvinkeitin, antaisi vain $2000\,\text{W} : 230\,\text{V} = 8{,}7\,\text{A}$. Vedenkeitin yksin ($8{,}7\,\text{A}$) mahtuu ryhmään, mutta mikään toinen laite ei mahdu sen rinnalle.

## fy6-15-L2-07
**Annettu:** sulake $16\,\text{A}$, kosketusjännite $U = 230\,\text{V}$, virtatien resistanssi $R = 2{,}00\,\text{k}\Omega$
**Kysytty:** a) virhe opiskelijan väitteessä ja laite, joka katkaisee pienen virran; b) kehon läpi kulkeva virta $I$ milliampeereina
**Periaate:** Sulake suojaa johtoa ylikuumenemiselta, ja sen nimellisvirta on kymmeniä ampeereita. Ihmisen läpi kulkeva virta on kymmeniä tai satoja milliampeereita eli satoja kertoja pienempi, joten sulake ei huomaa sitä lainkaan. Ihmisen kautta kulkevan pienen virran katkaisee vikavirtasuoja, joka laukeaa noin $30\,\text{mA}$:n vikavirrasta. Kehon läpi kulkeva virta saadaan Ohmin laista.
**Kaava:** $U = RI$, josta $I = \dfrac{U}{R}$
**Muunnokset:** $R = 2{,}00\,\text{k}\Omega = 2{,}00 \cdot 1000\,\Omega = 2000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $I = \dfrac{230\,\text{V}}{2000\,\Omega} = 0{,}115\,\text{A} = 115\,\text{mA}$
**Vastaus:** $115\,\text{mA}$, kolme merkitsevää numeroa kuten jännitteessä ja resistanssissa. Opiskelijan virhe on, että sulake suojaisi ihmistä: sulake ei huomaa kehon läpi kulkevaa virtaa, koska sen nimellisvirta $16\,\text{A}$ on moninkertainen kehon virtaan verrattuna. Ihmistä sulake suojaa vain yhdessä suojamaadoituksen kanssa. Kehon kautta kulkevan virran katkaisee vikavirtasuoja.
**Järkevyys:** Sulakkeen virta $16\,\text{A}$ on $16\,\text{A} : 0{,}115\,\text{A} \approx 139$-kertainen kehon virtaan verrattuna, joten sulake ei laukea. Virta $115\,\text{mA}$ on yli kaksinkertainen kammiovärinän vaaran rajaan $50\,\text{mA}$ nähden, ja se on myös moninkertainen vikavirtasuojan laukaisuvirtaan $30\,\text{mA}$ nähden, joten vikavirtasuoja laukeaisi.

## fy6-15-L3-01
**Annettu:** johtimien resistanssi $R = 0{,}50\,\Omega$, mitoitusvirta $I_1 = 10\,\text{A}$, todellinen virta $I_2 = 22\,\text{A}$
**Kysytty:** kuinka moninkertainen lämpöteho $P_2$ on tehoon $P_1$ verrattuna
**Periaate:** Johtimissa sähköenergia muuttuu sisäenergiaksi teholla $P = RI^2$. Resistanssi on molemmissa tilanteissa sama, joten tehojen suhde riippuu vain virtojen suhteesta toiseen potenssiin. $25\,\text{A}$:n sulake ei katkaise $22\,\text{A}$:n virtaa, joten johto kuormittuu yli mitoituksensa.
**Kaava:** $P_1 = RI_1^2$ ja $P_2 = RI_2^2$, joten $\dfrac{P_2}{P_1} = \dfrac{I_2^2}{I_1^2}$
**Muunnokset:** Ei tarvita: virrat ovat samassa yksikössä, ja yksiköt supistuvat.
**Sijoitus:** $P_1 = 0{,}50\,\Omega \cdot (10\,\text{A})^2 = 50\,\text{W}$, $P_2 = 0{,}50\,\Omega \cdot (22\,\text{A})^2 = 242\,\text{W}$ ja $\dfrac{P_2}{P_1} = \dfrac{242\,\text{W}}{50\,\text{W}} = 4{,}84$
**Vastaus:** noin $4{,}8$-kertainen, kaksi merkitsevää numeroa kuten virrassa $22\,\text{A}$.
**Järkevyys:** Virta on vähän yli kaksinkertainen, joten teho on vähän yli nelinkertainen, sillä $2^2 = 4$. Johto kuumenee siis paljon enemmän kuin se on suunniteltu kestämään, ja eriste voi sulaa ja syttyä. Tästä syystä sulaketta ei saa vaihtaa suurempaan.

## fy6-15-L3-02
**Annettu:** jännite $U = 230\,\text{V}$, kehon resistanssi $R_\text{keho} = 1{,}5\,\text{k}\Omega$, kenkien ja lattian resistanssi $R_\text{k} = 100\,\text{k}\Omega$
**Kysytty:** kehon läpi kulkeva virta $I$ milliampeereina
**Periaate:** Virta kulkee kehon, kenkien ja lattian läpi peräkkäin, joten resistanssit ovat sarjassa ja niiden kokonaisresistanssi on summa (luku *Vastusten sarja- ja rinnankytkennät*). Sama virta kulkee jokaisen läpi, ja se saadaan Ohmin laista kokonaisresistanssin avulla.
**Kaava:** $R = R_\text{keho} + R_\text{k}$ ja $I = \dfrac{U}{R}$, joten $I = \dfrac{U}{R_\text{keho} + R_\text{k}}$
**Muunnokset:** $R_\text{keho} = 1{,}5 \cdot 1000\,\Omega = 1500\,\Omega$ ja $R_\text{k} = 100 \cdot 1000\,\Omega = 100\,000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $I = \dfrac{230\,\text{V}}{1500\,\Omega + 100\,000\,\Omega} = \dfrac{230\,\text{V}}{101\,500\,\Omega} = 0{,}002266\,\text{A} = 2{,}3\,\text{mA}$
**Vastaus:** $2{,}3\,\text{mA}$, kaksi merkitsevää numeroa kuten kehon resistanssissa $1{,}5\,\text{k}\Omega$.
**Järkevyys:** Ilman kenkiä virta olisi $230\,\text{V} : 1500\,\Omega \approx 150\,\text{mA}$, yli kammiovärinän vaaran rajan. Kengät ja kuiva lattia pienentävät virran alle irrottamiskynnyksen $10\,\text{mA}$, mutta virta tuntuu, koska se on yli tuntokynnyksen $0{,}5\,\text{mA}$. Märkä lattia, vahingoittunut kenkä tai samanaikainen kosketus esimerkiksi hanaan tai maadoitettuun laitteeseen ohittaisi kengät kokonaan, joten kengät eivät ole suoja.

## fy6-15-L3-03
**Annettu:** kuvaajan $(r, V)$ maan potentiaali; jalat etäisyyksillä $r_1 = 2{,}0\,\text{m}$ ja $r_2 = 3{,}0\,\text{m}$; virtatien resistanssi $R = 4{,}0\,\text{k}\Omega$
**Kysytty:** jalasta toiseen kulkeva virta $I$ milliampeereina
**Periaate:** Jalkojen välinen jännite eli askeljännite on maan potentiaalien erotus jalkojen kohdilla. Virta kulkee jalasta kehon kautta toiseen jalkaan, ja se saadaan Ohmin laista.
**Kuvaajan lukeminen:** Kohdassa $r = 2{,}0\,\text{m}$ käyrä kulkee ruudukon risteyksen kautta arvossa $V_1 = 600\,\text{V}$ ja kohdassa $r = 3{,}0\,\text{m}$ arvossa $V_2 = 400\,\text{V}$. Askeljännite on niiden erotus.
**Kaava:** $U = V_1 - V_2$ ja $I = \dfrac{U}{R}$, joten $I = \dfrac{V_1 - V_2}{R}$
**Muunnokset:** $R = 4{,}0\,\text{k}\Omega = 4{,}0 \cdot 1000\,\Omega = 4000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $I = \dfrac{600\,\text{V} - 400\,\text{V}}{4000\,\Omega} = \dfrac{200\,\text{V}}{4000\,\Omega} = 0{,}050\,\text{A} = 50\,\text{mA}$
**Vastaus:** $50\,\text{mA}$, kaksi merkitsevää numeroa kuten resistanssissa $4{,}0\,\text{k}\Omega$.
**Järkevyys:** Virta on kammiovärinän vaaran rajalla, vaikka ihminen ei koske johtimeen lainkaan. Jos jalat olisivat yhdessä, potentiaaliero ja virta olisivat lähes nolla. Jalasta toiseen kulkeva virta ei välttämättä kulje sydämen kautta, mutta kaatuminen voi tuoda sydämen virran reitille. Kauempana käyrä loivenee: kohtien $4{,}0\,\text{m}$ ja $6{,}0\,\text{m}$ välinen jännite on vain $100\,\text{V}$, vaikka väli on kaksi metriä, joten pois kannattaa siirtyä lyhyin askelin.

## fy6-15-L3-04
**Annettu:** johtimien resistanssi $R = 0{,}40\,\Omega$; taulukosta virrat $I = 4{,}0$; $8{,}0$; $12{,}0$; $16{,}0\,\text{A}$ ja lämpötilan nousut $\Delta T = 2{,}1$; $7{,}6$; $17{,}2$; $30{,}4\,\text{K}$; eristeen raja $\Delta T_\text{max} = 50\,\text{K}$
**Kysytty:** a) kulmakerroin $k$ yksikössä $\text{K/W}$; b) virta $I_\text{max}$, jolla lämpötilan nousu on $50\,\text{K}$, ampeereina; c) riittävätkö $16\,\text{A}$:n ja $25\,\text{A}$:n sulakkeet
**Periaate:** Johtimen resistanssissa kehittyy lämpöteho $P = RI^2$ (luku *Sähköteho ja vastuksen lämpeneminen*). Kun lämpötila on vakiintunut, johto luovuttaa ympäristöön saman tehon, jonka siinä kehittyy, ja mittaus osoittaa lämpötilan nousun kasvavan tehon mukana. Jos pisteet $(P, \Delta T)$ ovat suoralla origon kautta, $\Delta T = kP$ eli lämpötilan nousu on suoraan verrannollinen tehoon. Kun tehoa ei kehity, johto on ympäristön lämpötilassa, joten suora kulkee origon kautta.
**Kuvaajan lukeminen:** Pisteet $(P, \Delta T)$ ovat $(6{,}4\,\text{W};\ 2{,}1\,\text{K})$, $(25{,}6\,\text{W};\ 7{,}6\,\text{K})$, $(57{,}6\,\text{W};\ 17{,}2\,\text{K})$ ja $(102{,}4\,\text{W};\ 30{,}4\,\text{K})$. Ne asettuvat lähes suoralle, joka kulkee origon kautta: suhteet $\Delta T : P$ ovat $0{,}33$; $0{,}30$; $0{,}30$ ja $0{,}30\,\text{K/W}$ (ensimmäinen poikkeaa, koska pienen lämpötilan nousun lukemistarkkuus on huonompi). Origon kautta sovitetun suoran kulmakerroin on $k = \dfrac{\sum P\,\Delta T}{\sum P^2}$.
**Kaava:** $\Delta T = kP = kRI^2$, josta $I_\text{max} = \sqrt{\dfrac{\Delta T_\text{max}}{kR}}$
**Muunnokset:** Ei tarvita: lämpötilan nousu on sama kelvineinä ja celsiusasteina, ja $1\,\text{K/W}$ on suoraan taulukon yksiköistä.
**Sijoitus:** $\sum P\,\Delta T = 6{,}4 \cdot 2{,}1 + 25{,}6 \cdot 7{,}6 + 57{,}6 \cdot 17{,}2 + 102{,}4 \cdot 30{,}4 = 4311{,}7$ ja $\sum P^2 = 6{,}4^2 + 25{,}6^2 + 57{,}6^2 + 102{,}4^2 = 14\,499{,}8$, joten $k = \dfrac{4311{,}7}{14\,499{,}8}\,\dfrac{\text{K}}{\text{W}} = 0{,}2974\,\dfrac{\text{K}}{\text{W}}$. Virta on $I_\text{max} = \sqrt{\dfrac{50\,\text{K}}{0{,}2974\,\text{K/W} \cdot 0{,}40\,\Omega}} = \sqrt{420{,}3\,\text{A}^2} = 20{,}50\,\text{A}$
**Vastaus:** $21\,\text{A}$, kaksi merkitsevää numeroa kuten rajassa $50\,\text{K}$ (kohta a: $k \approx 0{,}30\,\text{K/W}$). c) Virralla $16\,\text{A}$ lämpötilan nousu on $\Delta T = 0{,}2974 \cdot 0{,}40 \cdot 16^2\,\text{K} = 30\,\text{K}$, alle rajan $50\,\text{K}$, joten $16\,\text{A}$:n sulake riittää suojaamaan tämän johdon. Virralla $25\,\text{A}$ nousu olisi $0{,}2974 \cdot 0{,}40 \cdot 25^2\,\text{K} = 74\,\text{K}$, yli rajan, joten $25\,\text{A}$:n sulake ei suojaisi johtoa: johto saisi kuumentua vaarallisen kuumaksi, ennen kuin sulake laukeaa.
**Järkevyys:** Tarkistus: virralla $20{,}5\,\text{A}$ teho on $0{,}40 \cdot 20{,}5^2\,\text{W} = 168\,\text{W}$ ja nousu $0{,}2974 \cdot 168\,\text{K} = 50\,\text{K}$. Raja $20{,}5\,\text{A}$ on mitatun suurimman virran $16\,\text{A}$ ulkopuolella, joten se on ekstrapolaatio. Virta kasvaa tekijällä $20{,}5 : 16 = 1{,}28$, joten teho ja lämpötilan nousu kasvavat tekijällä $1{,}28^2 = 1{,}64$, joten $30{,}4\,\text{K} \cdot 1{,}64 = 50\,\text{K}$.

## fy6-15-L3-05
**Annettu:** jännite $U = 230\,\text{V}$, kehon virtatien resistanssi $R_\text{k} = 1{,}5\,\text{k}\Omega$, vikavirtasuojan laukaisuraja $30\,\text{mA}$; eristysresistanssit taulukosta: $R_\text{e} = 900$; $120$; $40$; $12$ ja $4{,}0\,\text{k}\Omega$ viikoilla 1, 3, 5, 7 ja 9
**Kysytty:** a) ihmisen läpi kulkeva virta $I$ jokaisena viikkona; b) viikko, jona vikavirtasuoja laukeaa, ja miksi se ei yksin riitä; c) suurin $R_\text{e}$, jolla vikavirtasuoja laukeaa, kiloohmeina
**Periaate:** Vuoto kulkee vaihejohtimesta eristyksen läpi runkoon, rungosta ihmisen läpi maahan ja takaisin, joten resistanssit $R_\text{e}$ ja $R_\text{k}$ ovat sarjassa ja koko virtatien resistanssi on niiden summa (luku *Vastusten sarja- ja rinnankytkennät*). Sama virta kulkee ihmisen ja vikavirtasuojan läpi, ja se saadaan Ohmin laista. Vikavirtasuoja laukeaa, kun virta ylittää $I_\text{raja} = 30\,\text{mA}$, joten rajatilanteessa $R_\text{e} + R_\text{k} = U : I_\text{raja}$.
**Kaava:** $I = \dfrac{U}{R_\text{e} + R_\text{k}}$; rajalla $I_\text{raja} = \dfrac{U}{R_\text{e} + R_\text{k}}$, josta $R_\text{e} = \dfrac{U}{I_\text{raja}} - R_\text{k}$
**Muunnokset:** $R_\text{k} = 1{,}5\,\text{k}\Omega = 1500\,\Omega$; $I_\text{raja} = 30\,\text{mA} = 0{,}030\,\text{A}$; esimerkiksi $R_\text{e} = 900\,\text{k}\Omega = 900\,000\,\Omega$; virrat ampeereista milliampeereiksi: $1\,\text{A} = 1000\,\text{mA}$; tulos ohmeista kiloohmeiksi: $1\,\text{k}\Omega = 1000\,\Omega$.
**Sijoitus:** Rajalla $R_\text{e} = \dfrac{230\,\text{V}}{0{,}030\,\text{A}} - 1500\,\Omega = 7667\,\Omega - 1500\,\Omega = 6167\,\Omega = 6{,}167\,\text{k}\Omega$. Virrat: viikko 1: $\dfrac{230\,\text{V}}{900\,000\,\Omega + 1500\,\Omega} = 0{,}26\,\text{mA}$; viikko 3: $\dfrac{230\,\text{V}}{121\,500\,\Omega} = 1{,}9\,\text{mA}$; viikko 5: $\dfrac{230\,\text{V}}{41\,500\,\Omega} = 5{,}5\,\text{mA}$; viikko 7: $\dfrac{230\,\text{V}}{13\,500\,\Omega} = 17{,}0\,\text{mA}$; viikko 9: $\dfrac{230\,\text{V}}{5500\,\Omega} = 41{,}8\,\text{mA}$
**Vastaus:** $6{,}2\,\text{k}\Omega$, kaksi merkitsevää numeroa kuten kehon resistanssissa $1{,}5\,\text{k}\Omega$. Kohta b): vikavirtasuoja laukeaa vasta viikon 9 mittauksessa, jossa virta ylittää rajan; viikoilla 3, 5 ja 7 virta on tuntokynnyksen yläpuolella, ja viikolla 7 se ylittää myös irrottamiskynnyksen $10\,\text{mA}$, joten ote ei välttämättä irtoa, vaikka vikavirtasuoja ei laukea. Vikavirtasuoja suojaa vasta, kun virta on lähellä kammiovärinän vaaraa, joten rungon maadoituksen on oltava kunnossa ja laitteen käyttö on lopetettava, kun eristys on heikentynyt.
**Järkevyys:** Raja-arvolla $R_\text{e} = 6167\,\Omega$ koko resistanssi on $7667\,\Omega$ ja virta $230\,\text{V} : 7667\,\Omega = 30\,\text{mA}$. Viikon 9 resistanssi $4{,}0\,\text{k}\Omega$ on pienempi kuin raja, joten virta $41{,}8\,\text{mA}$ ylittää laukaisurajan. Viikon 7 resistanssi $12\,\text{k}\Omega$ on suurempi kuin raja, joten virta $17{,}0\,\text{mA}$ jää sen alle, vaikka ihmiselle se on jo vaarallinen.
