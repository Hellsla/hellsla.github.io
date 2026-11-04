## fy6-14-L1-01
**Annettu:** LEDin jännite $U_\text{D} = 2{,}0\,\text{V}$, virta $I = 15\,\text{mA}$
**Kysytty:** LEDin teho $P_\text{D}$ milliwatteina
**Periaate:** Komponentin sähköteho on sen jännite kertaa sen läpi kulkeva virta. Tämä pätee myös LEDille, vaikka se ei noudata Ohmin lakia, koska teho on aina energia, jonka varaus luovuttaa komponentissa aikayksikössä.
**Kaava:** $P_\text{D} = U_\text{D} I$
**Muunnokset:** $I = 15\,\text{mA} = 15 \cdot 10^{-3}\,\text{A} = 0{,}015\,\text{A}$
**Sijoitus:** $P_\text{D} = 2{,}0\,\text{V} \cdot 0{,}015\,\text{A} = 0{,}030\,\text{W} = 30\,\text{mW}$
**Vastaus:** $30\,\text{mW}$, kaksi merkitsevää numeroa kuten jännitteessä ja virrassa.
**Järkevyys:** Yksikkö täsmää: $\text{V} \cdot \text{mA} = \text{mW}$, ja $2 \cdot 15 = 30$. Merkkivalon LEDin teho on kymmeniä milliwatteja, paljon pienempi kuin hehkulampun, kuten kokemuksesta tiedetään.

## fy6-14-L1-02
**Annettu:** lähteen jännite $U = 5{,}0\,\text{V}$, LEDin jännite $U_\text{D} = 3{,}1\,\text{V}$, virta $I = 20\,\text{mA}$
**Kysytty:** etuvastuksen resistanssi $R$ ohmeina
**Periaate:** Lähde, vastus ja LED ovat sarjassa, joten sama virta kulkee kaikkien läpi. Kirchhoffin jännitelain mukaan lähteen jännite jakautuu: $U = U_R + U_\text{D}$. Vastus noudattaa Ohmin lakia, $U_R = RI$.
**Kaava:** $U = RI + U_\text{D}$, josta $R = \dfrac{U - U_\text{D}}{I}$
**Muunnokset:** $I = 20\,\text{mA} = 20 \cdot 10^{-3}\,\text{A} = 0{,}020\,\text{A}$
**Sijoitus:** $R = \dfrac{5{,}0\,\text{V} - 3{,}1\,\text{V}}{0{,}020\,\text{A}} = \dfrac{1{,}9\,\text{V}}{0{,}020\,\text{A}} = 95\,\Omega$
**Vastaus:** $95\,\Omega$, kaksi merkitsevää numeroa kuten jännitteiden erotuksessa $1{,}9\,\text{V}$ ja virrassa.
**Järkevyys:** Tarkistus: $95\,\Omega \cdot 0{,}020\,\text{A} = 1{,}9\,\text{V}$, ja $1{,}9\,\text{V} + 3{,}1\,\text{V} = 5{,}0\,\text{V}$. Valkoisen LEDin jännite on suuri, joten vastukselle jää vain vähän jännitettä ja vastus on pieni.

## fy6-14-L1-03
**Annettu:** pariston jännite $U = 9{,}0\,\text{V}$, vastus $R = 1{,}0\,\text{k}\Omega$, diodin jännite $U_\text{D} = 0{,}70\,\text{V}$, diodi päästösuunnassa
**Kysytty:** virta $I$ milliampeereina
**Periaate:** Diodi on päästösuunnassa, joten virta kulkee, ja diodin jännite on tehtävässä annettu $0{,}70\,\text{V}$. Paristo, vastus ja diodi ovat sarjassa: pariston jännite jakautuu vastukselle ja diodille, ja vastuksen jännite on $U_R = RI$.
**Kaava:** $U = RI + U_\text{D}$, josta $I = \dfrac{U - U_\text{D}}{R}$
**Muunnokset:** $R = 1{,}0\,\text{k}\Omega = 1{,}0 \cdot 1000\,\Omega = 1000\,\Omega$
**Sijoitus:** $I = \dfrac{9{,}0\,\text{V} - 0{,}70\,\text{V}}{1000\,\Omega} = \dfrac{8{,}3\,\text{V}}{1000\,\Omega} = 0{,}0083\,\text{A} = 8{,}3\,\text{mA}$
**Vastaus:** $8{,}3\,\text{mA}$, kaksi merkitsevää numeroa kuten jännitteessä $9{,}0\,\text{V}$ ja resistanssissa $1{,}0\,\text{k}\Omega$.
**Järkevyys:** Ilman diodia virta olisi $9{,}0\,\text{V} : 1000\,\Omega = 9{,}0\,\text{mA}$. Diodi vie vain vähän jännitettä, joten virta on hieman pienempi, kuten pitääkin.

## fy6-14-L1-04
**Annettu:** paneelin jännite $U = 17{,}5\,\text{V}$, virta $I = 5{,}40\,\text{A}$
**Kysytty:** paneelin teho $P$ watteina
**Periaate:** Aurinkopaneeli on tasajännitelähde. Sen antama sähköteho on napojen välinen jännite kertaa virta, kuten minkä tahansa lähteen teho.
**Kaava:** $P = UI$
**Muunnokset:** Ei tarvita: jännite on voltteina ja virta ampeereina, ja $\text{V} \cdot \text{A} = \text{W}$.
**Sijoitus:** $P = 17{,}5\,\text{V} \cdot 5{,}40\,\text{A} = 94{,}5\,\text{W}$
**Vastaus:** $94{,}5\,\text{W}$, kolme merkitsevää numeroa kuten jännitteessä ja virrassa.
**Järkevyys:** Arvio $18\,\text{V} \cdot 5\,\text{A} = 90\,\text{W}$ on lähellä tulosta. Noin $100\,\text{W}$:n paneeli on tavallinen mökin aurinkopaneeli.

## fy6-14-L1-05
**Annettu:** vihreän LEDin ominaiskäyrä, virta $I = 10\,\text{mA}$
**Kysytty:** LEDin teho $P_\text{D}$ milliwatteina
**Periaate:** Ominaiskäyrä kertoo, mikä jännite LEDin yli on kullakin virralla. Teho on jännite kertaa virta, joten tarvitaan virtaa $10\,\text{mA}$ vastaava jännite.
**Kuvaajan lukeminen:** Kuljetaan pystyakselin kohdasta $10\,\text{mA}$ vaakasuoraan käyrälle. Käyrä leikkaa $10\,\text{mA}$:n ruudukkoviivan pystysuoralla ruudukkoviivalla, joka on $2{,}0\,\text{V}$:n kohdasta yhden $0{,}2\,\text{V}$:n ruudun oikealla, joten $U_\text{D} = 2{,}2\,\text{V}$.
**Kaava:** $P_\text{D} = U_\text{D} I$
**Muunnokset:** $I = 10\,\text{mA} = 0{,}010\,\text{A}$
**Sijoitus:** $P_\text{D} = 2{,}2\,\text{V} \cdot 0{,}010\,\text{A} = 0{,}022\,\text{W} = 22\,\text{mW}$
**Vastaus:** $22\,\text{mW}$, kaksi merkitsevää numeroa, koska jännite luetaan $0{,}2\,\text{V}$:n ruudukosta ja virta $5\,\text{mA}$:n ruudukosta.
**Järkevyys:** Vihreän LEDin jännite $2{,}2\,\text{V}$ on punaisen ($1{,}8$–$2{,}0\,\text{V}$) ja sinisen (noin $3\,\text{V}$) välissä, kuten luvun tekstissä. Teho on muutamia kymmeniä milliwatteja, tavallinen merkkivalolle.

## fy6-14-L2-01
**Annettu:** pariston jännite $U = 9{,}0\,\text{V}$, etuvastus $R = 470\,\Omega$, LED estosuunnassa; oletus: estosuunnassa virtaa ei kulje
**Kysytty:** LEDin jännite $U_\text{D}$ voltteina
**Periaate:** Estosuunnassa diodin läpi ei käytännössä kulje virtaa. Koska LED ja vastus ovat sarjassa, myös vastuksen virta on nolla, joten Ohmin lain mukaan vastuksen jännite on nolla. Kirchhoffin jännitelain mukaan koko pariston jännite on silloin LEDin yli.
**Kaava:** $U = U_R + U_\text{D}$ ja $U_R = RI$, josta virralla $I = 0$ saadaan $U_\text{D} = U - RI = U$
**Muunnokset:** Ei tarvita: virta on nolla, joten vastuksen arvoa ei tarvitse muuntaa.
**Sijoitus:** $U_\text{D} = 9{,}0\,\text{V} - 470\,\Omega \cdot 0\,\text{A} = 9{,}0\,\text{V}$
**Vastaus:** $9{,}0\,\text{V}$, kaksi merkitsevää numeroa kuten pariston jännitteessä.
**Järkevyys:** Etuvastus ei suojaa estosuunnassa olevaa LEDiä, koska vastuksen yli ei ole jännitettä. Tavallinen LED kestää estosuunnassa usein vain noin $5\,\text{V}$, joten $9{,}0\,\text{V}$ voi rikkoa sen; siksi napaisuus tarkistetaan ennen kytkemistä.

## fy6-14-L2-02
**Annettu:** pariston jännite $U = 9{,}0\,\text{V}$, kaksi LEDiä sarjassa, kummankin jännite $U_\text{D} = 2{,}0\,\text{V}$, virta $I = 20\,\text{mA}$
**Kysytty:** etuvastuksen resistanssi $R$ ohmeina
**Periaate:** Kaikki komponentit ovat sarjassa, joten sama virta kulkee niiden läpi. Pariston jännite jakautuu vastukselle ja molemmille LEDeille: $U = U_R + 2U_\text{D}$. Vastuksen jännite on $U_R = RI$.
**Kaava:** $U = RI + 2U_\text{D}$, josta $R = \dfrac{U - 2U_\text{D}}{I}$
**Muunnokset:** $I = 20\,\text{mA} = 0{,}020\,\text{A}$
**Sijoitus:** $R = \dfrac{9{,}0\,\text{V} - 2 \cdot 2{,}0\,\text{V}}{0{,}020\,\text{A}} = \dfrac{5{,}0\,\text{V}}{0{,}020\,\text{A}} = 250\,\Omega$
**Vastaus:** $250\,\Omega$, kaksi merkitsevää numeroa kuten jännitteissä ja virrassa.
**Järkevyys:** Yhdelle LEDille vastus olisi $7{,}0\,\text{V} : 0{,}020\,\text{A} = 350\,\Omega$. Toinen LED vie $2{,}0\,\text{V}$ lisää, joten vastukselle jää vähemmän jännitettä ja vastus on pienempi.

## fy6-14-L2-03
**Annettu:** pinta-ala $A = 1{,}6\,\text{m}^2$, valon voimakkuus $G = 800\,\text{W/m}^2$, sähköteho $P = 260\,\text{W}$
**Kysytty:** hyötysuhde $\eta$ prosentteina
**Periaate:** Hyötysuhde on hyödyllinen teho jaettuna otetulla teholla. Paneeli ottaa vastaan valon tehon, joka on valon voimakkuus kertaa pinta-ala, ja hyödyllinen teho on paneelin antama sähköteho.
**Kaava:** $\eta = \dfrac{P}{GA}$
**Muunnokset:** Ei tarvita: $\tfrac{\text{W}}{\text{m}^2} \cdot \text{m}^2 = \text{W}$. Lopuksi suhdeluku muutetaan prosenteiksi kertomalla sadalla.
**Sijoitus:** $\eta = \dfrac{260\,\text{W}}{800\,\tfrac{\text{W}}{\text{m}^2} \cdot 1{,}6\,\text{m}^2} = \dfrac{260\,\text{W}}{1280\,\text{W}} = 0{,}203 = 20{,}3\,\%$
**Vastaus:** $20\,\%$, kaksi merkitsevää numeroa kuten pinta-alassa $1{,}6\,\text{m}^2$.
**Järkevyys:** Paneeliin tulee valoa noin $1300\,\text{W}$, ja siitä noin viidesosa muuttuu sähköksi. Hyötysuhde on tavallisten piikennojen alueella $15$–$22\,\%$.

## fy6-14-L2-04
**Annettu:** kennon teho $P = 0{,}35\,\text{W}$, aika $t = 6{,}0\,\text{h}$
**Kysytty:** sähköenergia $E$ kilojouleina
**Periaate:** Teho on energia aikayksikköä kohti. Kun teho oletetaan koko ajan keskimääräiseksi tehoksi, energia on teho kertaa aika.
**Kaava:** $P = \dfrac{E}{t}$, josta $E = Pt$
**Muunnokset:** $t = 6{,}0\,\text{h} = 6{,}0 \cdot 3600\,\text{s} = 21\,600\,\text{s}$
**Sijoitus:** $E = 0{,}35\,\text{W} \cdot 21\,600\,\text{s} = 7560\,\text{J} = 7{,}56\,\text{kJ}$
**Vastaus:** $7{,}6\,\text{kJ}$, kaksi merkitsevää numeroa kuten tehossa ja ajassa.
**Järkevyys:** Wattitunteina energia on $0{,}35\,\text{W} \cdot 6{,}0\,\text{h} = 2{,}1\,\text{Wh}$, ja $2{,}1 \cdot 3600\,\text{J} = 7560\,\text{J}$, sama tulos. Määrä on pienen akun luokkaa, mikä riittää yhdelle LEDille koko yöksi.

## fy6-14-L3-01
**Annettu:** LEDin jännite $U_\text{D} = 2{,}0\,\text{V}$, etuvastus $R = 120\,\Omega$, paristojen jännite aluksi $U_1 = 4{,}5\,\text{V}$ ja lopuksi $U_2 = 3{,}6\,\text{V}$
**Kysytty:** virran pieneneminen prosentteina alkuperäisestä virrasta
**Periaate:** LEDin jännite pysyy oletuksen mukaan samana, joten koko jännitteen muutos kohdistuu vastukseen. Virta saadaan Kirchhoffin jännitelaista ja Ohmin laista. Vastuksen jännite pienenee suhteellisesti enemmän kuin paristojen jännite, koska siitä on vähennetty LEDin vakiojännite.
**Kaava:** $I = \dfrac{U - U_\text{D}}{R}$, joten $I_1 = \dfrac{U_1 - U_\text{D}}{R}$, $I_2 = \dfrac{U_2 - U_\text{D}}{R}$ ja suhteellinen muutos on $\dfrac{I_1 - I_2}{I_1}$
**Muunnokset:** Ei tarvita: virrat jaetaan keskenään, joten yksikkö supistuu. Suhdeluku muutetaan prosenteiksi kertomalla sadalla.
**Sijoitus:** $I_1 = \dfrac{4{,}5\,\text{V} - 2{,}0\,\text{V}}{120\,\Omega} = 0{,}02083\,\text{A}$, $I_2 = \dfrac{3{,}6\,\text{V} - 2{,}0\,\text{V}}{120\,\Omega} = 0{,}01333\,\text{A}$ ja $\dfrac{I_1 - I_2}{I_1} = \dfrac{0{,}00750\,\text{A}}{0{,}02083\,\text{A}} = 0{,}36$
**Vastaus:** $36\,\%$, kaksi merkitsevää numeroa kuten jännitteissä.
**Järkevyys:** Paristojen jännite pieneni vain $0{,}9\,\text{V} : 4{,}5\,\text{V} = 20\,\%$, mutta vastuksen jännite pieneni $2{,}5\,\text{V}$:sta $1{,}6\,\text{V}$:iin, eli $36\,\%$. Siksi LED-taskulamppu himmenee selvästi, kun paristot alkavat tyhjentyä.

## fy6-14-L3-02
**Annettu:** paneelin mittausparit $(U;\ I)$ samassa valaistuksessa (yhdeksän paria tehtävässä)
**Kysytty:** kuormitusvastus $R$ ohmeina, kun teho on mittauksista suurin
**Periaate:** Paneelin teho on $P = UI$. Se on nolla oikosulussa ja tyhjäkäynnissä, joten suurin teho on niiden välissä, maksimitehopisteessä. Lasketaan jokaisen mittauksen teho, valitaan suurin, ja kuormitusvastus saadaan Ohmin laista $U = RI$ kuormalle, koska kuorman jännite on paneelin jännite ja sen virta paneelin virta.
**Kaava:** $P = UI$, ja maksimitehopisteessä $U = RI$, josta $R = \dfrac{U}{I}$
**Muunnokset:** Ei tarvita: jännitteet ovat voltteina ja virrat ampeereina.
**Sijoitus:** Tehot ovat $0\,\text{W}$, $32{,}5\,\text{W}$, $44{,}5\,\text{W}$, $48{,}8\,\text{W}$, $49{,}3\,\text{W}$, $45{,}9\,\text{W}$, $36{,}1\,\text{W}$, $19{,}0\,\text{W}$ ja $0\,\text{W}$. Suurin on $17{,}0\,\text{V} \cdot 2{,}90\,\text{A} = 49{,}3\,\text{W}$, joten $R = \dfrac{17{,}0\,\text{V}}{2{,}90\,\text{A}} = 5{,}86\,\Omega$
**Vastaus:** $5{,}9\,\Omega$, kaksi merkitsevää numeroa, koska suurin teho ja viereinen $48{,}8\,\text{W}$ ovat niin lähellä toisiaan, että todellinen maksimitehopiste voi olla mittausten välissä.
**Järkevyys:** Oikosulussa kuormitusvastus on nolla ja tyhjäkäynnissä hyvin suuri, ja $5{,}9\,\Omega$ on niiden välissä. Suurin teho on käyrän polvessa, jossa virta on jo alkanut pienentyä mutta jännite on lähes suurimmillaan.

## fy6-14-L3-03
**Annettu:** nauhan jännite $U = 12\,\text{V}$, ryhmässä kolme LEDiä sarjassa, jokaisen jännite $U_\text{D} = 3{,}0\,\text{V}$, ryhmän virta $I = 20\,\text{mA}$
**Kysytty:** etuvastusten osuus nauhan tehosta prosentteina
**Periaate:** Ryhmät ovat rinnan, joten jokaisen ryhmän yli on $12\,\text{V}$, ja ryhmät ovat samanlaisia, joten riittää tarkastella yhtä ryhmää. Ryhmässä LEDit ja vastus ovat sarjassa, joten sama virta kulkee kaikkien läpi, ja jännite jakautuu: $U = U_R + 3U_\text{D}$. Vastuksen teho on $U_R I$ ja koko ryhmän teho $UI$.
**Kaava:** $U_R = U - 3U_\text{D}$ ja osuus $\dfrac{U_R I}{UI}$, josta osuus on $\dfrac{U - 3U_\text{D}}{U}$
**Muunnokset:** Ei tarvita: virta supistuu, ja jännitteiden suhde on suhdeluku. Lopuksi kerrotaan sadalla.
**Sijoitus:** $\dfrac{12\,\text{V} - 3 \cdot 3{,}0\,\text{V}}{12\,\text{V}} = \dfrac{3{,}0\,\text{V}}{12\,\text{V}} = 0{,}25 = 25\,\%$
**Vastaus:** $25\,\%$, kaksi merkitsevää numeroa kuten LEDin jännitteessä $3{,}0\,\text{V}$.
**Järkevyys:** Yhden ryhmän teho on $12\,\text{V} \cdot 0{,}020\,\text{A} = 0{,}24\,\text{W}$, ja vastuksen $3{,}0\,\text{V} \cdot 0{,}020\,\text{A} = 0{,}060\,\text{W}$, joka on neljäsosa. Siksi nauhassa on kolme LEDiä sarjassa: yhdellä LEDillä vastukseen muuttuisi $9{,}0\,\text{V} : 12\,\text{V} = 75\,\%$ tehosta.
