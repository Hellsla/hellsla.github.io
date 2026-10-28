## fy3-13-L1-01
**Annettu:** suora $p = p_0 + k\theta$, jossa $p_0 = 98{,}0\,\text{kPa}$ ja $k = 0{,}360\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$
**Kysytty:** lämpötila $\theta_0$ celsiusasteina, jossa suora antaa paineeksi $p = 0$
**Periaate:** Astia on suljettu ja jäykkä. Siksi kaasun ainemäärä ja tilavuus pysyvät vakioina, ja paine riippuu lämpötilasta lineaarisesti. Suoran yhtälö kuvaa siis kaasua mittausalueella. Suoraa voi jatkaa (ekstrapoloida) mittausalueen ulkopuolelle. Nollapaineen kohta saadaan asettamalla yhtälöön $p = 0$.
**Kaava:** $p = p_0 + k\theta$. Kun $p = 0$ ja $\theta = \theta_0$, niin $0 = p_0 + k\theta_0$, joten $\theta_0 = -\dfrac{p_0}{k}$
**Muunnokset:** Muunnoksia ei tarvita. Sekä $p_0$ että $k$ ovat kilopascaleina, joten kPa supistuu pois. Tulos jää celsiusasteiksi, kuten kysytään.
**Sijoitus:** $\theta_0 = -\dfrac{98{,}0\,\text{kPa}}{0{,}360\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -272{,}22\,{}^\circ\text{C}$
**Vastaus:** $-272\,{}^\circ\text{C}$. Vastauksessa on kolme merkitsevää numeroa, kuten arvoissa $98{,}0\,\text{kPa}$ ja $0{,}360$.
**Järkevyys:** Paine laskee $0{,}360\,\text{kPa}$ jokaista astetta kohti. Siksi $98\,\text{kPa}$ loppuu noin $98/0{,}36 \approx 270$ asteen jälkeen. Se on lähellä tulosta. Tulos on myös lähellä absoluuttista nollapistettä $-273{,}15\,{}^\circ\text{C}$. Tarkistus: $p = 98{,}0\,\text{kPa} + 0{,}360\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot (-272{,}22\,{}^\circ\text{C}) = 0\,\text{kPa}$.

## fy3-13-L1-02
**Annettu:** kaksi pistettä suoralta: $(\theta_1, p_1) = (20{,}0\,{}^\circ\text{C};\ 105{,}0\,\text{kPa})$ ja $(\theta_2, p_2) = (80{,}0\,{}^\circ\text{C};\ 127{,}0\,\text{kPa})$
**Kysytty:** suoran kulmakerroin $k$ yksikössä $\tfrac{\text{kPa}}{{}^\circ\text{C}}$
**Periaate:** Suljetussa jäykässä astiassa harvan kaasun paine on mittausalueella lämpötilan lineaarinen funktio. Siksi suoran kulmakerroin on kaikkialla sama. Se kertoo, kuinka monta kilopascalia paine kasvaa yhtä celsiusastetta kohti. Voit laskea sen mistä tahansa kahdesta suoran pisteestä.
**Kaava:** $k = \dfrac{\Delta p}{\Delta\theta}$, missä $\Delta p = p_2 - p_1$ ja $\Delta\theta = \theta_2 - \theta_1$, joten $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$
**Muunnokset:** Yksiköitä ei muunneta, sillä kulmakerroin kysytään yksikössä $\text{kPa}/{}^\circ\text{C}$. Lämpötilaero on $\Delta\theta = 80{,}0\,{}^\circ\text{C} - 20{,}0\,{}^\circ\text{C} = 60{,}0\,{}^\circ\text{C}$. Se on sama kelvineinä.
**Sijoitus:** $k = \dfrac{(127{,}0 - 105{,}0)\,\text{kPa}}{(80{,}0 - 20{,}0)\,{}^\circ\text{C}} = \dfrac{22{,}0\,\text{kPa}}{60{,}0\,{}^\circ\text{C}} = 0{,}36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$
**Vastaus:** $0{,}367\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$. Vastauksessa on kolme merkitsevää numeroa, koska molemmat erotukset tunnetaan kolmella numerolla. Ne ovat painemuutos $22{,}0\,\text{kPa}$ ja lämpötilaero $60{,}0\,{}^\circ\text{C}$.
**Järkevyys:** Kulmakerroin on positiivinen, koska paine kasvaa lämpötilan noustessa. Tarkistus: $105{,}0\,\text{kPa} + 0{,}36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot 60{,}0\,{}^\circ\text{C} = 127{,}0\,\text{kPa}$. Arvo on samaa suuruusluokkaa kuin muissa tämän luvun kokeissa ($0{,}36\ldots 0{,}39\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$).

## fy3-13-L1-03
**Annettu:** ryhmän tulos $\theta_0 = -267{,}90\,{}^\circ\text{C}$ ja hyväksytty arvo $\theta_\text{h} = -273{,}15\,{}^\circ\text{C}$
**Kysytty:** poikkeama $d$ celsiusasteina
**Periaate:** Mittausvirhe on tuloksen ja hyväksytyn arvon erotus. Sen etumerkki kertoo suunnan. Kysytty poikkeama on tämän erotuksen suuruus eli etäisyys. Se on positiivinen riippumatta siitä, onko tulos hyväksytyn arvon ylä- vai alapuolella. Siksi otetaan erotuksen itseisarvo.
**Kaava:** $d = |\theta_0 - \theta_\text{h}|$
**Muunnokset:** Molemmat arvot ovat celsiusasteina samalla asteikolla. Lämpötilojen erotus on sama celsiusasteina ja kelvineinä. Muunnoksia ei siis tarvita.
**Sijoitus:** $d = |-267{,}90\,{}^\circ\text{C} - (-273{,}15\,{}^\circ\text{C})| = |5{,}25\,{}^\circ\text{C}| = 5{,}25\,{}^\circ\text{C}$
**Vastaus:** $5{,}25\,{}^\circ\text{C}$. Vastauksessa on kolme merkitsevää numeroa. Molemmat lämpötilat, $-267{,}90\,{}^\circ\text{C}$ ja $-273{,}15\,{}^\circ\text{C}$, on annettu sadasosan tarkkuudella. Erotuksessa on yhtä monta desimaalia kuin epätarkimmassa luvussa.
**Järkevyys:** Ryhmän tulos on vähemmän negatiivinen kuin hyväksytty arvo. Siksi erotus on positiivinen ja tulos on hieman liian lämmin. Tarkistus: $-273{,}15\,{}^\circ\text{C} + 5{,}25\,{}^\circ\text{C} = -267{,}90\,{}^\circ\text{C}$. Poikkeama on vain noin $5{,}25/273 \approx 2\,\%$ koko ekstrapolointimatkasta. Tulos on siis hyvä.

## fy3-13-L1-04
**Annettu:** jyrkemmän ääriviivan nollapaineen lämpötila $\theta_{0,\text{max}} = -258\,{}^\circ\text{C}$ ja loivemman $\theta_{0,\text{min}} = -284\,{}^\circ\text{C}$
**Kysytty:** tuloksen epävarmuus $\Delta\theta_0$ celsiusasteina
**Periaate:** Kaikki suorat, jotka kulkevat kaikkien epävarmuusjanojen kautta, sopivat aineistoon yhtä hyvin. Niistä jyrkin ja loivin rajaavat välin, jolla todellinen nollapiste todennäköisesti on. Tulos kirjoitetaan muotoon $\theta_0 \pm \Delta\theta_0$. Siksi epävarmuus on välin puolikas.
**Kaava:** $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Muunnokset:** Molemmat lämpötilat ovat celsiusasteina, ja niiden erotus on sama kelvineinä. Muunnoksia ei siis tarvita.
**Sijoitus:** $\Delta\theta_0 = \dfrac{-258\,{}^\circ\text{C} - (-284\,{}^\circ\text{C})}{2} = \dfrac{26\,{}^\circ\text{C}}{2} = 13\,{}^\circ\text{C}$
**Vastaus:** $13\,{}^\circ\text{C}$. Vastauksessa on kaksi merkitsevää numeroa, koska ääriarvojen erotus $26\,{}^\circ\text{C}$ on annettu kokonaisina asteina eli kahdella numerolla. Jakaja $2$ on tarkka luku, eikä se rajoita.
**Järkevyys:** Välin keskikohta on $\dfrac{-258 + (-284)}{2}\,{}^\circ\text{C} = -271\,{}^\circ\text{C}$. Keskikohdasta pääsee $13\,{}^\circ\text{C}$ kumpaankin suuntaan täsmälleen ääriarvoihin $-258\,{}^\circ\text{C}$ ja $-284\,{}^\circ\text{C}$. Hyväksytty arvo $-273{,}15\,{}^\circ\text{C}$ kuuluu väliin. Tulos sopii siis sen kanssa yhteen.

## fy3-13-L1-05
**Annettu:** painemittarin lukema $p = 112\,\text{kPa}$ ja paineen lukeman arvioitu epävarmuus $\Delta p = 1{,}0\,\text{kPa}$
**Kysytty:** suhteellinen epävarmuus $\varepsilon$ prosentteina lukemasta
**Periaate:** Epävarmuuden merkitys riippuu siitä, kuinka suuri se on mitattuun arvoon verrattuna. Suhteellinen epävarmuus on epävarmuuden ja lukeman osamäärä. Kerro se luvulla $100\,\%$, niin saat prosentit.
**Kaava:** $\varepsilon = \dfrac{\Delta p}{p} \cdot 100\,\%$
**Muunnokset:** Molemmat paineet ovat kilopascaleina, joten yksikkö supistuu. Muunnoksia ei tarvita. Osamäärä on suhdeluku, ja kertominen luvulla $100\,\%$ muuttaa sen prosenteiksi.
**Sijoitus:** $\varepsilon = \dfrac{1{,}0\,\text{kPa}}{112\,\text{kPa}} \cdot 100\,\% = 0{,}8929\,\%$
**Vastaus:** $0{,}89\,\%$. Vastauksessa on kaksi merkitsevää numeroa, koska epävarmuus $1{,}0\,\text{kPa}$ on annettu kahdella numerolla. Lukema $112\,\text{kPa}$ on annettu kolmella numerolla, ja se rajoittaa vähemmän.
**Järkevyys:** Arvio: $\dfrac{1}{112} \approx \dfrac{1}{100} = 1\,\%$. Luku 112 on hieman yli sata, joten tulos on hieman alle prosentin. Jos lukema olisi vain $1\,\text{kPa}$, epävarmuus olisi $100\,\%$. Suuri lukema pienentää siis suhteellista epävarmuutta. Ekstrapoloinnissa tämä pieni epävarmuus silti kasvaa moninkertaiseksi.

## fy3-13-L2-01
**Annettu:** kaksi mittauspistettä $(\theta_1, p_1) = (15{,}0\,{}^\circ\text{C};\ 1{,}050\,\text{bar})$ ja $(\theta_2, p_2) = (95{,}0\,{}^\circ\text{C};\ 1{,}360\,\text{bar})$. Paine riippuu lämpötilasta lineaarisesti.
**Kysytty:** lämpötila $\theta_0$ celsiusasteina, jossa suora antaa nollapaineen
**Periaate:** Pullo on suljettu. Siksi ilman ainemäärä ja tilavuus pysyvät vakioina, ja paine on lämpötilan lineaarinen funktio. Kaksi pistettä määrää suoran. Suoraa jatketaan ekstrapoloimalla kohtaan, jossa $p = 0$.
**Kaava:** Kulmakerroin $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$. Suora pisteen 1 kautta on $p = p_1 + k(\theta - \theta_1)$, ja $p = 0$ antaa $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Muunnokset:** Molemmat paineet ovat barina. Osamäärässä $p_1/k$ yksikkö bar supistuu, joten pascaleiksi muuntamista ei tarvita. Lämpötilaero $95{,}0\,{}^\circ\text{C} - 15{,}0\,{}^\circ\text{C} = 80{,}0\,{}^\circ\text{C}$ on sama kelvineinä.
**Sijoitus:** $k = \dfrac{(1{,}360 - 1{,}050)\,\text{bar}}{(95{,}0 - 15{,}0)\,{}^\circ\text{C}} = \dfrac{0{,}310\,\text{bar}}{80{,}0\,{}^\circ\text{C}} = 0{,}003875\,\tfrac{\text{bar}}{{}^\circ\text{C}}$ ja $\theta_0 = 15{,}0\,{}^\circ\text{C} - \dfrac{1{,}050\,\text{bar}}{0{,}003875\,\tfrac{\text{bar}}{{}^\circ\text{C}}} = 15{,}0\,{}^\circ\text{C} - 270{,}97\,{}^\circ\text{C} = -255{,}97\,{}^\circ\text{C}$
**Vastaus:** $-256\,{}^\circ\text{C}$. Vastauksessa on kolme merkitsevää numeroa, koska paine-ero $0{,}310\,\text{bar}$ ja lämpötilaero $80{,}0\,{}^\circ\text{C}$ tunnetaan kolmella numerolla. Lopuksi vähennys $15{,}0 - 271$ antaa tuloksen kokonaisina asteina.
**Järkevyys:** Paine kasvaa noin $0{,}310\,\text{bar}$ kahdeksassakymmenessä asteessa. Yksi bar vastaa siis noin $270\,{}^\circ\text{C}$. Toinen tarkistus tehdään kelvineillä. Suhde $p_1/p_2 = 1{,}050/1{,}360 = 0{,}772$ on lähellä suhdetta $T_1/T_2 = 288{,}15/368{,}15 = 0{,}783$. Tulos on siis lähellä arvoa $-273{,}15\,{}^\circ\text{C}$. Ero johtuu kahden pisteen mittausvirheestä, joka kasvaa pitkässä ekstrapoloinnissa.

## fy3-13-L2-02
**Annettu:** kaksi ääriviivaa $p = 100\,\text{kPa} + 0{,}380\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot \theta$ (jyrkempi) ja $p = 102\,\text{kPa} + 0{,}350\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot \theta$ (loivempi)
**Kysytty:** epävarmuus $\Delta\theta_0$ celsiusasteina
**Periaate:** Molemmat suorat kulkevat kaikkien mittauspisteiden epävarmuusjanojen kautta. Todellinen suora on siis todennäköisesti niiden välissä. Ääriviivojen nollapaineen lämpötilat rajaavat nollapisteen arvioidun välin. Epävarmuus on tämän välin puolikas.
**Kaava:** Kummankin viivan nollapaine saadaan ehdosta $0 = p_0 + k\theta_0$, eli $\theta_0 = -\dfrac{p_0}{k}$. Jyrkempi antaa arvon $\theta_{0,\text{max}}$ ja loivempi arvon $\theta_{0,\text{min}}$, ja $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Muunnokset:** Muunnoksia ei tarvita. Suure $p_0$ on kilopascaleina ja $k$ yksikössä $\text{kPa}/{}^\circ\text{C}$, joten osamäärä on celsiusasteina.
**Sijoitus:** $\theta_{0,\text{max}} = -\dfrac{100\,\text{kPa}}{0{,}380\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -263{,}16\,{}^\circ\text{C}$ ja $\theta_{0,\text{min}} = -\dfrac{102\,\text{kPa}}{0{,}350\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -291{,}43\,{}^\circ\text{C}$. Siis $\Delta\theta_0 = \dfrac{-263{,}16\,{}^\circ\text{C} - (-291{,}43\,{}^\circ\text{C})}{2} = 14{,}14\,{}^\circ\text{C}$
**Vastaus:** $14\,{}^\circ\text{C}$. Vastauksessa on kaksi merkitsevää numeroa. Nollapisteet $-263\,{}^\circ\text{C}$ ja $-291\,{}^\circ\text{C}$ tunnetaan kolmella numerolla eli kokonaisina asteina. Niiden erotus $28\,{}^\circ\text{C}$ on vain kahden numeron luku. Jakaja $2$ on tarkka.
**Järkevyys:** Väli on $-277 \pm 14\,{}^\circ\text{C}$, sillä keskikohta on $\dfrac{-263{,}16 + (-291{,}43)}{2} = -277{,}3\,{}^\circ\text{C}$. Hyväksytty arvo $-273{,}15\,{}^\circ\text{C}$ kuuluu väliin, joten tulos on sopusoinnussa. Suuruusluokka on sama kuin luvun esimerkissä ($18\,{}^\circ\text{C}$), kun pisteet ja paineen lukeman epävarmuus ovat samanlaiset.

## fy3-13-L2-03
**Annettu:** ilmanpaine $p_\text{ilma} = 101{,}0\,\text{kPa}$. Mittarin ylipaine on $p_\text{y,1} = 9{,}0\,\text{kPa}$ lämpötilassa $\theta_1 = 30{,}0\,{}^\circ\text{C}$ ja $p_\text{y,2} = 31{,}0\,\text{kPa}$ lämpötilassa $\theta_2 = 90{,}0\,{}^\circ\text{C}$.
**Kysytty:** lämpötila $\theta_0$ celsiusasteina, jossa kaasun absoluuttinen paine on nolla
**Periaate:** Kaasun paine tarkoittaa absoluuttista painetta. Vain absoluuttinen paine on lineaarinen lämpötilan suhteen niin, että suoran nolla ennustaa tyhjiön. Mittari näyttää ylipainetta ilmanpaineeseen verrattuna. Siksi ilmanpaine on lisättävä ennen kuin suoraa sovitetaan.
**Kaava:** $p = p_\text{y} + p_\text{ilma}$. Sitten $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ ja nollapaineelle $0 = p_1 + k(\theta_0 - \theta_1)$, joten $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Muunnokset:** Muunna ylipaineet absoluuttisiksi paineiksi: $p_1 = 9{,}0\,\text{kPa} + 101{,}0\,\text{kPa} = 110{,}0\,\text{kPa}$ ja $p_2 = 31{,}0\,\text{kPa} + 101{,}0\,\text{kPa} = 132{,}0\,\text{kPa}$. Yksiköt ovat jo kilopascaleja ja celsiusasteita.
**Sijoitus:** $k = \dfrac{(132{,}0 - 110{,}0)\,\text{kPa}}{(90{,}0 - 30{,}0)\,{}^\circ\text{C}} = \dfrac{22{,}0\,\text{kPa}}{60{,}0\,{}^\circ\text{C}} = 0{,}36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ ja $\theta_0 = 30{,}0\,{}^\circ\text{C} - \dfrac{110{,}0\,\text{kPa}}{0{,}36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = 30{,}0\,{}^\circ\text{C} - 300\,{}^\circ\text{C} = -270\,{}^\circ\text{C}$
**Vastaus:** $-270\,{}^\circ\text{C}$. Vastauksessa on kolme merkitsevää numeroa, koska paine-ero $22{,}0\,\text{kPa}$ ja lämpötilaero $60{,}0\,{}^\circ\text{C}$ tunnetaan kolmella numerolla. Lopuksi vähennys $30{,}0 - 300$ antaa tuloksen kokonaisina asteina.
**Järkevyys:** Tulos on lähellä arvoa $-273{,}15\,{}^\circ\text{C}$, kuten pitääkin. Jos ilmanpainetta ei lisättäisi, ylipaineen suora menisi nollaan jo kohdassa $30{,}0 - 9{,}0/0{,}36667 = 5{,}5\,{}^\circ\text{C}$. Se on mahdotonta, koska huoneenlämpöinen kaasu ei ole lähelläkään tyhjiötä.

## fy3-13-L2-04
**Annettu:** lämpötilan lukematarkkuus $\Delta\theta = 0{,}50\,{}^\circ\text{C}$, suoran kulmakerroin $k = 0{,}36\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ ja paineen epävarmuus $\Delta p = 1{,}0\,\text{kPa}$
**Kysytty:** lämpötilan epävarmuutta vastaava paineen muutos $\Delta p_\theta$ prosentteina epävarmuudesta $\Delta p$
**Periaate:** Mittauspisteet ovat suoralla $p = p_0 + k\theta$. Lämpötilan virhe $\Delta\theta$ siirtää pistettä vaakasuunnassa. Suoran kohdalla se vastaa pystysuuntaista poikkeamaa $k\,\Delta\theta$. Kun virhe on muutettu paineeksi, sitä voi verrata suoraan paineen lukeman epävarmuuteen.
**Kaava:** $\Delta p_\theta = k\,\Delta\theta$ ja osuus $s = \dfrac{\Delta p_\theta}{\Delta p} \cdot 100\,\%$
**Muunnokset:** Muunnoksia ei tarvita. Celsiusasteet supistuvat tulossa $k\,\Delta\theta$, ja kilopascalit supistuvat osamäärässä. Kertominen luvulla $100\,\%$ muuttaa suhdeluvun prosenteiksi.
**Sijoitus:** $\Delta p_\theta = 0{,}36\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot 0{,}50\,{}^\circ\text{C} = 0{,}18\,\text{kPa}$ ja $s = \dfrac{0{,}18\,\text{kPa}}{1{,}0\,\text{kPa}} \cdot 100\,\% = 18\,\%$
**Vastaus:** $18\,\%$. Vastauksessa on kaksi merkitsevää numeroa, koska kulmakerroin $0{,}36\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ on annettu kahdella numerolla. Epävarmuudet $0{,}50\,{}^\circ\text{C}$ ja $1{,}0\,\text{kPa}$ ovat myös kahdella numerolla.
**Järkevyys:** Lämpötilan virhe vastaa vain noin viidesosaa paineen lukeman epävarmuudesta. Tuloksen tarkkuutta rajoittaa siis painemittari, ei lämpömittari. Rajatapaus: osuus olisi $100\,\%$, jos lämpötilan virhe olisi $1{,}0/0{,}36 = 2{,}8\,{}^\circ\text{C}$. Lämpömittarin pitäisi silloin olla paljon epätarkempi kuin nyt.

## fy3-13-L3-01
**Annettu:** päätepisteet $106{,}0 \pm 1{,}0\,\text{kPa}$ lämpötilassa $20{,}0\,{}^\circ\text{C}$ ja $137{,}0 \pm 1{,}0\,\text{kPa}$ lämpötilassa $100{,}0\,{}^\circ\text{C}$. Jyrkin ääriviiva kulkee pisteiden $(20{,}0\,{}^\circ\text{C};\ 105{,}0\,\text{kPa})$ ja $(100{,}0\,{}^\circ\text{C};\ 138{,}0\,\text{kPa})$ kautta. Loivin kulkee pisteiden $(20{,}0\,{}^\circ\text{C};\ 107{,}0\,\text{kPa})$ ja $(100{,}0\,{}^\circ\text{C};\ 136{,}0\,\text{kPa})$ kautta.
**Kysytty:** epävarmuus $\Delta\theta_0$ celsiusasteina ja syy siihen, miksi tulos on suurempi kuin seitsemän pisteen aineistolla
**Periaate:** Mitä jyrkemmän tai loivemman suoran sallitaan, sitä laajempi on nollapisteiden väli. Laske kummankin ääriviivan nollapaine suoran kahdesta pisteestä. Epävarmuus on näiden kahden arvon välin puolikas.
**Kaava:** Kummallekin suoralle $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ ja $\theta_0 = \theta_1 - \dfrac{p_1}{k}$, ja sitten $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Muunnokset:** Muunnoksia ei tarvita. Paineet ovat kilopascaleina ja lämpötilat celsiusasteina. Lämpötilaero $100{,}0\,{}^\circ\text{C} - 20{,}0\,{}^\circ\text{C} = 80{,}0\,{}^\circ\text{C}$ on sama kelvineinä.
**Sijoitus:** Jyrkin: $k = \dfrac{(138{,}0 - 105{,}0)\,\text{kPa}}{80{,}0\,{}^\circ\text{C}} = 0{,}4125\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ ja $\theta_0 = 20{,}0\,{}^\circ\text{C} - \dfrac{105{,}0\,\text{kPa}}{0{,}4125\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -234{,}55\,{}^\circ\text{C}$. Loivin: $k = \dfrac{(136{,}0 - 107{,}0)\,\text{kPa}}{80{,}0\,{}^\circ\text{C}} = 0{,}3625\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ ja $\theta_0 = 20{,}0\,{}^\circ\text{C} - \dfrac{107{,}0\,\text{kPa}}{0{,}3625\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -275{,}17\,{}^\circ\text{C}$. Siis $\Delta\theta_0 = \dfrac{-234{,}55 - (-275{,}17)}{2}\,{}^\circ\text{C} = 20{,}31\,{}^\circ\text{C}$
**Vastaus:** $20\,{}^\circ\text{C}$ (tarkasti $20{,}3\,{}^\circ\text{C}$). Vastauksessa on kaksi merkitsevää numeroa. Nollapisteet $-235\,{}^\circ\text{C}$ ja $-275\,{}^\circ\text{C}$ tunnetaan kolmella numerolla eli kokonaisina asteina. Niiden erotus $40\,{}^\circ\text{C}$ on kahden numeron luku. Kolmas numero vaatisi lähtöarvot sadasosan tarkkuudella, mikä ei sovi epävarmuuteen $\pm 1{,}0\,\text{kPa}$.
**Järkevyys:** Väli $-275{,}2\ldots -234{,}5\,{}^\circ\text{C}$ sisältää hyväksytyn arvon $-273{,}15\,{}^\circ\text{C}$. Tulos on suurempi kuin seitsemän pisteen aineiston $18\,{}^\circ\text{C}$, kuten pitääkin. Kahden pisteen suoralla ei ole muita rajoitteita. Jyrkin suora saa siis nousta toisessa päässä ja laskea toisessa epävarmuusjanan ääreen. Seitsemän pisteen aineistossa jokaisen suoran täytyy kulkea myös viiden välipisteen janojen kautta. Se kaventaa sallittujen kulmakertoimien väliä.

## fy3-13-L3-02
**Annettu:** $p_0 = 100{,}0\,\text{kPa}$ lämpötilassa $0\,{}^\circ\text{C}$, tavoitelämpötila $T = 77{,}0\,\text{K}$ ja $p \propto T$ kelvineinä. Typpi tiivistyy tässä paineessa nesteeksi vasta noin $67\,\text{K}$:ssä.
**Kysytty:** paine $p$ lämpötilassa $77{,}0\,\text{K}$ kilopascaleina ja perustelu sille, miksi suoraa ei voi jatkaa nollaan asti
**Periaate:** Jäykässä suljetussa astiassa kaasun ainemäärä ja tilavuus pysyvät vakioina. Siksi paine on suoraan verrannollinen kelvinlämpötilaan, ja $\dfrac{p}{T}$ on vakio. Verrannollisuus pätee vain kelvineinä, koska vain kelvinasteikon nolla on absoluuttinen nollapiste. Se edellyttää myös, että kaasu pysyy kaasuna.
**Kaava:** $\dfrac{p}{T} = \dfrac{p_0}{T_0}$, joten $p = p_0\,\dfrac{T}{T_0}$
**Muunnokset:** Muunna lähtölämpötila kelvineiksi: $T_0 = 0\,{}^\circ\text{C} = 273{,}15\,\text{K}$. Lämpötila $77{,}0\,\text{K}$ on jo kelvineinä. Suhteessa $T/T_0$ kelvinit supistuvat, joten paine jää kilopascaleiksi.
**Sijoitus:** $p = 100{,}0\,\text{kPa} \cdot \dfrac{77{,}0\,\text{K}}{273{,}15\,\text{K}} = 28{,}19\,\text{kPa}$
**Vastaus:** $28{,}2\,\text{kPa}$. Vastauksessa on kolme merkitsevää numeroa, koska lämpötila $77{,}0\,\text{K}$ on annettu kolmella numerolla. Luku $273{,}15\,\text{K}$ on määritelmä, eikä se rajoita. Suoraa ei voi jatkaa nollaan asti, koska typpi tiivistyy nesteeksi noin $67\,\text{K}$:ssä. Silloin kaasun ainemäärä pienenee ja paine putoaa nopeammin kuin suora ennustaa. Ehto "ainemäärä vakio" ei enää päde.
**Järkevyys:** Lämpötila $77{,}0\,\text{K}$ on noin $0{,}28$-kertainen lämpötilaan $273{,}15\,\text{K}$ verrattuna. Paine on samassa suhteessa: noin $0{,}28 \cdot 100 = 28\,\text{kPa}$. Suora antaisi lämpötilassa $67\,\text{K}$ paineen $100 \cdot 67/273{,}15 = 24{,}5\,\text{kPa}$. Noin siinä lämpötilassa kaasu alkaa tiivistyä nesteeksi. Sen jälkeen paine ei enää noudata suoraa. Ekstrapolointi on siis luotettava vain niin pitkälle kuin oletus kaasusta pitää paikkansa.

## fy3-13-L3-03
**Annettu:** ryhmän A tulos $\theta_0 = -262{,}00\,{}^\circ\text{C}$ ja epävarmuus $\Delta\theta_0 = 6{,}00\,{}^\circ\text{C}$. Hyväksytty arvo on $\theta_\text{h} = -273{,}15\,{}^\circ\text{C}$.
**Kysytty:** poikkeaman suhde epävarmuuteen $n$ (kuinka monta kertaa $\Delta\theta_0$ mahtuu tuloksen ja hyväksytyn arvon väliin) ja syy ristiriitaan
**Periaate:** Tässä luvussa tulosta pidetään sopusoinnussa hyväksytyn arvon kanssa, jos arvo kuuluu epävarmuusväliin $\theta_0 \pm \Delta\theta_0$. Silloin poikkeama on korkeintaan yksi epävarmuus. Suhde $n$ kertoo, kuinka moninkertainen poikkeama on epävarmuuteen verrattuna. Epävarmuus ei ole ehdoton raja. Siksi poikkeama ei yksin todista virhettä. Mitä suurempi $n$ on, sitä todennäköisemmin mittauksessa on systemaattinen virhe tai epävarmuus on arvioitu liian pieneksi.
**Kaava:** $n = \dfrac{|\theta_0 - \theta_\text{h}|}{\Delta\theta_0}$
**Muunnokset:** Kaikki lämpötilat ovat celsiusasteina, ja lämpötilaerot ovat samat kelvineinä. Suhde $n$ on dimensioton. Muunnoksia ei siis tarvita.
**Sijoitus:** $n = \dfrac{|-262{,}00\,{}^\circ\text{C} - (-273{,}15\,{}^\circ\text{C})|}{6{,}00\,{}^\circ\text{C}} = \dfrac{11{,}15\,{}^\circ\text{C}}{6{,}00\,{}^\circ\text{C}} = 1{,}858$
**Vastaus:** $1{,}86$ kertaa. Vastauksessa on kolme merkitsevää numeroa, koska erotus $11{,}15\,{}^\circ\text{C}$ ja epävarmuus $6{,}00\,{}^\circ\text{C}$ on annettu kolmella numerolla. Tulos $-262{,}00\,{}^\circ\text{C}$ ja hyväksytty arvo ovat sadasosan tarkkuudella.
**Järkevyys:** Poikkeama $11{,}15\,{}^\circ\text{C}$ on lähes kaksi epävarmuutta ($2 \cdot 6{,}00 = 12{,}0$). Epävarmuusväli $-268\ldots -256\,{}^\circ\text{C}$ ei sisällä hyväksyttyä arvoa $-273{,}15\,{}^\circ\text{C}$. Tämän säännön mukaan tulos ei siis ole sopusoinnussa arvon kanssa. Syynä voi olla systemaattinen virhe, esimerkiksi epätarkka lämpömittari, ilmavuoto tai pullon tilavuuden muutos. Syynä voi olla myös liian pieneksi arvioitu epävarmuus. Tarkistus: $1{,}858 \cdot 6{,}00\,{}^\circ\text{C} = 11{,}15\,{}^\circ\text{C}$.
