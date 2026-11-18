## fy9-liike-s1

### a)
**Annettu:** kaistan pituus $\Delta x = 270\,\text{m}$, nopeus kaistan alussa $v_0 = 54\,\text{km/h}$ ja lopussa $v = 108\,\text{km/h}$; kiihtyvyys on tasainen
**Kysytty:** kiihdytyksen kesto $t$ sekunteina
**Periaate:** Kiihtyvyys on vakio. Siksi $(t,v)$-kuvaaja on suora, ja sen alle jäävä alue on puolisuunnikas. Siirtymä on tämän alueen pinta-ala. Siksi keskinopeus on alkunopeuden ja loppunopeuden keskiarvo (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*). Aikaa laskiessa kiihtyvyyttä ei tarvita.
**Kaava:** $\Delta x = \dfrac{v_0 + v}{2}\,t$, joten $t = \dfrac{2\,\Delta x}{v_0 + v}$
**Muunnokset:** $$
\begin{aligned}
&54\,\text{km/h} \\
&= \dfrac{54 \cdot 1000\,\text{m}}{3600\,\text{s}} \\
&= 15\,\text{m/s}
\end{aligned}
$$ ja $108\,\text{km/h} = \dfrac{108 \cdot 1000\,\text{m}}{3600\,\text{s}} = 30\,\text{m/s}$
**Sijoitus:** $t = \dfrac{2 \cdot 270\,\text{m}}{15\,\text{m/s} + 30\,\text{m/s}} = \dfrac{540\,\text{m}}{45\,\text{m/s}} = 12{,}0\,\text{s}$
**Vastaus:** $t \approx 12\,\text{s}$. Tuloksessa on kaksi merkitsevää numeroa, kuten nopeuksissa $54\,\text{km/h}$ ja $108\,\text{km/h}$.
**Järkevyys:** Keskinopeus on $22{,}5\,\text{m/s}$, ja $22{,}5\,\text{m/s} \cdot 12{,}0\,\text{s} = 270\,\text{m}$. Se on kaistan pituus. Henkilöauto kiihdyttää moottoritien nopeuteen tavallisesti noin kymmenessä sekunnissa.

### b)
**Annettu:** $v_0 = 15\,\text{m/s}$, $v = 30\,\text{m/s}$ ja a-kohdasta $t = 12{,}0\,\text{s}$
**Kysytty:** kiihtyvyys $a$ yksikössä $\text{m/s}^2$
**Periaate:** Kiihtyvyys on nopeuden muutos jaettuna ajalla, joka muutokseen kului. Tasaisesti kiihtyvässä liikkeessä kiihtyvyys on sama koko ajan. Se on $(t,v)$-kuvaajan kulmakerroin (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*).
**Kaava:** $a = \dfrac{\Delta v}{\Delta t} = \dfrac{v - v_0}{t}$
**Muunnokset:** Nopeudet on muunnettu a-kohdassa yksikköön $\text{m/s}$. Aika on sekunteina.
**Sijoitus:** $a = \dfrac{30\,\text{m/s} - 15\,\text{m/s}}{12{,}0\,\text{s}} = \dfrac{15\,\text{m/s}}{12{,}0\,\text{s}} = 1{,}25\,\text{m/s}^2$
**Vastaus:** $a \approx 1{,}3\,\text{m/s}^2$. Tuloksessa on kaksi merkitsevää numeroa, kuten nopeuksissa (myös $1{,}25\,\text{m/s}^2$ hyväksytään).
**Järkevyys:** Nopeus kasvaa joka sekunti $1{,}25\,\text{m/s} = 4{,}5\,\text{km/h}$. Kahdessatoista sekunnissa se kasvaa siis $54\,\text{km/h}$, kuten aineistossa. Tarkistus paikan yhtälöllä: $$
\begin{aligned}
&15\,\text{m/s} \cdot 12{,}0\,\text{s} \\
&+ \tfrac{1}{2} \cdot 1{,}25\,\text{m/s}^2 \cdot (12{,}0\,\text{s})^2 \\
&= 180\,\text{m} + 90\,\text{m} \\
&= 270\,\text{m}
\end{aligned}
$$.

### c)
**Annettu:** origo on kiihdytyskaistan alussa, ja positiivinen suunta on ajosuunta; auto: $x_{0\text{A}} = 0$, $v_0 = 15\,\text{m/s}$, $a = 1{,}25\,\text{m/s}^2$; rekka: $x_{0\text{R}} = -40\,\text{m}$, $v_\text{R} = 81\,\text{km/h}$ (vakio)
**Kysytty:** ehtiikö rekka auton rinnalle eli viereen, ja pienin välimatka $d_\text{min}$
**Periaate:** Paikat kirjoitetaan samassa koordinaatistossa (luku *Kahden kappaleen liikkeiden vertailu*). Rekka on aluksi nopeampi, ja se lähestyy autoa. Välimatka pienenee niin kauan kuin rekka on nopeampi. Kun auto on nopeampi, välimatka alkaa kasvaa. Siksi välimatka on pienimmillään silloin, kun nopeudet ovat yhtä suuret. Jos välimatka on silloin positiivinen, rekka ei ehdi auton rinnalle.
**Kaava:** $x_\text{A} = v_0\,t + \tfrac{1}{2}\,a\,t^2$ ja $x_\text{R} = x_{0\text{R}} + v_\text{R}\,t$. Nopeudet ovat yhtä suuret, kun $v_0 + a\,t_1 = v_\text{R}$. Siis $t_1 = \dfrac{v_\text{R} - v_0}{a}$ ja $d_\text{min} = x_\text{A}(t_1) - x_\text{R}(t_1)$
**Muunnokset:** $81\,\text{km/h} = \dfrac{81 \cdot 1000\,\text{m}}{3600\,\text{s}} = 22{,}5\,\text{m/s}$
**Sijoitus:** $t_1 = \dfrac{22{,}5\,\text{m/s} - 15\,\text{m/s}}{1{,}25\,\text{m/s}^2} = 6{,}0\,\text{s}$; $$
\begin{aligned}
x_\text{A} &= 15\,\text{m/s} \cdot 6{,}0\,\text{s} \\
&+ \tfrac{1}{2} \cdot 1{,}25\,\text{m/s}^2 \cdot (6{,}0\,\text{s})^2 \\
&= 90\,\text{m} + 22{,}5\,\text{m} \\
&= 112{,}5\,\text{m}
\end{aligned}
$$; $x_\text{R} = -40\,\text{m} + 22{,}5\,\text{m/s} \cdot 6{,}0\,\text{s} = 95\,\text{m}$; $d_\text{min} = 112{,}5\,\text{m} - 95\,\text{m} = 17{,}5\,\text{m}$
**Vastaus:** Rekka ei ehdi auton rinnalle. Välimatka on pienimmillään noin $18\,\text{m}$ hetkellä $6{,}0\,\text{s}$. Tuloksessa on kaksi merkitsevää numeroa, kuten etäisyydessä $40\,\text{m}$ ja nopeuksissa.
**Järkevyys:** Kaistan lopussa ($12{,}0\,\text{s}$) rekka on kohdassa $$
\begin{aligned}
&-40\,\text{m} + 22{,}5\,\text{m/s} \cdot 12{,}0\,\text{s} \\
&= 230\,\text{m}
\end{aligned}
$$ ja auto kohdassa $270\,\text{m}$. Ero on siis taas $40\,\text{m}$, kuten pitääkin. Nopeuskuvaajien väliin jäävät alat ennen hetkeä $6{,}0\,\text{s}$ ja sen jälkeen ovat nimittäin yhtä suuret. Kohtaamisyhtälöllä $$
\tfrac{1}{2}\,a\,t^2 + (v_0 - v_\text{R})\,t - x_{0\text{R}} = 0
$$ ei ole reaalisia ratkaisuja, koska diskriminantti $$
(-7{,}5)^2 - 4 \cdot 0{,}625 \cdot 40 < 0
$$.

### d)
**Kysytty:** miksi rekka saavuttaa auton, joka kiihdyttää tasaisesti vain nopeuteen $72\,\text{km/h}$, ja miksi kannattaa kiihdyttää muun liikenteen nopeuteen
**Periaate:** Siirtymä on $(t,v)$-kuvaajan pinta-ala. Välimatka muuttuu sen alan verran, joka jää kahden kuvaajan väliin (luku *Kahden kappaleen liikkeiden vertailu*).
**Mallivastaus:** Tämä auto on koko kaistan ajan hitaampi kuin rekka. Sen suurin nopeus $72\,\text{km/h} = 20\,\text{m/s}$ on pienempi kuin rekan nopeus $22{,}5\,\text{m/s}$. $(t,v)$-kuvaajassa rekan vaakasuora viiva on koko ajan auton nousevan viivan yläpuolella. Siksi rekan siirtymä kasvaa joka hetki enemmän kuin auton siirtymä, ja $40\,\text{m}$:n ero pienenee koko ajan. Kun ero on kurottu umpeen eli kadonnut, rekka on auton rinnalla ja menee ohi. Laskelma vahvistaa tämän (auto kiihdyttää tasaisesti koko kaistan matkan). Kiihdytys kestää $$
\begin{aligned}
&2 \cdot 270\,\text{m} : (15\,\text{m/s} + 20\,\text{m/s}) \\
&\approx 15{,}4\,\text{s}
\end{aligned}
$$, ja auton keskinopeus on $17{,}5\,\text{m/s}$. Rekka kulkee siis keskimäärin $5\,\text{m/s}$ nopeammin. Se kuroo umpeen $5\,\text{m/s} \cdot 15{,}4\,\text{s} \approx 77\,\text{m}$, mikä on enemmän kuin $40\,\text{m}$:n ero. Sinä aikana rekka ehtii kohtaan $$
\begin{aligned}
&-40\,\text{m} + 22{,}5\,\text{m/s} \cdot 15{,}4\,\text{s} \\
&\approx 307\,\text{m}
\end{aligned}
$$. Se on auton ohi jo ennen kaistan loppua ($270\,\text{m}$). Auton on silloin hidastettava ja siirryttävä rekan taakse. Kun auto kiihdyttää muun liikenteen nopeuteen, se on loppuvaiheessa nopeampi kuin rekka. Silloin välimatka kasvaa taas, ja auto voi siirtyä turvallisesti rekan eteen.

### Yleisiä virheitä
- Nopeuksia ei muunneta yksikköön $\text{m/s}$, ja kilometrit tunnissa kerrotaan sekunneilla.
- a-kohdassa matka jaetaan loppunopeudella ($270\,\text{m} : 30\,\text{m/s} = 9{,}0\,\text{s}$), vaikka nopeus kasvaa vähitellen.
- c-kohdassa yritetään ratkaista kohtaamisehto. Negatiivinen diskriminantti tulkitaan laskuvirheeksi, vaikka se kertoo, että kohtaamista ei ole.
- c-kohdassa rekan paikasta unohdetaan $-40\,\text{m}$, tai pienimmäksi välimatkaksi luetaan alkuetäisyys $40\,\text{m}$.

### Hyväksytään myös
- a-kohdassa ratkaistaan ensin $a = \dfrac{v^2 - v_0^2}{2\,\Delta x}$ ja sitten $t = \dfrac{v - v_0}{a}$. Myös paikan yhtälöä ja nopeuden yhtälöä voi käyttää yhdessä.
- c-kohdassa välimatka $$
\begin{aligned}
d(t) &= x_\text{A} - x_\text{R} \\
&= 40\,\text{m} - 7{,}5\,\text{m/s} \cdot t \\
&+ 0{,}625\,\text{m/s}^2 \cdot t^2
\end{aligned}
$$ ja sen pienin arvo paraabelin huipusta.

## fy9-liike-s2

### a)
**Annettu:** heittokorkeus $y_{0\text{A}} = 1{,}5\,\text{m}$, alkunopeus $v_0 = 12{,}0\,\text{m/s}$ ylöspäin, $g = 9{,}81\,\text{m/s}^2$; ylös on positiivinen, ilmanvastusta ei oteta huomioon
**Kysytty:** lakipisteen eli korkeimman kohdan korkeus $y_\text{l}$ lattiasta
**Periaate:** Pallon kiihtyvyys on koko lennon ajan $g$ alaspäin. Siksi liike on tasaisesti kiihtyvää. Lakipisteessä pallon nopeus on hetken nolla, mutta kiihtyvyys ei ole nolla (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*).
**Kaava:** $v = v_0 - g\,t_\text{l} = 0$, joten $t_\text{l} = \dfrac{v_0}{g}$, ja $y_\text{l} = y_{0\text{A}} + v_0\,t_\text{l} - \tfrac{1}{2}\,g\,t_\text{l}^2 = y_{0\text{A}} + \dfrac{v_0^2}{2g}$
**Muunnokset:** Suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $t_\text{l} = \dfrac{12{,}0\,\text{m/s}}{9{,}81\,\text{m/s}^2} = 1{,}223\,\text{s}$; $$
\begin{aligned}
y_\text{l} &= 1{,}5\,\text{m} \\
&+ 12{,}0\,\text{m/s} \cdot 1{,}223\,\text{s} \\
&- \tfrac{1}{2} \cdot 9{,}81\,\text{m/s}^2 \cdot (1{,}223\,\text{s})^2 \\
&= 1{,}5\,\text{m} + 14{,}68\,\text{m} \\
&- 7{,}34\,\text{m} \\
&= 8{,}84\,\text{m}
\end{aligned}
$$
**Vastaus:** $y_\text{l} \approx 8{,}8\,\text{m}$. Tulos ilmoitetaan kymmenesosien tarkkuudella, koska heittokorkeus $1{,}5\,\text{m}$ tunnetaan kymmenesosien tarkkuudella.
**Järkevyys:** Pallo nousee $7{,}34\,\text{m}$. Nousun aikana pallon keskinopeus on $6{,}0\,\text{m/s}$, ja $6{,}0\,\text{m/s} \cdot 1{,}223\,\text{s} \approx 7{,}3\,\text{m}$. Pallo ei nouse kolmannen kerroksen kaiteelle ($9{,}0\,\text{m}$) asti. Tämä sopii voimakkaaseen mutta tavalliseen heittoon.

### b)
**Annettu:** pallo A: $y_{0\text{A}} = 1{,}5\,\text{m}$, $v_0 = 12{,}0\,\text{m/s}$; pallo B: $y_{0\text{B}} = 9{,}0\,\text{m}$, lähtee levosta; molempien kiihtyvyys on $g = 9{,}81\,\text{m/s}^2$ alaspäin
**Kysytty:** ohitushetki $t$ ja ohituskorkeus $y$
**Periaate:** Pallot ohittavat toisensa, kun ne ovat samalla korkeudella samalla hetkellä: $y_\text{A}(t) = y_\text{B}(t)$ (luku *Kahden kappaleen liikkeiden vertailu*). Kummankin pallon liike on tasaisesti kiihtyvää, ja kiihtyvyys on sama. Siksi termit $-\tfrac{1}{2}\,g\,t^2$ kumoutuvat eli häviävät yhtälöstä.
**Kaava:** $y_{0\text{A}} + v_0\,t - \tfrac{1}{2}\,g\,t^2 = y_{0\text{B}} - \tfrac{1}{2}\,g\,t^2$, joten $t = \dfrac{y_{0\text{B}} - y_{0\text{A}}}{v_0}$ ja $y = y_{0\text{B}} - \tfrac{1}{2}\,g\,t^2$
**Muunnokset:** Suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $t = \dfrac{9{,}0\,\text{m} - 1{,}5\,\text{m}}{12{,}0\,\text{m/s}} = \dfrac{7{,}5\,\text{m}}{12{,}0\,\text{m/s}} = 0{,}625\,\text{s}$; $$
\begin{aligned}
y &= 9{,}0\,\text{m} \\
&- \tfrac{1}{2} \cdot 9{,}81\,\text{m/s}^2 \cdot (0{,}625\,\text{s})^2 \\
&= 9{,}0\,\text{m} - 1{,}916\,\text{m} \\
&= 7{,}08\,\text{m}
\end{aligned}
$$
**Vastaus:** Pallot ohittavat toisensa hetkellä $t \approx 0{,}63\,\text{s}$ korkeudella $y \approx 7{,}1\,\text{m}$. Tuloksessa on kaksi merkitsevää numeroa, kuten korkeuserossa $7{,}5\,\text{m}$.
**Järkevyys:** Pallon A paikkafunktio antaa saman korkeuden: $$
\begin{aligned}
&1{,}5\,\text{m} + 12{,}0\,\text{m/s} \cdot 0{,}625\,\text{s} \\
&- 1{,}916\,\text{m} \\
&= 7{,}08\,\text{m}
\end{aligned}
$$. Ohitus tapahtuu ennen A:n lakipistettä, joka on hetkellä $1{,}22\,\text{s}$. Se tapahtuu myös ennen kuin B osuu lattiaan hetkellä $$
\begin{aligned}
&\sqrt{2 \cdot 9{,}0\,\text{m} : 9{,}81\,\text{m/s}^2} \\
&\approx 1{,}35\,\text{s}
\end{aligned}
$$.

### c)
**Kysytty:** miksi ohitushetki ei riipu putoamiskiihtyvyydestä, ja ohittaisivatko pallot toisensa Kuussa samalla hetkellä
**Periaate:** Kiihtyvyys kertoo, kuinka paljon nopeus muuttuu sekunnissa. Kun kahdella kappaleella on sama kiihtyvyys, niiden nopeudet muuttuvat yhtä paljon (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*).
**Mallivastaus:** Molemmat pallot lähtevät käsistä samalla hetkellä. Sen jälkeen kummankin kiihtyvyys on $g$ alaspäin. Niiden nopeudet pienenevät joka sekunti yhtä paljon. Siksi nopeuksien erotus pysyy koko ajan alkuarvossaan $12{,}0\,\text{m/s}$. Pallojen välimatka $7{,}5\,\text{m}$ pienenee siis tasaisesti nopeudella $12{,}0\,\text{m/s}$, aivan kuin kumpikaan pallo ei kiihtyisi. Ohitus tapahtuu hetkellä $7{,}5\,\text{m} : 12{,}0\,\text{m/s} \approx 0{,}63\,\text{s}$, oli putoamiskiihtyvyys mikä tahansa. Kuussa ohitushetki olisi siis sama. Ohituskorkeus sen sijaan riippuu putoamiskiihtyvyydestä. Kuussa ($g = 1{,}62\,\text{m/s}^2$) kumpikin pallo putoaa tässä ajassa vain noin $0{,}32\,\text{m}$. Siksi ohitus tapahtuisi noin $8{,}7\,\text{m}$:n korkeudella.

### d)
**Annettu:** $v_0 = 12{,}0\,\text{m/s}$ (A), B lähtee levosta, $g = 9{,}81\,\text{m/s}^2$ alaspäin, b-kohdasta $t = 0{,}625\,\text{s}$; ylös on positiivinen
**Kysytty:** nopeudet $v_\text{A}$ ja $v_\text{B}$ etumerkin kanssa ohitushetkellä
**Periaate:** Tasaisesti kiihtyvässä liikkeessä nopeus muuttuu joka sekunti kiihtyvyyden verran. Ylös on positiivinen, joten kiihtyvyys on $-g$. Nopeuden etumerkki kertoo suunnan (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*).
**Kaava:** $v_\text{A} = v_0 - g\,t$ ja $v_\text{B} = -g\,t$
**Muunnokset:** Suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $$
\begin{aligned}
v_\text{A} &= 12{,}0\,\text{m/s} \\
&- 9{,}81\,\text{m/s}^2 \cdot 0{,}625\,\text{s} \\
&= 12{,}0\,\text{m/s} - 6{,}131\,\text{m/s} \\
&= 5{,}869\,\text{m/s}
\end{aligned}
$$ ja $v_\text{B} = -9{,}81\,\text{m/s}^2 \cdot 0{,}625\,\text{s} = -6{,}131\,\text{m/s}$
**Vastaus:** $v_\text{A} \approx 5{,}9\,\text{m/s}$ ylöspäin ja $v_\text{B} \approx -6{,}1\,\text{m/s}$ eli $6{,}1\,\text{m/s}$ alaspäin. Tuloksissa on kaksi merkitsevää numeroa, kuten ohitushetkessä.
**Järkevyys:** Nopeuksien erotus on $$
\begin{aligned}
&5{,}869\,\text{m/s} - (-6{,}131\,\text{m/s}) \\
&= 12{,}0\,\text{m/s}
\end{aligned}
$$, kuten c-kohdan päättely vaatii. Pallo A nousee vielä, koska se on lakipisteessä vasta hetkellä $1{,}22\,\text{s}$.

### Yleisiä virheitä
- Lakipisteessä kiihtyvyyden oletetaan olevan nolla, tai korkeus lasketaan ilman heittokorkeutta $1{,}5\,\text{m}$.
- Putoavan pallon paikaksi kirjoitetaan $y_\text{B} = \tfrac{1}{2}\,g\,t^2$. Silloin unohdetaan, että ylös on positiivinen ja pallo lähtee korkeudelta $9{,}0\,\text{m}$.
- b-kohdassa ratkaistaan hetki, jolloin nopeudet ovat yhtä suuret. Pitäisi ratkaista hetki, jolloin korkeudet ovat yhtä suuret.
- d-kohdassa nopeuksien etumerkit jätetään pois. Silloin vastauksesta ei näe, että pallot liikkuvat vastakkaisiin suuntiin.

### Hyväksytään myös
- Koordinaatisto, jossa alas on positiivinen, kun etumerkit ovat sen mukaiset.
- b-kohdan päättely suoraan pallojen suhteellisesta liikkeestä, kuten c-kohdan mallivastauksessa.

## fy9-liike-s3

### a)
**Kysytty:** junan nopeus $v$ ajan $t$ funktiona kuvaajana ja kuvaajaan sovitettu malli
**Kuvaaja:** Vaaka-akselilla on aika $t\ (\text{s})$ ja pystyakselilla nopeus $v\ (\text{km/h})$. Aika-akseli jatkuu noin $55\,\text{s}$:iin. Silloin c-kohdan pysähtymishetki mahtuu kuvaajaan.

<svg data-fig="fy9-liike-s3-graph" viewBox="0 0 440 400" role="img" aria-label="Kuvaaja: junan nopeus v kilometreinä tunnissa ajan t funktiona. Kuvaajassa on yksitoista mustaa pistettä hetkiltä 0–40 s. Kolmen ensimmäisen pisteen kohdalla on vaakasuora suora tasolla 90 km/h. Muihin pisteisiin on sovitettu laskeva suora. Se leikkaa vaakasuoran suoran noin hetkellä 10 s. Laskevaa suoraa on jatkettu katkoviivana aika-akselille noin hetkeen 48,5 s. Suoran pisteet (12 s; 85 km/h) ja (40 s; 20 km/h) on ympyröity. Niistä luetaan kulmakerroin, noin −2,3 km/h sekunnissa. Laskevan suoran ja aika-akselin väliin jää kolmio, joka on vihreä. Sen pinta-ala on jarrutusmatka." style="max-width:100%;font-size:24px">
  <line x1="83.5" y1="356" x2="83.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="103" y1="356" x2="103" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="122.5" y1="356" x2="122.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="141.5" y1="356" x2="141.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="161" y1="356" x2="161" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180.5" y1="356" x2="180.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="356" x2="200" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="219.5" y1="356" x2="219.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="239" y1="356" x2="239" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="258.5" y1="356" x2="258.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="277.5" y1="356" x2="277.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="297" y1="356" x2="297" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="316.5" y1="356" x2="316.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336" y1="356" x2="336" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="325.5" x2="336" y2="325.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="295" x2="336" y2="295" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="265" x2="336" y2="265" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="234.5" x2="336" y2="234.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="204" x2="336" y2="204" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="173.5" x2="336" y2="173.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="143" x2="336" y2="143" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="113" x2="336" y2="113" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="82.5" x2="336" y2="82.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="52" x2="336" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="63" y1="356" x2="350" y2="356" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M362,356 L349,362 L349,350 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="64" y1="357" x2="64" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M64,26 L70,39 L58,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="83.5" y1="356" x2="83.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="356" x2="103" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="93" y="365.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="122.5" y1="356" x2="122.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="141.5" y1="356" x2="141.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="125" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$16$</div></foreignObject>
  <line x1="161" y1="356" x2="161" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="180.5" y1="356" x2="180.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="164" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$24$</div></foreignObject>
  <line x1="200" y1="356" x2="200" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="219.5" y1="356" x2="219.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="203" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$32$</div></foreignObject>
  <line x1="239" y1="356" x2="239" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="258.5" y1="356" x2="258.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="242" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="277.5" y1="356" x2="277.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="297" y1="356" x2="297" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="280.5" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$48$</div></foreignObject>
  <line x1="316.5" y1="356" x2="316.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="336" y1="356" x2="336" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="319.5" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$56$</div></foreignObject>
  <line x1="57" y1="325.5" x2="64" y2="325.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="57" y1="295" x2="64" y2="295" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="19" y="280.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="57" y1="265" x2="64" y2="265" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="57" y1="234.5" x2="64" y2="234.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="19" y="220" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="57" y1="204" x2="64" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="57" y1="173.5" x2="64" y2="173.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="19" y="159" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="57" y1="143" x2="64" y2="143" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="57" y1="113" x2="64" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="19" y="98.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="57" y1="82.5" x2="64" y2="82.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="57" y1="52" x2="64" y2="52" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="7" y="37.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="34" y="361.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="368" y="341.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="78" y="17.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$v\ (\text{km/h})$</span></div></foreignObject>
  <polygon points="112,82.5 301,356 112,356" fill="#b2f2bb" fill-opacity="0.75"/>
  <polyline points="64,82.5 112,82.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="112,82.5 258.5,294.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="258.5,294.5 301,356" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="64" cy="79.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="83.5" cy="85.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="103" cy="82.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="122.5" cy="100.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="141.5" cy="122" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="161" cy="152.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="180.5" cy="186" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="200" cy="207" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="219.5" cy="237.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="239" cy="271" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="258.5" cy="292" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="122.5" cy="97.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="258.5" cy="295" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="112" y1="82.5" x2="112" y2="356" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="118" y="317" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$10\,\text{s}$</div></foreignObject>
  <foreignObject x="307" y="296" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$48{,}5\,\text{s}$</div></foreignObject>
  <foreignObject x="195" y="110.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$k \approx -2{,}3\,\tfrac{\text{km/h}}{\text{s}}$</div></foreignObject>
  <foreignObject x="81" y="274.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{jarrutusmatka}$</div></foreignObject>
</svg>

**Mallivastaus:** Pisteistä näkyy kaksi vaihetta. Hetkinä $0$, $4$ ja $8\,\text{s}$ nopeus pysyy noin $90\,\text{km/h}$:ssa. Vaihtelu $\pm 1\,\text{km/h}$ on yhtä suuri kuin sovelluksen epävarmuus. Juna siis kulkee tasaisesti, ja näille pisteille piirretään vaakasuora suora.

Hetkestä $12\,\text{s}$ alkaen nopeus pienenee joka neljässä sekunnissa suunnilleen yhtä paljon. Juna siis jarruttaa tasaisesti. Näihin pisteisiin sovitetaan laskeva suora niin, että pisteitä jää suoran molemmille puolille. Kolmea ensimmäistä pistettä ei oteta mukaan jarrutussuoraan. Ne kuuluvat eri vaiheeseen, ja ne kääntäisivät suoran väärään asentoon. Laskevaa suoraa jatketaan katkoviivana aika-akselille c-kohtaa varten.

### b)
**Annettu:** a-kohdan jarrutussuora; siltä luetaan pisteet $(12\,\text{s};\ 85\,\text{km/h})$ ja $(40\,\text{s};\ 20\,\text{km/h})$
**Kysytty:** jarrutuksen kiihtyvyys $a$ yksikössä $\text{m/s}^2$
**Periaate:** Jarrutuksen pisteet ovat suoralla. Siksi kiihtyvyys on vakio, ja se on $(t,v)$-kuvaajan kulmakerroin (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*). Kulmakerroin luetaan sovitetulta suoralta kahdesta pisteestä, jotka ovat kaukana toisistaan. Sitä ei lueta vierekkäisistä mittauspisteistä, koska jokaisessa mittauksessa on pieni virhe (luku *Graafinen esitys ja suoran sovittaminen*).
**Kuvaajan lukeminen:** Suora kulkee pisteiden $(12\,\text{s};\ 85\,\text{km/h})$ ja $(40\,\text{s};\ 20\,\text{km/h})$ kautta. Pisteet on ympyröity mallikuvaajaan.
**Kaava:** $a = \dfrac{\Delta v}{\Delta t} = \dfrac{v_2 - v_1}{t_2 - t_1}$
**Muunnokset:** Nopeuden muutos muunnetaan metreiksi sekunnissa, ja yksiköt sijoitetaan: $20\,\text{km/h} - 85\,\text{km/h} = -65\,\text{km/h} = \dfrac{-65 \cdot 1000\,\text{m}}{3600\,\text{s}} = -18{,}06\,\text{m/s}$
**Sijoitus:** $a = \dfrac{-18{,}06\,\text{m/s}}{40\,\text{s} - 12\,\text{s}} = \dfrac{-18{,}06\,\text{m/s}}{28\,\text{s}} = -0{,}645\,\text{m/s}^2$
**Vastaus:** $a \approx -0{,}65\,\text{m/s}^2$. Tuloksessa on kaksi merkitsevää numeroa, koska suoralta luetut nopeudet tunnetaan noin kahden numeron tarkkuudella. Tulokset $-0{,}61$…$-0{,}68\,\text{m/s}^2$ ovat sovituksen vaihteluvälin sisällä.
**Järkevyys:** Kiihtyvyys on negatiivinen eli vastakkainen nopeudelle. Siksi vauhti pienenee, kuten jarrutuksessa pitää. Suuruus $0{,}65\,\text{m/s}^2$ on junan tavallinen jarrutus, jossa matkustajat pysyvät pystyssä. Taulukkolaskennan sovitus antaa $-2{,}31\,\text{km/h}$ sekunnissa eli $-0{,}642\,\text{m/s}^2$. Se on lähes sama.

### c)
**Annettu:** a-kohdan kuvaaja: jarrutus alkaa kohdasta, jossa vaakasuora ja laskeva suora leikkaavat; nopeus on siinä $v_0 = 90\,\text{km/h}$
**Kysytty:** pysähtymishetki $t_\text{p}$ ja jarrutusmatka $\Delta x$ jarrutuksen alusta
**Periaate:** Juna pysähtyy, kun jarrutussuora leikkaa aika-akselin. Mittaus päättyi hetkellä $40\,\text{s}$. Siksi suoraa on jatkettava mittausalueen ulkopuolelle. Siirtymä on $(t,v)$-kuvaajan ja aika-akselin välinen pinta-ala. Tässä alue on suorakulmainen kolmio (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*).
**Kuvaajan lukeminen:** Vaakasuora ja laskeva suora leikkaavat noin hetkellä $t_0 = 10\,\text{s}$. Jatkettu jarrutussuora leikkaa aika-akselin noin hetkellä $t_\text{p} = 48{,}5\,\text{s}$.
**Kaava:** $\Delta x = \tfrac{1}{2}\,v_0\,(t_\text{p} - t_0)$
**Muunnokset:** $90\,\text{km/h} = \dfrac{90 \cdot 1000\,\text{m}}{3600\,\text{s}} = 25\,\text{m/s}$
**Sijoitus:** $\Delta x = \tfrac{1}{2} \cdot 25\,\text{m/s} \cdot (48{,}5\,\text{s} - 10\,\text{s}) = \tfrac{1}{2} \cdot 25\,\text{m/s} \cdot 38{,}5\,\text{s} = 481\,\text{m}$
**Vastaus:** Juna pysähtyy noin hetkellä $49\,\text{s}$, ja jarrutusmatka on noin $480\,\text{m}$. Tuloksessa on kaksi merkitsevää numeroa, koska leikkauskohdat luetaan kuvaajasta noin puolen sekunnin tarkkuudella. Tulokset $450$–$520\,\text{m}$ hyväksytään.
**Järkevyys:** b-kohdan kiihtyvyydellä jarrutus nopeudesta $25\,\text{m/s}$ kestää $25\,\text{m/s} : 0{,}645\,\text{m/s}^2 \approx 39\,\text{s}$. Se on lähes sama kuin kuvaajasta luettu $38{,}5\,\text{s}$. Keskinopeus jarrutuksen aikana on $12{,}5\,\text{m/s}$, ja $12{,}5\,\text{m/s} \cdot 38{,}5\,\text{s} \approx 480\,\text{m}$. Noin puolen kilometrin jarrutusmatka sopii junalle, joka pysähtyy asemalle tavallisella jarrutuksella.

### d)
**Kysytty:** kuinka luotettava on päätelmä, että juna pysähtyi tarkalleen c-kohdan matkan päähän
**Periaate:** Malli on luotettava vain sillä alueella, jolla on mitattu. Ekstrapolointi tarkoittaa, että mallia jatketaan mittausalueen ulkopuolelle. Silloin oletetaan, että liike jatkuu samanlaisena. Tuloksen tarkkuus riippuu myös siitä, kuinka hyvin kulmakerroin tunnetaan (luvut *Graafinen esitys ja suoran sovittaminen* ja *Mittaaminen ja mittauksen luotettavuus*).
**Mallivastaus:** Päätelmä on suuruusluokaltaan hyvä, mutta se ei ole tarkka. Tallennus päättyi hetkellä $40\,\text{s}$, kun nopeus oli vielä noin $20\,\text{km/h}$. Pysähtymishetki $48{,}5\,\text{s}$ ja viimeisten noin $9\,\text{s}$:n matka perustuvat siis oletukseen. Oletus on, että juna jarrutti samalla kiihtyvyydellä loppuun asti. Todellisuudessa kuljettaja usein keventää jarrutusta juuri ennen pysähtymistä. Silloin juna kulkee vähän pidemmälle. Lisäksi kulmakertoimen epävarmuus siirtyy tulokseen. Jyrkin ja loivin pisteisiin sopiva suora antavat pysähtymishetkelle noin sekunnin vaihteluvälin ja matkalle noin $\pm 20\,\text{m}$:n vaihteluvälin. Sovelluksen nopeuden epävarmuus $\pm 1\,\text{km/h}$ on pieni verrattuna nopeuden muutokseen $70\,\text{km/h}$. Se ei siis ole suurin epävarmuuden lähde. Tulos kannattaa ilmoittaa muodossa ”noin $480\,\text{m}$, epävarmuus muutamia kymmeniä metrejä”, ei ”tarkalleen”.

### Yleisiä virheitä
- Kaikki pisteet yhdistetään murtoviivaksi, tai kaikkiin yhteentoista pisteeseen sovitetaan yksi suora. Silloin tasaisen vaiheen pisteet kääntävät kulmakerrointa.
- Kulmakerroin lasketaan kahdesta vierekkäisestä mittauspisteestä tai taulukon arvoista eikä suoralta.
- Kiihtyvyys jätetään yksikköön $\text{km/h}$ sekunnissa, tai muunnoksessa kerrotaan luvulla $3{,}6$, vaikka pitäisi jakaa.
- Jarrutusmatkaksi lasketaan suorakulmio $25\,\text{m/s} \cdot 38{,}5\,\text{s}$ eikä kolmio, tai matka lasketaan hetkestä $0$ alkaen.

### Hyväksytään myös
- b-kohdan kulmakerroin taulukkolaskennan sovituksesta jarrutuspisteisiin: $-2{,}31\,\text{km/h}$ sekunnissa eli $-0{,}642\,\text{m/s}^2$.
- c-kohdan matka laskettuna b-kohdan kiihtyvyydestä: $t = v_0 : |a|$ ja $\Delta x = \tfrac{1}{2}\,v_0\,t$.

## fy9-liike-s4

### a)
**Kysytty:** todistaako yli $80\,\text{km/h}$:n keskinopeus, että kuljettaja on jossain kohdassa ajanut ylinopeutta
**Periaate:** Keskinopeus on siirtymä jaettuna ajalla. $(t,x)$-kuvaajassa se on sen suoran kulmakerroin, joka kulkee osuuden alku- ja loppupisteen kautta. Hetkellinen nopeus on kuvaajan tangentin kulmakerroin. Siirtymä on $(t,v)$-kuvaajan alle jäävä pinta-ala (luvut *Paikka, nopeus ja tasainen liike kuvaajina* ja *Kiihtyvyys ja tasaisesti kiihtyvä liike*).
**Mallivastaus:** Kannanotto on väärä. Ajatellaan, että auton nopeus olisi koko ajan enintään $80\,\text{km/h}$. Silloin sen $(t,v)$-kuvaaja olisi koko ajan vaakasuoran viivan $v = 80\,\text{km/h}$ alapuolella tai viivalla. Kuvaajan alle jäävä pinta-ala eli kuljettu matka olisi silloin enintään $80\,\text{km/h}$ kertaa kulkuaika. Keskinopeus olisi siis enintään $80\,\text{km/h}$. Sama näkyy $(t,x)$-kuvaajasta: kuvaaja ei voi nousta alusta loppuun keskimäärin jyrkemmin kuin sen jyrkimmässä kohdassa. Kun keskinopeus on yli $80\,\text{km/h}$, nopeus on siis varmasti ollut jossain kohdassa yli $80\,\text{km/h}$. Toisin päin päätelmä ei kuitenkaan pidä. Kuljettaja voi ajaa osan matkasta ylinopeutta ja ajaa toisaalla hitaasti. Silloin keskinopeus jää alle rajan. Valvonta ei siis tuomitse syyttömiä, mutta se ei myöskään huomaa kaikkia ylinopeuksia.

### b)
**Annettu:** osuudet $\Delta x_1 = 2{,}0\,\text{km}$ nopeudella $v_1 = 100\,\text{km/h}$ ja $\Delta x_2 = 1{,}0\,\text{km}$ nopeudella $v_2 = 60\,\text{km/h}$; koko osuus $\Delta x = 3{,}0\,\text{km}$
**Kysytty:** keskinopeus $v_\text{ka}$ yksikössä $\text{km/h}$
**Periaate:** Keskinopeus on koko siirtymä jaettuna koko ajalla (luku *Paikka, nopeus ja tasainen liike kuvaajina*). Kummallakin osalla nopeus on vakio. Siksi osan aika on sen matka jaettuna nopeudella. Nopeuksien keskiarvo ei kelpaa, koska nopeuksilla ajetaan eri pitkään.
**Kaava:** $t_1 = \dfrac{\Delta x_1}{v_1}$, $t_2 = \dfrac{\Delta x_2}{v_2}$ ja $v_\text{ka} = \dfrac{\Delta x}{t_1 + t_2}$
**Muunnokset:** Matkat ovat kilometreinä ja nopeudet kilometreinä tunnissa. Siksi ajat tulevat tunteina, eikä muunnoksia tarvita. Vertailun vuoksi tunnit muunnetaan sekunneiksi: $1\,\text{h} = 3600\,\text{s}$.
**Sijoitus:** $t_1 = \dfrac{2{,}0\,\text{km}}{100\,\text{km/h}} = 0{,}020\,\text{h} = 72\,\text{s}$, $t_2 = \dfrac{1{,}0\,\text{km}}{60\,\text{km/h}} = 0{,}01667\,\text{h} = 60\,\text{s}$ ja $v_\text{ka} = \dfrac{3{,}0\,\text{km}}{0{,}020\,\text{h} + 0{,}01667\,\text{h}} = \dfrac{3{,}0\,\text{km}}{0{,}03667\,\text{h}} = 81{,}8\,\text{km/h}$
**Vastaus:** $v_\text{ka} \approx 82\,\text{km/h}$. Tuloksessa on kaksi merkitsevää numeroa, kuten matkoissa $2{,}0\,\text{km}$ ja $1{,}0\,\text{km}$. Kannanotto on väärä: keskinopeus ylittää rajoituksen.
**Järkevyys:** Rajoitusnopeudella osuuteen kuluisi $3{,}0\,\text{km} : 80\,\text{km/h} = 0{,}0375\,\text{h} = 135\,\text{s}$. Kuljettajalta kului $132\,\text{s}$. Se on vähemmän kuin $135\,\text{s}$, joten hän ajoi rajoitusnopeutta nopeammin. Keskinopeus on lähempänä nopeutta $100\,\text{km/h}$, koska sillä nopeudella ajettiin suurempi osa ajasta.

### c)
**Kysytty:** keskinopeuden epävarmuus $3{,}0\,\text{km}$:n ja $100\,\text{m}$:n osuudella, kun auto ajaa nopeudella $80\,\text{km/h}$, ja pitääkö kolmas kannanotto
**Periaate:** Keskinopeus lasketaan kulkuajasta. Kulkuaika on kahden kirjauksen erotus. Siksi kummankin kirjauksen $0{,}5\,\text{s}$:n epävarmuus vaikuttaa siihen. Yhteensä epävarmuus on enintään noin $1\,\text{s}$. Mitä lyhyempi kulkuaika on, sitä suurempi on saman aikavirheen suhteellinen vaikutus (luku *Mittaaminen ja mittauksen luotettavuus*).
**Mallivastaus:** Nopeus on $$
\begin{aligned}
&80\,\text{km/h} \\
&= \dfrac{80 \cdot 1000\,\text{m}}{3600\,\text{s}} \\
&= 22{,}2\,\text{m/s}
\end{aligned}
$$. Pitkän osuuden kulkuaika on $3000\,\text{m} : 22{,}2\,\text{m/s} = 135\,\text{s}$. Yhden sekunnin virhe on siitä alle $1\,\%$. Siksi keskinopeuden epävarmuus on noin $$
\begin{aligned}
&80\,\text{km/h} \cdot 1\,\text{s} : 135\,\text{s} \\
&\approx 0{,}6\,\text{km/h}
\end{aligned}
$$. Lyhyellä osuudella kulkuaika on vain $100\,\text{m} : 22{,}2\,\text{m/s} = 4{,}5\,\text{s}$. Yhden sekunnin virhe on siitä yli $20\,\%$. Mitattu keskinopeus voisi silloin olla noin $65$–$100\,\text{km/h}$, eli epävarmuus on noin $18\,\text{km/h}$. Kolmas kannanotto ei siis pidä. Lyhyellä osuudella järjestelmä ei pystyisi erottamaan rajoitusnopeutta ajavaa kuljettajaa ylinopeutta ajavasta. Tulos voisi mennä kumpaan suuntaan tahansa. Valvontaosuuden on oltava pitkä, jotta ajanoton epävarmuus on pieni verrattuna kulkuaikaan.

### Yleisiä virheitä
- b-kohdassa lasketaan nopeuksien keskiarvo tai matkoilla painotettu keskiarvo ($\tfrac{2}{3} \cdot 100 + \tfrac{1}{3} \cdot 60 \approx 87\,\text{km/h}$), tai matka jaetaan väärällä nopeudella.
- a-kohdassa sekoitetaan keskinopeus ja hetkellinen nopeus. Tai väitetään, että keskinopeus voi olla yli rajan, vaikka ylinopeutta ei ole ajettu.
- c-kohdassa ajanoton epävarmuutta verrataan matkaan tai nopeuteen, vaikka sitä pitää verrata kulkuaikaan.

### Hyväksytään myös
- b-kohta sekunteina ja metreinä: $$
\begin{aligned}
&3000\,\text{m} : 132\,\text{s} \\
&= 22{,}7\,\text{m/s} \\
&\approx 82\,\text{km/h}
\end{aligned}
$$.
- c-kohdassa epävarmuus $0{,}5\,\text{s}$:n perusteella ($0{,}3\,\text{km/h}$ ja $9\,\text{km/h}$), kun johtopäätös on sama.

## fy9-liike-s5

### a)
**Annettu:** matka $x = 1{,}20\,\text{m}$ levosta, aika $t = 1{,}6\,\text{s}$, ajanoton epävarmuus $\Delta t = 0{,}2\,\text{s}$
**Kysytty:** ryhmän laskema kiihtyvyys $a$ ja sen vaihteluväli ajanoton epävarmuuden takia
**Periaate:** Ryhmä olettaa, että liike on tasaisesti kiihtyvää. Silloin levosta lähtevän kappaleen paikka on $x = \tfrac{1}{2}\,a\,t^2$ (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*). Epävarmuuden vaikutus arvioidaan niin, että tulos lasketaan ajan ääriarvoilla $t \pm \Delta t$. Ääriarvo on suurin tai pienin mahdollinen arvo (luku *Mittaaminen ja mittauksen luotettavuus*).
**Kaava:** $x = \tfrac{1}{2}\,a\,t^2$, joten $a = \dfrac{2x}{t^2}$; ajanoton epävarmuuden ääriarvot ovat $a_\text{min} = \dfrac{2x}{(t + \Delta t)^2}$ ja $a_\text{max} = \dfrac{2x}{(t - \Delta t)^2}$
**Muunnokset:** Matka on metreinä ja aika sekunteina. Muunnoksia ei tarvita.
**Sijoitus:** $a = \dfrac{2 \cdot 1{,}20\,\text{m}}{(1{,}6\,\text{s})^2} = \dfrac{2{,}40\,\text{m}}{2{,}56\,\text{s}^2} = 0{,}9375\,\text{m/s}^2$; ääriarvot $\dfrac{2{,}40\,\text{m}}{(1{,}8\,\text{s})^2} = 0{,}741\,\text{m/s}^2$ ja $\dfrac{2{,}40\,\text{m}}{(1{,}4\,\text{s})^2} = 1{,}224\,\text{m/s}^2$
**Vastaus:** $a \approx 0{,}94\,\text{m/s}^2$. Epävarmuuden takia tulos on kuitenkin välillä $0{,}74$…$1{,}22\,\text{m/s}^2$, eli $a \approx (0{,}9 \pm 0{,}3)\,\text{m/s}^2$. Vaihteluvälin puolikas on $0{,}24\,\text{m/s}^2$. Väli on kuitenkin epäsymmetrinen: yläraja on $0{,}29\,\text{m/s}^2$ parhaan arvion yläpuolella. Siksi epävarmuus pyöristetään ylöspäin. Epävarmuus on suuri, joten tulos kannattaa ilmoittaa yhdellä tai kahdella merkitsevällä numerolla.
**Järkevyys:** Ajan suhteellinen epävarmuus on $0{,}2\,\text{s} : 1{,}6\,\text{s} \approx 13\,\%$. Aika on kaavassa toisessa potenssissa. Siksi kiihtyvyyden suhteellinen epävarmuus on noin kaksi kertaa niin suuri, $25\,\%$. Tämä vastaa laskettua vaihteluväliä. Kiihtyvyys alle $1\,\text{m/s}^2$ sopii loivalle radalle.

### b)
**Kysytty:** onko ryhmän johtopäätös perusteltu, ja mitkä ovat mittauksen tärkeimmät heikkoudet
**Periaate:** Mallin sopivuuden voi osoittaa vain niin, että mallia verrataan moneen mittauspisteeseen. Tasaisesti kiihtyvässä liikkeessä $(t,x)$-pisteet osuvat paraabelille ja $(t,v)$-pisteet suoralle (luvut *Kiihtyvyys ja tasaisesti kiihtyvä liike* ja *Graafinen esitys ja suoran sovittaminen*).
**Mallivastaus:** Johtopäätös ei ole perusteltu. Ryhmä käytti kaavaa $a = \dfrac{2x}{t^2}$. Kaava on johdettu olettaen, että kiihtyvyys on tasainen. Siksi kaavalla saatu luku ei voi todistaa oletusta. Yhdestä matkasta ja ajasta saadaan aina jokin luku, oli liike millainen tahansa. Kyse on kehäpäätelmästä: päättely olettaa sen, mikä pitäisi osoittaa. Yksi $(t,x)$-piste sopii mihin tahansa kiihtyvään liikkeeseen. Tarvitaan useita pisteitä eri hetkiltä. Lisäksi mittauksessa on heikkouksia. Kun aika otetaan käsin, reaktioaika vaikuttaa sekä alussa että lopussa. Kärryn lähtöhetki ja ohituskohta arvioidaan silmällä ja sivulta katsoen. Kärry on voinut saada vauhtia, kun se päästettiin liikkeelle. Mittaus tehtiin vain kerran, joten satunnaisen virheen suuruutta ei tiedetä. Luku $0{,}94\,\text{m/s}^2$ on parhaimmillaankin karkea arvio kiihtyvyydestä, jos liike on tasaisesti kiihtyvää.

### c)
**Kysytty:** koesuunnitelma, jolla selvitetään luotettavasti, onko liike tasaisesti kiihtyvää, ja määritetään kiihtyvyys
**Periaate:** Mallia testataan niin, että paikka mitataan monella hetkellä ja mittauspisteisiin sovitetaan mallin mukainen käyrä. Kiihtyvyys saadaan sovituksen kertoimesta. Muuttujat pidetään vakioina, ja mittaukset toistetaan (luvut *Kiihtyvyys ja tasaisesti kiihtyvä liike*, *Graafinen esitys ja suoran sovittaminen* ja *Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi*).
**Mallivastaus:** Kärryn liike kuvataan videolle. Kamera on jalustalla kohtisuoraan rataa vastaan. Mittakaava asetetaan mittanauhan avulla, joka on radan tasossa. Videoanalyysillä luetaan kärryn paikka esimerkiksi joka kolmannesta kuvasta. Näin saadaan kymmeniä $(t,x)$-pisteitä. Toinen vaihtoehto on asettaa radalle valoportteja eri etäisyyksille ja mitata ajat elektronisesti. Kärry päästetään levosta ilman tönäisyä, esimerkiksi irrottamalla pidike. Radan kaltevuus pidetään samana kaikissa toistoissa. Pisteet esitetään $(t,x)$-kuvaajana, ja niihin sovitetaan toisen asteen polynomi $x = A\,t^2 + B\,t + C$. Jos pisteet osuvat käyrälle ilman järjestelmällistä poikkeamaa, liike on tasaisesti kiihtyvää. Silloin kiihtyvyys on $a = 2A$. Toinen tapa on laskea nopeudet peräkkäisistä pisteistä ja tarkastella, ovatko $(t,v)$-pisteet suoralla. Koe toistetaan vähintään kolme kertaa. Kiihtyvyyden epävarmuus arvioidaan toistojen hajonnasta tai siitä kertoimen epävarmuudesta, jonka sovitus antaa.

### Yleisiä virheitä
- a-kohdassa kaavana käytetään $a = \dfrac{x}{t^2}$ ilman kerrointa $2$. Tai käytetään kaavaa $a = \dfrac{v}{t}$, jossa $v = x : t$ on keskinopeus eikä loppunopeus.
- Epävarmuus arvioidaan vain sanallisesti. Sen vaikutusta tulokseen ei lasketa.
- c-kohdassa ehdotetaan vain ”tarkempaa sekuntikelloa” tai ”useampia toistoja” samalla menetelmällä. Silloin yksi piste ei vieläkään testaa mallia.
- Kehäpäätelmää ei huomata. Johtopäätöstä kritisoidaan vain epävarmuuden takia.

### Hyväksytään myös
- a-kohdan epävarmuus suhteellisen epävarmuuden avulla: $\dfrac{\Delta a}{a} \approx 2 \cdot \dfrac{\Delta t}{t} = 25\,\%$, $\Delta a \approx 0{,}23\,\text{m/s}^2$.
- c-kohdassa mittaus sensorilla tai liikeanturilla, joka antaa $(t,x)$- tai $(t,v)$-pisteet suoraan.

## fy9-liike-s6

### a)
**Annettu:** sovitettu polynomi $y = A\,t^2 + B\,t + C$, jossa $A = -4{,}44\,\text{m/s}^2$, $B = -0{,}007\,\text{m/s}$ ja $C = 1{,}651\,\text{m}$; pallo lähti levosta, ja $y$ kasvaa ylöspäin
**Kysytty:** mitattu putoamiskiihtyvyys $a$
**Periaate:** Vapaasti putoavan pallon liike on tasaisesti kiihtyvää. Siksi sen paikka on $y = y_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2$. Kun sovitettua polynomia verrataan tähän, $t^2$:n kertoimet ovat samat: $A = \tfrac{1}{2}\,a$ (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*). Kerroin $B \approx 0$ tarkoittaa, että alkunopeus on nolla. $C$ on alkukorkeus.
**Kaava:** $A = \tfrac{1}{2}\,a$, joten $a = 2A$
**Muunnokset:** Kertoimen yksikkö on jo $\text{m/s}^2$. Muunnoksia ei tarvita.
**Sijoitus:** $a = 2 \cdot (-4{,}44\,\text{m/s}^2) = -8{,}88\,\text{m/s}^2$
**Vastaus:** Mitattu putoamiskiihtyvyys on $8{,}88\,\text{m/s}^2$ alaspäin. Miinusmerkki tulee siitä, että $y$ kasvaa ylöspäin. Tuloksessa on kolme merkitsevää numeroa, kuten kertoimessa $A$.
**Järkevyys:** Tarkistus taulukosta: kun $t = 0{,}50\,\text{s}$, pallo on pudonnut $$
1{,}653\,\text{m} - 0{,}538\,\text{m} = 1{,}115\,\text{m}
$$, ja $\tfrac{1}{2} \cdot 8{,}88\,\text{m/s}^2 \cdot (0{,}50\,\text{s})^2 = 1{,}11\,\text{m}$. Tulos on samaa suuruusluokkaa kuin $9{,}81\,\text{m/s}^2$, mutta se on selvästi pienempi. Jokin siis vaikuttaa mittaukseen.

### b)
**Annettu:** $A = (-4{,}44 \pm 0{,}05)\,\text{m/s}^2$, a-kohdasta $a = 8{,}88\,\text{m/s}^2$; taulukkoarvo $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** kiihtyvyyden epävarmuus $\Delta a$ ja sopiiko tulos taulukkoarvoon
**Periaate:** Kun suure kerrotaan vakiolla, myös sen epävarmuus kerrotaan samalla vakiolla. Tulos sopii vertailuarvoon, jos ero on yhtä suuri kuin epävarmuus tai pienempi (luku *Mittaaminen ja mittauksen luotettavuus*).
**Kaava:** $a = 2A$, joten $\Delta a = 2\,\Delta A$
**Muunnokset:** Ei tarvita, koska yksiköt ovat samat.
**Sijoitus:** $$
\begin{aligned}
\Delta a &= 2 \cdot 0{,}05\,\text{m/s}^2 \\
&= 0{,}10\,\text{m/s}^2
\end{aligned}
$$; ero taulukkoarvoon $$
\begin{aligned}
&9{,}81\,\text{m/s}^2 - 8{,}88\,\text{m/s}^2 \\
&= 0{,}93\,\text{m/s}^2
\end{aligned}
$$
**Vastaus:** $a = (8{,}88 \pm 0{,}10)\,\text{m/s}^2$. Ero taulukkoarvoon on $0{,}93\,\text{m/s}^2$. Se on noin yhdeksän kertaa epävarmuus, joten tulos ei sovi taulukkoarvoon.
**Järkevyys:** Suhteellinen epävarmuus on $0{,}10 : 8{,}88 \approx 1{,}1\,\%$. Se sopii siihen, että pisteiden hajonta on pieni, vain muutamia millimetrejä. Sovituksen epävarmuus kertoo vain satunnaisesta hajonnasta. Se ei kerro systemaattisesta virheestä, joka siirtää kaikkia pisteitä samaan suuntaan.

### c)
**Annettu:** mittakaava asetettiin metrimitan tasossa $3{,}00\,\text{m}$:n päässä kamerasta, ja pallo putosi $3{,}30\,\text{m}$:n päässä kamerasta; a- ja b-kohdasta $a = (8{,}88 \pm 0{,}10)\,\text{m/s}^2$
**Kysytty:** systemaattisen virheen syy ja suunta sekä korjattu kiihtyvyys $a_\text{k}$
**Periaate:** Kauempana oleva kohde näkyy kuvassa pienempänä. Se näkyy pienempänä samassa suhteessa kuin sen etäisyys kamerasta on suurempi. Ohjelma muuntaa pallon kuvassa kulkemat matkat metreiksi mittakaavalla, joka asetettiin mitan tasossa. Siksi ohjelma antaa pallon matkoiksi liian pienet arvot. Kiihtyvyys on verrannollinen matkaan, joten kiihtyvyys korjataan samalla suhteella (luku *Mittaaminen ja mittauksen luotettavuus*).
**Kaava:** $a_\text{k} = \dfrac{d_\text{pallo}}{d_\text{mitta}}\,a$ ja $\Delta a_\text{k} = \dfrac{d_\text{pallo}}{d_\text{mitta}}\,\Delta a$
**Muunnokset:** Etäisyydet ovat samassa yksikössä, joten niiden suhteella ei ole yksikköä.
**Sijoitus:** $a_\text{k} = \dfrac{3{,}30\,\text{m}}{3{,}00\,\text{m}} \cdot 8{,}88\,\text{m/s}^2 = 1{,}10 \cdot 8{,}88\,\text{m/s}^2 = 9{,}768\,\text{m/s}^2$ ja $\Delta a_\text{k} = 1{,}10 \cdot 0{,}10\,\text{m/s}^2 = 0{,}11\,\text{m/s}^2$
**Vastaus:** Korjattu putoamiskiihtyvyys on $a_\text{k} \approx (9{,}8 \pm 0{,}1)\,\text{m/s}^2$. Tulos ilmoitetaan yhdellä desimaalilla eikä kahdella, koska epävarmuus on noin $0{,}1\,\text{m/s}^2$. Virhe pienensi tulosta noin $9\,\%$.
**Järkevyys:** Korjattu tulos poikkeaa taulukkoarvosta $9{,}81\,\text{m/s}^2$ vain $0{,}04\,\text{m/s}^2$. Ero on pienempi kuin epävarmuus, joten mittakaavavirhe selittää koko eron. Myös virheen suunta on oikea: liian pieni mittakaava antaa liian pienen kiihtyvyyden.

### d)
**Kysytty:** onko hyvä menetelmä laskea kiihtyvyys vain ensimmäisestä ja viimeisestä pisteestä
**Periaate:** Jokaisessa mittauspisteessä on pieni satunnainen virhe. Sovitus käyttää kaikkia pisteitä yhtä aikaa. Siksi yhden pisteen virhe vaikuttaa siihen vähemmän. Sovitus antaa myös kertoimen epävarmuuden (luku *Graafinen esitys ja suoran sovittaminen*).
**Mallivastaus:** Ehdotus on huonompi kuin sovitus. Kahden pisteen laskulla saadaan tässä $a = \dfrac{2 \cdot 1{,}115\,\text{m}}{(0{,}50\,\text{s})^2} \approx 8{,}92\,\text{m/s}^2$. Se on lähes sama kuin sovituksen tulos. Tulos riippuu kuitenkin kokonaan kahdesta pisteestä. Muutaman millimetrin virhe tai väärin valittu lähtöhetki muuttaisi tulosta suoraan. Menetelmä ei myöskään kerro tuloksen epävarmuutta. Kaava olettaa lisäksi, että pallo on täsmälleen levossa hetkellä $0$. Sovitus käyttää kaikkia yhtätoista pistettä. Se sallii pienen alkunopeuden kertoimessa $B$, antaa epävarmuuden $\Delta A$ ja näyttää, sopiiko malli pisteisiin. Kumpikaan menetelmä ei kuitenkaan korjaa mittakaavan systemaattista virhettä. Virhe on korjattava erikseen, tai mittakaava on asetettava siihen tasoon, jossa pallo putoaa.

### Yleisiä virheitä
- Kiihtyvyydeksi luetaan suoraan $A = 4{,}44\,\text{m/s}^2$ ilman kerrointa $2$.
- Ero taulukkoarvoon selitetään ilmanvastuksella tai reaktioajalla. Pisteiden hajonta on kuitenkin pieni, ja aineisto kertoo, missä mittakaava oli.
- Korjaus tehdään väärään suuntaan, eli tulos kerrotaan suhteella $3{,}00 : 3{,}30$.
- Sovituksen epävarmuutta pidetään tuloksen koko epävarmuutena, ja systemaattinen virhe jätetään huomiotta.

### Hyväksytään myös
- c-kohdassa korjataan ensin kerroin $A$: $$
\begin{aligned}
A_\text{k} &= 1{,}10 \cdot (-4{,}44\,\text{m/s}^2) \\
&= -4{,}88\,\text{m/s}^2
\end{aligned}
$$ ja sitten $a_\text{k} = 2A_\text{k}$.
- b-kohdassa vertailu suhteellisina lukuina: ero on noin $9{,}5\,\%$ ja epävarmuus noin $1\,\%$.

## fy9-liike-s7

### a)
**Annettu:** $(t,x)$-kuvaaja, jossa $x$ kasvaa oikealle; ensimmäinen vaihe on kuvaajan ensimmäinen suora
**Kysytty:** nopeus $v_1$ ensimmäisessä vaiheessa
**Periaate:** Tasaisessa liikkeessä $(t,x)$-kuvaaja on suora. Suoran kulmakerroin on nopeus (luku *Paikka, nopeus ja tasainen liike kuvaajina*).
**Kuvaajan lukeminen:** Ensimmäiseltä suoralta luetaan kaksi pistettä, jotka ovat kaukana toisistaan: $(0\,\text{s};\ 4\,\text{m})$ ja $(4\,\text{s};\ 16\,\text{m})$.
**Kaava:** $v = \dfrac{\Delta x}{\Delta t} = \dfrac{x_2 - x_1}{t_2 - t_1}$
**Muunnokset:** Muunnoksia ei tarvita. Paikat ovat metreinä ja ajat sekunteina.
**Sijoitus:** $$
\begin{aligned}
v_1 &= \dfrac{16\,\text{m} - 4\,\text{m}}{4\,\text{s} - 0\,\text{s}} \\
&= \dfrac{12\,\text{m}}{4\,\text{s}} \\
&= 3{,}0\,\text{m/s}
\end{aligned}
$$
**Vastaus:** $v_1 = 3{,}0\,\text{m/s}$ oikealle. Tuloksessa on kaksi merkitsevää numeroa, kuten kuvaajasta luetuissa arvoissa.
**Järkevyys:** Kärry etenee $12\,\text{m}$ neljässä sekunnissa. Se on $3{,}0\,\text{m}$ joka sekunti eli noin $11\,\text{km/h}$. Se sopii moottoroidun kärryn nopeudeksi.

### b)
**Annettu:** $(t,x)$-kuvaaja ja hetki $8\,\text{s}$
**Kysytty:** nopeus $v$ hetkellä $8\,\text{s}$ ja liikkeen suunta
**Periaate:** Hetki $8\,\text{s}$ on kolmannessa vaiheessa. Siinä kuvaaja on laskeva suora. Nopeus on vakio, ja se on sama kuin suoran kulmakerroin (luku *Paikka, nopeus ja tasainen liike kuvaajina*). Laskeva suora tarkoittaa, että paikka $x$ pienenee. Siksi nopeus on negatiivinen.
**Kuvaajan lukeminen:** Kolmannelta suoralta luetaan kaksi pistettä, jotka ovat kaukana toisistaan: $(6\,\text{s};\ 16\,\text{m})$ ja $(10\,\text{s};\ 8\,\text{m})$.
**Kaava:** $v = \dfrac{\Delta x}{\Delta t} = \dfrac{x_2 - x_1}{t_2 - t_1}$
**Muunnokset:** Muunnoksia ei tarvita.
**Sijoitus:** $$
\begin{aligned}
v_3 &= \dfrac{8\,\text{m} - 16\,\text{m}}{10\,\text{s} - 6\,\text{s}} \\
&= \dfrac{-8\,\text{m}}{4\,\text{s}} \\
&= -2{,}0\,\text{m/s}
\end{aligned}
$$
**Vastaus:** $v = -2{,}0\,\text{m/s}$. Miinusmerkki kertoo, että kärry liikkuu vasemmalle, vastakkaiseen suuntaan kuin $x$-akseli osoittaa. Vauhti on $2{,}0\,\text{m/s}$. Nopeus on sama koko vaiheen ajan, joten se on tämä myös hetkellä $8\,\text{s}$.
**Järkevyys:** Kolmannessa vaiheessa kärry kulkee takaisin päin. Paikka pienenee $8\,\text{m}$ neljässä sekunnissa. Kuvaaja laskee, joten etumerkin pitää olla negatiivinen. Suora on loivempi kuin ensimmäisessä vaiheessa ($2{,}0\,\text{m/s} < 3{,}0\,\text{m/s}$), ja sen näkee kuvaajasta.

### c)
**Annettu:** paikka $x = 12\,\text{m}$; ensimmäisessä vaiheessa $x_0 = 4\,\text{m}$ hetkellä $0\,\text{s}$ ja $v_1 = 3{,}0\,\text{m/s}$; kolmannessa vaiheessa $x_0 = 16\,\text{m}$ hetkellä $6\,\text{s}$ ja $v_3 = -2{,}0\,\text{m/s}$
**Kysytty:** hetket $t_1$ ja $t_2$, joilla kärry on paikassa $12\,\text{m}$
**Periaate:** Kuvaajasta nähdään, että kärry ohittaa paikan $12\,\text{m}$ kahdessa vaiheessa. Ensimmäisessä vaiheessa paikka nousee arvosta $4\,\text{m}$ arvoon $16\,\text{m}$. Kolmannessa vaiheessa se laskee arvosta $16\,\text{m}$ arvoon $8\,\text{m}$. Toisessa vaiheessa kärry on koko ajan paikassa $16\,\text{m}$. Kussakin vaiheessa liike on tasaista, joten paikka on $x = x_0 + v\,(t - t_0)$ (luku *Paikka, nopeus ja tasainen liike kuvaajina*).
**Kuvaajan lukeminen:** Nopeudet ja alkupisteet saatiin a- ja b-kohdassa. Ensimmäinen suora alkaa pisteestä $(0\,\text{s};\ 4\,\text{m})$. Kolmas suora alkaa pisteestä $(6\,\text{s};\ 16\,\text{m})$.
**Kaava:** $x = x_0 + v\,(t - t_0)$, joten $t = t_0 + \dfrac{x - x_0}{v}$
**Muunnokset:** Muunnoksia ei tarvita. Paikat ovat metreinä ja ajat sekunteina.
**Sijoitus:** $$
\begin{aligned}
t_1 &= 0\,\text{s} + \dfrac{12\,\text{m} - 4\,\text{m}}{3{,}0\,\text{m/s}} \\
&= \dfrac{8\,\text{m}}{3{,}0\,\text{m/s}} \\
&\approx 2{,}67\,\text{s}
\end{aligned}
$$; $$
\begin{aligned}
t_2 &= 6\,\text{s} + \dfrac{12\,\text{m} - 16\,\text{m}}{-2{,}0\,\text{m/s}} \\
&= 6\,\text{s} + 2{,}0\,\text{s} \\
&= 8{,}0\,\text{s}
\end{aligned}
$$
**Vastaus:** Kärry on paikassa $12\,\text{m}$ ensimmäisen kerran hetkellä $t_1 \approx 2{,}7\,\text{s}$ ja toisen kerran hetkellä $t_2 = 8{,}0\,\text{s}$. Kaksi merkitsevää numeroa riittää, koska luetut arvot ovat kaksinumeroisia.
**Järkevyys:** Hetki $2{,}7\,\text{s}$ on ensimmäisen vaiheen aikavälillä $0\ldots 4\,\text{s}$. Hetki $8{,}0\,\text{s}$ on kolmannen vaiheen aikavälillä $6\ldots 10\,\text{s}$. Tarkistus: $$
\begin{aligned}
x(8{,}0\,\text{s}) &= 16\,\text{m} \\
&- 2{,}0\,\text{m/s} \cdot 2{,}0\,\text{s} \\
&= 12\,\text{m}
\end{aligned}
$$.

### d)
**Annettu:** alkupaikka $x = 4\,\text{m}$ hetkellä $0\,\text{s}$ ja loppupaikka $x = 8\,\text{m}$ hetkellä $10\,\text{s}$; vaiheiden paikan muutokset ovat $+12\,\text{m}$, $0\,\text{m}$ ja $-8\,\text{m}$
**Kysytty:** keskinopeus $v_\text{ka}$. Lisäksi se, miksi keskinopeus on eri kuin keskivauhti ja kumpi on suurempi.
**Periaate:** Keskinopeus on siirtymä jaettuna ajalla. Siirtymä on vain alkupaikan ja loppupaikan ero (luku *Paikka, nopeus ja tasainen liike kuvaajina*). Keskivauhtia laskettaessa jaetaan kuljettu matka. Siihen kertyy kaikki liike, vaikka suunta vaihtuu. Jos kärry liikkuu osan matkasta takaisin päin, keskinopeus ja keskivauhti ovat eri suuria.
**Kuvaajan lukeminen:** Kuvaajan ensimmäinen piste on $(0\,\text{s};\ 4\,\text{m})$ ja viimeinen piste $(10\,\text{s};\ 8\,\text{m})$.
**Kaava:** $v_\text{ka} = \dfrac{\Delta x}{\Delta t} = \dfrac{x_\text{loppu} - x_\text{alku}}{t_\text{loppu} - t_\text{alku}}$
**Muunnokset:** Muunnoksia ei tarvita.
**Sijoitus:** $$
\begin{aligned}
v_\text{ka} &= \dfrac{8\,\text{m} - 4\,\text{m}}{10\,\text{s} - 0\,\text{s}} \\
&= \dfrac{4\,\text{m}}{10\,\text{s}} \\
&= +0{,}40\,\text{m/s}
\end{aligned}
$$
**Vastaus:** $v_\text{ka} = +0{,}40\,\text{m/s}$ eli $0{,}40\,\text{m/s}$ oikealle. Keskinopeus on pieni, koska kärry palaa viimeisessä vaiheessa takaisin päin. Siksi paikka muuttuu vain $4\,\text{m}$. Keskivauhti on tässä suurempi: $2{,}0\,\text{m/s}$.
**Järkevyys:** Kuljettu matka on $$
\begin{aligned}
s &= 12\,\text{m} + 0\,\text{m} + 8\,\text{m} \\
&= 20\,\text{m}
\end{aligned}
$$ Keskivauhti on $$
\begin{aligned}
v_\text{vauhti} &= \dfrac{20\,\text{m}}{10\,\text{s}} \\
&= 2{,}0\,\text{m/s}
\end{aligned}
$$ Keskivauhti on aina vähintään yhtä suuri kuin keskinopeuden suuruus. Ne ovat yhtä suuret vain, jos kärry ei vaihda suuntaa. Tässä kärry vaihtaa suuntaa. Siksi keskivauhti ($2{,}0\,\text{m/s}$) on suurempi kuin keskinopeuden suuruus ($0{,}40\,\text{m/s}$).

### Yleisiä virheitä
- Nopeudeksi merkitään kuvaajan arvo $x/t$, esimerkiksi $16\,\text{m} : 4\,\text{s} = 4{,}0\,\text{m/s}$. Kuvaajan alkupaikka on kuitenkin $4\,\text{m}$, ei nolla.
- b-kohdassa nopeus annetaan positiivisena. Tai ajat ja paikat vähennetään eri järjestyksessä, jolloin etumerkki menee väärin.
- c-kohdassa löydetään vain toinen hetki. Tai toinen hetki lasketaan kaavalla $t = x : v$ ilman alkupaikkaa ja alkuhetkeä. Silloin tulos on $12\,\text{m} : (-2{,}0\,\text{m/s}) = -6\,\text{s}$.
- d-kohdassa keskinopeus lasketaan vaiheiden nopeuksien keskiarvona $(3{,}0 + 0 - 2{,}0)\,\text{m/s} : 3$ tai kuljetusta matkasta. Kumpikin antaa väärän tuloksen.

### Hyväksytään myös
- c-kohdassa toisen hetken voi ratkaista kolmannen suoran yhtälöstä $$
\begin{aligned}
x &= 16\,\text{m} \\
&- 2{,}0\,\text{m/s} \cdot (t - 6\,\text{s})
\end{aligned}
$$.
- d-kohdassa keskinopeuden voi lukea kuvaajalta. Se on alkupisteen ja loppupisteen kautta kulkevan suoran kulmakerroin.

## fy9-liike-s8

### a)
**Annettu:** kuvaajan suorat: A kulkee pisteestä $(0\,\text{s};\ 4\,\text{m})$ pisteeseen $(8\,\text{s};\ 20\,\text{m})$ ja B pisteestä $(0\,\text{s};\ 20\,\text{m})$ pisteeseen $(8\,\text{s};\ 4\,\text{m})$; $x$ kasvaa siihen suuntaan, johon A kulkee
**Kysytty:** nopeudet $v_\text{A}$ ja $v_\text{B}$ etumerkkeineen
**Periaate:** Tasaisessa liikkeessä $(t,x)$-kuvaajan suoran kulmakerroin on nopeus. Etumerkki kertoo suunnan: nouseva suora on positiivinen ja laskeva suora negatiivinen (luku *Paikka, nopeus ja tasainen liike kuvaajina*).
**Kuvaajan lukeminen:** Kummankin suoran päätepisteet ovat kaukana toisistaan, joten paikat luetaan niistä. A: $4\,\text{m}$ ja $20\,\text{m}$. B: $20\,\text{m}$ ja $4\,\text{m}$. Aikaväli on $0\ldots 8\,\text{s}$.
**Kaava:** $v = \dfrac{\Delta x}{\Delta t} = \dfrac{x_2 - x_1}{t_2 - t_1}$
**Muunnokset:** Muunnoksia ei tarvita. Paikat ovat metreinä ja ajat sekunteina.
**Sijoitus:** $$
\begin{aligned}
v_\text{A} &= \dfrac{20\,\text{m} - 4\,\text{m}}{8\,\text{s} - 0\,\text{s}} \\
&= \dfrac{16\,\text{m}}{8\,\text{s}} \\
&= 2{,}0\,\text{m/s}
\end{aligned}
$$; $$
\begin{aligned}
v_\text{B} &= \dfrac{4\,\text{m} - 20\,\text{m}}{8\,\text{s} - 0\,\text{s}} \\
&= \dfrac{-16\,\text{m}}{8\,\text{s}} \\
&= -2{,}0\,\text{m/s}
\end{aligned}
$$
**Vastaus:** $v_\text{A} = +2{,}0\,\text{m/s}$ ja $v_\text{B} = -2{,}0\,\text{m/s}$. A kulkee $x$-akselin suuntaan ja B sitä vastaan. Tuloksissa on kaksi merkitsevää numeroa, kuten luetuissa arvoissa.
**Järkevyys:** Kumpikin kulkee $16\,\text{m}$ kahdeksassa sekunnissa. Vauhti on siis $2{,}0\,\text{m/s} = 7{,}2\,\text{km/h}$, mikä on reipasta kävelyä. Nopeuksien etumerkit ovat vastakkaiset. Se sopii tilanteeseen, jossa kulkijat tulevat toisiaan kohti.

### b)
**Annettu:** a-kohdasta $x_{0\text{A}} = 4\,\text{m}$, $v_\text{A} = 2{,}0\,\text{m/s}$, $x_{0\text{B}} = 20\,\text{m}$ ja $v_\text{B} = -2{,}0\,\text{m/s}$
**Kysytty:** paikat ajan funktiona ja kohtaamishetki $t$
**Periaate:** Tasaisessa liikkeessä paikka on $x = x_0 + v\,t$ (luku *Paikka, nopeus ja tasainen liike kuvaajina*). Kulkijat kohtaavat, kun heidän paikkansa ovat samat samalla hetkellä (luku *Kahden kappaleen liikkeiden vertailu*). Silloin kuvaajan suorat leikkaavat.
**Kaava:** $x_\text{A} = x_{0\text{A}} + v_\text{A}\,t$ ja $x_\text{B} = x_{0\text{B}} + v_\text{B}\,t$. Kohtaamisehto $x_\text{A} = x_\text{B}$ antaa $x_{0\text{A}} + v_\text{A}\,t = x_{0\text{B}} + v_\text{B}\,t$. Siitä saadaan $t\,(v_\text{A} - v_\text{B}) = x_{0\text{B}} - x_{0\text{A}}$ ja $t = \dfrac{x_{0\text{B}} - x_{0\text{A}}}{v_\text{A} - v_\text{B}}$
**Muunnokset:** Muunnoksia ei tarvita.
**Sijoitus:** Paikat ovat $x_\text{A} = 4\,\text{m} + 2{,}0\,\text{m/s} \cdot t$ ja $x_\text{B} = 20\,\text{m} - 2{,}0\,\text{m/s} \cdot t$. Kohtaamishetki: $$
\begin{aligned}
t &= \dfrac{20\,\text{m} - 4\,\text{m}}{2{,}0\,\text{m/s} - (-2{,}0\,\text{m/s})} \\
&= \dfrac{16\,\text{m}}{4{,}0\,\text{m/s}} \\
&= 4{,}0\,\text{s}
\end{aligned}
$$
**Vastaus:** Kulkijat kohtaavat hetkellä $t = 4{,}0\,\text{s}$. Tuloksessa on kaksi merkitsevää numeroa, kuten luetuissa arvoissa.
**Järkevyys:** Kulkijoiden välimatka alussa on $20\,\text{m} - 4\,\text{m} = 16\,\text{m}$. Välimatka pienenee nopeudella $$
\begin{aligned}
v &= 2{,}0\,\text{m/s} + 2{,}0\,\text{m/s} \\
&= 4{,}0\,\text{m/s}
\end{aligned}
$$. Siksi $16\,\text{m} : 4{,}0\,\text{m/s} = 4{,}0\,\text{s}$. Hetki on kuvaajan aikavälillä $0\ldots 8\,\text{s}$.

### c)
**Annettu:** a-kohdan yhtälö $x_\text{A} = 4\,\text{m} + 2{,}0\,\text{m/s} \cdot t$ ja b-kohdan hetki $t = 4{,}0\,\text{s}$
**Kysytty:** kohtaamispaikka $x$
**Periaate:** Kohtaamishetkellä kummankin paikka on sama. Siksi paikan voi laskea kummalla tahansa yhtälöllä.
**Kaava:** $x = x_{0\text{A}} + v_\text{A}\,t$
**Muunnokset:** Muunnoksia ei tarvita.
**Sijoitus:** $$
\begin{aligned}
x &= 4\,\text{m} + 2{,}0\,\text{m/s} \cdot 4{,}0\,\text{s} \\
&= 4\,\text{m} + 8{,}0\,\text{m} \\
&= 12\,\text{m}
\end{aligned}
$$
**Vastaus:** Kulkijat kohtaavat paikassa $x = 12\,\text{m}$. Tuloksessa on kaksi merkitsevää numeroa, kuten luetuissa arvoissa.
**Järkevyys:** Tarkistus B:n yhtälöllä: $x_\text{B} = 20\,\text{m} - 2{,}0\,\text{m/s} \cdot 4{,}0\,\text{s} = 12\,\text{m}$. Paikka on sama. Paikka on lähtöpaikkojen $4\,\text{m}$ ja $20\,\text{m}$ puolivälissä, koska nopeuksien suuruudet ovat samat.

### d)
**Kysytty:** miten kohtaamishetki ja kohtaamispaikka muuttuisivat, jos $v_\text{B} = -1{,}0\,\text{m/s}$
**Periaate:** Kohtaamisehto $x_\text{A} = x_\text{B}$ on sama kuin ennen. Vain B:n suora muuttuu. Se loivenee, koska B:n nopeuden suuruus pienenee. Suora lähtee silti pisteestä $20\,\text{m}$ (luku *Kahden kappaleen liikkeiden vertailu*).
**Mallivastaus:** Kuvaajassa B:n suora olisi loivempi ja laskisi hitaammin. Siksi se leikkaisi A:n suoran myöhemmin ja ylempänä. Lasketaan: ehto $$
\begin{aligned}
x_\text{A} &= x_\text{B} \\
4\,\text{m} + 2{,}0\,\text{m/s} \cdot t &= 20\,\text{m} \\
&\quad - 1{,}0\,\text{m/s} \cdot t
\end{aligned}
$$ antaa $t = \dfrac{x_{0\text{B}} - x_{0\text{A}}}{v_\text{A} - v_\text{B}}$, eli $$
\begin{aligned}
t &= \dfrac{20\,\text{m} - 4\,\text{m}}{2{,}0\,\text{m/s} - (-1{,}0\,\text{m/s})} \\
&= \dfrac{16\,\text{m}}{3{,}0\,\text{m/s}} \\
&\approx 5{,}3\,\text{s}
\end{aligned}
$$ Paikka on $$
\begin{aligned}
x &= 4\,\text{m} + 2{,}0\,\text{m/s} \cdot 5{,}33\,\text{s} \\
&\approx 4\,\text{m} + 10{,}7\,\text{m} \\
&\approx 14{,}7\,\text{m}
\end{aligned}
$$ Kohtaaminen tapahtuisi siis myöhemmin ($5{,}3\,\text{s} > 4{,}0\,\text{s}$). Se tapahtuisi lähempänä B:n alkupaikkaa ($14{,}7\,\text{m} > 12\,\text{m}$). Välimatka $16\,\text{m}$ pienenee nyt hitaammin, nopeudella $3{,}0\,\text{m/s}$ eikä $4{,}0\,\text{m/s}$. Siksi A ehtii kulkea pidemmälle ennen kohtaamista. Hetki $5{,}3\,\text{s}$ on yhä kuvaajan aikavälillä $0\ldots 8\,\text{s}$.

### Yleisiä virheitä
- B:n nopeuden etumerkki unohdetaan ($v_\text{B} = +2{,}0\,\text{m/s}$). Silloin yhtälöllä $4 + 2t = 20 + 2t$ ei ole ratkaisua, tai kohtaamishetki tulee väärin.
- Kohtaamishetki lasketaan jakamalla koko välimatka $16\,\text{m}$ vain toisen nopeudella ($16\,\text{m} : 2{,}0\,\text{m/s} = 8\,\text{s}$). Välimatka pienenee kuitenkin molempien nopeuksilla.
- Kohtaamispaikaksi merkitään kohtaamishetki tai matka, jonka A on kulkenut ($8{,}0\,\text{m}$). Paikkaan kuuluu kuitenkin myös alkupaikka $4\,\text{m}$.
- d-kohdassa oletetaan, että kulkijat kohtaisivat yhä samalla hetkellä tai välin keskellä. Nopeuksien suuruudet eivät kuitenkaan enää ole yhtä suuret.

### Hyväksytään myös
- b-kohdassa yhtälön $$
\begin{aligned}
x_\text{A} &= x_\text{B} \\
4\,\text{m} + 2{,}0\,\text{m/s} \cdot t &= 20\,\text{m} \\
&\quad - 2{,}0\,\text{m/s} \cdot t
\end{aligned}
$$ voi ratkaista suoraan: $4{,}0\,\text{m/s} \cdot t = 16\,\text{m}$.
- d-kohdassa kohtaamishetken voi laskea myös välimatkasta: $$
\begin{aligned}
t &= 16\,\text{m} : (2{,}0 + 1{,}0)\,\text{m/s} \\
&\approx 5{,}3\,\text{s}
\end{aligned}
$$.
