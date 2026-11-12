## fy9-moderni-s1

### a)
**Annettu:** cesiumin järjestysluku $55$, bariumin $56$, massaluku $137$, gammafotonin energia $E = 662\,\text{keV}$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$
**Kysytty:** hajoamisen ja purkautumisen yhtälöt sekä gammafotonin aallonpituus $\lambda$
**Periaate:** Beeta miinus -hajoamisessa ytimen neutroni muuttuu protoniksi, joten järjestysluku kasvaa yhdellä ja massaluku säilyy. Ydin lähettää elektronin ja antineutriinon. Virittynyt ydin purkautuu lähettämällä gammafotonin, eikä järjestysluku tai massaluku muutu (luku *Atomiydin ja radioaktiivinen hajoaminen*). Gammafotoni on valon tavoin fotoni, jonka energia ja aallonpituus liittyvät toisiinsa (luku *Valosähköinen ilmiö ja fotoni*).
**Kaava:** ${}^{137}_{55}\text{Cs} \to {}^{137}_{56}\text{Ba}^{\ast} + {}^{0}_{-1}\text{e} + \bar{\nu}$ ja ${}^{137}_{56}\text{Ba}^{\ast} \to {}^{137}_{56}\text{Ba} + \gamma$; $E = \dfrac{hc}{\lambda}$, joten $\lambda = \dfrac{hc}{E}$
**Muunnokset:** $662\,\text{keV} = 662 \cdot 1000 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 1{,}0605 \cdot 10^{-13}\,\text{J}$ ja lopuksi $1\,\text{pm} = 10^{-12}\,\text{m}$
**Sijoitus:** $\lambda = \dfrac{6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s}}{1{,}0605 \cdot 10^{-13}\,\text{J}} = 1{,}873 \cdot 10^{-12}\,\text{m} = 1{,}873\,\text{pm}$
**Vastaus:** Yhtälöt ovat yllä. Gammafotonin aallonpituus on $\lambda \approx 1{,}87\,\text{pm}$, kolme merkitsevää numeroa kuten energia $662\,\text{keV}$.
**Järkevyys:** Molemmissa yhtälöissä massaluvut ($137 = 137 + 0$) ja varausluvut ($55 = 56 - 1$) säilyvät. Aallonpituus on noin satakertaisesti pienempi kuin atomin halkaisija, kuten gammasäteilyllä pitää: näkyvän valon fotoni on noin $2\,\text{eV}$ ja aallonpituus noin $600\,\text{nm}$, ja $662\,000\,\text{eV}$ on noin $330\,000$-kertainen.

### b)
**Annettu:** $A_0 = 2400\,\tfrac{\text{Bq}}{\text{kg}}$ vuonna 1990, puoliintumisaika $T_{1/2} = 30{,}1\,\text{a}$, aikaa $t = 2026 - 1990 = 36\,\text{a}$
**Kysytty:** pitoisuus $A$ vuonna 2026
**Periaate:** Sienissä on valtava määrä cesiumytimiä, ja jokainen hajoaa samalla todennäköisyydellä. Siksi jäljellä olevien ytimien määrä ja aktiivisuus puolittuvat jokaisessa puoliintumisajassa (luku *Hajoamislaki ja puoliintumisaika*). Oletuksen mukaan cesiumia ei poistu muuten eikä tule lisää.
**Kaava:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Muunnokset:** Ajat ovat samassa yksikössä, joten muunnoksia ei tarvita.
**Sijoitus:** $\dfrac{t}{T_{1/2}} = \dfrac{36\,\text{a}}{30{,}1\,\text{a}} = 1{,}196$, joten $A = 2400\,\tfrac{\text{Bq}}{\text{kg}} \cdot 0{,}5^{1{,}196} = 1047{,}6\,\tfrac{\text{Bq}}{\text{kg}}$
**Vastaus:** $A \approx 1050\,\tfrac{\text{Bq}}{\text{kg}} = 1{,}05 \cdot 10^{3}\,\tfrac{\text{Bq}}{\text{kg}}$, kolme merkitsevää numeroa kuten puoliintumisaika.
**Järkevyys:** Aikaa on kulunut vähän yli yksi puoliintumisaika, joten pitoisuuden on oltava vähän alle puolet alkuperäisestä $1200\,\tfrac{\text{Bq}}{\text{kg}}$:sta. Tulos on sitä.

### c)
**Annettu:** pitoisuus $1047{,}6\,\tfrac{\text{Bq}}{\text{kg}}$ (b-kohta), syöty massa $m = 5{,}0\,\text{kg}$, annoskerroin $1{,}3 \cdot 10^{-8}\,\tfrac{\text{Sv}}{\text{Bq}}$, keskimääräinen vuosiannos $H_\text{v} = 5{,}9\,\text{mSv}$
**Kysytty:** efektiivinen annos $H$ ja sen osuus keskimääräisestä vuosiannoksesta
**Periaate:** Annoskerroin kertoo, kuinka suuren efektiivisen annoksen elimistöön joutunut becquerel aiheuttaa ennen kuin cesium poistuu elimistöstä. Syötyjen becquerelien määrä on pitoisuus kertaa massa (luku *Säteilyannos ja säteilyturvallisuus Suomessa*).
**Kaava:** $H = A_m \cdot m \cdot k_\text{annos}$, missä $A_m$ on pitoisuus ja $k_\text{annos}$ annoskerroin, ja osuus $= \dfrac{H}{H_\text{v}} = \dfrac{A_m \cdot m \cdot k_\text{annos}}{H_\text{v}}$
**Muunnokset:** Lopuksi $1\,\text{Sv} = 1000\,\text{mSv}$.
**Sijoitus:** Syödään $1047{,}6\,\tfrac{\text{Bq}}{\text{kg}} \cdot 5{,}0\,\text{kg} = 5238\,\text{Bq}$, joten $H = 5238\,\text{Bq} \cdot 1{,}3 \cdot 10^{-8}\,\tfrac{\text{Sv}}{\text{Bq}} = 6{,}81 \cdot 10^{-5}\,\text{Sv} = 6{,}81 \cdot 10^{-5} \cdot 1000\,\text{mSv} = 0{,}0681\,\text{mSv}$. Osuus on $0{,}0681\,\text{mSv} : 5{,}9\,\text{mSv} = 0{,}0115 = 1{,}15\,\%$.
**Vastaus:** Sienestäjä saa sienistä noin $0{,}068\,\text{mSv}$:n annoksen, kaksi merkitsevää numeroa kuten massa $5{,}0\,\text{kg}$ ja annoskerroin. Se on noin $1\,\%$ suomalaisen keskimääräisestä vuosiannoksesta.
**Järkevyys:** Annos vastaa noin seitsemää hammasröntgenkuvaa, joista kunkin annos on noin $0{,}01\,\text{mSv}$. Se on pieni verrattuna radonin noin $3\,\text{mSv}$:n keskimääräiseen osuuteen, mikä sopii siihen, että sienet ovat Suomessa vain pieni annoksen lähde.

### d)
**Annettu:** pitoisuus $A = 1047{,}6\,\text{Bq}$ yhdessä kilogrammassa (b-kohta), $T_{1/2} = 30{,}1\,\text{a}$, $1\,\text{a} = 3{,}156 \cdot 10^{7}\,\text{s}$, atomin massa $m_\text{a} = 137\,\text{u}$, $1\,\text{u} = 1{,}66 \cdot 10^{-27}\,\text{kg}$
**Kysytty:** cesium-137-ytimien lukumäärä $N$ ja niiden massa $m$
**Periaate:** Aktiivisuus on hajoamisvakion ja jäljellä olevien ytimien lukumäärän tulo, ja hajoamisvakio saadaan puoliintumisajasta (luku *Hajoamislaki ja puoliintumisaika*). Becquerel on yksi hajoaminen sekunnissa, joten puoliintumisaika muunnetaan sekunneiksi.
**Kaava:** $A = \lambda N$ ja $\lambda = \dfrac{\ln 2}{T_{1/2}}$, joten $N = \dfrac{A\,T_{1/2}}{\ln 2}$; $m = N\,m_\text{a}$
**Muunnokset:** $30{,}1\,\text{a} = 30{,}1 \cdot 3{,}156 \cdot 10^{7}\,\text{s} = 9{,}500 \cdot 10^{8}\,\text{s}$, $m_\text{a} = 137\,\text{u} = 137 \cdot 1{,}66 \cdot 10^{-27}\,\text{kg} = 2{,}274 \cdot 10^{-25}\,\text{kg}$ ja lopuksi $1\,\text{kg} = 10^{12}\,\text{ng}$
**Sijoitus:** $N = \dfrac{1047{,}6\,\tfrac{1}{\text{s}} \cdot 9{,}500 \cdot 10^{8}\,\text{s}}{0{,}6931} = 1{,}436 \cdot 10^{12}$ ja $m = 1{,}436 \cdot 10^{12} \cdot 2{,}274 \cdot 10^{-25}\,\text{kg} = 3{,}27 \cdot 10^{-13}\,\text{kg} = 0{,}327\,\text{ng}$
**Vastaus:** Kilogrammassa sieniä on noin $1{,}44 \cdot 10^{12}$ cesium-137-ydintä, joiden massa on noin $0{,}327\,\text{ng}$, kolme merkitsevää numeroa kuten puoliintumisaika.
**Järkevyys:** Ytimiä on biljoonia, mutta massa on alle nanogramman, koska yksittäinen atomi on hyvin kevyt. Hajoamisvakio $\lambda = 7{,}30 \cdot 10^{-10}\,\tfrac{1}{\text{s}}$ on pieni, joten tuhat hajoamista sekunnissa vaatii valtavan ydinjoukon.

### Yleisiä virheitä
- a-kohdassa beeta miinus -hajoamisessa järjestysluku pienennetään tai massaluku muutetaan, tai antineutriino unohdetaan.
- a-kohdassa energia sijoitetaan kiloelektronivoltteina kaavaan, jossa $h$ on jouleina.
- b-kohdassa aktiivisuus puolitetaan vain kerran, koska aikaa on ”noin yksi puoliintumisaika”, tai vähennetään lineaarisesti.
- c-kohdassa unohdetaan kertoa massalla tai muunnetaan sievertit millisieverteiksi väärään suuntaan.
- d-kohdassa puoliintumisaika sijoitetaan vuosina, jolloin ytimiä saadaan $3{,}2 \cdot 10^{7}$-kertaisesti liian vähän (vuoden sekuntimäärä).

## fy9-moderni-s2

### a)
**Annettu:** $E_n = -\tfrac{E_0}{n^2}$, $E_0 = 13{,}6\,\text{eV}$, siirtymä tasolta $3$ tasolle $2$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$
**Kysytty:** viivan aallonpituus $\lambda$
**Periaate:** Kun elektroni siirtyy ylemmältä tasolta alemmalle, atomi lähettää fotonin, jonka energia on tasojen erotus, koska energia säilyy (luku *Vetyatomin energiatasot ja Bohrin malli*). Fotonin energiasta saadaan aallonpituus (luku *Valosähköinen ilmiö ja fotoni*).
**Kaava:** $E_\text{f} = E_3 - E_2 = E_0\left(\tfrac{1}{2^2} - \tfrac{1}{3^2}\right)$ ja $E_\text{f} = \dfrac{hc}{\lambda}$, joten $\lambda = \dfrac{hc}{E_0\left(\tfrac{1}{2^2} - \tfrac{1}{3^2}\right)}$
**Muunnokset:** $1{,}8889\,\text{eV} = 1{,}8889 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 3{,}0260 \cdot 10^{-19}\,\text{J}$ ja lopuksi $1\,\text{nm} = 10^{-9}\,\text{m}$
**Sijoitus:** $E_3 - E_2 = 13{,}6\,\text{eV} \cdot \left(\tfrac{1}{4} - \tfrac{1}{9}\right) = 13{,}6\,\text{eV} \cdot \tfrac{5}{36} = 1{,}8889\,\text{eV}$, joten $\lambda = \dfrac{6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s}}{3{,}0260 \cdot 10^{-19}\,\text{J}} = 6{,}565 \cdot 10^{-7}\,\text{m} = 656{,}5\,\text{nm}$
**Vastaus:** $\lambda \approx 656\,\text{nm}$, kolme merkitsevää numeroa kuten $13{,}6\,\text{eV}$.
**Järkevyys:** Tulos poikkeaa laboratorioarvosta $656{,}3\,\text{nm}$ vain $0{,}03\,\%$, ja $1{,}9\,\text{eV}$:n fotoni on punaista valoa, kuten viivan nimi kertoo.

### b)
**Annettu:** laboratorioarvo $\lambda_0 = 656{,}3\,\text{nm}$, havaittu $\lambda = 671{,}8\,\text{nm}$, $c = 2{,}998 \cdot 10^{5}\,\text{km/s}$, $H_0 = 70\,\tfrac{\text{km/s}}{\text{Mpc}}$
**Kysytty:** etääntymisnopeus $v$ ja etäisyys $d$
**Periaate:** Avaruus laajenee, ja kaukaiset galaksit etääntyvät meistä. Siksi niiden valon aallonpituus on venynyt, ja punasiirtymä $z$ kertoo, kuinka paljon. Kun $z$ on pieni, etääntymisnopeus on $v = cz$. Hubblen lain mukaan nopeus on suoraan verrannollinen etäisyyteen (luku *Maailmankaikkeuden kehitys*).
**Kaava:** $z = \dfrac{\lambda - \lambda_0}{\lambda_0}$, $v = cz$ ja $v = H_0 d$, joten $d = \dfrac{v}{H_0}$
**Muunnokset:** Aallonpituudet ovat samassa yksikössä, ja nopeudet ovat yksikössä $\tfrac{\text{km}}{\text{s}}$, joten muunnoksia ei tarvita.
**Sijoitus:** $z = \dfrac{671{,}8\,\text{nm} - 656{,}3\,\text{nm}}{656{,}3\,\text{nm}} = \dfrac{15{,}5\,\text{nm}}{656{,}3\,\text{nm}} = 0{,}02362$, $v = 2{,}998 \cdot 10^{5}\,\text{km/s} \cdot 0{,}02362 = 7080\,\text{km/s}$ ja $d = \dfrac{7080\,\text{km/s}}{70\,\tfrac{\text{km/s}}{\text{Mpc}}} = 101{,}1\,\text{Mpc}$
**Vastaus:** Galaksi etääntyy nopeudella $v \approx 7080\,\text{km/s}$, kolme merkitsevää numeroa kuten aallonpituuksien erotus $15{,}5\,\text{nm}$. Se on noin $1{,}0 \cdot 10^{2}\,\text{Mpc}$:n etäisyydellä, kaksi merkitsevää numeroa kuten Hubblen vakio.
**Järkevyys:** Nopeus on noin $2\,\%$ valon nopeudesta, joten $v = cz$ pätee. $100\,\text{Mpc}$ on noin $330$ miljoonaa valovuotta, mikä on lähigalaksien joukkoja kauempana mutta vielä kaukoputkella helposti havaittava etäisyys.

### c)
**Annettu:** syaanin viivan laboratorioarvo $\lambda_0 = 486{,}1\,\text{nm}$, punasiirtymä $z = 0{,}02362$ (b-kohta)
**Kysytty:** havaittu aallonpituus $\lambda$
**Periaate:** Avaruuden laajeneminen venyttää kaikkia aallonpituuksia samassa suhteessa, joten punasiirtymä on sama jokaiselle spektrin viivalle (luku *Maailmankaikkeuden kehitys*).
**Kaava:** $z = \dfrac{\lambda - \lambda_0}{\lambda_0}$, joten $\lambda = \lambda_0(1 + z)$
**Muunnokset:** Aallonpituus pysyy nanometreinä, joten muunnoksia ei tarvita.
**Sijoitus:** $\lambda = 486{,}1\,\text{nm} \cdot (1 + 0{,}02362) = 497{,}58\,\text{nm}$
**Vastaus:** $\lambda \approx 497{,}6\,\text{nm}$, neljä merkitsevää numeroa kuten laboratorioarvo, koska siirtymä $z$ tunnetaan kolmen numeron tarkkuudella ja se muuttaa vain viimeisiä numeroita.
**Järkevyys:** Siirtymä $11{,}5\,\text{nm}$ on pienempi kuin punaisen viivan $15{,}5\,\text{nm}$, koska lyhyempi aallonpituus venyy samassa suhteessa vähemmän nanometrejä. Laskettu laboratorioarvo $13{,}6\,\text{eV}\left(\tfrac{1}{4} - \tfrac{1}{16}\right)$ antaa $486{,}3\,\text{nm}$, joten tasot ja syaanin viiva sopivat yhteen.

### d)
**Kysytty:** miksi vedyn viivat näkyvät galaksin spektrissä tummina
**Periaate:** Kuuma, tiheä kappale lähettää jatkuvan spektrin. Harva kaasu absorboi vain fotoneja, joiden energia on täsmälleen kahden energiatason erotus (luvut *Spektrit paljastavat atomin energiatasot* ja *Vetyatomin energiatasot ja Bohrin malli*).
**Mallivastaus:** Galaksin valo on sen tähtien valoa. Tähden kuuma, tiheä pinta lähettää jatkuvan spektrin, jossa on kaikkia aallonpituuksia. Valo kulkee tähden uloimpien, harvempien ja viileämpien kaasukerrosten läpi, ja niissä on vetyä. Vetyatomi absorboi fotonin vain, jos fotonin energia on täsmälleen kahden energiatason erotus, esimerkiksi $E_3 - E_2 = 1{,}89\,\text{eV}$ punaiselle viivalle. Atomi virittyy ja purkautuu pian lähettämällä samanlaisen fotonin, mutta satunnaiseen suuntaan. Siksi meidän suuntaamme tulee näillä aallonpituuksilla vähemmän valoa kuin viereisillä, ja viivat näkyvät tummina absorptioviivoina. Kirkkaita viivoja nähtäisiin, jos katsottaisiin harvaa kuumaa kaasua ilman sen takana olevaa jatkuvaa spektriä, kuten kaasupurkausputkessa.

### Yleisiä virheitä
- a-kohdassa lasketaan yhden tason energia, esimerkiksi $|E_3| = 1{,}51\,\text{eV}$, eikä tasojen erotusta.
- a-kohdassa elektronivoltit sijoitetaan kaavaan jouleina olevan $h$:n kanssa, jolloin aallonpituudeksi tulee noin $10^{-25}\,\text{m}$, noin $10^{19}$ kertaa liian pieni arvo.
- b-kohdassa punasiirtymä lasketaan jakamalla havaitulla aallonpituudella tai unohdetaan jakaa, jolloin $z = 15{,}5$.
- b-kohdassa nopeus sijoitetaan metreinä sekunnissa Hubblen lakiin, jossa $H_0$ on yksikössä $\tfrac{\text{km/s}}{\text{Mpc}}$.
- c-kohdassa syaaniin lisätään sama $15{,}5\,\text{nm}$ kuin punaiseen viivaan, vaikka sama on suhteellinen muutos.
- d-kohdassa viivojen sanotaan olevan tummia, koska galaksi on kaukana tai koska punasiirtymä tummentaa ne.

### Hyväksytään myös
- c-kohdassa suhteella $\lambda = 486{,}1\,\text{nm} \cdot \dfrac{671{,}8}{656{,}3} = 497{,}6\,\text{nm}$, koska $1 + z$ on havaitun ja laboratorioarvon suhde.

## fy9-moderni-s3

### a)
**Kysytty:** pysäytysjännite $U$ valon taajuuden $f$ funktiona kuvaajana
**Kuvaaja:** Taajuus lasketaan aallonpituudesta, $f = \tfrac{c}{\lambda}$: esimerkiksi $\tfrac{2{,}998 \cdot 10^{8}\,\text{m/s}}{365 \cdot 10^{-9}\,\text{m}} = 8{,}214 \cdot 10^{14}\,\text{Hz}$. Taajuudet ovat $8{,}214$, $7{,}402$, $6{,}876$, $6{,}379$ ja $5{,}937$ kertaa $10^{14}\,\text{Hz}$ aallonpituuksille $365$–$505\,\text{nm}$. Vaaka-akselilla on $f\ (10^{14}\,\text{Hz})$ ja pystyakselilla $U\ (\text{V})$. Aallonpituudelle $590\,\text{nm}$ ei piirretä pistettä, koska valovirtaa ei synny lainkaan, joten pysäytysjännitettä ei ole. Pisteitä ei yhdistetä murtoviivaksi.

<svg data-fig="fy9-moderni-s3-p" viewBox="0 0 600 400" role="img" aria-label="Kuvaaja: pysäytysjännite U voltteina valon taajuuden f funktiona, taajuusakselin yksikkö 10 potenssiin 14 hertsiä. Vaaka-akseli alkaa arvosta 5,0 ja päättyy arvoon 8,5, pystyakseli nollasta 1,4 volttiin. Viisi mustaa pistettä taajuuksilla 5,94–8,21 ja jännitteillä 0,21–1,15 volttia nousevat tasaisesti ja asettuvat likimain samalle suoralle." style="max-width:100%;font-size:28px">
  <line x1="143.5" y1="340" x2="143.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="187" y1="340" x2="187" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="340" x2="230.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="274.5" y1="340" x2="274.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="318" y1="340" x2="318" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="361.5" y1="340" x2="361.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="405" y1="340" x2="405" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="301" x2="405" y2="301" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="261.5" x2="405" y2="261.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="222.5" x2="405" y2="222.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="183.5" x2="405" y2="183.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="144.5" x2="405" y2="144.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="105" x2="405" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="66" x2="405" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="340" x2="419" y2="340" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M431,340 L418,346 L418,334 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="341" x2="100" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,40 L106,53 L94,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="143.5" y1="340" x2="143.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="187" y1="340" x2="187" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="161" y="347" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$6{,}0$</div></foreignObject>
  <line x1="230.5" y1="340" x2="230.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="274.5" y1="340" x2="274.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="248.5" y="347" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$7{,}0$</div></foreignObject>
  <line x1="318" y1="340" x2="318" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="361.5" y1="340" x2="361.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="335.5" y="347" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$8{,}0$</div></foreignObject>
  <line x1="405" y1="340" x2="405" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="301" x2="100" y2="301" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="261.5" x2="100" y2="261.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="36" y="244.5" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$0{,}4$</div></foreignObject>
  <line x1="93" y1="222.5" x2="100" y2="222.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="183.5" x2="100" y2="183.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="36" y="166.5" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$0{,}8$</div></foreignObject>
  <line x1="93" y1="144.5" x2="100" y2="144.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="105" x2="100" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="36" y="88" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$1{,}2$</div></foreignObject>
  <line x1="93" y1="66" x2="100" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="437" y="323" width="158" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$f\ (10^{14}\,\text{Hz})$</div></foreignObject>
  <foreignObject x="90" y="7" width="71" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$U\ (\text{V})$</div></foreignObject>
  <circle cx="380" cy="115" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="309.5" cy="183.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="263.5" cy="220.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="220" cy="265.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="181.5" cy="299" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
</svg>

**Mallivastaus:** Pisteet nousevat tasaisesti taajuuden kasvaessa ja asettuvat likimain samalle suoralle. Suurempi taajuus antaa suuremman pysäytysjännitteen, eli elektronit irtoavat suuremmalla liike-energialla.

### b)
**Kysytty:** perustelu sille, että pisteisiin sopii suora, sovitettu suora ja sen jatke akseleille
**Kuvaaja:** Yksi fotoni luovuttaa koko energiansa $hf$ yhdelle elektronille. Osa energiasta kuluu irrotustyöhön $W$, ja nopeimmalle elektronille jää liike-energia $E_\text{k,max} = hf - W$ (luku *Valosähköinen ilmiö ja fotoni*). Kun anodi on katodia negatiivisempi, sähkökenttä jarruttaa elektronia, ja sen liike-energia muuttuu sähköiseksi potentiaalienergiaksi. Virta lakkaa, kun nopeinkin elektroni pysähtyy juuri ennen anodia: $eU = E_\text{k,max}$ (luku *Potentiaalienergia ja potentiaali sähkökentässä*). Yhdistämällä saadaan $eU = hf - W$ eli $U = \tfrac{h}{e}\,f - \tfrac{W}{e}$, joten $U$ on taajuuden lineaarinen funktio, jonka kulmakerroin on $\tfrac{h}{e}$ ja vakiotermi $-\tfrac{W}{e}$. Suora sovitetaan pisteiden lomitse ja jatketaan katkoviivana pystyakselille asti, koska vakiotermi tarvitaan irrotustyön määrittämiseen (luku *Graafinen esitys ja suoran sovittaminen*).

<svg data-fig="fy9-moderni-s3-fit" viewBox="0 0 600 470" role="img" aria-label="Kuvaaja: pysäytysjännite U voltteina valon taajuuden f funktiona, taajuusakseli nollasta 9 kertaa 10 potenssiin 14 hertsiin ja jänniteakseli miinus 2,5:stä plus 1,5 volttiin. Viiteen pisteeseen on sovitettu nouseva suora, jota on jatkettu katkoviivana pystyakselille asti. Suora leikkaa pystyakselin noin arvossa miinus 2,24 volttia ja vaaka-akselin noin kohdassa 5,43 kertaa 10 potenssiin 14 hertsiä. Suoralta on ympyröity lukemiseen käytetyt pisteet nolla ja miinus 2,24 volttia sekä 8,0 kertaa 10 potenssiin 14 hertsiä ja 1,06 volttia." style="max-width:100%;font-size:28px">
  <line x1="130.5" y1="410" x2="130.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="164.5" y1="410" x2="164.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="199" y1="410" x2="199" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="233.5" y1="410" x2="233.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="267.5" y1="410" x2="267.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="302" y1="410" x2="302" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336.5" y1="410" x2="336.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370.5" y1="410" x2="370.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="405" y1="410" x2="405" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="367.5" x2="405" y2="367.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="325" x2="405" y2="325" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="282.5" x2="405" y2="282.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="240" x2="405" y2="240" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="155" x2="405" y2="155" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="112.5" x2="405" y2="112.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="70" x2="405" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="410" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="197.5" x2="419" y2="197.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M431,197.5 L418,203.5 L418,191.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="198.5" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="130.5" y1="197.5" x2="130.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="164.5" y1="197.5" x2="164.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="199" y1="197.5" x2="199" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="233.5" y1="197.5" x2="233.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="267.5" y1="197.5" x2="267.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="302" y1="197.5" x2="302" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="336.5" y1="197.5" x2="336.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="370.5" y1="197.5" x2="370.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="405" y1="197.5" x2="405" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="410" x2="96" y2="410" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="367.5" x2="96" y2="367.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="350.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$-2$</div></foreignObject>
  <line x1="89" y1="325" x2="96" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="282.5" x2="96" y2="282.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="265.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$-1$</div></foreignObject>
  <line x1="89" y1="240" x2="96" y2="240" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="61" y="180.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$0$</div></foreignObject>
  <line x1="89" y1="155" x2="96" y2="155" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="112.5" x2="96" y2="112.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="61" y="95.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$1$</div></foreignObject>
  <line x1="89" y1="70" x2="96" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="437" y="180.5" width="158" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$f\ (10^{14}\,\text{Hz})$</div></foreignObject>
  <foreignObject x="86" y="11" width="71" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$U\ (\text{V})$</div></foreignObject>
  <foreignObject x="153" y="204.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$2$</div></foreignObject>
  <foreignObject x="222" y="204.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$4$</div></foreignObject>
  <foreignObject x="290.5" y="204.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$6$</div></foreignObject>
  <foreignObject x="359" y="204.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$8$</div></foreignObject>
  <polyline points="291,188.5 388.5,89.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,388 291,188.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="378" cy="100" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="350" cy="129.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332" cy="145.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="315" cy="165" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="300" cy="179.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="96" cy="388" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="370.5" cy="107.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="370.5" y1="107.5" x2="370.5" y2="410" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="107.5" x2="370.5" y2="107.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="282.5" cy="197.5" r="6" fill="#2b8a3e"/>
  <foreignObject x="252.5" y="253" width="226" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$f_0 \approx 5{,}43 \cdot 10^{14}\,\text{Hz}$</span></div></foreignObject>
  <foreignObject x="108" y="371" width="154" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$-\tfrac{W}{e} \approx -2{,}24\,\text{V}$</span></div></foreignObject>
  <foreignObject x="247" y="299.5" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$k = \tfrac{h}{e}$</div></foreignObject>
</svg>

**Mallivastaus:** Mallin $U = \tfrac{h}{e}\,f - \tfrac{W}{e}$ mukaan pisteiden pitää olla suoralla, ja ne ovatkin noin $0{,}01\,\text{V}$:n tarkkuudella samalla suoralla. Sovitettu suora leikkaa pystyakselin noin kohdassa $-2{,}24\,\text{V}$ ja vaaka-akselin noin kohdassa $5{,}43 \cdot 10^{14}\,\text{Hz}$. Suoran jatke negatiivisiin jännitteisiin on vain matemaattinen apu: rajataajuutta pienemmillä taajuuksilla elektroneja ei irtoa lainkaan.

### c)
**Annettu:** b-kohdan sovitettu suora, $e = 1{,}602 \cdot 10^{-19}\,\text{C}$
**Kysytty:** Planckin vakio $h$ ja sen vertailu arvoon $6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$
**Periaate:** Mallin $U = \tfrac{h}{e}\,f - \tfrac{W}{e}$ mukaan suoran kulmakerroin on $k = \tfrac{h}{e}$. Kulmakerroin luetaan kahdesta kaukana toisistaan olevasta sovitetun suoran pisteestä eikä mittauspisteistä (luku *Graafinen esitys ja suoran sovittaminen*).
**Kuvaajan lukeminen:** Suoralta luetaan pisteet $(0;\ -2{,}24\,\text{V})$ ja $(8{,}0 \cdot 10^{14}\,\text{Hz};\ 1{,}06\,\text{V})$.
**Kaava:** $k = \dfrac{\Delta U}{\Delta f}$ ja $k = \dfrac{h}{e}$, joten $h = ek$
**Muunnokset:** $1\,\text{C} \cdot 1\,\text{V} \cdot 1\,\text{s} = 1\,\text{J}\,\text{s}$, koska $1\,\text{V} = 1\,\tfrac{\text{J}}{\text{C}}$ ja $\tfrac{1}{\text{Hz}} = 1\,\text{s}$.
**Sijoitus:** $k = \dfrac{1{,}06\,\text{V} - (-2{,}24\,\text{V})}{8{,}0 \cdot 10^{14}\,\text{Hz} - 0} = \dfrac{3{,}30\,\text{V}}{8{,}0 \cdot 10^{14}\,\tfrac{1}{\text{s}}} = 4{,}125 \cdot 10^{-15}\,\text{V}\,\text{s}$, joten $h = 1{,}602 \cdot 10^{-19}\,\text{C} \cdot 4{,}125 \cdot 10^{-15}\,\text{V}\,\text{s} = 6{,}608 \cdot 10^{-34}\,\text{J}\,\text{s}$
**Vastaus:** $h \approx 6{,}61 \cdot 10^{-34}\,\text{J}\,\text{s}$, kolme merkitsevää numeroa, koska jännitteet luetaan kuvaajalta noin sadasosavoltin tarkkuudella. Tulos on $0{,}3\,\%$ pienempi kuin taulukkoarvo $6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$.
**Järkevyys:** Ero on paljon pienempi kuin lukemisen epävarmuus, noin $1\,\%$, joten mittaus tukee mallia. Kulmakerroin ei riipu katodin aineesta, joten mikä tahansa metalli antaisi saman $h$:n.

### d)
**Annettu:** b-kohdan suora, joka leikkaa pystyakselin kohdassa $b = -2{,}24\,\text{V}$, kulmakerroin $k = 4{,}125 \cdot 10^{-15}\,\text{V}\,\text{s}$ (c-kohta), $\lambda = 590\,\text{nm}$
**Kysytty:** irrotustyö $W$ elektronivoltteina, rajataajuus $f_0$ ja selitys aallonpituuden $590\,\text{nm}$ tulokselle
**Periaate:** Suoran vakiotermi on $-\tfrac{W}{e}$, joten irrotustyö elektronivoltteina on vakiotermin itseisarvo. Rajataajuudella fotonin energia riittää juuri irrotustyöhön, ja $U = 0$, joten se on suoran ja vaaka-akselin leikkauskohta. Valon intensiteetti muuttaa vain fotonien määrää, ei yhden fotonin energiaa (luku *Valosähköinen ilmiö ja fotoni*).
**Kuvaajan lukeminen:** Suora leikkaa pystyakselin kohdassa $-2{,}24\,\text{V}$ ja vaaka-akselin noin kohdassa $5{,}43 \cdot 10^{14}\,\text{Hz}$.
**Kaava:** $b = -\dfrac{W}{e}$, joten $W = -e\,b$; $hf_0 = W$, joten $f_0 = \dfrac{W}{h} = -\dfrac{b}{k}$, koska $k = \dfrac{h}{e}$; $f = \dfrac{c}{\lambda}$ ja $E = hf$
**Muunnokset:** $e \cdot 1\,\text{V} = 1\,\text{eV}$, joten $W = 2{,}24\,\text{eV}$ suoraan. Aallonpituus $590\,\text{nm} = 590 \cdot 10^{-9}\,\text{m}$, ja energia muunnetaan elektronivolteiksi jakamalla luvulla $1{,}602 \cdot 10^{-19}\,\tfrac{\text{J}}{\text{eV}}$.
**Sijoitus:** $W = -e \cdot (-2{,}24\,\text{V}) = 2{,}24\,\text{eV}$ ja $f_0 = -\dfrac{-2{,}24\,\text{V}}{4{,}125 \cdot 10^{-15}\,\text{V}\,\text{s}} = 5{,}43 \cdot 10^{14}\,\text{Hz}$. Aallonpituudella $590\,\text{nm}$: $f = \dfrac{2{,}998 \cdot 10^{8}\,\text{m/s}}{590 \cdot 10^{-9}\,\text{m}} = 5{,}08 \cdot 10^{14}\,\text{Hz}$ ja $E = \dfrac{6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 5{,}08 \cdot 10^{14}\,\tfrac{1}{\text{s}}}{1{,}602 \cdot 10^{-19}\,\tfrac{\text{J}}{\text{eV}}} = 2{,}10\,\text{eV}$
**Vastaus:** Kaliumin irrotustyö on $W \approx 2{,}24\,\text{eV}$ ja rajataajuus $f_0 \approx 5{,}43 \cdot 10^{14}\,\text{Hz}$, kolme merkitsevää numeroa kuvaajan lukutarkkuuden mukaan. Aallonpituuden $590\,\text{nm}$ valon taajuus $5{,}08 \cdot 10^{14}\,\text{Hz}$ on rajataajuutta pienempi, eli yhden fotonin energia $2{,}10\,\text{eV}$ ei riitä irrottamaan elektronia. Kymmenkertainen valomäärä tarkoittaa kymmenkertaista määrää samanlaisia fotoneja. Yksi fotoni luovuttaa energiansa yhdelle elektronille, joten elektroneja ei irtoa edelleenkään, eikä valovirtaa synny.
**Järkevyys:** Rajataajuutta vastaa aallonpituus $\tfrac{c}{f_0} \approx 552\,\text{nm}$, vihreää valoa, joten keltainen $590\,\text{nm}$:n valo on rajan väärällä puolella ja kaikki mitatut violetit ja siniset aallonpituudet oikealla puolella, kuten taulukossa. Alkalimetallien irrotustyöt ovat noin $2\,\text{eV}$, joten tulos on uskottava.

### Yleisiä virheitä
- a-kohdassa vaaka-akselille piirretään aallonpituus, jolloin pisteet eivät ole suoralla, tai pisteet yhdistetään murtoviivaksi.
- a-kohdassa aallonpituudelle $590\,\text{nm}$ piirretään piste $U = 0$, vaikka virtaa ei synny lainkaan.
- b-kohdassa suora pakotetaan origon kautta, jolloin irrotustyötä ei voi määrittää.
- c-kohdassa kulmakerroin luetaan kahdesta mittauspisteestä eikä sovitetusta suorasta, tai $10^{14}$ unohdetaan, jolloin $h \approx 6{,}6 \cdot 10^{-20}\,\text{J}\,\text{s}$.
- d-kohdassa irrotustyö ilmoitetaan negatiivisena tai jouleina, vaikka kysytään elektronivoltteja.
- d-kohdassa väitetään, että kirkkaampi valo irrottaa elektroneja, koska energiaa on enemmän.

### Hyväksytään myös
- c-kohdassa laskimen tai taulukkolaskennan sovitus: $k = 4{,}13 \cdot 10^{-15}\,\text{V}\,\text{s}$, $h = 6{,}61 \cdot 10^{-34}\,\text{J}\,\text{s}$ ja vakiotermi $-2{,}24\,\text{V}$.
- d-kohdassa rajataajuus suoran yhtälöstä $f_0 = \tfrac{W}{h}$ c-kohdan arvolla tai suoraan vaaka-akselin leikkauskohdasta.

## fy9-moderni-s4

### a)
**Kysytty:** pitääkö väite 1 paikkansa ja miten radon aiheuttaa säteilyannoksen
**Periaate:** Alfahiukkanen on raskas ja kaksinkertaisesti varattu, joten se ionisoi tiheästi ja menettää energiansa lyhyellä matkalla: ilmassa muutamassa senttimetrissä ja kudoksessa alle kymmenesosamillimetrissä. Ulkopuolinen alfasäteily pysähtyy ihon kuolleeseen pintakerrokseen, mutta elimistön sisällä alfahiukkanen osuu suoraan eläviin soluihin. Siksi sen säteilyn painotuskerroin on $20$ (luku *Ionisoiva säteily ja elimistö*). Radon on kaasu, ja sen lyhytikäiset hajoamistuotteet ovat kiinteitä aineita, jotka tarttuvat ilman pölyhiukkasiin (luku *Säteilyannos ja säteilyturvallisuus Suomessa*).
**Mallivastaus:** Väitteen ensimmäinen osa pitää paikkansa: radonin alfasäteily ei läpäise paperia eikä ihoa, joten huoneen ilmassa oleva radon ei säteilytä ihoa vaarallisesti ulkopuolelta. Johtopäätös on silti väärä. Radon ja sen hajoamistuotteet, poloniumin, lyijyn ja vismutin isotoopit, hengitetään keuhkoihin, ja hajoamistuotteet tarttuvat keuhkoputkien pintaan. Siellä niiden alfahiukkaset osuvat suoraan keuhkojen soluihin. Alfahiukkanen luovuttaa koko energiansa, useita megaelektronivoltteja, muutaman solun matkalle ja voi katkaista DNA:n molemmat juosteet. Siksi saman absorboituneen annoksen ekvivalenttiannos on $20$-kertainen fotonisäteilyyn verrattuna. Radon on Suomessa suurin yksittäinen säteilyannoksen lähde ja tupakoinnin jälkeen yleisin keuhkosyövän aiheuttaja. Asunnon $450\,\tfrac{\text{Bq}}{\text{m}^3}$ ylittää viitearvon $300\,\tfrac{\text{Bq}}{\text{m}^3}$ $1{,}5$-kertaisesti, joten korjaustoimet kannattavat.

### b)
**Kysytty:** pitääkö väite 2 paikkansa, kuinka suuri osa radonytimistä on hajoamatta kuukauden kuluttua ja häviääkö radon
**Periaate:** Suuri joukko radonytimiä hajoaa hajoamislain mukaan, ja jäljellä oleva osuus on $\left(\tfrac{1}{2}\right)^{t/T_{1/2}}$ (luku *Hajoamislaki ja puoliintumisaika*). Laki koskee vain ytimiä, jotka ovat huoneessa alussa. Uusia radonytimiä syntyy jatkuvasti maaperän uraanin hajoamissarjassa radiumista, ja niitä virtaa sisään perustusten raoista (luku *Säteilyannos ja säteilyturvallisuus Suomessa*).
**Mallivastaus:** Kuukaudessa, $30\,\text{vrk}$, on $\tfrac{30\,\text{vrk}}{3{,}8\,\text{vrk}} = 7{,}89$ puoliintumisaikaa, joten huoneessa alussa olleista radonytimistä on jäljellä $\left(\tfrac{1}{2}\right)^{7{,}89} = 0{,}0042$, eli noin $0{,}4\,\%$. Laskelma on oikein, mutta väite on silti väärä. Radonin emoaine radium-226, jonka puoliintumisaika on noin $1600$ vuotta, ja hajoamissarjan alku uraani-238 ovat maaperässä ja kalliossa, joten radonia syntyy koko ajan uudelleen. Kun lämmin sisäilma nousee ylös ja poistuu, talon alaosaan syntyy alipaine, joka imee maaperän radonpitoista ilmaa perustusten raoista sisään. Kun ikkunat ovat kiinni, radonia hajoaa ja tulee sisään yhtä paljon, ja pitoisuus asettuu korkealle tasolle. Tiiviisti suljetussa asunnossa pitoisuus yleensä kasvaa, koska ilma vaihtuu vähemmän. Pitoisuutta pienennetään tehostamalla ilmanvaihtoa, tiivistämällä perustusten raot ja asentamalla radonimuri, joka imee ilman talon alta ulos.

### c)
**Kysytty:** pitääkö väite 3 paikkansa
**Periaate:** Radioaktiivisuus on epävakaiden ytimien ominaisuus: ydin hajoaa ja lähettää säteilyä. Röntgensäteily on fotonisäteilyä, joka syntyy röntgenputkessa vain, kun putkessa on jännite (luku *Säteily lääketieteessä ja teknologiassa*). Röntgenfotonin energia, noin $60\,\text{keV}$, riittää ionisoimaan atomeja, mutta on liian pieni muuttamaan ytimiä (luku *Ionisoiva säteily ja elimistö*).
**Mallivastaus:** Väite on väärä. Hammasröntgenissä naapuria säteilytettiin hetken ulkoisella röntgensäteilyllä. Jokainen fotoni joko kulki kudoksen läpi kuvalevylle tai absorboitui ja ionisoi atomin kuvauksen aikana. Fotoneja ei jää elimistöön, eikä niiden energia, noin $60\,\text{keV}$, riitä muuttamaan atomiytimiä epävakaiksi, sillä ytimen hiukkasten sidosenergiat ovat megaelektronivolttien luokkaa. Kun laite sammuu, säteilyä ei enää ole, ja naapuri on säteilyn kannalta täsmälleen samanlainen kuin ennen. Ihminen voi olla hetkellisesti säteilylähde vain, jos hänen elimistöönsä viedään radioaktiivista ainetta, kuten isotooppitutkimuksen merkkiainetta tai kilpirauhasen jodihoidossa. Silloin ohjeet annetaan sairaalassa. Lasten ei siis tarvitse välttää naapuria. Hammasröntgenkuvan annos, noin $0{,}01\,\text{mSv}$, on lisäksi pieni verrattuna asunnon radonin annokseen.

### Yleisiä virheitä
- a-kohdassa alfasäteilyn sanotaan olevan vaaratonta tai vaarallista ilman, että erotetaan ulkoinen säteily ja hengitetyt hajoamistuotteet.
- b-kohdassa lasketaan, että kuukaudessa puolittuu kerran tai että $2 \cdot 3{,}8\,\text{vrk}$:ssa kaikki hajoaa.
- b-kohdassa todetaan, että radon häviää, koska laskelma antaa alle $1\,\%$, eikä huomata, että radonia syntyy koko ajan lisää.
- c-kohdassa sekoitetaan säteily ja radioaktiivinen aine tai väitetään, että röntgensäteily ”jää kehoon”.

## fy9-moderni-s5

### a)
**Annettu:** pulssimäärät $10\,\text{s}$:n jaksoissa ajanhetkillä $0$–$300\,\text{s}$ ($11$ lukemaa), alussa $398$ ja lopussa $104$, tausta $5$ pulssia $10\,\text{s}$:ssa
**Kysytty:** puoliintumisaika $T_{1/2}$ taustasäteily huomioon ottaen
**Periaate:** GM-putki laskee sekä näytteen että taustasäteilyn pulssit, joten näytteen osuus saadaan vähentämällä tausta jokaisesta lukemasta. Näytteen pulssimäärä on verrannollinen aktiivisuuteen, ja suuren ydinjoukon aktiivisuus pienenee hajoamislain mukaan, koska jokainen ydin hajoaa samalla todennäköisyydellä (luku *Hajoamislaki ja puoliintumisaika*). Kaikki $11$ pistettä käytetään sovittamalla suora, koska yksittäinen lukema vaihtelee satunnaisesti.
**Kuvaajan lukeminen:** Taustan vähentämisen jälkeen kaikista $11$ lukemasta lasketaan $\ln N$ ($N$ pulssia $10\,\text{s}$:ssa, esimerkiksi $\ln 393 = 5{,}974$ ja $\ln 99 = 4{,}595$), ja pisteet $(t,\ \ln N)$ piirretään pisteinä. Eksponentiaalinen väheneminen on $\ln N$:n suhteen suora, joten pisteisiin sovitetaan yksi suora koko välille $0$–$300\,\text{s}$. Kulmakerroin $k$ luetaan suoralta kahdesta kaukana toisistaan olevasta pisteestä, esimerkiksi $(0;\ 5{,}993)$ ja $(300\,\text{s};\ 4{,}635)$, eikä yksittäisistä mittauspisteistä.
**Kaava:** $N = N_0 e^{-\lambda t}$, joten $\ln N = \ln N_0 - \lambda t$. Suoran kulmakerroin on $k = -\lambda$, ja $T_{1/2} = \dfrac{\ln 2}{\lambda}$, joten $T_{1/2} = \dfrac{\ln 2}{-k}$, missä $k = \dfrac{\Delta(\ln N)}{\Delta t}$
**Muunnokset:** Kaikki pulssimäärät ovat samassa yksikössä, pulssia $10\,\text{s}$:ssa, ja $\ln N$ on paljas luku, joten muunnoksia ei tarvita.
**Sijoitus:** Sovitetun suoran kulmakerroin on $k = \dfrac{4{,}635 - 5{,}993}{300\,\text{s} - 0\,\text{s}} = -4{,}528 \cdot 10^{-3}\,\tfrac{1}{\text{s}}$, joten $T_{1/2} = \dfrac{0{,}6931}{4{,}528 \cdot 10^{-3}\,\tfrac{1}{\text{s}}} = 153{,}1\,\text{s}$
**Vastaus:** $T_{1/2} \approx 153\,\text{s}$, kolme merkitsevää numeroa, mutta laskentojen satunnaisvaihtelu tekee viimeisestä numerosta epävarman. Taustan vähentäminen muuttaa tulosta, ja sovitus käyttää kaikkia pisteitä.
**Järkevyys:** Kahden päätepisteen laskulla $T_{1/2} = \dfrac{t \ln 2}{\ln (N_0 : N)} = \dfrac{300\,\text{s} \cdot 0{,}6931}{\ln (393 : 99)} = 151\,\text{s}$, joka poikkeaa sovituksesta vain $1{,}4\,\%$. Pulssimäärä on $300\,\text{s}$:ssa pudonnut $393$:sta noin $99$:ään eli noin neljäsosaan, kaksi puoliintumisaikaa antaisi $\tfrac{393}{4} \approx 98$, joten $T_{1/2} \approx \tfrac{300\,\text{s}}{2} = 150\,\text{s}$ on oikeaa luokkaa.

### b)
**Kysytty:** ryhmän johtopäätöksen arvio
**Periaate:** Ytimellä ei ole muistia eikä ikää: jokainen barium-137m-ydin hajoaa samalla todennäköisyydellä sekunnissa riippumatta siitä, kuinka kauan se on ollut olemassa (luku *Hajoamislaki ja puoliintumisaika*). GM-putken pulssimäärä vaihtelee satunnaisesti noin $\sqrt{N}$:n verran (luku *Mittaaminen ja mittauksen luotettavuus*).
**Mallivastaus:** Ryhmän selitys on väärä. Minuutin seisominen pienentää näytteen aktiivisuutta, mutta ei muuta puoliintumisaikaa, koska jäljellä olevat ytimet hajoavat täsmälleen samalla todennäköisyydellä kuin aiemmin. Ero johtuu menetelmästä. Ryhmä luki puoliintumisajan yhden pisteparin väliltä, ja yksittäinen lukema vaihtelee satunnaisesti: $212$ pulssin lukeman epävarmuus on noin $\sqrt{212} \approx 15$ pulssia eli $7\,\%$. Kohdan $150\,\text{s}$ lukema on sattumalta suuri, mikä siirtää lukemaa myöhemmäksi. Myös taustan sivuuttaminen oli virhe. Alussa tausta on vain $1\,\%$ lukemasta, mutta lopussa jo $5\,\%$, ja vähentämättä jätetty tausta hidastaa näennäisesti vähenemistä ja pidentää puoliintumisaikaa. Lisäksi taustaa mitattiin vain kerran $10\,\text{s}$, joten sen arvo $5 \pm 2$ on hyvin epätarkka. Johtopäätös ”$166\,\text{s}$” ei siis ole luotettava. Kaikista pisteistä taustan vähentämisen jälkeen saadaan noin $153\,\text{s}$, mikä vastaa kirjan arvoa.

### c)
**Kysytty:** miten mittausta ja tulosten käsittelyä parannetaan
**Periaate:** Satunnaisvirhe pienenee, kun pulsseja lasketaan enemmän tai mittaus toistetaan, ja systemaattinen virhe poistetaan korjaamalla sen syy. Kaikki mittauspisteet otetaan käyttöön sovittamalla malli (luvut *Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi* ja *Graafinen esitys ja suoran sovittaminen*).
**Mallivastaus:** Taustaa mitataan ennen mittausta ja sen jälkeen pitkään, esimerkiksi $10\,\text{min}$, jolloin pulsseja kertyy noin $300$ ja taustan epävarmuus on noin $6\,\%$ eikä $45\,\%$. Tausta muunnetaan samaan yksikköön, pulssia $10\,\text{s}$:ssa, ja vähennetään jokaisesta lukemasta. Laskenta-aikaa voi pidentää esimerkiksi $20\,\text{s}$:iin ja mitata tiheämmin, jolloin yksittäisen lukeman suhteellinen epävarmuus pienenee. Kaikki pisteet käytetään: piirretään $\ln(N - N_\text{tausta})$ ajan funktiona, ja suoran kulmakerroin on $-\tfrac{\ln 2}{T_{1/2}}$, tai sovitetaan laskimella malli $N = A\,e^{-Ct} + B$, jossa vakio $B$ on tausta. Mittaus toistetaan uudella näytteellä, ja tuloksia verrataan, jolloin nähdään hajonta. Näytteen etäisyys GM-putkesta pidetään koko ajan samana. Ilmoitetaan tulos epävarmuuksineen, esimerkiksi $T_{1/2} = (152 \pm 4)\,\text{s}$.

### Yleisiä virheitä
- a-kohdassa taustaa ei vähennetä tai se vähennetään vain alkulukemasta.
- a-kohdassa puoliintumisaika luetaan suoraan lineaarisella interpoloinnilla, ikään kuin väheneminen olisi tasaista.
- b-kohdassa hyväksytään ryhmän selitys ”vanhemmista ytimistä” tai arvioidaan vain laskuvirheitä mainitsematta satunnaisvaihtelua.
- c-kohdassa ehdotetaan vain ”tarkempaa mittaria” kertomatta, mikä mittauksessa muuttuu ja miksi.

### Hyväksytään myös
- a-kohdassa kahden päätepisteen lasku taustan vähentämisen jälkeen: $T_{1/2} = \dfrac{t \ln 2}{\ln (N_0 : N)} \approx 151\,\text{s}$.
- a-kohdassa jokin muu kaukana toisistaan oleva pistepari taustan vähentämisen jälkeen, kunhan tulos on välillä $145$–$157\,\text{s}$.

## fy9-moderni-s6

### a)
**Annettu:** sähköteho $P_\text{s} = 1600\,\text{MW}$, lämpöteho $P_\text{l} = 4300\,\text{MW}$, energia fissiota kohden $E_\text{f} = 200\,\text{MeV}$
**Kysytty:** hyötysuhde $\eta$ ja fissioiden määrä sekunnissa $n$
**Periaate:** Hyötysuhde on hyödyllisen tehon ja käytetyn tehon suhde (luku *Energiantuotanto ja voimalaitosten hyötysuhde*). Reaktorin lämpöteho on yhden fission energia kertaa fissioiden määrä sekunnissa (luku *Fissio, fuusio ja ydinvoima*).
**Kaava:** $\eta = \dfrac{P_\text{s}}{P_\text{l}}$ ja $P_\text{l} = nE_\text{f}$, joten $n = \dfrac{P_\text{l}}{E_\text{f}}$
**Muunnokset:** $200\,\text{MeV} = 200 \cdot 10^{6} \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 3{,}204 \cdot 10^{-11}\,\text{J}$ ja $4300\,\text{MW} = 4300 \cdot 10^{6}\,\text{W}$
**Sijoitus:** $\eta = \dfrac{1600\,\text{MW}}{4300\,\text{MW}} = 0{,}3721 = 37{,}21\,\%$ ja $n = \dfrac{4300 \cdot 10^{6}\,\tfrac{\text{J}}{\text{s}}}{3{,}204 \cdot 10^{-11}\,\text{J}} = 1{,}342 \cdot 10^{20}\,\tfrac{1}{\text{s}}$
**Vastaus:** Hyötysuhde on $\eta \approx 37{,}2\,\%$, ja reaktorissa tapahtuu noin $1{,}34 \cdot 10^{20}$ fissiota sekunnissa, kolme merkitsevää numeroa kuten tehot.
**Järkevyys:** Höyryturbiinilla toimivan lämpövoimalan hyötysuhde on tyypillisesti $30$–$40\,\%$. Fissioita on valtavasti, koska yksi fissio vapauttaa vain noin $3 \cdot 10^{-11}\,\text{J}$.

### b)
**Annettu:** $n = 1{,}342 \cdot 10^{20}\,\tfrac{1}{\text{s}}$ (a-kohta), $1\,\text{a} = 3{,}156 \cdot 10^{7}\,\text{s}$, uraani-235-atomin massa $m_\text{U} = 235\,\text{u}$, $1\,\text{u} = 1{,}661 \cdot 10^{-27}\,\text{kg}$, $P_\text{l} = 4300\,\text{MW}$, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$
**Kysytty:** vuodessa fissioituvan uraani-235:n massa $m$ ja energiaksi muuttuva massa $\Delta m$
**Periaate:** Jokainen fissio kuluttaa yhden uraani-235-ytimen. Vapautuva energia vastaa massavajetta: reaktiotuotteiden massa on pienempi kuin lähtöaineiden (luvut *Massavaje ja ytimen sidosenergia* ja *Fissio, fuusio ja ydinvoima*).
**Kaava:** $m = n t\,m_\text{U}$ ja $E = \Delta m\,c^2$, joten $\Delta m = \dfrac{P_\text{l}t}{c^2}$
**Muunnokset:** $m_\text{U} = 235\,\text{u} = 235 \cdot 1{,}661 \cdot 10^{-27}\,\text{kg} = 3{,}903 \cdot 10^{-25}\,\text{kg}$
**Sijoitus:** $nt = 1{,}342 \cdot 10^{20}\,\tfrac{1}{\text{s}} \cdot 3{,}156 \cdot 10^{7}\,\text{s} = 4{,}236 \cdot 10^{27}$, joten $m = 4{,}236 \cdot 10^{27} \cdot 3{,}903 \cdot 10^{-25}\,\text{kg} = 1653\,\text{kg}$. $\Delta m = \dfrac{4300 \cdot 10^{6}\,\tfrac{\text{J}}{\text{s}} \cdot 3{,}156 \cdot 10^{7}\,\text{s}}{(2{,}998 \cdot 10^{8}\,\text{m/s})^2} = \dfrac{1{,}357 \cdot 10^{17}\,\text{J}}{8{,}988 \cdot 10^{16}\,\tfrac{\text{m}^2}{\text{s}^2}} = 1{,}51\,\text{kg}$
**Vastaus:** Uraani-235:tä fissioituu vuodessa noin $1650\,\text{kg}$, ja massaa muuttuu energiaksi noin $1{,}51\,\text{kg}$, kolme merkitsevää numeroa kuten tehot.
**Järkevyys:** Energiaksi muuttuu vain $1{,}51 : 1653 \approx 0{,}09\,\%$ uraanin massasta, mikä on sama kuin $200\,\text{MeV}$ jaettuna uraaniatomin lepoenergialla $235 \cdot 931{,}5\,\text{MeV}$. Loput massasta jää fissiotuotteiksi ja neutroneiksi, koska nukleonien määrä säilyy.

### c)
**Annettu:** $P_\text{l} = 4300\,\text{MW}$, $P_\text{s} = 1600\,\text{MW}$, meriveden ominaislämpökapasiteetti $c_\text{v} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, lämpeneminen $\Delta T = 11\,\text{K}$
**Kysytty:** meriveden massavirta $\tfrac{m}{t}$
**Periaate:** Energia säilyy: reaktorin lämpötehosta se osa, josta ei tule sähköä, siirtyy lauhduttimessa meriveteen (luku *Energiantuotanto ja voimalaitosten hyötysuhde*). Veden lämpenemiseen tarvittava lämpö on $Q = c_\text{v}m\Delta T$ (luku *Sisäenergia, lämpömäärä ja energian säilyminen*).
**Kaava:** $P_\text{l} - P_\text{s} = \dfrac{Q}{t} = c_\text{v}\dfrac{m}{t}\Delta T$, joten $\dfrac{m}{t} = \dfrac{P_\text{l} - P_\text{s}}{c_\text{v}\Delta T}$
**Muunnokset:** $4300\,\text{MW} - 1600\,\text{MW} = 2700\,\text{MW} = 2700 \cdot 10^{6}\,\text{W}$
**Sijoitus:** $\dfrac{m}{t} = \dfrac{2700 \cdot 10^{6}\,\tfrac{\text{J}}{\text{s}}}{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 11\,\text{K}} = 58\,581\,\tfrac{\text{kg}}{\text{s}}$
**Vastaus:** Merivettä on pumpattava noin $5{,}9 \cdot 10^{4}\,\tfrac{\text{kg}}{\text{s}}$, kaksi merkitsevää numeroa kuten lämpeneminen $11\,\text{K}$.
**Järkevyys:** Se on noin $59\,\text{m}^3$ sekunnissa, keskikokoisen joen virtaama. Suuren ydinvoimalan jäähdytysvesi on todella tätä luokkaa, ja lämpö näkyy talvella sulana vesialueena voimalan edustalla.

### d)
**Annettu:** sähköteho $P_\text{s} = 1600\,\text{MW}$, $t = 1\,\text{a} = 3{,}156 \cdot 10^{7}\,\text{s}$, kivihiilen lämpöarvo $H = 24\,\tfrac{\text{MJ}}{\text{kg}}$, hiilivoimalan hyötysuhde $\eta_\text{h} = 40\,\%$
**Kysytty:** vuodessa poltettavan kivihiilen massa $m_\text{h}$
**Periaate:** Hiilivoimala tuottaa saman sähköenergian, mutta polttoaineen energiasta vain $40\,\%$ muuttuu sähköksi (luku *Energiantuotanto ja voimalaitosten hyötysuhde*). Polttoaineen energia on lämpöarvo kertaa massa (luku *Polttoaineet ja lämpöarvo*).
**Kaava:** $E_\text{s} = P_\text{s}t$, $\eta_\text{h}Hm_\text{h} = E_\text{s}$, joten $m_\text{h} = \dfrac{P_\text{s}t}{\eta_\text{h}H}$
**Muunnokset:** $1600\,\text{MW} = 1600 \cdot 10^{6}\,\text{W}$, $24\,\tfrac{\text{MJ}}{\text{kg}} = 24 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}}$ ja lopuksi $1\,\text{t} = 1000\,\text{kg}$
**Sijoitus:** $E_\text{s} = 1600 \cdot 10^{6}\,\tfrac{\text{J}}{\text{s}} \cdot 3{,}156 \cdot 10^{7}\,\text{s} = 5{,}050 \cdot 10^{16}\,\text{J}$, joten $m_\text{h} = \dfrac{5{,}050 \cdot 10^{16}\,\text{J}}{0{,}40 \cdot 24 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}}} = 5{,}26 \cdot 10^{9}\,\text{kg} = 5{,}26 \cdot 10^{6}\,\text{t}$
**Vastaus:** Hiilivoimala polttaisi noin $5{,}3 \cdot 10^{6}\,\text{t}$ eli viisi miljoonaa tonnia kivihiiltä vuodessa, kaksi merkitsevää numeroa kuten lämpöarvo ja hyötysuhde.
**Järkevyys:** Määrä on noin kolme miljoonaa kertaa fissioituvan uraani-235:n massa, koska yksi fissio vapauttaa noin $200\,\text{MeV}$, kun hiiliatomin palaminen vapauttaa vain muutaman elektronivoltin. Se on noin $14\,000$ tonnia päivässä, satoja junavaunullisia.

### Yleisiä virheitä
- a-kohdassa hyötysuhde lasketaan väärin päin, $\tfrac{4300}{1600}$, tai megaelektronivoltteja ei muunneta jouleiksi.
- b-kohdassa massaksi otetaan $\Delta m$, eli väitetään, että koko polttoaine muuttuu energiaksi, tai $\Delta m$ lasketaan sähköenergiasta lämpöenergian sijaan.
- c-kohdassa merivedelle siirtyväksi tehoksi otetaan koko lämpöteho $4300\,\text{MW}$ tai sähköteho $1600\,\text{MW}$.
- d-kohdassa hyötysuhteella kerrotaan eikä jaeta, jolloin hiiltä tulee $6{,}25$-kertaisesti liian vähän, tai kilogrammat jätetään muuntamatta tonneiksi.
