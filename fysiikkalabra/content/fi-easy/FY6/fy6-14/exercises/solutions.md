## fy6-14-L1-01
**Annettu:** LEDin jännite $U_\text{D} = 2{,}0\,\text{V}$, virta $I = 15\,\text{mA}$
**Kysytty:** LEDin teho $P_\text{D}$ milliwatteina
**Periaate:** Komponentin sähköteho on sen jännite kertaa sen läpi kulkeva virta. Tämä pätee myös LEDille, vaikka se ei noudata Ohmin lakia. Teho on nimittäin aina se energia, jonka varaus luovuttaa komponentille yhdessä sekunnissa.
**Kaava:** $P_\text{D} = U_\text{D} I$
**Muunnokset:** $I = 15\,\text{mA} = 15 \cdot 10^{-3}\,\text{A} = 0{,}015\,\text{A}$
**Sijoitus:** $P_\text{D} = 2{,}0\,\text{V} \cdot 0{,}015\,\text{A} = 0{,}030\,\text{W} = 30\,\text{mW}$
**Vastaus:** $30\,\text{mW}$, kaksi merkitsevää numeroa kuten jännitteessä ja virrassa.
**Järkevyys:** Yksikkö täsmää: $\text{V} \cdot \text{mA} = \text{mW}$, ja $2 \cdot 15 = 30$. Merkkivalon LEDin teho on kymmeniä milliwatteja. Se on paljon pienempi kuin hehkulampun teho, kuten arkikokemuksestakin tiedetään.

## fy6-14-L1-02
**Annettu:** lähteen jännite $U = 5{,}0\,\text{V}$, LEDin jännite $U_\text{D} = 3{,}1\,\text{V}$, virta $I = 20\,\text{mA}$
**Kysytty:** etuvastuksen resistanssi $R$ ohmeina
**Periaate:** Lähde, vastus ja LED ovat peräkkäin eli sarjassa, joten sama virta kulkee kaikkien läpi. Kirchhoffin jännitelain mukaan lähteen jännite jakautuu komponenteille: $U = U_R + U_\text{D}$. Vastus noudattaa Ohmin lakia, $U_R = RI$.
**Kaava:** $U = RI + U_\text{D}$, josta $R = \dfrac{U - U_\text{D}}{I}$
**Muunnokset:** $I = 20\,\text{mA} = 20 \cdot 10^{-3}\,\text{A} = 0{,}020\,\text{A}$
**Sijoitus:** $R = \dfrac{5{,}0\,\text{V} - 3{,}1\,\text{V}}{0{,}020\,\text{A}} = \dfrac{1{,}9\,\text{V}}{0{,}020\,\text{A}} = 95\,\Omega$
**Vastaus:** $95\,\Omega$, kaksi merkitsevää numeroa kuten jännitteiden erotuksessa $1{,}9\,\text{V}$ ja virrassa.
**Järkevyys:** Tarkistus: $95\,\Omega \cdot 0{,}020\,\text{A} = 1{,}9\,\text{V}$, ja $1{,}9\,\text{V} + 3{,}1\,\text{V} = 5{,}0\,\text{V}$. Valkoisen LEDin jännite on suuri. Siksi vastukselle jää vain vähän jännitettä, ja vastus on pieni.

## fy6-14-L1-03
**Annettu:** pariston jännite $U = 9{,}0\,\text{V}$, vastus $R = 1{,}0\,\text{k}\Omega$, diodin jännite $U_\text{D} = 0{,}70\,\text{V}$, diodi päästösuunnassa
**Kysytty:** virta $I$ milliampeereina
**Periaate:** Diodi on päästösuunnassa, joten virta kulkee. Diodin jännite on tehtävässä annettu $0{,}70\,\text{V}$. Paristo, vastus ja diodi ovat sarjassa. Pariston jännite jakautuu vastukselle ja diodille, ja vastuksen jännite on $U_R = RI$.
**Kaava:** $U = RI + U_\text{D}$, josta $I = \dfrac{U - U_\text{D}}{R}$
**Muunnokset:** $R = 1{,}0\,\text{k}\Omega = 1{,}0 \cdot 1000\,\Omega = 1000\,\Omega$
**Sijoitus:** $I = \dfrac{9{,}0\,\text{V} - 0{,}70\,\text{V}}{1000\,\Omega} = \dfrac{8{,}3\,\text{V}}{1000\,\Omega} = 0{,}0083\,\text{A} = 8{,}3\,\text{mA}$
**Vastaus:** $8{,}3\,\text{mA}$, kaksi merkitsevää numeroa kuten jännitteessä $9{,}0\,\text{V}$ ja resistanssissa $1{,}0\,\text{k}\Omega$.
**Järkevyys:** Ilman diodia virta olisi $9{,}0\,\text{V} : 1000\,\Omega = 9{,}0\,\text{mA}$. Diodi vie vain vähän jännitettä. Siksi virta on hieman pienempi, kuten pitääkin.

## fy6-14-L1-04
**Annettu:** paneelin jännite $U = 17{,}5\,\text{V}$, virta $I = 5{,}40\,\text{A}$
**Kysytty:** paneelin teho $P$ watteina
**Periaate:** Aurinkopaneeli on tasajännitelähde. Sen antama sähköteho on napojen välinen jännite kertaa virta, aivan kuten minkä tahansa muun lähteen teho.
**Kaava:** $P = UI$
**Muunnokset:** Ei tarvita: jännite on voltteina ja virta ampeereina, ja $\text{V} \cdot \text{A} = \text{W}$.
**Sijoitus:** $P = 17{,}5\,\text{V} \cdot 5{,}40\,\text{A} = 94{,}5\,\text{W}$
**Vastaus:** $94{,}5\,\text{W}$, kolme merkitsevää numeroa kuten jännitteessä ja virrassa.
**Järkevyys:** Arvio $18\,\text{V} \cdot 5\,\text{A} = 90\,\text{W}$ on lähellä tulosta. Noin $100\,\text{W}$:n paneeli on tavallinen mökin aurinkopaneeli.

## fy6-14-L1-05
**Annettu:** vihreän LEDin ominaiskäyrä, virta $I = 10\,\text{mA}$
**Kysytty:** LEDin teho $P_\text{D}$ milliwatteina
**Periaate:** Ominaiskäyrä kertoo, mikä jännite LEDin yli on kullakin virralla. Teho on jännite kertaa virta. Siksi tarvitaan se jännite, joka vastaa virtaa $10\,\text{mA}$ vastaava jännite.
**Kuvaajan lukeminen:** Mennään pystyakselin kohdasta $10\,\text{mA}$ vaakasuoraan käyrälle. Käyrä leikkaa $10\,\text{mA}$:n ruudukkoviivan pystysuoralla ruudukkoviivalla, joka on $2{,}0\,\text{V}$:n kohdasta yhden $0{,}2\,\text{V}$:n ruudun oikealla, joten $U_\text{D} = 2{,}2\,\text{V}$.
**Kaava:** $P_\text{D} = U_\text{D} I$
**Muunnokset:** $I = 10\,\text{mA} = 0{,}010\,\text{A}$
**Sijoitus:** $P_\text{D} = 2{,}2\,\text{V} \cdot 0{,}010\,\text{A} = 0{,}022\,\text{W} = 22\,\text{mW}$
**Vastaus:** $22\,\text{mW}$, kaksi merkitsevää numeroa, koska jännite luetaan $0{,}2\,\text{V}$:n ruudukosta ja virta $5\,\text{mA}$:n ruudukosta.
**Järkevyys:** Vihreän LEDin jännite $2{,}2\,\text{V}$ on punaisen ($1{,}8$–$2{,}0\,\text{V}$) ja sinisen (noin $3\,\text{V}$) välissä, kuten luvun tekstissä. Teho on muutamia kymmeniä milliwatteja, tavallinen merkkivalolle.

## fy6-14-L2-01
**Annettu:** pariston jännite $U = 9{,}0\,\text{V}$, etuvastus $R = 470\,\Omega$, LED estosuunnassa; oletus: estosuunnassa virtaa ei kulje
**Kysytty:** LEDin jännite $U_\text{D}$ voltteina
**Periaate:** Estosuunnassa diodin läpi ei käytännössä kulje virtaa. LED ja vastus ovat sarjassa, joten myös vastuksen virta on nolla. Ohmin lain mukaan vastuksen jännite on silloin nolla. Kirchhoffin jännitelain mukaan koko pariston jännite on tällöin LEDin yli.
**Kaava:** $U = U_R + U_\text{D}$ ja $U_R = RI$, josta virralla $I = 0$ saadaan $U_\text{D} = U - RI = U$
**Muunnokset:** Ei tarvita: virta on nolla, joten vastuksen arvoa ei tarvitse muuntaa.
**Sijoitus:** $U_\text{D} = 9{,}0\,\text{V} - 470\,\Omega \cdot 0\,\text{A} = 9{,}0\,\text{V}$
**Vastaus:** $9{,}0\,\text{V}$, kaksi merkitsevää numeroa kuten pariston jännitteessä.
**Järkevyys:** Etuvastus ei suojaa estosuunnassa olevaa LEDiä, koska vastuksen yli ei ole jännitettä. Tavallinen LED kestää estosuunnassa usein vain noin $5\,\text{V}$, joten $9{,}0\,\text{V}$ voi rikkoa sen. Siksi napaisuus tarkistetaan ennen kytkemistä.

## fy6-14-L2-02
**Annettu:** pariston jännite $U = 9{,}0\,\text{V}$, kaksi LEDiä sarjassa, kummankin jännite $U_\text{D} = 2{,}0\,\text{V}$, virta $I = 20\,\text{mA}$
**Kysytty:** etuvastuksen resistanssi $R$ ohmeina
**Periaate:** Kaikki komponentit ovat sarjassa, joten sama virta kulkee niiden kaikkien läpi. Pariston jännite jakautuu vastukselle ja molemmille LEDeille: $U = U_R + 2U_\text{D}$. Vastuksen jännite on $U_R = RI$.
**Kaava:** $U = RI + 2U_\text{D}$, josta $R = \dfrac{U - 2U_\text{D}}{I}$
**Muunnokset:** $I = 20\,\text{mA} = 0{,}020\,\text{A}$
**Sijoitus:** $R = \dfrac{9{,}0\,\text{V} - 2 \cdot 2{,}0\,\text{V}}{0{,}020\,\text{A}} = \dfrac{5{,}0\,\text{V}}{0{,}020\,\text{A}} = 250\,\Omega$
**Vastaus:** $250\,\Omega$, kaksi merkitsevää numeroa kuten jännitteissä ja virrassa.
**Järkevyys:** Yhdelle LEDille vastus olisi $7{,}0\,\text{V} : 0{,}020\,\text{A} = 350\,\Omega$. Toinen LED vie vielä $2{,}0\,\text{V}$ lisää, joten vastukselle jää vähemmän jännitettä ja vastus on pienempi.

## fy6-14-L2-03
**Annettu:** pinta-ala $A = 1{,}6\,\text{m}^2$, valon voimakkuus $G = 800\,\text{W/m}^2$, sähköteho $P = 260\,\text{W}$
**Kysytty:** hyötysuhde $\eta$ prosentteina
**Periaate:** Hyötysuhde on hyödyllinen teho jaettuna käytetyllä teholla. Paneeli ottaa vastaan valon tehon. Se on valon voimakkuus kertaa pinta-ala. Hyödyllinen teho on paneelin antama sähköteho.
**Kaava:** $\eta = \dfrac{P}{GA}$
**Muunnokset:** Ei tarvita: $\tfrac{\text{W}}{\text{m}^2} \cdot \text{m}^2 = \text{W}$. Lopuksi suhdeluku muutetaan prosenteiksi kertomalla sadalla.
**Sijoitus:** $\eta = \dfrac{260\,\text{W}}{800\,\tfrac{\text{W}}{\text{m}^2} \cdot 1{,}6\,\text{m}^2} = \dfrac{260\,\text{W}}{1280\,\text{W}} = 0{,}203 = 20{,}3\,\%$
**Vastaus:** $20\,\%$, kaksi merkitsevää numeroa kuten pinta-alassa $1{,}6\,\text{m}^2$.
**Järkevyys:** Paneeliin tulee valon tehoa noin $1300\,\text{W}$, ja siitä noin viidesosa muuttuu sähköksi. Hyötysuhde on tavallisten piikennojen alueella $15$–$22\,\%$.

## fy6-14-L2-04
**Annettu:** kennon teho $P = 0{,}35\,\text{W}$, aika $t = 6{,}0\,\text{h}$
**Kysytty:** sähköenergia $E$ kilojouleina
**Periaate:** Teho on energia yhtä sekuntia kohti. Oletetaan, että kennon teho on koko ajan sama keskimääräinen teho. Silloin energia on teho kertaa aika.
**Kaava:** $P = \dfrac{E}{t}$, josta $E = Pt$
**Muunnokset:** $t = 6{,}0\,\text{h} = 6{,}0 \cdot 3600\,\text{s} = 21\,600\,\text{s}$
**Sijoitus:** $E = 0{,}35\,\text{W} \cdot 21\,600\,\text{s} = 7560\,\text{J} = 7{,}56\,\text{kJ}$
**Vastaus:** $7{,}6\,\text{kJ}$, kaksi merkitsevää numeroa kuten tehossa ja ajassa.
**Järkevyys:** Wattitunteina energia on $0{,}35\,\text{W} \cdot 6{,}0\,\text{h} = 2{,}1\,\text{Wh}$, ja $2{,}1 \cdot 3600\,\text{J} = 7560\,\text{J}$, sama tulos. Tämä on pienen akun energian suuruusluokkaa eli suunnilleen samaa kokoluokkaa. Se riittää yhdelle LEDille koko yöksi.

## fy6-14-L3-01
**Annettu:** LEDin jännite $U_\text{D} = 2{,}0\,\text{V}$, etuvastus $R = 120\,\Omega$, paristojen jännite aluksi $U_1 = 4{,}5\,\text{V}$ ja lopuksi $U_2 = 3{,}6\,\text{V}$
**Kysytty:** virran pieneneminen prosentteina alkuperäisestä virrasta
**Periaate:** Oletuksen mukaan LEDin jännite pysyy samana. Siksi koko jännitteen muutos tulee vastukselle. Virta saadaan Kirchhoffin jännitelaista ja Ohmin laista. Vastuksen jännite pienenee suhteellisesti enemmän kuin paristojen jännite, koska siitä on vähennetty LEDin vakiojännite.
**Kaava:** $I = \dfrac{U - U_\text{D}}{R}$, joten $I_1 = \dfrac{U_1 - U_\text{D}}{R}$, $I_2 = \dfrac{U_2 - U_\text{D}}{R}$ ja suhteellinen muutos on $\dfrac{I_1 - I_2}{I_1}$
**Muunnokset:** Ei tarvita: virrat jaetaan keskenään, joten yksikkö supistuu. Suhdeluku muutetaan prosenteiksi kertomalla sadalla.
**Sijoitus:** $I_1 = \dfrac{4{,}5\,\text{V} - 2{,}0\,\text{V}}{120\,\Omega} = 0{,}02083\,\text{A}$, $I_2 = \dfrac{3{,}6\,\text{V} - 2{,}0\,\text{V}}{120\,\Omega} = 0{,}01333\,\text{A}$ ja $\dfrac{I_1 - I_2}{I_1} = \dfrac{0{,}00750\,\text{A}}{0{,}02083\,\text{A}} = 0{,}36$
**Vastaus:** $36\,\%$, kaksi merkitsevää numeroa kuten jännitteissä.
**Järkevyys:** Paristojen jännite pieneni vain $0{,}9\,\text{V} : 4{,}5\,\text{V} = 20\,\%$, mutta vastuksen jännite pieneni $2{,}5\,\text{V}$:sta $1{,}6\,\text{V}$:iin, eli $36\,\%$. Siksi LED-taskulamppu himmenee selvästi, kun paristot alkavat tyhjentyä.

## fy6-14-L3-02
**Annettu:** paneelin mittausparit $(U;\ I)$ samassa valaistuksessa (yhdeksän paria tehtävässä)
**Kysytty:** kuormitusvastus $R$ ohmeina, kun teho on mittauksista suurin
**Periaate:** Paneelin teho on $P = UI$. Se on nolla oikosulussa ja tyhjäkäynnissä, joten suurin teho on niiden välissä, maksimitehopisteessä. Lasketaan jokaisen mittauksen teho ja valitaan suurin. Kuormitusvastus saadaan kuorman Ohmin laista $U = RI$. Kuorman jännite on nimittäin paneelin jännite ja kuorman virta on paneelin virta.
**Kaava:** $P = UI$, ja maksimitehopisteessä $U = RI$, josta $R = \dfrac{U}{I}$
**Muunnokset:** Ei tarvita: jännitteet ovat voltteina ja virrat ampeereina.
**Sijoitus:** Tehot ovat $0\,\text{W}$, $32{,}5\,\text{W}$, $44{,}5\,\text{W}$, $48{,}8\,\text{W}$, $49{,}3\,\text{W}$, $45{,}9\,\text{W}$, $36{,}1\,\text{W}$, $19{,}0\,\text{W}$ ja $0\,\text{W}$. Suurin on $17{,}0\,\text{V} \cdot 2{,}90\,\text{A} = 49{,}3\,\text{W}$, joten $R = \dfrac{17{,}0\,\text{V}}{2{,}90\,\text{A}} = 5{,}86\,\Omega$
**Vastaus:** $5{,}9\,\Omega$, kaksi merkitsevää numeroa, koska suurin teho ja viereinen $48{,}8\,\text{W}$ ovat niin lähellä toisiaan, että todellinen maksimitehopiste voi olla mittausten välissä.
**Järkevyys:** Oikosulussa kuormitusvastus on nolla ja tyhjäkäynnissä hyvin suuri, ja $5{,}9\,\Omega$ on niiden välissä. Suurin teho on käyrän polvessa, jossa virta on jo alkanut pienentyä mutta jännite on lähes suurimmillaan.

## fy6-14-L3-03
**Annettu:** nauhan jännite $U = 12\,\text{V}$, ryhmässä kolme LEDiä sarjassa, jokaisen jännite $U_\text{D} = 3{,}0\,\text{V}$, ryhmän virta $I = 20\,\text{mA}$
**Kysytty:** etuvastusten osuus nauhan tehosta prosentteina
**Periaate:** Ryhmät ovat rinnan, joten jokaisen ryhmän yli on $12\,\text{V}$. Ryhmät ovat samanlaisia, joten riittää tarkastella yhtä ryhmää. Ryhmässä LEDit ja vastus ovat sarjassa. Sama virta kulkee kaikkien läpi, ja jännite jakautuu: $U = U_R + 3U_\text{D}$. Vastuksen teho on $U_R I$ ja koko ryhmän teho $UI$.
**Kaava:** $U_R = U - 3U_\text{D}$ ja osuus $\dfrac{U_R I}{UI}$, josta osuus on $\dfrac{U - 3U_\text{D}}{U}$
**Muunnokset:** Ei tarvita: virta supistuu, ja jännitteiden suhde on suhdeluku. Lopuksi kerrotaan sadalla.
**Sijoitus:** $\dfrac{12\,\text{V} - 3 \cdot 3{,}0\,\text{V}}{12\,\text{V}} = \dfrac{3{,}0\,\text{V}}{12\,\text{V}} = 0{,}25 = 25\,\%$
**Vastaus:** $25\,\%$, kaksi merkitsevää numeroa kuten LEDin jännitteessä $3{,}0\,\text{V}$.
**Järkevyys:** Yhden ryhmän teho on $12\,\text{V} \cdot 0{,}020\,\text{A} = 0{,}24\,\text{W}$, ja vastuksen $3{,}0\,\text{V} \cdot 0{,}020\,\text{A} = 0{,}060\,\text{W}$, joka on neljäsosa. Siksi nauhassa on kolme LEDiä sarjassa. Yhdellä LEDillä vastukseen muuttuisi $9{,}0\,\text{V} : 12\,\text{V} = 75\,\%$ tehosta.

## fy6-14-L1-06
**Kysytty:** mitä piirissä tapahtuu, kun pariston jännite on $9{,}0\,\text{V}$ ja diodin symbolin kolmio osoittaa kohti vastusta, joka on kytketty miinusnapaan
**Periaate:** Virran suunnaksi sovitaan plusnavasta miinusnapaan. Diodi päästää virran läpi, kun virran suunta on sama kuin symbolin kolmion osoittama suunta (päästösuunta). Vastakkaiseen suuntaan diodi ei päästä virtaa (estosuunta). Päästösuunnassa diodin jännite on pieni. Loput pariston jännitteestä jää sarjassa olevalle vastukselle Kirchhoffin jännitelain mukaan.
**Mallivastaus:** Kolmio osoittaa kohti miinusnapaa eli virran kulkusuuntaan, joten diodi on päästösuunnassa. Virta kulkee piirissä. Diodin yli on vain pieni jännite (korkeintaan noin $1\,\text{V}$), koska vastus ottaa suurimman osan pariston $9{,}0\,\text{V}$:n jännitteestä. Muut vaihtoehdot ovat vääriä: ne joko pitävät diodia estosuunnassa tai antavat päästösuunnassa olevalle diodille koko pariston jännitteen.

## fy6-14-L1-07
**Kysytty:** miksi LEDin kanssa sarjaan tarvitaan etuvastus
**Periaate:** LEDin jännite pysyy päästösuunnassa lähes samana, vaikka virta muuttuu paljon: ominaiskäyrä nousee jyrkästi. Jos LED kytketään suoraan pariston napoihin, ylimääräiselle jännitteelle ei ole paikkaa muualla. Silloin virta kasvaa niin suureksi, että LED palaa loppuun. Sarjaan kytketty vastus ottaa Kirchhoffin jännitelain mukaan osan jännitteestä ($U = U_R + U_\text{D}$). Ohmin lain mukaan sen jännite määrää virran: $I = U_R : R$.
**Mallivastaus:** Etuvastus tarvitaan, koska LEDin virta kasvaa jyrkästi, kun LEDin jännite kasvaa vähänkin. Vastus ottaa pariston ylimääräisen jännitteen itselleen ja pitää virran sopivana. Muut vaihtoehdot ovat vääriä: vastus ei lisää virtaa, ei muuta jännitteen lajia eikä estä virtaa väärään suuntaan.

## fy6-14-L1-08
**Annettu:** pinta-ala $A = 12\,\text{cm}^2$, valon voimakkuus $G = 1000\,\text{W/m}^2$, jännite $U = 2{,}0\,\text{V}$, virta $I = 100\,\text{mA}$
**Kysytty:** hyötysuhde $\eta$ prosentteina
**Periaate:** Hyötysuhde kertoo, kuinka suuri osa valon tehosta muuttuu sähköksi. Se on kennon sähköteho jaettuna kennolle tulevan valon teholla. Sähköteho on jännite kertaa virta. Valon teho on valon voimakkuus kertaa pinta-ala.
**Kaava:** $P = UI$ ja $\eta = \dfrac{P}{GA}$
**Muunnokset:** $A = 12\,\text{cm}^2 = 12 \cdot 10^{-4}\,\text{m}^2 = 0{,}0012\,\text{m}^2$ ja $I = 100\,\text{mA} = 0{,}100\,\text{A}$
**Sijoitus:** $P = 2{,}0\,\text{V} \cdot 0{,}100\,\text{A} = 0{,}20\,\text{W}$ ja $\eta = \dfrac{0{,}20\,\text{W}}{1000\,\tfrac{\text{W}}{\text{m}^2} \cdot 0{,}0012\,\text{m}^2} = \dfrac{0{,}20\,\text{W}}{1{,}2\,\text{W}} = 0{,}167 = 16{,}7\,\%$
**Vastaus:** $17\,\%$, kaksi merkitsevää numeroa kuten jännitteessä ja pinta-alassa.
**Järkevyys:** Kennolle tulee valoa $1{,}2\,\text{W}$. Siitä noin kuudesosa, $0{,}20\,\text{W}$, muuttuu sähköksi: $1{,}2\,\text{W} : 6 = 0{,}20\,\text{W}$. Hyötysuhde on tavallisten piikennojen alueella $15$–$22\,\%$.

## fy6-14-L2-05
**Annettu:** LEDien jännitteet virralla $15\,\text{mA}$: sininen $3{,}10\,\text{V}$, punainen $1{,}90\,\text{V}$, keltainen $2{,}10\,\text{V}$, lähteen jännite $U = 5{,}0\,\text{V}$, virta $I = 15\,\text{mA}$
**Kysytty:** a) mikä LED tarvitsee suurimman etuvastuksen, b) sen etuvastuksen resistanssi $R$ ohmeina
**Periaate:** Lähde, vastus ja LED ovat sarjassa, joten molempien läpi kulkee sama virta ja $U = U_R + U_\text{D}$. Vastuksen jännite $U_R = U - U_\text{D}$ on sitä suurempi, mitä pienempi LEDin jännite on. Virta on kaikilla sama. Ohmin lain $R = U_R : I$ mukaan suurin vastuksen jännite antaa siis suurimman resistanssin. Suurin etuvastus tarvitaan LEDille, jonka jännite on pienin. Se on punainen LED.
**Kaava:** $R = \dfrac{U - U_\text{D}}{I}$
**Muunnokset:** $I = 15\,\text{mA} = 0{,}015\,\text{A}$
**Sijoitus:** Punaiselle LEDille $R = \dfrac{5{,}0\,\text{V} - 1{,}90\,\text{V}}{0{,}015\,\text{A}} = \dfrac{3{,}1\,\text{V}}{0{,}015\,\text{A}} = 207\,\Omega$
**Vastaus:** $210\,\Omega$ (punaisen LEDin etuvastus), kaksi merkitsevää numeroa kuten virrassa.
**Järkevyys:** Tarkistus: $207\,\Omega \cdot 0{,}015\,\text{A} = 3{,}1\,\text{V}$, ja $3{,}1\,\text{V} + 1{,}90\,\text{V} = 5{,}0\,\text{V}$. Muille LEDeille tulee pienemmät vastukset: keltaiselle $2{,}9\,\text{V} : 0{,}015\,\text{A} = 193\,\Omega$ ja siniselle $1{,}9\,\text{V} : 0{,}015\,\text{A} = 127\,\Omega$. Punainen on siis suurin.

## fy6-14-L2-06
**Annettu:** taulukon mittausparit $(R;\ U;\ I)$ kahdeksalla kuormitusvastuksella
**Kysytty:** kennon suurin mitattu teho $P$ milliwatteina
**Periaate:** Aurinkokennon teho on napojen välinen jännite kertaa virta. Teho lasketaan jokaisella kuormalla, ja suurin arvo valitaan. Kuormitusvastus ei vaikuta laskuun, koska sen vaikutus on jo mukana mitatussa jännitteessä ja virrassa.
**Kaava:** $P = UI$
**Muunnokset:** Ei tarvita: $\text{V} \cdot \text{mA} = \text{mW}$.
**Sijoitus:** Tehot ovat $10\,\Omega$: $0{,}99\,\text{V} \cdot 99\,\text{mA} = 98\,\text{mW}$, $15\,\Omega$: $146\,\text{mW}$, $20\,\Omega$: $178\,\text{mW}$, $22\,\Omega$: $1{,}99\,\text{V} \cdot 91\,\text{mA} = 181\,\text{mW}$, $27\,\Omega$: $165\,\text{mW}$, $33\,\Omega$: $145\,\text{mW}$, $47\,\Omega$: $109\,\text{mW}$ ja $100\,\Omega$: $54\,\text{mW}$. Suurin on $22\,\Omega$:n kohdalla.
**Vastaus:** $181\,\text{mW}$, kolme merkitsevää numeroa kuten jännitteessä ja virrassa.
**Järkevyys:** Teho on pieni kuormilla $10\,\Omega$ (jännite on pieni) ja $100\,\Omega$ (virta on pieni). Suurin teho on niiden välissä käyrän polvessa. Tarkistus: $U : I = 1{,}99\,\text{V} : 0{,}091\,\text{A} = 21{,}9\,\Omega \approx 22\,\Omega$, joten mittaus täsmää kuormitusvastuksen kanssa.

## fy6-14-L2-07
**Annettu:** pariston jännite $U = 9{,}0\,\text{V}$, LEDin jännite $U_\text{D} = 3{,}2\,\text{V}$, virta $I = 15\,\text{mA}$; opiskelija sai $600\,\Omega$
**Kysytty:** a) opiskelijan virhe, b) oikea etuvastus $R$ ohmeina
**Periaate:** Lähde, vastus ja LED ovat sarjassa, joten pariston jännite jakautuu vastukselle ja LEDille: $U = U_R + U_\text{D}$. Ohmin laki $R = U_R : I$ koskee vastuksen omaa jännitettä, ei koko pariston jännitettä. Opiskelija käytti vastuksen jännitteenä koko pariston jännitettä ja unohti LEDin jännitteen. Virhe tekee vastuksesta liian suuren, ja virta jäisi tavoitetta pienemmäksi.
**Kaava:** $R = \dfrac{U - U_\text{D}}{I}$
**Muunnokset:** $I = 15\,\text{mA} = 0{,}015\,\text{A}$
**Sijoitus:** $R = \dfrac{9{,}0\,\text{V} - 3{,}2\,\text{V}}{0{,}015\,\text{A}} = \dfrac{5{,}8\,\text{V}}{0{,}015\,\text{A}} = 387\,\Omega$
**Vastaus:** $390\,\Omega$, kaksi merkitsevää numeroa kuten jännitteissä ja virrassa.
**Järkevyys:** Tarkistus: $387\,\Omega \cdot 0{,}015\,\text{A} = 5{,}8\,\text{V}$, ja $5{,}8\,\text{V} + 3{,}2\,\text{V} = 9{,}0\,\text{V}$. Opiskelijan $600\,\Omega$ antaisi virraksi vain $5{,}8\,\text{V} : 600\,\Omega = 9{,}7\,\text{mA}$, joten LED olisi himmeämpi kuin haluttiin.

## fy6-14-L2-08
**Kysytty:** mitkä kolmesta valosta palavat ja miksi.
**Periaate:** Diodi ja LED johtavat vain päästösuunnassa, kun anodi on pariston plusnavan puolella. Estosuunnassa virtaa ei kulje. Rinnan kytketyt haarat ovat kukin pariston koko jännitteessä, joten jokainen haara on oma virtapiirinsä. Yhden haaran estosuuntainen diodi katkaisee vain sen haaran virran. Sarjassa olevien komponenttien läpi kulkee sama virta.
**Mallivastaus:** Vain LED A palaa.

Haara 1: LEDin anodi on plusnavan puolella, joten LED on päästösuunnassa. Haaran jännite $4{,}5\,\text{V}$ on suurempi kuin LEDin jännite $2{,}0\,\text{V}$. Etuvastuksen yli jää $4{,}5\,\text{V} - 2{,}0\,\text{V} = 2{,}5\,\text{V}$. Virta kulkee, ja LED A palaa.

Haara 2: LEDin katodi on plusnavan puolella, joten LED B on estosuunnassa. Virtaa ei kulje, ja koko $4{,}5\,\text{V}$ on LEDin yli.

Haara 3: piidiodin katodi on plusnavan puolella, joten diodi on estosuunnassa. Lampun lanka johtaisi kumpaankin suuntaan. Sarjassa lampun ja diodin läpi kulkee kuitenkin sama virta, ja diodi pysäyttää sen. Lamppu C ei pala.

Perustelu on siis, että diodi johtaa vain, kun anodi on plusnavan puolella, ja jokainen rinnakkainen haara toimii omana virtapiirinään. Etuvastuksen tarve on tosi asia, mutta se ei kerro virran suunnasta. Jos haarat olisivat sarjassa, yksikin estosuuntainen diodi katkaisisi koko piirin virran, eikä mikään valo palaisi.

## fy6-14-L3-04
**Annettu:** pinta-ala $A = 24\,\text{m}^2$, hyötysuhde $\eta = 19\,\%$, kuukausittaiset säteilyenergiat $H$ ja kulutukset $E_\text{kul}$ taulukossa
**Kysytty:** a) vuosituotanto $E$, b) omavaraisuusaste prosentteina, c) kuukaudet, joissa tuotanto on kulutusta pienempi, ja omavaraisuusasteen rajoitus
**Periaate:** Hyötysuhde on sähköenergia jaettuna paneeleille tulevalla säteilyenergialla. Säteilyenergia on säteilyenergia neliömetriä kohti kertaa pinta-ala, $H A$. Tuotettu sähköenergia on siis $E = \eta H A$. Vuosituotanto saadaan laskemalla kuukausien säteilyenergiat yhteen. Omavaraisuusaste on vuosituotannon ja vuosikulutuksen suhde.
**Kaava:** $E = \eta A \sum H$ ja omavaraisuusaste $= \dfrac{E}{\sum E_\text{kul}}$
**Muunnokset:** $\eta = 19\,\% = 0{,}19$. Muita ei tarvita: energiat ovat kilowattitunteina.
**Sijoitus:** a) Säteilyenergioiden summa on $\sum H = 1027\,\text{kWh/m}^2$, joten $E = 0{,}19 \cdot 24\,\text{m}^2 \cdot 1027\,\tfrac{\text{kWh}}{\text{m}^2} = 4683\,\text{kWh}$. b) Kulutusten summa on $\sum E_\text{kul} = 5340\,\text{kWh}$, joten omavaraisuusaste on $\dfrac{4683\,\text{kWh}}{5340\,\text{kWh}} = 0{,}877 = 87{,}7\,\%$. c) Kuukausituotanto on $E_\text{kk} = 0{,}19 \cdot 24\,\text{m}^2 \cdot H = 4{,}56\,\text{m}^2 \cdot H$. Se on pienempi kuin kulutus tammi-, helmi- ja maaliskuussa sekä loka-, marras- ja joulukuussa. Esimerkiksi tammikuussa $4{,}56\,\text{m}^2 \cdot 12\,\tfrac{\text{kWh}}{\text{m}^2} = 55\,\text{kWh}$, kun kulutus on $620\,\text{kWh}$. Joulukuussa tuotanto on $36\,\text{kWh}$, kun kulutus on $650\,\text{kWh}$. Näiden kuuden kuukauden kulutus on yhteensä $3370\,\text{kWh}$ ja tuotanto yhteensä $853\,\text{kWh}$, joten vajaus on $2517\,\text{kWh}$.
**Vastaus:** $88\,\%$, kaksi merkitsevää numeroa kuten hyötysuhteessa $19\,\%$. Vuosituotanto on noin $4700\,\text{kWh}$.
**Järkevyys:** Tuotanto on noin $4{,}7\,\text{MWh}$. Se sopii $24\,\text{m}^2$:n paneelistolle Suomessa. Se on vähän alle talon kulutuksen $5340\,\text{kWh}$, joten omavaraisuusaste on alle $100\,\%$. Omavaraisuusaste on vuosisumma. Kesän ylijäämää ei voi käyttää talvella ilman varastointia. Talven vajaus $2517\,\text{kWh}$ on $2517 : 5340 = 47\,\%$ vuosikulutuksesta. Verkosta ostetaan siis vähintään tämä osuus, vaikka omavaraisuusaste on $88\,\%$.

## fy6-14-L3-05
**Annettu:** LEDin ominaiskäyrän mittauspisteet $(U_\text{D};\ I)$, pariston jännite $U = 4{,}5\,\text{V}$, etuvastus $R = 180\,\Omega$, suurin sallittu virta $25\,\text{mA}$
**Kysytty:** a) kynnysjännite, b) työpisteen virta milliampeereina, c) LEDin jännitteen muutos virran kasvaessa ja vakiojännitteen perustelu
**Periaate:** Sarjapiirissä sama virta kulkee vastuksen ja LEDin läpi, ja $U = U_R + U_\text{D}$. Vastuksen kautta tuleva virta on $I = \dfrac{U - U_\text{D}}{R}$ kullakin LEDin jännitteellä. LEDin virta saadaan ominaiskäyrästä. Työpiste on se jännite, jolla nämä kaksi virtaa ovat yhtä suuret: kuormasuoran ja ominaiskäyrän leikkauspiste.
**Kuvaajan lukeminen:** a) Ominaiskäyrän jyrkkä suora osa on taulukon kahden viimeisen pisteen välissä: virta kasvaa $20\,\text{mA}$:sta $41\,\text{mA}$:iin, kun jännite kasvaa $2{,}05\,\text{V}$:sta $2{,}10\,\text{V}$:iin. Suoran kulmakerroin on siis $\dfrac{41\,\text{mA} - 20\,\text{mA}}{2{,}10\,\text{V} - 2{,}05\,\text{V}} = 420\,\tfrac{\text{mA}}{\text{V}}$. Suora leikkaa jänniteakselin kohdassa $2{,}05\,\text{V} - \dfrac{20\,\text{mA}}{420\,\text{mA/V}} = 2{,}05\,\text{V} - 0{,}048\,\text{V} = 2{,}00\,\text{V}$. Kynnysjännite on noin $2{,}0\,\text{V}$.
**Kaava:** $I = \dfrac{U - U_\text{D}}{R}$ vastuksen kautta ja ominaiskäyrän virta taulukosta
**Muunnokset:** Ei tarvita: jännitteet ovat voltteina ja resistanssi ohmeina. Tulos $\text{V} : \Omega = \text{A}$ muutetaan milliampeereiksi kertomalla luvulla $1000$.
**Sijoitus:** Vastuksen kautta tuleva virta on jännitteellä $2{,}00\,\text{V}$ $\dfrac{4{,}5\,\text{V} - 2{,}00\,\text{V}}{180\,\Omega} = 13{,}9\,\text{mA}$ ja jännitteellä $2{,}05\,\text{V}$ $\dfrac{4{,}5\,\text{V} - 2{,}05\,\text{V}}{180\,\Omega} = 13{,}6\,\text{mA}$. LEDin virta on näillä jännitteillä $9{,}8\,\text{mA}$ ja $20\,\text{mA}$. Jännitteellä $2{,}00\,\text{V}$ vastuksen kautta tuleva virta on LEDin virtaa suurempi, jännitteellä $2{,}05\,\text{V}$ pienempi. Leikkaus on siis välillä. Suorina kuvattuna leikkaus on kohdassa $U_\text{D} \approx 2{,}02\,\text{V}$ ja $I \approx 13{,}8\,\text{mA}$. Tarkistus: $\dfrac{4{,}5\,\text{V} - 2{,}02\,\text{V}}{180\,\Omega} = 13{,}8\,\text{mA}$. c) Kun virta kasvaa arvosta $9{,}8\,\text{mA}$ arvoon $41\,\text{mA}$ eli yli nelinkertaiseksi, jännite muuttuu arvosta $2{,}00\,\text{V}$ arvoon $2{,}10\,\text{V}$ eli $0{,}10\,\text{V}$.
**Vastaus:** $14\,\text{mA}$, kaksi merkitsevää numeroa, koska taulukon pisteiden väli on karkea ja tulos on luettu kahden pisteen väliltä. Työpisteen jännite on noin $2{,}0\,\text{V}$. Virta on sallittua pienempi kuin $25\,\text{mA}$.
**Järkevyys:** Virta $13{,}8\,\text{mA}$ on pienempi kuin sallittu $25\,\text{mA}$, joten LED kestää. Jännite $2{,}02\,\text{V}$ on vihreän LEDin tavallisella alueella. Työpisteen jännite on hieman kynnysjännitettä $2{,}0\,\text{V}$ suurempi, kuten jyrkällä käyrällä kuuluukin. Perustelu c): jännite muuttuu vain $0{,}10\,\text{V}$ eli noin $5\,\%$, vaikka virta kasvaa yli nelinkertaiseksi. Siksi LEDin jännite voidaan pitää vakiona, ja etuvastukselle jää jännite $U - U_\text{D}$, joka määrää virran. Ilman vastusta virta määräytyisi pelkästään jyrkästä käyrästä, ja jo pieni jännitteen kasvu tekisi virrasta suuren.
