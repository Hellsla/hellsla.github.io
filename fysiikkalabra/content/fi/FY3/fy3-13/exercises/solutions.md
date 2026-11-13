## fy3-13-L1-01
**Annettu:** suora $p = p_0 + k\theta$, jossa $p_0 = 98{,}0\,\text{kPa}$ ja $k = 0{,}360\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$
**Kysytty:** lämpötila $\theta_0$ celsiusasteina, jossa suora antaa paineeksi $p = 0$
**Periaate:** Astia on suljettu ja jäykkä, joten kaasun ainemäärä ja tilavuus pysyvät vakioina ja paine riippuu lämpötilasta lineaarisesti. Siksi suoran yhtälö kuvaa kaasua mittausalueella, ja suoraa voi jatkaa (ekstrapoloida) sen ulkopuolelle: nollapaineen kohta saadaan asettamalla yhtälöön $p = 0$.
**Kaava:** $p = p_0 + k\theta$. Kun $p = 0$ ja $\theta = \theta_0$, niin $0 = p_0 + k\theta_0$, joten $\theta_0 = -\dfrac{p_0}{k}$
**Muunnokset:** Muunnoksia ei tarvita: $p_0$ ja $k$ ovat kilopascaleina, joten kPa supistuu pois ja tulos jää celsiusasteiksi, kuten kysytään.
**Sijoitus:** $\theta_0 = -\dfrac{98{,}0\,\text{kPa}}{0{,}360\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -272{,}22\,{}^\circ\text{C}$
**Vastaus:** $-272\,{}^\circ\text{C}$, kolme merkitsevää numeroa kuten arvoissa $98{,}0\,\text{kPa}$ ja $0{,}360$.
**Järkevyys:** Paine laskee $0{,}360\,\text{kPa}$ jokaista astetta kohti, joten $98\,\text{kPa}$ loppuu noin $98/0{,}36 \approx 270$ asteen jälkeen, mikä on lähellä tulosta. Tulos on myös lähellä absoluuttista nollapistettä $-273{,}15\,{}^\circ\text{C}$. Tarkistus: $p = 98{,}0\,\text{kPa} + 0{,}360\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot (-272{,}22\,{}^\circ\text{C}) = 0\,\text{kPa}$.

## fy3-13-L1-02
**Annettu:** kaksi pistettä suoralta: $(\theta_1, p_1) = (20{,}0\,{}^\circ\text{C};\ 105{,}0\,\text{kPa})$ ja $(\theta_2, p_2) = (80{,}0\,{}^\circ\text{C};\ 127{,}0\,\text{kPa})$
**Kysytty:** suoran kulmakerroin $k$ yksikössä $\tfrac{\text{kPa}}{{}^\circ\text{C}}$
**Periaate:** Suljetussa jäykässä astiassa harvan kaasun paine on mittausalueella lämpötilan lineaarinen funktio, joten suoran kulmakerroin on kaikkialla sama: se kertoo, kuinka monta kilopascalia paine kasvaa yhtä celsiusastetta kohti. Sen voi siksi laskea mistä tahansa kahdesta suoran pisteestä.
**Kaava:** $k = \dfrac{\Delta p}{\Delta\theta}$, missä $\Delta p = p_2 - p_1$ ja $\Delta\theta = \theta_2 - \theta_1$, joten $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$
**Muunnokset:** Yksiköitä ei muunneta, sillä kulmakerroin kysytään yksikössä $\text{kPa}/{}^\circ\text{C}$. Lämpötilaero on $\Delta\theta = 80{,}0\,{}^\circ\text{C} - 20{,}0\,{}^\circ\text{C} = 60{,}0\,{}^\circ\text{C}$, ja se on sama kelvineinä.
**Sijoitus:** $k = \dfrac{(127{,}0 - 105{,}0)\,\text{kPa}}{(80{,}0 - 20{,}0)\,{}^\circ\text{C}} = \dfrac{22{,}0\,\text{kPa}}{60{,}0\,{}^\circ\text{C}} = 0{,}36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$
**Vastaus:** $0{,}367\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$, kolme merkitsevää numeroa, koska molemmat erotukset, painemuutos $22{,}0\,\text{kPa}$ ja lämpötilaero $60{,}0\,{}^\circ\text{C}$, tunnetaan kolmella numerolla.
**Järkevyys:** Kulmakerroin on positiivinen, koska paine kasvaa lämpötilan noustessa. Tarkistus: $105{,}0\,\text{kPa} + 0{,}36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot 60{,}0\,{}^\circ\text{C} = 127{,}0\,\text{kPa}$. Arvo on samaa suuruusluokkaa kuin muissa tämän luvun kokeissa ($0{,}36\ldots 0{,}39\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$).

## fy3-13-L1-03
**Annettu:** ryhmän tulos $\theta_0 = -267{,}90\,{}^\circ\text{C}$ ja hyväksytty arvo $\theta_\text{h} = -273{,}15\,{}^\circ\text{C}$
**Kysytty:** poikkeama $d$ celsiusasteina
**Periaate:** Mittausvirhe on tuloksen ja hyväksytyn arvon erotus, ja sen etumerkki kertoo suunnan. Kysytty poikkeama on tämän erotuksen suuruus eli etäisyys, joka on positiivinen riippumatta siitä, onko tulos hyväksytyn arvon ylä- vai alapuolella, joten otetaan erotuksen itseisarvo.
**Kaava:** $d = |\theta_0 - \theta_\text{h}|$
**Muunnokset:** Molemmat arvot ovat celsiusasteina samalla asteikolla. Lämpötilojen erotus on sama celsiusasteina ja kelvineinä, joten muunnoksia ei tarvita.
**Sijoitus:** $d = |-267{,}90\,{}^\circ\text{C} - (-273{,}15\,{}^\circ\text{C})| = |5{,}25\,{}^\circ\text{C}| = 5{,}25\,{}^\circ\text{C}$
**Vastaus:** $5{,}25\,{}^\circ\text{C}$, kolme merkitsevää numeroa, koska molemmat lämpötilat, $-267{,}90\,{}^\circ\text{C}$ ja $-273{,}15\,{}^\circ\text{C}$, on annettu sadasosan tarkkuudella ja erotuksessa on yhtä monta desimaalia kuin epätarkimmassa luvussa.
**Järkevyys:** Ryhmän tulos on vähemmän negatiivinen kuin hyväksytty arvo, joten erotus on positiivinen ja tulos on hieman liian lämmin. Tarkistus: $-273{,}15\,{}^\circ\text{C} + 5{,}25\,{}^\circ\text{C} = -267{,}90\,{}^\circ\text{C}$. Poikkeama on vain noin $5{,}25/273 \approx 2\,\%$ koko ekstrapolointimatkasta, joten tulos on hyvä.

## fy3-13-L1-04
**Annettu:** jyrkemmän ääriviivan nollapaineen lämpötila $\theta_{0,\text{max}} = -258\,{}^\circ\text{C}$ ja loivemman $\theta_{0,\text{min}} = -284\,{}^\circ\text{C}$
**Kysytty:** tuloksen epävarmuus $\Delta\theta_0$ celsiusasteina
**Periaate:** Kaikki suorat, jotka kulkevat kaikkien epävarmuusjanojen kautta, sopivat aineistoon yhtä hyvin. Jyrkin ja loivin niistä rajaavat välin, jolla todellinen nollapiste todennäköisesti on. Tulos kirjoitetaan muotoon $\theta_0 \pm \Delta\theta_0$, joten epävarmuus on välin puolikas.
**Kaava:** $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Muunnokset:** Molemmat lämpötilat ovat celsiusasteina, ja niiden erotus on sama kelvineinä, joten muunnoksia ei tarvita.
**Sijoitus:** $\Delta\theta_0 = \dfrac{-258\,{}^\circ\text{C} - (-284\,{}^\circ\text{C})}{2} = \dfrac{26\,{}^\circ\text{C}}{2} = 13\,{}^\circ\text{C}$
**Vastaus:** $13\,{}^\circ\text{C}$, kaksi merkitsevää numeroa, koska ääriarvojen erotus $26\,{}^\circ\text{C}$ on annettu kokonaisina asteina eli kahdella numerolla; jakaja $2$ on tarkka luku eikä rajoita.
**Järkevyys:** Välin keskikohta on $\dfrac{-258 + (-284)}{2}\,{}^\circ\text{C} = -271\,{}^\circ\text{C}$, ja siitä $13\,{}^\circ\text{C}$ kumpaankin suuntaan päästään täsmälleen ääriarvoihin $-258\,{}^\circ\text{C}$ ja $-284\,{}^\circ\text{C}$. Hyväksytty arvo $-273{,}15\,{}^\circ\text{C}$ kuuluu väliin, joten tulos sopii sen kanssa yhteen.

## fy3-13-L1-05
**Annettu:** painemittarin lukema $p = 112\,\text{kPa}$ ja paineen lukeman arvioitu epävarmuus $\Delta p = 1{,}0\,\text{kPa}$
**Kysytty:** suhteellinen epävarmuus $\varepsilon$ prosentteina lukemasta
**Periaate:** Epävarmuuden merkitys riippuu siitä, kuinka suuri se on mitattuun arvoon verrattuna. Suhteellinen epävarmuus on epävarmuuden ja lukeman osamäärä, ja kertomalla se luvulla $100\,\%$ saadaan prosentit.
**Kaava:** $\varepsilon = \dfrac{\Delta p}{p} \cdot 100\,\%$
**Muunnokset:** Molemmat paineet ovat kilopascaleina, joten yksikkö supistuu eikä muunnoksia tarvita. Osamäärä on suhdeluku, ja kertominen luvulla $100\,\%$ muuttaa sen prosenteiksi.
**Sijoitus:** $\varepsilon = \dfrac{1{,}0\,\text{kPa}}{112\,\text{kPa}} \cdot 100\,\% = 0{,}8929\,\%$
**Vastaus:** $0{,}89\,\%$, kaksi merkitsevää numeroa, koska epävarmuus $1{,}0\,\text{kPa}$ on annettu kahdella numerolla (lukema $112\,\text{kPa}$ on kolmella ja rajoittaa vähemmän).
**Järkevyys:** Arviona $\dfrac{1}{112} \approx \dfrac{1}{100} = 1\,\%$, ja koska 112 on hieman yli sata, tulos on hieman alle prosentin. Jos lukema olisi vain $1\,\text{kPa}$, epävarmuus olisi $100\,\%$, joten suuri lukema pienentää suhteellista epävarmuutta. Ekstrapoloinnissa tämä pieni epävarmuus silti kasvaa moninkertaiseksi.

## fy3-13-L2-01
**Annettu:** kaksi mittauspistettä $(\theta_1, p_1) = (15{,}0\,{}^\circ\text{C};\ 1{,}050\,\text{bar})$ ja $(\theta_2, p_2) = (95{,}0\,{}^\circ\text{C};\ 1{,}360\,\text{bar})$; paine riippuu lämpötilasta lineaarisesti
**Kysytty:** lämpötila $\theta_0$ celsiusasteina, jossa suora antaa nollapaineen
**Periaate:** Pullo on suljettu, joten ilman ainemäärä ja tilavuus pysyvät vakioina ja paine on lämpötilan lineaarinen funktio. Kaksi pistettä määrää suoran, ja sitä jatketaan ekstrapoloimalla kohtaan, jossa $p = 0$.
**Kaava:** Kulmakerroin $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$. Suora pisteen 1 kautta on $p = p_1 + k(\theta - \theta_1)$, ja $p = 0$ antaa $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Muunnokset:** Molemmat paineet ovat barina. Osamäärässä $p_1/k$ yksikkö bar supistuu, joten pascaleiksi muuntamista ei tarvita. Lämpötilaero $95{,}0\,{}^\circ\text{C} - 15{,}0\,{}^\circ\text{C} = 80{,}0\,{}^\circ\text{C}$ on sama kelvineinä.
**Sijoitus:** $k = \dfrac{(1{,}360 - 1{,}050)\,\text{bar}}{(95{,}0 - 15{,}0)\,{}^\circ\text{C}} = \dfrac{0{,}310\,\text{bar}}{80{,}0\,{}^\circ\text{C}} = 0{,}003875\,\tfrac{\text{bar}}{{}^\circ\text{C}}$ ja $\theta_0 = 15{,}0\,{}^\circ\text{C} - \dfrac{1{,}050\,\text{bar}}{0{,}003875\,\tfrac{\text{bar}}{{}^\circ\text{C}}} = 15{,}0\,{}^\circ\text{C} - 270{,}97\,{}^\circ\text{C} = -255{,}97\,{}^\circ\text{C}$
**Vastaus:** $-256\,{}^\circ\text{C}$, kolme merkitsevää numeroa, koska paine-ero $0{,}310\,\text{bar}$ ja lämpötilaero $80{,}0\,{}^\circ\text{C}$ tunnetaan kolmella numerolla; lopuksi vähennys $15{,}0 - 271$ antaa tuloksen kokonaisina asteina.
**Järkevyys:** Paine kasvaa noin $0{,}310\,\text{bar}$ kahdeksassakymmenessä asteessa, joten yksi bar vastaa noin $270\,{}^\circ\text{C}$. Toinen tarkistus kelvineillä: suhde $p_1/p_2 = 1{,}050/1{,}360 = 0{,}772$ on lähellä suhdetta $T_1/T_2 = 288{,}15/368{,}15 = 0{,}783$. Tulos on siis lähellä arvoa $-273{,}15\,{}^\circ\text{C}$, ja ero johtuu kahden pisteen mittausvirheestä, joka kasvaa pitkässä ekstrapoloinnissa.

## fy3-13-L2-02
**Annettu:** kaksi ääriviivaa $p = 100\,\text{kPa} + 0{,}380\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot \theta$ (jyrkempi) ja $p = 102\,\text{kPa} + 0{,}350\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot \theta$ (loivempi)
**Kysytty:** epävarmuus $\Delta\theta_0$ celsiusasteina
**Periaate:** Molemmat suorat kulkevat kaikkien mittauspisteiden epävarmuusjanojen kautta, joten todellinen suora on todennäköisesti niiden välissä. Ääriviivojen nollapaineen lämpötilat rajaavat nollapisteen arvioidun välin, ja epävarmuus on tämän välin puolikas.
**Kaava:** Kummankin viivan nollapaine saadaan ehdosta $0 = p_0 + k\theta_0$, eli $\theta_0 = -\dfrac{p_0}{k}$. Jyrkempi antaa arvon $\theta_{0,\text{max}}$ ja loivempi arvon $\theta_{0,\text{min}}$, ja $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Muunnokset:** Muunnoksia ei tarvita: $p_0$ on kilopascaleina ja $k$ yksikössä $\text{kPa}/{}^\circ\text{C}$, joten osamäärä on celsiusasteina.
**Sijoitus:** $\theta_{0,\text{max}} = -\dfrac{100\,\text{kPa}}{0{,}380\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -263{,}16\,{}^\circ\text{C}$ ja $\theta_{0,\text{min}} = -\dfrac{102\,\text{kPa}}{0{,}350\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -291{,}43\,{}^\circ\text{C}$. Siis $\Delta\theta_0 = \dfrac{-263{,}16\,{}^\circ\text{C} - (-291{,}43\,{}^\circ\text{C})}{2} = 14{,}14\,{}^\circ\text{C}$
**Vastaus:** $14\,{}^\circ\text{C}$, kaksi merkitsevää numeroa, koska nollapisteet $-263\,{}^\circ\text{C}$ ja $-291\,{}^\circ\text{C}$ tunnetaan kolmella numerolla eli kokonaisina asteina, ja niiden erotus $28\,{}^\circ\text{C}$ on vain kahden numeron luku; jakaja $2$ on tarkka.
**Järkevyys:** Väli on $-277 \pm 14\,{}^\circ\text{C}$, sillä keskikohta on $\dfrac{-263{,}16 + (-291{,}43)}{2} = -277{,}3\,{}^\circ\text{C}$. Hyväksytty arvo $-273{,}15\,{}^\circ\text{C}$ kuuluu väliin, joten tulos on sopusoinnussa. Suuruusluokka on sama kuin luvun esimerkissä ($18\,{}^\circ\text{C}$), kun pisteet ja paineen lukeman epävarmuus ovat samanlaiset.

## fy3-13-L2-03
**Annettu:** ilmanpaine $p_\text{ilma} = 101{,}0\,\text{kPa}$; mittarin ylipaine $p_\text{y,1} = 9{,}0\,\text{kPa}$ lämpötilassa $\theta_1 = 30{,}0\,{}^\circ\text{C}$ ja $p_\text{y,2} = 31{,}0\,\text{kPa}$ lämpötilassa $\theta_2 = 90{,}0\,{}^\circ\text{C}$
**Kysytty:** lämpötila $\theta_0$ celsiusasteina, jossa kaasun absoluuttinen paine on nolla
**Periaate:** Kaasun paine tarkoittaa absoluuttista painetta, ja vain se on lineaarinen lämpötilan suhteen niin, että suoran nolla ennustaa tyhjiön. Mittari näyttää ylipainetta ilmanpaineeseen verrattuna, joten ilmanpaine on lisättävä ennen kuin suoraa sovitetaan.
**Kaava:** $p = p_\text{y} + p_\text{ilma}$. Sitten $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ ja nollapaineelle $0 = p_1 + k(\theta_0 - \theta_1)$, joten $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Muunnokset:** Ylipaineet muunnetaan absoluuttisiksi paineiksi: $p_1 = 9{,}0\,\text{kPa} + 101{,}0\,\text{kPa} = 110{,}0\,\text{kPa}$ ja $p_2 = 31{,}0\,\text{kPa} + 101{,}0\,\text{kPa} = 132{,}0\,\text{kPa}$. Yksiköt ovat jo kilopascaleja ja celsiusasteita.
**Sijoitus:** $k = \dfrac{(132{,}0 - 110{,}0)\,\text{kPa}}{(90{,}0 - 30{,}0)\,{}^\circ\text{C}} = \dfrac{22{,}0\,\text{kPa}}{60{,}0\,{}^\circ\text{C}} = 0{,}36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ ja $\theta_0 = 30{,}0\,{}^\circ\text{C} - \dfrac{110{,}0\,\text{kPa}}{0{,}36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = 30{,}0\,{}^\circ\text{C} - 300\,{}^\circ\text{C} = -270\,{}^\circ\text{C}$
**Vastaus:** $-270\,{}^\circ\text{C}$, kolme merkitsevää numeroa, koska paine-ero $22{,}0\,\text{kPa}$ ja lämpötilaero $60{,}0\,{}^\circ\text{C}$ tunnetaan kolmella numerolla; lopuksi vähennys $30{,}0 - 300$ antaa tuloksen kokonaisina asteina.
**Järkevyys:** Tulos on lähellä arvoa $-273{,}15\,{}^\circ\text{C}$, kuten pitääkin. Jos ilmanpainetta ei lisättäisi, ylipaineen suora menisi nollaan jo kohdassa $30{,}0 - 9{,}0/0{,}36667 = 5{,}5\,{}^\circ\text{C}$, mikä on mahdotonta, koska huoneenlämpöinen kaasu ei ole lähelläkään tyhjiötä.

## fy3-13-L2-04
**Annettu:** lämpötilan lukematarkkuus $\Delta\theta = 0{,}50\,{}^\circ\text{C}$, suoran kulmakerroin $k = 0{,}36\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ ja paineen epävarmuus $\Delta p = 1{,}0\,\text{kPa}$
**Kysytty:** lämpötilan epävarmuutta vastaava paineen muutos $\Delta p_\theta$ prosentteina epävarmuudesta $\Delta p$
**Periaate:** Mittauspisteet ovat suoralla $p = p_0 + k\theta$, joten lämpötilan virhe $\Delta\theta$ siirtää pistettä vaakasuunnassa, ja suoran kohdalla se vastaa pystysuuntaista poikkeamaa $k\,\Delta\theta$. Kun se muutetaan paineeksi, sitä voi verrata suoraan paineen lukeman epävarmuuteen.
**Kaava:** $\Delta p_\theta = k\,\Delta\theta$ ja osuus $s = \dfrac{\Delta p_\theta}{\Delta p} \cdot 100\,\%$
**Muunnokset:** Muunnoksia ei tarvita: celsiusasteet supistuvat tulossa $k\,\Delta\theta$, ja kilopascalit supistuvat osamäärässä. Kertominen luvulla $100\,\%$ muuttaa suhdeluvun prosenteiksi.
**Sijoitus:** $\Delta p_\theta = 0{,}36\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot 0{,}50\,{}^\circ\text{C} = 0{,}18\,\text{kPa}$ ja $s = \dfrac{0{,}18\,\text{kPa}}{1{,}0\,\text{kPa}} \cdot 100\,\% = 18\,\%$
**Vastaus:** $18\,\%$, kaksi merkitsevää numeroa, koska kulmakerroin $0{,}36\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ on annettu kahdella numerolla; epävarmuudet $0{,}50\,{}^\circ\text{C}$ ja $1{,}0\,\text{kPa}$ ovat myös kahdella numerolla.
**Järkevyys:** Lämpötilan virhe vastaa vain noin viidesosaa paineen lukeman epävarmuudesta, joten tuloksen tarkkuutta rajoittaa painemittari, ei lämpömittari. Rajatapaus: osuus olisi $100\,\%$, jos lämpötilan virhe olisi $1{,}0/0{,}36 = 2{,}8\,{}^\circ\text{C}$, eli lämpömittarin pitäisi olla paljon epätarkempi kuin nyt.

## fy3-13-L3-01
**Annettu:** päätepisteet $106{,}0 \pm 1{,}0\,\text{kPa}$ lämpötilassa $20{,}0\,{}^\circ\text{C}$ ja $137{,}0 \pm 1{,}0\,\text{kPa}$ lämpötilassa $100{,}0\,{}^\circ\text{C}$. Jyrkin ääriviiva kulkee pisteiden $(20{,}0\,{}^\circ\text{C};\ 105{,}0\,\text{kPa})$ ja $(100{,}0\,{}^\circ\text{C};\ 138{,}0\,\text{kPa})$, loivin pisteiden $(20{,}0\,{}^\circ\text{C};\ 107{,}0\,\text{kPa})$ ja $(100{,}0\,{}^\circ\text{C};\ 136{,}0\,\text{kPa})$ kautta
**Kysytty:** epävarmuus $\Delta\theta_0$ celsiusasteina ja syy siihen, miksi tulos on suurempi kuin seitsemän pisteen aineistolla
**Periaate:** Mitä jyrkempi tai loivempi suora sallitaan, sitä laajempi on nollapisteiden väli. Kummankin ääriviivan nollapaine lasketaan suoran kahdesta pisteestä, ja epävarmuus on näiden kahden arvon välin puolikas.
**Kaava:** Kummallekin suoralle $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ ja $\theta_0 = \theta_1 - \dfrac{p_1}{k}$, ja sitten $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Muunnokset:** Muunnoksia ei tarvita: paineet ovat kilopascaleina ja lämpötilat celsiusasteina, ja lämpötilaero $100{,}0\,{}^\circ\text{C} - 20{,}0\,{}^\circ\text{C} = 80{,}0\,{}^\circ\text{C}$ on sama kelvineinä.
**Sijoitus:** Jyrkin: $k = \dfrac{(138{,}0 - 105{,}0)\,\text{kPa}}{80{,}0\,{}^\circ\text{C}} = 0{,}4125\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ ja $\theta_0 = 20{,}0\,{}^\circ\text{C} - \dfrac{105{,}0\,\text{kPa}}{0{,}4125\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -234{,}55\,{}^\circ\text{C}$. Loivin: $k = \dfrac{(136{,}0 - 107{,}0)\,\text{kPa}}{80{,}0\,{}^\circ\text{C}} = 0{,}3625\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ ja $\theta_0 = 20{,}0\,{}^\circ\text{C} - \dfrac{107{,}0\,\text{kPa}}{0{,}3625\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -275{,}17\,{}^\circ\text{C}$. Siis $\Delta\theta_0 = \dfrac{-234{,}55 - (-275{,}17)}{2}\,{}^\circ\text{C} = 20{,}31\,{}^\circ\text{C}$
**Vastaus:** $20\,{}^\circ\text{C}$ (tarkasti $20{,}3\,{}^\circ\text{C}$), kaksi merkitsevää numeroa, koska nollapisteet $-235\,{}^\circ\text{C}$ ja $-275\,{}^\circ\text{C}$ tunnetaan kolmella numerolla eli kokonaisina asteina ja niiden erotus $40\,{}^\circ\text{C}$ on kahden numeron luku. Kolmas numero vaatisi lähtöarvot sadasosan tarkkuudella, mikä ei sovi epävarmuuteen $\pm 1{,}0\,\text{kPa}$.
**Järkevyys:** Väli $-275{,}2\ldots -234{,}5\,{}^\circ\text{C}$ sisältää hyväksytyn arvon $-273{,}15\,{}^\circ\text{C}$. Tulos on suurempi kuin seitsemän pisteen aineiston $18\,{}^\circ\text{C}$, kuten pitääkin: kahden pisteen suoralla ei ole muita rajoitteita, joten jyrkin suora saa nousta toisessa päässä ja laskea toisessa epävarmuusjanan ääreen. Seitsemän pisteen aineistossa jokaisen suoran täytyy kulkea myös viiden välipisteen janojen kautta, mikä kaventaa sallittujen kulmakertoimien väliä.

## fy3-13-L3-02
**Annettu:** $p_0 = 100{,}0\,\text{kPa}$ lämpötilassa $0\,{}^\circ\text{C}$, tavoitelämpötila $T = 77{,}0\,\text{K}$ ja $p \propto T$ kelvineinä; typpi tiivistyy tässä paineessa nesteeksi vasta noin $67\,\text{K}$:ssä
**Kysytty:** paine $p$ lämpötilassa $77{,}0\,\text{K}$ kilopascaleina ja perustelu sille, miksi suoraa ei voi jatkaa nollaan asti
**Periaate:** Jäykässä suljetussa astiassa kaasun ainemäärä ja tilavuus pysyvät vakioina, joten paine on suoraan verrannollinen kelvinlämpötilaan ja $\dfrac{p}{T}$ on vakio. Verrannollisuus pätee vain kelvineinä, koska vain kelvinasteikon nolla on absoluuttinen nollapiste. Se edellyttää myös, että kaasu pysyy kaasuna.
**Kaava:** $\dfrac{p}{T} = \dfrac{p_0}{T_0}$, joten $p = p_0\,\dfrac{T}{T_0}$
**Muunnokset:** Lähtölämpötila muunnetaan kelvineiksi: $T_0 = 0\,{}^\circ\text{C} = 273{,}15\,\text{K}$. Lämpötila $77{,}0\,\text{K}$ on jo kelvineinä. Suhteessa $T/T_0$ kelvinit supistuvat, joten paine jää kilopascaleiksi.
**Sijoitus:** $p = 100{,}0\,\text{kPa} \cdot \dfrac{77{,}0\,\text{K}}{273{,}15\,\text{K}} = 28{,}19\,\text{kPa}$
**Vastaus:** $28{,}2\,\text{kPa}$, kolme merkitsevää numeroa, koska lämpötila $77{,}0\,\text{K}$ on annettu kolmella numerolla ($273{,}15\,\text{K}$ on määritelmä eikä rajoita). Suoraa ei voi jatkaa nollaan asti, koska typpi tiivistyy nesteeksi noin $67\,\text{K}$:ssä. Silloin kaasun ainemäärä pienenee, paine putoaa nopeammin kuin suora ennustaa, eikä ehto "ainemäärä vakio" enää päde.
**Järkevyys:** Lämpötila $77{,}0\,\text{K}$ on noin $0{,}28$-kertainen lämpötilaan $273{,}15\,\text{K}$ verrattuna, ja paine on samassa suhteessa: noin $0{,}28 \cdot 100 = 28\,\text{kPa}$. Suora antaisi lämpötilassa $67\,\text{K}$ paineen $100 \cdot 67/273{,}15 = 24{,}5\,\text{kPa}$, mutta noin siinä lämpötilassa kaasu alkaa tiivistyä nesteeksi, eikä paine sen jälkeen enää noudata suoraa. Ekstrapolointi on siis luotettava vain niin pitkälle kuin oletus kaasusta pitää paikkansa.

## fy3-13-L3-03
**Annettu:** ryhmän A tulos $\theta_0 = -262{,}00\,{}^\circ\text{C}$ ja epävarmuus $\Delta\theta_0 = 6{,}00\,{}^\circ\text{C}$; hyväksytty arvo $\theta_\text{h} = -273{,}15\,{}^\circ\text{C}$
**Kysytty:** poikkeaman suhde epävarmuuteen $n$ (kuinka monta kertaa $\Delta\theta_0$ mahtuu tuloksen ja hyväksytyn arvon väliin) ja syy ristiriitaan
**Periaate:** Tässä luvussa tulosta pidetään sopusoinnussa hyväksytyn arvon kanssa, jos arvo kuuluu epävarmuusväliin $\theta_0 \pm \Delta\theta_0$, eli kun poikkeama on korkeintaan yksi epävarmuus. Suhde $n$ kertoo, kuinka moninkertainen poikkeama on epävarmuuteen verrattuna. Epävarmuus ei ole ehdoton raja, joten poikkeama ei yksin todista virhettä, mutta mitä suurempi $n$ on, sitä todennäköisemmin mittauksessa on systemaattinen virhe tai epävarmuus on arvioitu liian pieneksi.
**Kaava:** $n = \dfrac{|\theta_0 - \theta_\text{h}|}{\Delta\theta_0}$
**Muunnokset:** Kaikki lämpötilat ovat celsiusasteina, ja lämpötilaerot ovat samat kelvineinä. Suhde $n$ on dimensioton, joten muunnoksia ei tarvita.
**Sijoitus:** $n = \dfrac{|-262{,}00\,{}^\circ\text{C} - (-273{,}15\,{}^\circ\text{C})|}{6{,}00\,{}^\circ\text{C}} = \dfrac{11{,}15\,{}^\circ\text{C}}{6{,}00\,{}^\circ\text{C}} = 1{,}858$
**Vastaus:** $1{,}86$ kertaa, kolme merkitsevää numeroa, koska erotus $11{,}15\,{}^\circ\text{C}$ ja epävarmuus $6{,}00\,{}^\circ\text{C}$ on annettu kolmella numerolla (tulos $-262{,}00\,{}^\circ\text{C}$ ja hyväksytty arvo ovat sadasosan tarkkuudella).
**Järkevyys:** Poikkeama $11{,}15\,{}^\circ\text{C}$ on lähes kaksi epävarmuutta ($2 \cdot 6{,}00 = 12{,}0$). Epävarmuusväli $-268\ldots -256\,{}^\circ\text{C}$ ei sisällä hyväksyttyä arvoa $-273{,}15\,{}^\circ\text{C}$, joten tulos ei tämän säännön mukaan ole sopusoinnussa. Syynä voi olla systemaattinen virhe, esimerkiksi epätarkka lämpömittari, ilmavuoto tai pullon tilavuuden muutos, tai liian pieneksi arvioitu epävarmuus. Tarkistus: $1{,}858 \cdot 6{,}00\,{}^\circ\text{C} = 11{,}15\,{}^\circ\text{C}$.

## fy3-13-L1-06
**Kysytty:** mitä lämpötila $0\,\text{K}$ eli absoluuttinen nollapiste tarkoittaa.
**Periaate:** Lämpötila kuvaa hiukkasten keskimääräistä liike-energiaa. Kelvinasteikko alkaa lämpötilasta, jota alempaa ei ole, koska hiukkasten energia on siinä pienimmillään.
**Mallivastaus:** Absoluuttinen nollapiste on alin mahdollinen lämpötila, $0\,\text{K} = -273{,}15\,{}^\circ\text{C}$, jossa hiukkasten keskimääräinen liike-energia on pienimmillään. Se ei ole veden jäätymispiste ($273{,}15\,\text{K}$), eikä sitä pidä ymmärtää niin, että hiukkaset pysähtyisivät: kyse on pienimmästä mahdollisesta energiasta, ja tarkempi kuva kuuluu myöhempään kurssiin. Kaikki kaasut eivät myöskään tiivisty juuri siinä: tiivistymislämpötila riippuu aineesta.

## fy3-13-L1-07
**Annettu:** typen kiehumispiste $\theta = -195{,}8\,{}^\circ\text{C}$
**Kysytty:** sama lämpötila kelvineinä, $T$
**Periaate:** Celsius- ja kelvinasteikon asteen koko on sama, mutta nollakohdat eroavat: kelvinasteikon nolla on absoluuttinen nollapiste. Muunnos on siis pelkkä siirto.
**Kaava:** $T = \theta + 273{,}15$
**Muunnokset:** Lämpötila $0\,{}^\circ\text{C}$ on $273{,}15\,\text{K}$, joten celsiusarvoon lisätään $273{,}15$ ja yksiköksi tulee kelvin.
**Sijoitus:** $T = (-195{,}8 + 273{,}15)\,\text{K} = 77{,}35\,\text{K} \approx 77{,}4\,\text{K}$
**Vastaus:** $77{,}4\,\text{K}$, kymmenesosan tarkkuudella kuten $-195{,}8\,{}^\circ\text{C}$; tarkka $273{,}15$ ei rajoita.
**Järkevyys:** Tulos on positiivinen, kuten kelvinlämpötilan kuuluukin, ja se on selvästi alle veden jäätymispisteen $273{,}15\,\text{K}$. Tarkistus takaisin: $77{,}4\,\text{K} - 273{,}15\,\text{K} = -195{,}75\,{}^\circ\text{C} \approx -195{,}8\,{}^\circ\text{C}$.

## fy3-13-L1-08
**Kysytty:** mitä ekstrapolointi tarkoittaa, kun mittauspisteisiin sovitettua suoraa jatketaan kohtaan $p = 0$.
**Periaate:** Mittaus kattaa vain välin $20\ldots 100\,{}^\circ\text{C}$. Kun suora jatketaan tämän välin ulkopuolelle, tulos ei ole mitattu vaan päätelty, ja päätelmä olettaa, että sama lineaarinen riippuvuus pätee myös mitatun alueen ulkopuolella.
**Mallivastaus:** Ekstrapolointi tarkoittaa mittauspisteisiin sovitetun suoran jatkamista mittausalueen ulkopuolelle olettaen, että paineen lineaarinen riippuvuus lämpötilasta pätee myös siellä. Ekstrapoloitu arvo on siis mallin perusteella tehty arvio, ei suoraan mitattu tulos. Kahden mitatun pisteen välistä lukeminen on interpolointia, toistaminen pienentää keskiarvon satunnaista virhettä, ja suora kulkee pisteiden joukon keskeltä eikä jokaisen pisteen kautta.

## fy3-13-L2-05
**Annettu:** viisi pistettä taulukosta; sovitetun suoran kulmakerroin $k = 0{,}363\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$; suora kulkee keskipisteen $(\theta_{\text{ka}}, p_{\text{ka}})$ kautta
**Kysytty:** a) keskipiste; b) nollapaineen lämpötila $\theta_0$ celsiusasteina
**Periaate:** Pullo on suljettu ja jäykkä, joten ainemäärä ja tilavuus pysyvät vakioina ja paine on lämpötilan lineaarinen funktio. Sovitettu suora kulkee pisteiden joukon keskeltä, joten se kulkee keskipisteen kautta. Suoraa jatketaan ekstrapoloimalla kohtaan $p = 0$.
**Kuvaajan lukeminen:** Taulukon keskipiste lasketaan keskiarvoina $\theta_{\text{ka}}$ ja $p_{\text{ka}}$. Lämpötilojen summa on $250\,{}^\circ\text{C}$ ja paineiden summa $588{,}9\,\text{kPa}$. Suora kulkee tämän pisteen kautta kulmakertoimella $k$.
**Kaava:** Suora pisteen $(\theta_{\text{ka}}, p_{\text{ka}})$ kautta on $p = p_{\text{ka}} + k(\theta - \theta_{\text{ka}})$. Kun $p = 0$ ja $\theta = \theta_0$, niin $\theta_0 = \theta_{\text{ka}} - \dfrac{p_{\text{ka}}}{k}$
**Muunnokset:** Muunnoksia ei tarvita: paineet ovat kilopascaleina, joten osamäärässä $p_{\text{ka}}/k$ kPa supistuu ja jäljelle jää celsiusaste.
**Sijoitus:** a) $\theta_{\text{ka}} = 250\,{}^\circ\text{C} : 5 = 50\,{}^\circ\text{C}$ ja $p_{\text{ka}} = 588{,}9\,\text{kPa} : 5 = 117{,}78\,\text{kPa}$. b)

$$\begin{aligned} \theta_0 &= 50\,{}^\circ\text{C} - \dfrac{117{,}78\,\text{kPa}}{0{,}363\,\text{kPa}/{}^\circ\text{C}} \\ &= 50\,{}^\circ\text{C} - 324{,}46\,{}^\circ\text{C} \\ &= -274{,}46\,{}^\circ\text{C} \end{aligned}$$

**Vastaus:** $-274\,{}^\circ\text{C}$, kolme merkitsevää numeroa kuten kulmakertoimessa $0{,}363$. Keskipiste on $(50\,{}^\circ\text{C};\ 117{,}78\,\text{kPa})$.
**Järkevyys:** Suora antaa pisteessä $\theta = 10\,{}^\circ\text{C}$ paineen $117{,}78\,\text{kPa} + 0{,}363\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot (-40\,{}^\circ\text{C}) = 103{,}26\,\text{kPa}$, mikä poikkeaa mitatusta $103{,}4\,\text{kPa}$:sta vain $0{,}14\,\text{kPa}$, selvästi alle epävarmuuden $1{,}0\,\text{kPa}$. Tulos poikkeaa hyväksytystä arvosta $-273{,}15\,{}^\circ\text{C}$ vain noin $1{,}3\,{}^\circ\text{C}$.

## fy3-13-L2-06
**Annettu:** ryhmä B käyttää pisteitä $(\theta_1, p_1) = (20\,{}^\circ\text{C};\ 107{,}4\,\text{kPa})$ ja $(\theta_2, p_2) = (35\,{}^\circ\text{C};\ 112{,}4\,\text{kPa})$; ryhmän A tulos $-270\,{}^\circ\text{C}$; paineen epävarmuus $\pm 1{,}0\,\text{kPa}$
**Kysytty:** a) ryhmän B nollapaineen lämpötila $\theta_0$ celsiusasteina; b) miksi tulos eroaa ryhmän A tuloksesta
**Periaate:** Suljetussa jäykässä astiassa paine on lämpötilan lineaarinen funktio, joten kaksi pistettä määrää suoran, jota jatketaan kohtaan $p = 0$. Mittauspisteissä on satunnaista hajontaa, joten suoran kulmakerroin on sitä epävarmempi, mitä lyhyemmältä väliltä se lasketaan.
**Kuvaajan lukeminen:** Ryhmä B lukee taulukosta vain kaksi ensimmäistä riviä, lämpötilat $20\,{}^\circ\text{C}$ ja $35\,{}^\circ\text{C}$.
**Kaava:** $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ ja $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Muunnokset:** Muunnoksia ei tarvita: paineet ovat kilopascaleina, joten kPa supistuu osamäärässä $p_1/k$. Lämpötilaero $15\,{}^\circ\text{C}$ on sama kelvineinä.
**Sijoitus:**

$$\begin{aligned} k &= \dfrac{(112{,}4 - 107{,}4)\,\text{kPa}}{(35 - 20)\,{}^\circ\text{C}} \\ &= \dfrac{5{,}0\,\text{kPa}}{15\,{}^\circ\text{C}} \\ &= 0{,}3333\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 20\,{}^\circ\text{C} - \dfrac{107{,}4\,\text{kPa}}{0{,}3333\,\text{kPa}/{}^\circ\text{C}} \\ &= 20\,{}^\circ\text{C} - 322{,}2\,{}^\circ\text{C} \\ &= -302{,}2\,{}^\circ\text{C} \end{aligned}$$

**Vastaus:** $-302\,{}^\circ\text{C}$, mutta vain noin kahden numeron tarkkuudella ($-3{,}0 \cdot 10^{2}\,{}^\circ\text{C}$), koska kulmakerroin $0{,}33\,\text{kPa}/{}^\circ\text{C}$ tunnetaan kahdella numerolla.
**Mallivastaus (b):** Ryhmä B laskee kulmakertoimen vain $15\,{}^\circ\text{C}$:n välistä, jolla paine kasvaa $5{,}0\,\text{kPa}$. Kummankin paineen epävarmuus $1{,}0\,\text{kPa}$ voi muuttaa paine-eroa jopa $2{,}0\,\text{kPa}$, joten kulmakerroin on epävarma noin $2{,}0 : 15 = 0{,}13\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$, eli noin $40\,\%$ itse arvosta. Ekstrapolointimatka on yli $300\,{}^\circ\text{C}$, joten pieni kulmakertoimen virhe kasvaa suureksi. Ryhmä A käyttää kuutta pistettä $75\,{}^\circ\text{C}$:n levyiseltä väliltä, jolloin hajonta tasoittuu ja kulmakerroin $0{,}370\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ on luotettavampi.
**Järkevyys:** Ryhmän B suora antaisi lämpötilassa $95\,{}^\circ\text{C}$ paineen $107{,}4\,\text{kPa} + 0{,}3333\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot 75\,{}^\circ\text{C} = 132{,}4\,\text{kPa}$, mutta mitattu on $135{,}0\,\text{kPa}$. Ero $2{,}6\,\text{kPa}$ on suurempi kuin epävarmuus $1{,}0\,\text{kPa}$, joten ryhmän B suora ei sovi muihin pisteisiin. Ryhmän A erotus mitatusta olisi alle $0{,}2\,\text{kPa}$.

## fy3-13-L2-07
**Annettu:** pisteet $(20\,{}^\circ\text{C};\ 104{,}0\,\text{kPa})$, $(40\,{}^\circ\text{C};\ 110{,}6\,\text{kPa})$, $(60\,{}^\circ\text{C};\ 116{,}0\,\text{kPa})$ ja $(80\,{}^\circ\text{C};\ 120{,}0\,\text{kPa})$; paineen epävarmuus $\pm 0{,}5\,\text{kPa}$; suora ensimmäisen ja viimeisen pisteen kautta
**Kysytty:** a) ryhmän saama nollapaineen lämpötila $\theta_0$ celsiusasteina; b) tukeeko taulukko vuotoepäilyä ja miksi vuoto vääristää tulosta
**Periaate:** Vuodottomassa suljetussa pullossa ainemäärä on vakio ja paine kasvaa lämpötilan mukana lineaarisesti. Jos kaasua pääsee pois, ainemäärä pienenee eikä lineaarinen malli enää päde. Ekstrapolointi olettaa mallin pätevän, joten tulos vääristyy.
**Kuvaajan lukeminen:** Luetaan taulukosta ensimmäinen piste $(20\,{}^\circ\text{C};\ 104{,}0\,\text{kPa})$ ja viimeinen piste $(80\,{}^\circ\text{C};\ 120{,}0\,\text{kPa})$.
**Kaava:** $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ ja $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Muunnokset:** Muunnoksia ei tarvita: kilopascalit supistuvat osamäärässä, ja lämpötilaero $60\,{}^\circ\text{C}$ on sama kelvineinä.
**Sijoitus:**

$$\begin{aligned} k &= \dfrac{(120{,}0 - 104{,}0)\,\text{kPa}}{(80 - 20)\,{}^\circ\text{C}} \\ &= \dfrac{16{,}0\,\text{kPa}}{60\,{}^\circ\text{C}} \\ &= 0{,}2667\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 20\,{}^\circ\text{C} - \dfrac{104{,}0\,\text{kPa}}{0{,}2667\,\text{kPa}/{}^\circ\text{C}} \\ &= 20\,{}^\circ\text{C} - 390\,{}^\circ\text{C} \\ &= -370\,{}^\circ\text{C} \end{aligned}$$

**Vastaus:** $-370\,{}^\circ\text{C}$, kolme merkitsevää numeroa kuten paineissa; tulos on selvästi alle $-273{,}15\,{}^\circ\text{C}$.
**Mallivastaus (b):** Taulukko tukee epäilyä. Paine kasvaa jokaisella $20\,{}^\circ\text{C}$:n välillä vähemmän: $6{,}6\,\text{kPa}$, $5{,}4\,\text{kPa}$ ja $4{,}0\,\text{kPa}$, eli kulmakerroin pienenee arvoista $0{,}33$ ja $0{,}27$ arvoon $0{,}20\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$. Erot ovat paljon suurempia kuin epävarmuus $\pm 0{,}5\,\text{kPa}$, joten kyse ei ole hajonnasta vaan mallin rikkoutumisesta: pisteet eivät ole suoralla. Vuodossa kuumasta pullosta poistuu kaasua, joten ainemäärä pienenee ja paine kasvaa vähemmän kuin vuodottomassa pullossa. Päätepisteiden suoran kulmakerroin $0{,}267\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ on liian pieni, ja pieni kulmakerroin vie nollapaineen liian kauas, kohtaan $-370\,{}^\circ\text{C}$.
**Järkevyys:** Kahden ensimmäisen pisteen kulmakerroin $0{,}33\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ antaisi $20\,{}^\circ\text{C} - 104{,}0\,\text{kPa} : 0{,}33\,\tfrac{\text{kPa}}{{}^\circ\text{C}} = -295\,{}^\circ\text{C}$, joka on lähempänä oikeaa arvoa, koska vuotoa on ehtinyt tapahtua vähemmän. Tulos $-370\,{}^\circ\text{C}$ poikkeaa hyväksytystä arvosta $-273{,}15\,{}^\circ\text{C}$ lähes sadalla asteella, mikä on liikaa pelkäksi mittausepävarmuudeksi.

## fy3-13-L3-04
**Annettu:** sarja A: $(25\,{}^\circ\text{C};\ 108{,}0\,\text{kPa})$ ja $(85\,{}^\circ\text{C};\ 130{,}0\,\text{kPa})$; sarja B: $(25\,{}^\circ\text{C};\ 108{,}0\,\text{kPa})$ ja $(225\,{}^\circ\text{C};\ 181{,}5\,\text{kPa})$; paineen epävarmuus $\Delta p = 1{,}0\,\text{kPa}$
**Kysytty:** a) kummankin sarjan nollapaineen lämpötilan epävarmuus $\Delta\theta_0$ celsiusasteina; b) mittausalueen leveyden vaikutus ja yhteensopivuus arvon $-273{,}15\,{}^\circ\text{C}$ kanssa
**Periaate:** Jokaisen pisteen paine tunnetaan välillä $p \pm \Delta p$. Jyrkin suora kulkee alemman pisteen alapään ja ylemmän pisteen yläpään kautta, loivin päinvastoin; molemmat sopivat aineistoon. Niiden nollapaineen lämpötilat rajaavat välin, ja epävarmuus on välin puolikas. Malli olettaa, että paine on lämpötilan lineaarinen funktio suljetussa jäykässä astiassa myös mitatun alueen ulkopuolella.
**Kuvaajan lukeminen:** Kustakin sarjasta luetaan kaksi pistettä. Jyrkin suora kulkee pisteiden $(\theta_1;\ p_1 - \Delta p)$ ja $(\theta_2;\ p_2 + \Delta p)$ kautta, loivin pisteiden $(\theta_1;\ p_1 + \Delta p)$ ja $(\theta_2;\ p_2 - \Delta p)$ kautta.
**Kaava:** Suoran paine pisteessä $\theta_1$ on $p_a$ ja pisteessä $\theta_2$ on $p_b$. Silloin $k = \dfrac{p_b - p_a}{\theta_2 - \theta_1}$, $\theta_0 = \theta_1 - \dfrac{p_a}{k}$ ja $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Muunnokset:** Muunnoksia ei tarvita: kilopascalit supistuvat osamäärässä $p_a/k$, ja lämpötilaerot ovat samat kelvineinä.
**Sijoitus:**

Sarja A, jyrkin:

$$\begin{aligned} k &= \dfrac{(131{,}0 - 107{,}0)\,\text{kPa}}{(85 - 25)\,{}^\circ\text{C}} \\ &= 0{,}4000\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 25\,{}^\circ\text{C} - \dfrac{107{,}0\,\text{kPa}}{0{,}4000\,\text{kPa}/{}^\circ\text{C}} \\ &= -242{,}5\,{}^\circ\text{C} \end{aligned}$$

Sarja A, loivin:

$$\begin{aligned} k &= \dfrac{(129{,}0 - 109{,}0)\,\text{kPa}}{(85 - 25)\,{}^\circ\text{C}} \\ &= 0{,}3333\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 25\,{}^\circ\text{C} - \dfrac{109{,}0\,\text{kPa}}{0{,}3333\,\text{kPa}/{}^\circ\text{C}} \\ &= -302{,}0\,{}^\circ\text{C} \end{aligned}$$

Siis $\Delta\theta_{0,\text{A}} = \dfrac{(-242{,}5 + 302{,}0)\,{}^\circ\text{C}}{2} = 29{,}75\,{}^\circ\text{C}$.

Sarja B, jyrkin:

$$\begin{aligned} k &= \dfrac{(182{,}5 - 107{,}0)\,\text{kPa}}{(225 - 25)\,{}^\circ\text{C}} \\ &= 0{,}3775\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 25\,{}^\circ\text{C} - \dfrac{107{,}0\,\text{kPa}}{0{,}3775\,\text{kPa}/{}^\circ\text{C}} \\ &= -258{,}44\,{}^\circ\text{C} \end{aligned}$$

Sarja B, loivin:

$$\begin{aligned} k &= \dfrac{(180{,}5 - 109{,}0)\,\text{kPa}}{(225 - 25)\,{}^\circ\text{C}} \\ &= 0{,}3575\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 25\,{}^\circ\text{C} - \dfrac{109{,}0\,\text{kPa}}{0{,}3575\,\text{kPa}/{}^\circ\text{C}} \\ &= -279{,}90\,{}^\circ\text{C} \end{aligned}$$

$$\begin{aligned} \Delta\theta_{0,\text{B}} &= \dfrac{(-258{,}44 + 279{,}90)\,{}^\circ\text{C}}{2} \\ &= 10{,}73\,{}^\circ\text{C} \end{aligned}$$

**Vastaus:** Sarjan B epävarmuus on $10{,}7\,{}^\circ\text{C}$; kolme merkitsevää numeroa, koska paineet on annettu neljällä ja ääriarvojen erotus $21{,}46\,{}^\circ\text{C}$ tunnetaan kolmella. Sarjan A epävarmuus on noin $30\,{}^\circ\text{C}$. Tulokset ovat $\theta_{0,\text{A}} = -272 \pm 30\,{}^\circ\text{C}$ ja $\theta_{0,\text{B}} = -269 \pm 11\,{}^\circ\text{C}$.
**Mallivastaus (b):** Sarjan B mittausalue on $200\,{}^\circ\text{C}$ leveä ja sarjan A $60\,{}^\circ\text{C}$, ja B:n epävarmuus on vain noin kolmasosa A:n epävarmuudesta. Sama paineen epävarmuus $\pm 1{,}0\,\text{kPa}$ vaikuttaa kulmakertoimeen sitä vähemmän, mitä pidemmältä väliltä se lasketaan, ja pieni kulmakertoimen virhe kasvaa ekstrapoloitaessa. Leveämpi mittausalue siis pienentää epävarmuutta. Kummankin sarjan väli sisältää arvon $-273{,}15\,{}^\circ\text{C}$ (A: $-302\ldots -243\,{}^\circ\text{C}$, B: $-280\ldots -258\,{}^\circ\text{C}$), joten tulokset sopivat yhteen hyväksytyn arvon kanssa. Väli on arvio, ja se olettaa, että paine pysyy lineaarisena myös mitatun alueen ulkopuolella.
**Järkevyys:** Alueiden leveyksien suhde on $200:60 \approx 3{,}3$ ja epävarmuuksien suhde $29{,}75:10{,}73 \approx 2{,}8$, eli epävarmuus pienenee suunnilleen leveyden kasvun mukana. Sarjojen välien keskikohdat $-272\,{}^\circ\text{C}$ ja $-269\,{}^\circ\text{C}$ ovat lähellä toisiaan ja lähellä arvoa $-273{,}15\,{}^\circ\text{C}$.

## fy3-13-L3-05
**Annettu:** kalibrointipisteet taulukosta, ensimmäinen $(\theta_1, p_1) = (0\,{}^\circ\text{C};\ 100{,}4\,\text{kPa})$ ja viimeinen $(\theta_2, p_2) = (100\,{}^\circ\text{C};\ 137{,}0\,\text{kPa})$; pakastimessa luettu paine $p = 94{,}0\,\text{kPa}$ ja sen epävarmuus $\Delta p = 1{,}0\,\text{kPa}$
**Kysytty:** a) pakastimen lämpötila $\theta$ celsiusasteina; b) painelukeman epävarmuudesta johtuva lämpötilan epävarmuus $\Delta\theta$; c) miksi tulos on ekstrapolointia mutta luotettava
**Periaate:** Pullo on suljettu ja jäykkä, joten kaasun ainemäärä ja tilavuus pysyvät vakioina ja paine on lämpötilan lineaarinen funktio. Kalibrointisuora kulkee kaukana toisistaan olevien pisteiden kautta, ja se ratkaistaan lämpötilan suhteen, kun paine tunnetaan. Pakastimen lämpötila on kalibrointialueen $0\ldots 100\,{}^\circ\text{C}$ ulkopuolella.
**Kuvaajan lukeminen:** Luetaan taulukosta kaukaisimmat pisteet $(0\,{}^\circ\text{C};\ 100{,}4\,\text{kPa})$ ja $(100\,{}^\circ\text{C};\ 137{,}0\,\text{kPa})$. Muut pisteet toimivat tarkistuksena.
**Kaava:** $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ ja suoran $p = p_1 + k(\theta - \theta_1)$ ratkaisu $\theta = \theta_1 + \dfrac{p - p_1}{k}$. Painelukeman epävarmuutta vastaa lämpötilan epävarmuus $\Delta\theta = \dfrac{\Delta p}{k}$.
**Muunnokset:** Muunnoksia ei tarvita: kilopascalit supistuvat, joten tulos on celsiusasteina. Lämpötilaero $100\,{}^\circ\text{C}$ on sama kelvineinä.
**Sijoitus:**

$$\begin{aligned} k &= \dfrac{(137{,}0 - 100{,}4)\,\text{kPa}}{(100 - 0)\,{}^\circ\text{C}} \\ &= 0{,}3660\,\text{kPa}/{}^\circ\text{C} \end{aligned}$$

a)

$$\begin{aligned} \theta &= 0\,{}^\circ\text{C} + \dfrac{(94{,}0 - 100{,}4)\,\text{kPa}}{0{,}3660\,\text{kPa}/{}^\circ\text{C}} \\ &= -17{,}49\,{}^\circ\text{C} \end{aligned}$$

b)

$$\begin{aligned} \Delta\theta &= \dfrac{1{,}0\,\text{kPa}}{0{,}3660\,\text{kPa}/{}^\circ\text{C}} \\ &= 2{,}73\,{}^\circ\text{C} \end{aligned}$$

**Vastaus:** $-17{,}5\,{}^\circ\text{C}$ ja epävarmuus noin $2{,}7\,{}^\circ\text{C}$, eli tulos on $-17{,}5 \pm 2{,}7\,{}^\circ\text{C}$. Rajoittava tieto on paine-ero $94{,}0 - 100{,}4 = -6{,}4\,\text{kPa}$ (kaksi numeroa), joten yksinkertaisimmillaan tulos on $-17 \pm 3\,{}^\circ\text{C}$; desimaali annetaan, jotta tulos vastaa vastauskentän arvoa.
**Mallivastaus (c):** Pakastimen lämpötila on kalibroidun alueen $0\ldots 100\,{}^\circ\text{C}$ ulkopuolella, joten suoraa jatketaan mitatun alueen yli ja tulos on ekstrapolointia, joka olettaa paineen pysyvän lineaarisena. Jatke on kuitenkin vain noin $17{,}5\,{}^\circ\text{C}$ pitkä, kun nollapisteen määrityksessä suoraa jatketaan yli $270\,{}^\circ\text{C}$. Kalibrointisuoran kulmakertoimen epävarmuus vaikuttaa tulokseen vain jatkeen pituudelta, joten sen vaikutus on muutaman asteen osa. Lisäksi lämpötila $-17{,}5\,{}^\circ\text{C}$ on kaukana lämpötilasta, jossa ilma alkaisi tiivistyä, joten lineaarinen malli on järkevä.
**Järkevyys:** Tulos on tyypillinen pakastimen lämpötila. Välipiste tarkistaa suoran: $100{,}4\,\text{kPa} + 0{,}3660\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot 50\,{}^\circ\text{C} = 118{,}7\,\text{kPa}$, kun mitattu on $118{,}6\,\text{kPa}$. Kelvineinä lämpötila on $T = 273{,}15\,\text{K} - 17{,}49\,\text{K} = 255{,}66\,\text{K}$, ja paineiden suhde $94{,}0:100{,}4 = 0{,}936$ on sama kuin lämpötilojen suhde $255{,}66:273{,}15 = 0{,}936$.

## fy3-13-L2-08
**Kysytty:** mikä päätelmä on se, jonka taulukon aineisto ja annettu epävarmuus $\Delta p = 1{,}0\,\text{kPa}$ tukevat.
**Periaate:** Kahden lukeman eron voi pitää todellisena vasta, kun se on selvästi suurempi kuin lukemien epävarmuus eli kun epävarmuusvälit eivät mene päällekkäin. Jos välit menevät päällekkäin, eroa ei voi osoittaa, mutta se ei todista eron puuttumista. Mittausalueen ulkopuolelle jatkettu suora on arvio eikä mittaustulos.
**Mallivastaus:** Lukemien $102{,}0\,\text{kPa}$ ja $115{,}5\,\text{kPa}$ ero on

$115{,}5\,\text{kPa} - 102{,}0\,\text{kPa} = 13{,}5\,\text{kPa}$

mikä on yli kymmenkertainen epävarmuuteen $1{,}0\,\text{kPa}$ nähden. Epävarmuusvälit $101{,}0$–$103{,}0\,\text{kPa}$ ja $114{,}5$–$116{,}5\,\text{kPa}$ ovat erillään, joten paine kasvoi lämpötilasta $20{,}0\,{}^\circ\text{C}$ lämpötilaan $60{,}0\,{}^\circ\text{C}$. Muut päätelmät eivät kestä. Lämpötilojen $20{,}0\,{}^\circ\text{C}$ ja $22{,}0\,{}^\circ\text{C}$ lukemien ero $0{,}8\,\text{kPa}$ jää epävarmuuden $1{,}0\,\text{kPa}$ sisään, joten kasvua ei voi osoittaa tästä parista. Sama ero ei kuitenkaan todista, ettei paine muutu, koska pieni muutos voi hukkua epävarmuuteen ja koko aineistossa kasvu näkyy selvästi. Pisteisiin sovitettu suora antaisi lämpötilassa $-100\,{}^\circ\text{C}$ arvion noin $62\,\text{kPa}$, mutta piste on $120\,{}^\circ\text{C}$ mittausalueen alapuolella, joten arvo on epävarma arvio, ei varma tulos. Tulos on järkevä: paineen kasvu lämpötilan mukana sopii suljettuun jäykkään pulloon, jossa kaasun paine kasvaa lämpötilan noustessa.

## fy3-13-L1-09
**Annettu:** kelvinlämpötila nollapisteessä $T = 0\,\text{K}$; taulukosta (MAFY-taulukko, yksikkömuunnoksia) $0\,{}^\circ\text{C} = 273{,}15\,\text{K}$, joten $T_0 = 273{,}15\,\text{K}$
**Kysytty:** absoluuttisen nollapisteen celsiuslämpötila $\theta_0$ celsiusasteina
**Periaate:** Celsius- ja kelvinasteikon asteet ovat yhtä suuret, ja asteikot ovat siirtyneet toistensa suhteen vakion $T_0$ verran. Absoluuttinen nollapiste on kelvinasteikon nollakohta, joten sen celsiuslämpötila saadaan asettamalla $T = 0$.
**Kaava:** $T = \theta + T_0$, joten $0 = \theta_0 + T_0$ ja $\theta_0 = -T_0$
**Muunnokset:** Muunnoksia ei tarvita: $T_0$ on jo taulukossa, ja lämpötilan muutos on yhtä suuri kelvineinä ja celsiusasteina.
**Sijoitus:** $\theta_0 = -273{,}15\,{}^\circ\text{C}$
**Vastaus:** $\theta_0 = -273{,}15\,{}^\circ\text{C} \approx -273\,{}^\circ\text{C}$. Arvo $T_0 = 273{,}15\,\text{K}$ on MAFY-taulukosta (yksikkömuunnoksia); taulukon arvo on sovittu tarkaksi, ja vastaus hyväksytään noin $\pm 4\,\%$ tarkkuudella.
**Järkevyys:** Tulos on samaa kokoluokkaa kuin kaasun painemittauksista ekstrapoloidut arvot, noin $-270\,{}^\circ\text{C}$. Se on myös selvästi alempana kuin nestetypen kiehumispiste $-195{,}8\,{}^\circ\text{C}$, mikä sopii, koska nestetyppeä voi jäähdyttää pidemmälle. Kelvinasteikko alkaa absoluuttisesta nollapisteestä, joten negatiivista kelvinlämpötilaa eikä tätä kylmempää lämpötilaa ole.

## fy3-13-L2-09
**Annettu:** kuvaajasta luettuna pisteet $(0\,{}^\circ\text{C};\ 75\,\text{kPa})$ ja $(100\,{}^\circ\text{C};\ 102{,}5\,\text{kPa})$; pisteet ovat lähes suoralla
**Kysytty:** lämpötila $\theta_0$, jossa suoran paine on nolla, celsiusasteina
**Periaate:** Jäykässä suljetussa astiassa kaasun määrä ja tilavuus pysyvät samoina, joten paine riippuu vain lämpötilasta. Pisteet ovat lähes suoralla, joten suoraa voidaan jatkaa mittausalueen ulkopuolelle eli ekstrapoloida, kunnes paine on nolla.
**Kuvaajan lukeminen:** Ensimmäinen piste on ruudukon risteyksessä $(0\,{}^\circ\text{C};\ 75\,\text{kPa})$. Viimeinen piste on hieman $100\,\text{kPa}$:n viivan yläpuolella, $102{,}5\,\text{kPa}$, lämpötilassa $100\,{}^\circ\text{C}$. Näistä kahdesta pisteestä lasketaan suoran kulmakerroin. Kuvaajan vaaka-akseli ei ulotu nollapaineeseen asti, joten nollakohtaa ei voi lukea kuvaajasta vaan se lasketaan kulmakertoimen avulla. Laskettu arvo hyväksytään $5\,\%$:n toleranssilla.
**Kaava:** $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ ja $p = p_1 + k(\theta - \theta_1) = 0$, joten $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Muunnokset:** Muunnoksia ei tarvita: paineet ovat kilopascaleina ja lämpötilat celsiusasteina.
**Sijoitus:** $k = \dfrac{(102{,}5 - 75)\,\text{kPa}}{(100 - 0)\,{}^\circ\text{C}} = 0{,}275\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$, ja $\theta_0 = 0\,{}^\circ\text{C} - \dfrac{75\,\text{kPa}}{0{,}275\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -272{,}7\,{}^\circ\text{C}$
**Vastaus:** $\theta_0 \approx -273\,{}^\circ\text{C}$. Kuvaajasta luetun paineen tarkkuus on noin $1\,\text{kPa}$, joten tuloksen epävarmuus on noin kymmenen celsiusastetta tai enemmän, eikä kolmas numero ole luotettava.
**Järkevyys:** Tulos on lähellä hyväksyttyä arvoa $-273{,}15\,{}^\circ\text{C}$. Riippumaton tarkistus: jos paine on verrannollinen kelvinlämpötilaan, kulmakerroin on $75\,\text{kPa} / 273{,}15\,\text{K} = 0{,}275\,\text{kPa/K}$, mikä on sama kuin luettu kulmakerroin.

## fy3-13-L2-10
**Annettu:** kuvaajasta luettuna pisteet $(0\,{}^\circ\text{C};\ 75\,\text{kPa})$ ja $(100\,{}^\circ\text{C};\ 102{,}5\,\text{kPa})$; paine riippuu lämpötilasta lineaarisesti myös mittausalueen ulkopuolella; $T = 200\,\text{K}$
**Kysytty:** paine $p$ lämpötilassa $200\,\text{K}$ kilopascaleina
**Periaate:** Jäykässä suljetussa astiassa kaasun määrä ja tilavuus pysyvät samoina, joten paine riippuu vain lämpötilasta. Pisteet ovat suoralla, joten suoraa voidaan jatkaa mittausalueen ulkopuolelle. Kuvaajan lämpötila on celsiusasteina, joten kelvinlämpötila on ensin muunnettava celsiusasteiksi.
**Kuvaajan lukeminen:** Ensimmäinen piste on ruudukon risteyksessä $(0\,{}^\circ\text{C};\ 75\,\text{kPa})$ ja viimeinen hieman $100\,\text{kPa}$:n viivan yläpuolella, $(100\,{}^\circ\text{C};\ 102{,}5\,\text{kPa})$. Näistä lasketaan suoran kulmakerroin, ja suoraa jatketaan vasemmalle. Silmämääräisesti piirtämällä saa arvon $53$–$57\,\text{kPa}$, joka hyväksytään.
**Kaava:** $\theta = T - 273{,}15\,\text{K}$ (celsiusasteina), $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ ja $p = p_1 + k(\theta - \theta_1)$
**Muunnokset:** $\theta = 200 - 273{,}15 = -73{,}15\,{}^\circ\text{C}$
**Sijoitus:** $k = \dfrac{(102{,}5 - 75)\,\text{kPa}}{(100 - 0)\,{}^\circ\text{C}} = 0{,}275\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$, ja $p = 75\,\text{kPa} + 0{,}275\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot (-73{,}15 - 0)\,{}^\circ\text{C} = 75\,\text{kPa} - 20{,}1\,\text{kPa} = 54{,}9\,\text{kPa}$
**Vastaus:** $p \approx 55\,\text{kPa}$, kaksi merkitsevää numeroa, koska kuvaajasta luettu paine on noin $1\,\text{kPa}$:n tarkkuudella.
**Järkevyys:** Lämpötila $200\,\text{K}$ on alle mittausalueen alarajan $273{,}15\,\text{K}$, joten paineen pitää olla pienempi kuin $75\,\text{kPa}$ mutta yli nollan. Riippumaton tarkistus: kun paine on verrannollinen kelvinlämpötilaan, $p \approx 75\,\text{kPa} \cdot \dfrac{200\,\text{K}}{273{,}15\,\text{K}} = 54{,}9\,\text{kPa}$.
