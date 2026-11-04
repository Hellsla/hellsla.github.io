## fy7-5-L1-01
**Annettu:** neliön sivu $a = 0{,}12\,\text{m}$, magneettivuon tiheys $B = 0{,}35\,\text{T}$, kenttä kohtisuorassa silmukan tasoa vastaan
**Kysytty:** silmukan läpi kulkeva magneettivuo $\Phi$ millivebereinä
**Periaate:** Kun homogeeninen kenttä on kohtisuorassa silmukan tasoa vastaan, magneettivuo on kentän ja pinta-alan tulo. Silmukka on neliö, joten sen pinta-ala on sivun neliö.
**Kaava:** $\Phi = BA$ ja $A = a^2$, joten $\Phi = B a^2$
**Muunnokset:** Lähtöarvot ovat SI-yksiköissä. Vastaus muunnetaan millivebereiksi: $1\,\text{Wb} = 1000\,\text{mWb}$.
**Sijoitus:** $\Phi = 0{,}35\,\text{T} \cdot (0{,}12\,\text{m})^2 = 0{,}35\,\text{T} \cdot 0{,}0144\,\text{m}^2 = 0{,}00504\,\text{Wb} = 5{,}04\,\text{mWb}$
**Vastaus:** $5{,}0\,\text{mWb}$, kaksi merkitsevää numeroa kuten lähtöarvoissa.
**Järkevyys:** Silmukan pinta-ala on vähän alle $0{,}015\,\text{m}^2$ eli noin A6-arkin (postikortin) kokoinen, ja kenttä on kymmenesosien teslojen luokkaa, joten vuo on tuhannesosien vebereiden luokkaa. Kaksinkertainen sivu antaisi nelinkertaisen vuon.

## fy7-5-L1-02
**Annettu:** kierrosten lukumäärä $N = 400$, yhden kierroksen vuon muutos $\Delta\Phi = 1{,}5\,\text{mWb}$, aika $\Delta t = 0{,}20\,\text{s}$
**Kysytty:** käämiin syntyvän induktiojännitteen suuruus $|e|$ voltteina
**Periaate:** Käämin läpi kulkeva magneettivuo muuttuu, kun magneetti työnnetään käämiin, joten käämiin syntyy induktiojännite induktiolain mukaan. Vuo kasvaa tasaisesti, joten jännite on vakio koko ajan. Kierrokset ovat sarjassa, joten jännite on $N$-kertainen yhden kierroksen jännitteeseen verrattuna.
**Kaava:** $|e| = N\dfrac{\Delta\Phi}{\Delta t}$
**Muunnokset:** $\Delta\Phi = 1{,}5\,\text{mWb} = 1{,}5 \cdot 10^{-3}\,\text{Wb}$
**Sijoitus:** $|e| = 400 \cdot \dfrac{1{,}5 \cdot 10^{-3}\,\text{Wb}}{0{,}20\,\text{s}} = 400 \cdot 7{,}5 \cdot 10^{-3}\,\text{V} = 3{,}0\,\text{V}$
**Vastaus:** $3{,}0\,\text{V}$, kaksi merkitsevää numeroa kuten vuon muutoksessa ja ajassa.
**Järkevyys:** Yksiköt sopivat: $\tfrac{\text{Wb}}{\text{s}} = \text{V}$. Yksi kierros antaisi vain $7{,}5\,\text{mV}$; satojen kierrosten käämillä jännite nousee voltteihin, mikä vastaa koulun käämeillä tehtyjä kokeita.

## fy7-5-L1-03
**Annettu:** tangon pituus $l = 0{,}25\,\text{m}$, vauhti $v = 2{,}0\,\text{m/s}$, magneettivuon tiheys $B = 0{,}40\,\text{T}$; tanko, nopeus ja kenttä keskenään kohtisuorassa
**Kysytty:** tangon päiden välinen induktiojännite $e$ voltteina
**Periaate:** Tangon mukana liikkuviin elektroneihin kohdistuu magneettinen voima $evB$ tangon suuntaan, joten elektroneja kertyy tangon toiseen päähän. Siirtyminen loppuu, kun syntyvä sähkökenttä $E = vB$ kumoaa magneettisen voiman, ja päiden välinen jännite on $El$.
**Kaava:** $e = vBl$
**Muunnokset:** Ei tarvita: kaikki suureet ovat SI-yksiköissä, ja $\tfrac{\text{m}}{\text{s}} \cdot \text{T} \cdot \text{m} = \text{V}$.
**Sijoitus:** $e = 2{,}0\,\text{m/s} \cdot 0{,}40\,\text{T} \cdot 0{,}25\,\text{m} = 0{,}20\,\text{V}$
**Vastaus:** $0{,}20\,\text{V}$, kaksi merkitsevää numeroa kuten lähtöarvoissa.
**Järkevyys:** Tanko pyyhkäisee joka sekunti pinta-alan $0{,}25\,\text{m} \cdot 2{,}0\,\text{m} = 0{,}50\,\text{m}^2$, joten vuo kasvaa nopeudella $0{,}40\,\text{T} \cdot 0{,}50\,\tfrac{\text{m}^2}{\text{s}} = 0{,}20\,\tfrac{\text{Wb}}{\text{s}}$: induktiolaki antaa saman jännitteen.

## fy7-5-L1-04
**Annettu:** kierrosten lukumäärä $N = 150$, keskimääräinen induktiojännite $|e| = 0{,}45\,\text{V}$, aika $\Delta t = 0{,}12\,\text{s}$
**Kysytty:** yhden kierroksen läpi kulkevan magneettivuon muutos $\Delta\Phi$ millivebereinä
**Periaate:** Jännite syntyy, koska vuo pienenee, kun magneetti vedetään pois. Induktiolain mukaan keskimääräinen jännite on vuon muutos jaettuna ajalla kerrottuna kierrosten lukumäärällä, joten kun jännite, aika ja kierrokset tunnetaan, vuon muutos voidaan ratkaista.
**Kaava:** $|e| = N\dfrac{\Delta\Phi}{\Delta t}$, josta $\Delta\Phi = \dfrac{|e|\,\Delta t}{N}$
**Muunnokset:** Lähtöarvot ovat SI-yksiköissä, ja $\text{V}\cdot\text{s} = \text{Wb}$. Vastaus muunnetaan millivebereiksi: $1\,\text{Wb} = 1000\,\text{mWb}$.
**Sijoitus:** $\Delta\Phi = \dfrac{0{,}45\,\text{V} \cdot 0{,}12\,\text{s}}{150} = \dfrac{0{,}054\,\text{V}\cdot\text{s}}{150} = 3{,}6 \cdot 10^{-4}\,\text{Wb} = 0{,}36\,\text{mWb}$
**Vastaus:** $0{,}36\,\text{mWb}$, kaksi merkitsevää numeroa kuten jännitteessä ja ajassa.
**Järkevyys:** Tarkistus: $150 \cdot 3{,}6 \cdot 10^{-4}\,\text{Wb} : 0{,}12\,\text{s} = 0{,}45\,\text{V}$. Jos käämin pinta-ala on noin $10\,\text{cm}^2$, vuo vastaa noin $0{,}4\,\text{T}$:n kenttää käämin sisällä, mikä sopii voimakkaalle kestomagneetille.

## fy7-5-L1-05
**Annettu:** induktiojännite $e = 12\,\text{mV}$, tangon kentässä oleva pituus $l = 0{,}30\,\text{m}$, magneettivuon tiheys $B = 0{,}080\,\text{T}$, nopeus kohtisuorassa tankoa ja kenttää vastaan
**Kysytty:** tangon vauhti $v$ metreinä sekunnissa
**Periaate:** Liikkuvan tangon elektroneihin kohdistuva magneettinen voima siirtää niitä tangon päähän, ja päiden välille syntyy jännite $e = vBl$. Jännite on verrannollinen vauhtiin, joten mitatusta jännitteestä voidaan ratkaista vauhti.
**Kaava:** $e = vBl$, josta $v = \dfrac{e}{Bl}$
**Muunnokset:** $e = 12\,\text{mV} = 12 \cdot 0{,}001\,\text{V} = 0{,}012\,\text{V}$
**Sijoitus:** $v = \dfrac{0{,}012\,\text{V}}{0{,}080\,\text{T} \cdot 0{,}30\,\text{m}} = \dfrac{0{,}012\,\text{V}}{0{,}024\,\text{T}\cdot\text{m}} = 0{,}50\,\text{m/s}$
**Vastaus:** $0{,}50\,\text{m/s}$, kaksi merkitsevää numeroa kuten lähtöarvoissa.
**Järkevyys:** Tarkistus: $0{,}50\,\text{m/s} \cdot 0{,}080\,\text{T} \cdot 0{,}30\,\text{m} = 0{,}012\,\text{V}$. Puoli metriä sekunnissa on hidasta kävelyä hitaampi vauhti, joka sopii pöydällä tehtävään kiskokokeeseen.

## fy7-5-L2-01
**Annettu:** magneettivuon tiheys $B = 0{,}80\,\text{T}$ kohtisuorassa silmukan tasoa vastaan, pinta-ala aluksi $A_1 = 200\,\text{cm}^2$ ja lopuksi $A_2 = 50\,\text{cm}^2$, aika $\Delta t = 0{,}25\,\text{s}$, yksi kierros $N = 1$
**Kysytty:** silmukkaan syntyvän induktiojännitteen suuruus $|e|$ millivoltteina
**Periaate:** Kenttä pysyy samana, mutta silmukan pinta-ala pienenee, joten silmukan läpi kulkeva vuo $\Phi = BA$ pienenee. Vuon muutos synnyttää induktiolain mukaan jännitteen. Pinta-ala pienenee tasaisesti, joten jännite on vakio.
**Kaava:** $\Delta\Phi = B(A_1 - A_2)$ ja $|e| = N\dfrac{\Delta\Phi}{\Delta t}$, joten $|e| = \dfrac{B(A_1 - A_2)}{\Delta t}$, kun $N = 1$
**Muunnokset:** $A_1 = 200\,\text{cm}^2 = 200 \cdot (0{,}01\,\text{m})^2 = 0{,}0200\,\text{m}^2$ ja $A_2 = 50\,\text{cm}^2 = 50 \cdot (0{,}01\,\text{m})^2 = 0{,}0050\,\text{m}^2$
**Sijoitus:** $A_1 - A_2 = 0{,}0200\,\text{m}^2 - 0{,}0050\,\text{m}^2 = 0{,}0150\,\text{m}^2$ ja $|e| = \dfrac{0{,}80\,\text{T} \cdot 0{,}0150\,\text{m}^2}{0{,}25\,\text{s}} = \dfrac{0{,}012\,\text{Wb}}{0{,}25\,\text{s}} = 0{,}048\,\text{V} = 48\,\text{mV}$
**Vastaus:** $48\,\text{mV}$, kaksi merkitsevää numeroa kuten kentässä $0{,}80\,\text{T}$ ja ajassa $0{,}25\,\text{s}$.
**Järkevyys:** Yksi kierros antaa vain kymmenien millivolttien jännitteen, vaikka kenttä on voimakas; tämä sopii siihen, että käytännön laitteissa tarvitaan paljon kierroksia. Jos silmukka puristettaisiin kaksi kertaa nopeammin, jännite olisi kaksinkertainen.

## fy7-5-L2-02
**Annettu:** kierrosten lukumäärä $N = 50$; kuvaajassa yhden kierroksen läpi kulkeva magneettivuo $\Phi$ ajan $t$ funktiona
**Kysytty:** induktiojännitteen suurin itseisarvo $|e|$ voltteina
**Periaate:** Induktiolain mukaan jännite on verrannollinen vuon muutosnopeuteen $\Delta\Phi : \Delta t$, joka on vuon kuvaajan kulmakerroin. Jännite on siis suurin siellä, missä kuvaaja on jyrkin, eikä siellä, missä vuo on suurin.
**Kuvaajan lukeminen:** Kuvaaja koostuu suorista osista. Aikavälillä $0$–$0{,}20\,\text{s}$ vuo kasvaa nollasta arvoon $4{,}0\,\text{mWb}$, joten kulmakertoimen itseisarvo on $4{,}0\,\text{mWb} : 0{,}20\,\text{s} = 20\,\tfrac{\text{mWb}}{\text{s}}$. Aikavälillä $0{,}20$–$0{,}50\,\text{s}$ kuvaaja on vaakasuora, joten jännite on nolla. Aikavälillä $0{,}50$–$0{,}60\,\text{s}$ vuo pienenee arvosta $4{,}0\,\text{mWb}$ nollaan, joten kulmakertoimen itseisarvo on $4{,}0\,\text{mWb} : 0{,}10\,\text{s} = 40\,\tfrac{\text{mWb}}{\text{s}}$. Jyrkin osa on siis $0{,}50$–$0{,}60\,\text{s}$, jossa $\Delta\Phi = 4{,}0\,\text{mWb}$ ja $\Delta t = 0{,}10\,\text{s}$.
**Kaava:** $|e| = N\dfrac{\Delta\Phi}{\Delta t}$
**Muunnokset:** $\Delta\Phi = 4{,}0\,\text{mWb} = 4{,}0 \cdot 10^{-3}\,\text{Wb}$
**Sijoitus:** $|e| = 50 \cdot \dfrac{4{,}0 \cdot 10^{-3}\,\text{Wb}}{0{,}10\,\text{s}} = 50 \cdot 0{,}040\,\text{V} = 2{,}0\,\text{V}$
**Vastaus:** $2{,}0\,\text{V}$, kaksi merkitsevää numeroa kuten kuvaajasta luettu vuo $4{,}0\,\text{mWb}$.
**Järkevyys:** Nousuvaiheessa jännite on $50 \cdot 4{,}0 \cdot 10^{-3}\,\text{Wb} : 0{,}20\,\text{s} = 1{,}0\,\text{V}$, eli puolet suurimmasta, koska sama vuon muutos kestää kaksi kertaa kauemmin. Laskuvaiheessa jännitteen merkki on vastakkainen kuin nousuvaiheessa, koska vuo pienenee.

## fy7-5-L2-03
**Annettu:** kiskojen väli eli tangon kentässä oleva pituus $l = 0{,}40\,\text{m}$, vauhti $v = 3{,}0\,\text{m/s}$, magneettivuon tiheys $B = 0{,}50\,\text{T}$, vastus $R = 2{,}0\,\Omega$; kiskojen ja tangon resistanssi hyvin pieni
**Kysytty:** vastuksen läpi kulkeva virta $I$ ampeereina
**Periaate:** Liikkuvan tangon päiden välille syntyy induktiojännite $e = vBl$, koska tangon elektroneihin kohdistuu magneettinen voima. Tanko, kiskot ja vastus muodostavat suljetun virtapiirin, jossa tanko toimii jännitelähteenä. Muun piirin resistanssi on pieni, joten koko jännite on vastuksen yli, ja virta saadaan Ohmin laista.
**Kaava:** $e = vBl$ ja $I = \dfrac{e}{R}$, joten $I = \dfrac{vBl}{R}$
**Muunnokset:** Ei tarvita: kaikki suureet ovat SI-yksiköissä.
**Sijoitus:** $e = 3{,}0\,\text{m/s} \cdot 0{,}50\,\text{T} \cdot 0{,}40\,\text{m} = 0{,}60\,\text{V}$ ja $I = \dfrac{0{,}60\,\text{V}}{2{,}0\,\Omega} = 0{,}30\,\text{A}$
**Vastaus:** $0{,}30\,\text{A}$, kaksi merkitsevää numeroa kuten lähtöarvoissa.
**Järkevyys:** Vuo kasvaa nopeudella $0{,}50\,\text{T} \cdot 0{,}40\,\text{m} \cdot 3{,}0\,\tfrac{\text{m}}{\text{s}} = 0{,}60\,\tfrac{\text{Wb}}{\text{s}}$, mikä antaa saman jännitteen. Kun tankoon kulkee virta, kenttä kohdistaa siihen voiman $IlB = 0{,}060\,\text{N}$; sen suunta selviää luvussa *Lenzin laki ja pyörrevirrat*.

## fy7-5-L2-04
**Annettu:** käämin sivu $l = 5{,}0\,\text{cm}$, kierrosten lukumäärä $N = 20$, vauhti $v = 0{,}25\,\text{m/s}$, magneettivuon tiheys $B = 0{,}30\,\text{T}$ kohtisuorassa käämin tasoa vastaan
**Kysytty:** käämiin sisääntulon aikana syntyvä induktiojännite $|e|$ millivoltteina
**Periaate:** Kun käämi tulee kenttään, kentässä oleva osa käämin pinta-alasta kasvaa tasaisesti, joten jokaisen kierroksen läpi kulkeva vuo kasvaa tasaisesti ja jännite on vakio. Ajassa $\Delta t$ käämi siirtyy matkan $v\Delta t$, joten vuo kasvaa määrällä $\Delta\Phi = Bl \cdot v\Delta t$.
**Kaava:** $|e| = N\dfrac{\Delta\Phi}{\Delta t} = N\dfrac{Bl \cdot v\Delta t}{\Delta t}$, joten $|e| = NBlv$
**Muunnokset:** $l = 5{,}0\,\text{cm} = 5{,}0 \cdot 0{,}01\,\text{m} = 0{,}050\,\text{m}$
**Sijoitus:** $|e| = 20 \cdot 0{,}30\,\text{T} \cdot 0{,}050\,\text{m} \cdot 0{,}25\,\text{m/s} = 0{,}075\,\text{V} = 75\,\text{mV}$
**Vastaus:** $75\,\text{mV}$, kaksi merkitsevää numeroa kuten lähtöarvoissa.
**Järkevyys:** Tarkistus koko sisääntulolla: vuo kasvaa nollasta arvoon $BA = 0{,}30\,\text{T} \cdot (0{,}050\,\text{m})^2 = 7{,}5 \cdot 10^{-4}\,\text{Wb}$ ajassa $0{,}050\,\text{m} : 0{,}25\,\text{m/s} = 0{,}20\,\text{s}$, joten $|e| = 20 \cdot 7{,}5 \cdot 10^{-4}\,\text{Wb} : 0{,}20\,\text{s} = 0{,}075\,\text{V}$.

## fy7-5-L3-01
**Annettu:** junan vauhti $v = 200\,\text{km/h}$, akselin pituus kiskosta kiskoon $l = 1524\,\text{mm}$, Maan magneettikentän pystykomponentti $B_\text{v} = 50\,\mu\text{T}$
**Kysytty:** akselin päiden välinen induktiojännite $e$ millivoltteina
**Periaate:** Akseli on metallitanko, joka liikkuu vaakasuoraan kohtisuoraan itseään vastaan. Elektroneihin kohdistuva magneettinen voima on kohtisuorassa nopeutta ja kenttää vastaan; akselin suuntainen komponentti syntyy vain kentän pystykomponentista, sillä vaakakomponentti joko on nopeuden suuntainen tai antaa pystysuoran voiman. Siksi jännitteen antaa $e = vB_\text{v}l$.
**Kaava:** $e = vB_\text{v}l$
**Muunnokset:** $v = 200\,\text{km/h} = 200 \cdot \dfrac{1000\,\text{m}}{3600\,\text{s}} = 55{,}56\,\text{m/s}$, $l = 1524\,\text{mm} = 1524 \cdot 0{,}001\,\text{m} = 1{,}524\,\text{m}$ ja $B_\text{v} = 50\,\mu\text{T} = 50 \cdot 10^{-6}\,\text{T}$
**Sijoitus:** $e = 55{,}56\,\text{m/s} \cdot 50 \cdot 10^{-6}\,\text{T} \cdot 1{,}524\,\text{m} = 4{,}233 \cdot 10^{-3}\,\text{V} = 4{,}2\,\text{mV}$
**Vastaus:** $4{,}2\,\text{mV}$, kaksi merkitsevää numeroa kuten kentässä $50\,\mu\text{T}$.
**Järkevyys:** Maan kenttä on noin kymmenentuhannesosa laboratoriomagneetin kentästä, joten suuresta vauhdista huolimatta jännite jää millivolttien luokkaan. Pyöräilijän vauhdilla $20\,\text{km/h}$ jännite olisi kymmenesosa tästä, noin $0{,}4\,\text{mV}$.

## fy7-5-L3-02
**Annettu:** kierrosten lukumäärä $N = 100$, pinta-ala $A = 0{,}020\,\text{m}^2$, kelan taso aluksi kohtisuorassa kenttää vastaan, puolen kierroksen kääntö ajassa $\Delta t = 0{,}10\,\text{s}$, keskimääräinen jännite $|e| = 2{,}0\,\text{mV}$
**Kysytty:** Maan magneettikentän magneettivuon tiheys $B$ mikrotesloina
**Periaate:** Aluksi yhden kierroksen läpi kulkee vuo $\Phi_1 = BA$. Puolen kierroksen jälkeen sama kenttä kulkee kierroksen läpi vastakkaisesta suunnasta, joten vuo on $\Phi_2 = -BA$. Vuon muutoksen suuruus on siis $\Delta\Phi = 2BA$, ja induktiolain mukaan keskimääräinen jännite on $N \cdot 2BA : \Delta t$.
**Kaava:** $|e| = N\dfrac{2BA}{\Delta t}$, josta $B = \dfrac{|e|\,\Delta t}{2NA}$
**Muunnokset:** $|e| = 2{,}0\,\text{mV} = 2{,}0 \cdot 10^{-3}\,\text{V}$; vastaus muunnetaan mikrotesloiksi: $1\,\text{T} = 10^{6}\,\mu\text{T}$
**Sijoitus:** $B = \dfrac{2{,}0 \cdot 10^{-3}\,\text{V} \cdot 0{,}10\,\text{s}}{2 \cdot 100 \cdot 0{,}020\,\text{m}^2} = \dfrac{2{,}0 \cdot 10^{-4}\,\text{V}\cdot\text{s}}{4{,}0\,\text{m}^2} = 5{,}0 \cdot 10^{-5}\,\text{T} = 50\,\mu\text{T}$
**Vastaus:** $50\,\mu\text{T}$, kaksi merkitsevää numeroa kuten jännitteessä $2{,}0\,\text{mV}$.
**Järkevyys:** Maan magneettikenttä on Suomessa noin $50\,\mu\text{T}$, joten tulos on uskottava. Jos vuon muutokseksi olisi virheellisesti otettu $BA$, tulos olisi kaksinkertainen, $100\,\mu\text{T}$, mikä on liian suuri.

## fy7-5-L3-03
**Annettu:** kierrosten lukumäärä $N = 300$, kolmion muotoinen jännitepulssi, huippuarvo $e_0 = 0{,}90\,\text{V}$, kesto $\Delta t = 40\,\text{ms}$; aluksi magneetti on kaukana, joten vuo on nolla
**Kysytty:** yhden kierroksen läpi kulkeva magneettivuo $\Phi$ keskimäärin millivebereinä, kun magneetti on käämin keskellä
**Periaate:** Induktiolaista seuraa, että lyhyen aikavälin jännitteen ja keston tulo on $N$ kertaa vuon muutos. Kun pulssin aikavälit lasketaan yhteen, jännitteen kuvaajan $(t, e)$ ja aika-akselin väliin jäävä pinta-ala on $N\Delta\Phi$. Pulssin lopussa jännite on nolla, koska vuo on suurimmillaan eikä enää kasva; silloin magneetti on käämin keskellä. Vuo kasvaa nollasta tähän arvoon, joten $\Delta\Phi = \Phi$.
**Kaava:** kolmion pinta-ala on $N\Phi = \tfrac{1}{2} e_0 \Delta t$, josta $\Phi = \dfrac{e_0 \Delta t}{2 \cdot N}$
**Muunnokset:** $\Delta t = 40\,\text{ms} = 40 \cdot 0{,}001\,\text{s} = 0{,}040\,\text{s}$; vastaus muunnetaan millivebereiksi: $1\,\text{Wb} = 1000\,\text{mWb}$
**Sijoitus:** $\Phi = \dfrac{0{,}90\,\text{V} \cdot 0{,}040\,\text{s}}{2 \cdot 300} = \dfrac{0{,}036\,\text{V}\cdot\text{s}}{600} = 6{,}0 \cdot 10^{-5}\,\text{Wb} = 0{,}060\,\text{mWb}$
**Vastaus:** $0{,}060\,\text{mWb}$, kaksi merkitsevää numeroa kuten huippuarvossa $0{,}90\,\text{V}$ ja kestossa $40\,\text{ms}$.
**Järkevyys:** Jos käämin poikkipinta-ala on noin $2\,\text{cm}^2 = 2 \cdot 10^{-4}\,\text{m}^2$, keskimääräinen kenttä kierroksen läpi on $6{,}0 \cdot 10^{-5}\,\text{Wb} : 2 \cdot 10^{-4}\,\text{m}^2 = 0{,}3\,\text{T}$, mikä sopii pienelle voimakkaalle magneetille. Kun magneetti lähtee käämistä, syntyy vastakkaismerkkinen pulssi, jonka pinta-ala on yhtä suuri.
