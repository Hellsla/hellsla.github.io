## fy9-voimat-s1

### a)
**Kysytty:** veneen voimakuvio, kun vinssi vetää venettä luiskaa ylös tasaisella nopeudella
**Periaate:** Valitaan kappaleeksi vene. Etsitään sen vuorovaikutukset: Maa (paino), luiskan liukulistat (tukivoima ja kitka) ja vaijeri (jännitysvoima). Vene liukuu luiskaa ylös. Siksi liikekitka osoittaa luiskaa alas. Nopeus on vakio, joten voimien summa on nolla.
**Mallivastaus:** Vene piirretään suorakulmioksi, joka on luiskan suuntainen.
- Paino $\overline{G}$ lähtee keskipisteestä suoraan alas. Se ei ole kohtisuorassa luiskaa vastaan.
- Tukivoima $\overline{N}$ lähtee pohjasta. Se on kohtisuorassa luiskaa vastaan ja osoittaa luiskasta ulospäin. Se on yhtä suuri kuin painon se komponentti, joka on kohtisuorassa luiskaa vastaan. Siksi tukivoima on vähän pienempi kuin paino.
- Liikekitka $\overline{F}_\mu$ lähtee pohjan alemmasta kulmasta ja osoittaa luiskaa alas.
- Vaijerin jännitysvoima $\overline{T}$ lähtee keulasta eli veneen etuosasta ja osoittaa luiskaa ylös.

Nuolten pituudet: $\overline{T}$ on yhtä pitkä kuin kitka ja painon luiskan suuntainen komponentti yhteensä. Tämä johtuu siitä, että kokonaisvoima on nolla. Nopeuden saa merkitä erikseen kuvion viereen, mutta sitä ei piirretä voimaksi.
```voimakuvio
pinta 14
G 2746,8
N 2665,2
F_mu 666,3 alas
T 1330,8 14
a 0
v ylös
```

### b)
**Annettu:** massa $m = 280\,\text{kg}$, luiskan kaltevuuskulma $\alpha = 14^\circ$, liikekitkakerroin $\mu = 0{,}25$, nopeus on vakio, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** vaijerin jännitysvoima $T$
**Periaate:** Nopeus on vakio. Siksi Newtonin ensimmäisen lain mukaan voimien summa on nolla sekä luiskan suunnassa että luiskaa vastaan kohtisuorassa suunnassa. Vene liukuu, joten kitka on liikekitkaa $\mu N$. Kohtisuorassa suunnassa vaikuttavat vain painon komponentti ja tukivoima (luku *Paino, kitka ja kalteva taso*).
**Voimakuvio:** a-kohdan kuvio. $x$-akseli osoittaa luiskaa ylös, ja $y$-akseli osoittaa kohtisuoraan luiskasta ulos. Painon komponentit ovat $G_x = mg\sin\alpha$ luiskaa alas ja $G_y = mg\cos\alpha$ luiskaa kohti.
```voimakuvio
pinta 14
G 2746,8
N 2665,2
F_mu 666,3 alas
T 1330,8 14
a 0
akselit 14
komponentit G
```
**Kaava:** $y$: $N - mg\cos\alpha = 0$ ja $x$: $T - mg\sin\alpha - \mu N = 0$, joten $T = mg(\sin\alpha + \mu\cos\alpha)$
**Muunnokset:** Ei tarvita. Suureet ovat perusyksiköissä.
**Sijoitus:** $T = 280\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \cdot (\sin 14^\circ + 0{,}25 \cdot \cos 14^\circ) = 2746{,}8\,\text{N} \cdot (0{,}2419 + 0{,}2426) = 1330{,}8\,\text{N}$
**Vastaus:** $T \approx 1{,}3\,\text{kN}$. Tuloksessa on kaksi merkitsevää numeroa, kuten kulmassa $14^\circ$ ja kitkakertoimessa $0{,}25$.
**Järkevyys:** Painon luiskan suuntainen komponentti on $665\,\text{N}$, ja kitka on $666\,\text{N}$. Vinssi siis tekee työtä kitkaa vastaan melkein yhtä paljon kuin se nostaa venettä. Veto on noin puolet painosta $2{,}7\,\text{kN}$. Luiska keventää työtä, mutta kitka vie siitä paljon.

### c)
**Annettu:** $m = 280\,\text{kg}$, $\alpha = 14^\circ$, lepokitkakerroin $\mu_0 = 0{,}35$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** pysyykö vene levossa, ja pienin kaltevuuskulma $\alpha_0$, jolla vene lähtee itsestään liukumaan
**Periaate:** Kun vaijeri löystyy, veneeseen vaikuttavat paino, tukivoima ja lepokitka. Lepokitka osoittaa luiskaa ylös. Lepokitka on vain niin suuri kuin tilanne vaatii, enintään $\mu_0 N$. Vene pysyy paikallaan, jos tarvittava lepokitka $mg\sin\alpha$ ei ylitä tätä ylärajaa (luku *Paino, kitka ja kalteva taso*).
**Voimakuvio:** Vene on luiskan suuntainen suorakulmio. Paino lähtee keskipisteestä alas. Tukivoima lähtee pohjasta kohtisuoraan luiskasta ulos. Lepokitka lähtee pohjan ylemmästä kulmasta luiskaa ylös. Se on yhtä suuri kuin painon luiskan suuntainen komponentti.
```voimakuvio
pinta 14
G 2746,8
N 2665,2
F_mu 664,5 ylös
a 0
```
**Kaava:** Vene pysyy paikallaan, kun $mg\sin\alpha \le \mu_0 mg\cos\alpha$ eli $\tan\alpha \le \mu_0$. Rajakulmalla $\tan\alpha_0 = \mu_0$, joten $\alpha_0 = \arctan\mu_0$
**Muunnokset:** Ei tarvita. Massa supistuu eli häviää yhtälöstä.
**Sijoitus:** Tarvittava lepokitka on $mg\sin\alpha = 2746{,}8\,\text{N} \cdot \sin 14^\circ = 664{,}5\,\text{N}$. Yläraja on $\mu_0 mg\cos\alpha = 0{,}35 \cdot 2746{,}8\,\text{N} \cdot \cos 14^\circ = 932{,}8\,\text{N}$. Rajakulma on $\alpha_0 = \arctan 0{,}35 = 19{,}29^\circ$
**Vastaus:** Vene pysyy paikallaan, koska $664{,}5\,\text{N} < 932{,}8\,\text{N}$ (yhtä hyvin $\tan 14^\circ \approx 0{,}25 < 0{,}35$). Vene lähtisi itsestään liukumaan, jos luiskan kulma olisi vähintään noin $19^\circ$. Tuloksessa on kaksi merkitsevää numeroa, kuten kitkakertoimessa $0{,}35$.
**Järkevyys:** Rajakulma ei riipu massasta. Tämä johtuu siitä, että sekä alas vievä komponentti että kitkan yläraja ovat verrannollisia massaan eli kasvavat samassa suhteessa kuin massa. Märkä, liukas tai jäinen lista voi pienentää lepokitkakerrointa. Silloin vene voi lähteä liikkeelle loivemmallakin luiskalla. Venettä ei siis kannata jättää pelkän kitkan varaan.

### Yleisiä virheitä
- Voimakuvioon piirretään vaijerin voiman lisäksi ”liikkeen voima”, joka vie venettä luiskaa ylös. Tai painon komponentit piirretään omiksi voimikseen painon lisäksi.
- Tukivoimaksi otetaan $N = mg$, vaikka luiskalla $N = mg\cos\alpha$.
- Kitka piirretään luiskaa ylös. Vene kuitenkin liukuu ylös, ja liikekitka vastustaa liukumista.
- c-kohdassa lepokitkaksi otetaan suoraan $\mu_0 N$, vaikka se on vain yläraja. Tai liukumisen ehto kirjoitetaan sinin avulla, $\sin\alpha_0 = \mu_0$.

### Hyväksytään myös
- c-kohdassa vertailu $\tan 14^\circ \approx 0{,}25 < \mu_0 = 0{,}35$ ilman voimien lukuarvoja.

## fy9-voimat-s2

### a)
**Kysytty:** reen A ja reen B voimakuviot kiihdytyksen aikana
**Periaate:** Kytketyistä kappaleista kumpikin valitaan vuorollaan kappaleeksi. Kummallekin piirretään oma kuvio. Kuviossa ovat vain ne voimat, jotka vaikuttavat siihen rekeen. Köysi vetää kumpaakin rekeä itseään kohti. Köysi 2 vetää A:ta taaksepäin ja B:tä eteenpäin. Voimat ovat yhtä suuret, koska köysi on kevyt.
**Mallivastaus:** Kumpikin reki piirretään omaksi suorakulmiokseen.
- Reki A: paino $\overline{G}_\text{A}$ alas, tukivoima $\overline{N}_\text{A}$ ylös, köyden 1 voima $\overline{T}_1$ eteenpäin, köyden 2 voima $\overline{T}_2$ taaksepäin ja liikekitka $\overline{F}_{\mu\text{A}}$ taaksepäin.
- Reki B: paino $\overline{G}_\text{B}$ alas, tukivoima $\overline{N}_\text{B}$ ylös, köyden 2 voima $\overline{T}_2$ eteenpäin ja liikekitka $\overline{F}_{\mu\text{B}}$ taaksepäin.

Kummankin reen kokonaisvoima osoittaa eteenpäin, koska reet kiihtyvät. Kiihtyvyys merkitään kuvioiden viereen omalla värillään. Kelkkaa ei piirretä. B:n voimaa köyteen ei piirretä B:n kuvioon. Vaakasuorat voimat on piirretty omassa mittakaavassaan, koska ne ovat paljon pienempiä kuin painot.
```voimakuvio
pinta 0
G 1177,2
N 1177,2
T_1 296,2 0
T_2 118,48 180
F_mu 117,72 vasen
a oikea
---
pinta 0
G 784,8
N 784,8
T_2 118,48 0
F_mu 78,48 vasen
a oikea
```

### b)
**Annettu:** $m_\text{B} = 80\,\text{kg}$, liikekitkakerroin $\mu = 0{,}10$, kiihtyvyys $a = 0{,}50\,\text{m/s}^2$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** köyden 2 jännitysvoima $T_2$
**Periaate:** Rekeen B vaikuttaa kaksi vaakasuoraa voimaa: köyden 2 veto eteenpäin ja kitka taaksepäin. Newtonin toisen lain mukaan niiden summa on $m_\text{B} a$. Pystysuunnassa ei ole kiihtyvyyttä. Siksi $N_\text{B} = m_\text{B} g$, ja kitka on $\mu m_\text{B} g$ (luku *Liikeyhtälö kytketyille kappaleille*).
**Kaava:** $T_2 - \mu m_\text{B} g = m_\text{B} a$, joten $T_2 = m_\text{B}(a + \mu g)$
**Muunnokset:** Ei tarvita. Suureet ovat perusyksiköissä.
**Sijoitus:** $T_2 = 80\,\text{kg} \cdot (0{,}50\,\text{m/s}^2 + 0{,}10 \cdot 9{,}81\,\text{m/s}^2) = 80\,\text{kg} \cdot 1{,}481\,\text{m/s}^2 = 118{,}48\,\text{N}$
**Vastaus:** $T_2 \approx 120\,\text{N}$. Tuloksessa on kaksi merkitsevää numeroa, kuten kiihtyvyydessä $0{,}50\,\text{m/s}^2$ ja kitkakertoimessa $0{,}10$.
**Järkevyys:** B:n kitka on $0{,}10 \cdot 80\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \approx 78\,\text{N}$. Kiihdyttämiseen tarvitaan $80\,\text{kg} \cdot 0{,}50\,\text{m/s}^2 = 40\,\text{N}$. Yhteensä tarvitaan noin $118\,\text{N}$, kuten pitää.

### c)
**Annettu:** $m_\text{A} = 120\,\text{kg}$, $m_\text{B} = 80\,\text{kg}$, $\mu = 0{,}10$, $a = 0{,}50\,\text{m/s}^2$, b-kohdasta $T_2 = 118{,}48\,\text{N}$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** köyden 1 jännitysvoima $T_1$
**Periaate:** Rekeen A vaikuttaa kolme vaakasuoraa voimaa: köyden 1 veto eteenpäin sekä köyden 2 veto ja kitka taaksepäin. Niiden summa on $m_\text{A} a$. Saman tuloksen saa myös, kun molemmat reet käsitellään yhtenä systeeminä eli kokonaisuutena. Silloin köyden 2 voimat ovat sisäisiä voimia, ja ne kumoavat toisensa.
**Kaava:** $T_1 - T_2 - \mu m_\text{A} g = m_\text{A} a$, joten $T_1 = T_2 + m_\text{A}(a + \mu g) = (m_\text{A} + m_\text{B})(a + \mu g)$
**Muunnokset:** Ei tarvita. Suureet ovat perusyksiköissä.
**Sijoitus:** $T_1 = 118{,}48\,\text{N} + 120\,\text{kg} \cdot 1{,}481\,\text{m/s}^2 = 118{,}48\,\text{N} + 177{,}72\,\text{N} = 296{,}2\,\text{N}$
**Vastaus:** $T_1 \approx 300\,\text{N}$ ($296\,\text{N}$). Tuloksessa on kaksi merkitsevää numeroa, kuten lähtötiedoissa.
**Järkevyys:** Tarkistus systeemin avulla: $(120 + 80)\,\text{kg} \cdot 1{,}481\,\text{m/s}^2 = 296{,}2\,\text{N}$. Tulos on sama. Etummainen köysi on kireämpi, koska se kiihdyttää ja vetää molempia rekiä.

### d)
**Kysytty:** pitääkö väite ”takimmaisen köyden voima on puolet etummaisen köyden voimasta” paikkansa
**Periaate:** Kumpikin köysi vetää kaikkia niitä rekiä, jotka ovat köyden takana. Kun kitkakerroin on sama, jokainen reki tarvitsee vetoa $m(a + \mu g)$. Tarvittava veto on siis verrannollinen massaan.
**Mallivastaus:** Väite ei pidä paikkaansa. Köysi 2 vetää vain rekeä B. Köysi 1 vetää molempia rekiä. b- ja c-kohdan tuloksista saadaan $T_2 : T_1 = 118\,\text{N} : 296\,\text{N} = 0{,}40$. Tämä on sama kuin massojen suhde $80\,\text{kg} : 200\,\text{kg}$. Suhde riippuu siis rekien massoista, ei rekien lukumäärästä. Suhde olisi puolet vain, jos reet olisivat yhtä raskaat ja niillä olisi sama kitkakerroin.

### Yleisiä virheitä
- Molemmat reet piirretään samaan kuvioon. Tai kelkan voima piirretään suoraan rekeen B.
- Reen A kuviosta puuttuu köyden 2 voima, joka vetää taaksepäin. Silloin $T_1$ saadaan liian pieneksi ($T_1 = m_\text{A}(a + \mu g) \approx 178\,\text{N}$).
- Kitka unohdetaan, ja jännitysvoimaksi lasketaan pelkkä $ma$.
- Köysien voimat $\overline{T}_1$ ja $\overline{T}_2$ merkitään samalla symbolilla. Silloin yhtälöistä ei näe, kummasta köydestä on kyse.

### Hyväksytään myös
- c-kohdassa molemmat reet käsitellään yhtenä kappaleena, kun ratkaisussa todetaan, että köyden 2 voimat ovat systeemin sisäisiä voimia.

## fy9-voimat-s3

### a)
**Kysytty:** kuvaaja vaunun kiihtyvyydestä vetävän voiman funktiona ja siihen sovitettu malli
**Kuvaaja:** Vaaka-akselilla on vetävä voima $F\ (\text{N})$. Pystyakselilla on kiihtyvyys $a\ (\text{m/s}^2)$. Vaaka-akseli alkaa nollasta. Silloin näkyy kohta, jossa suora leikkaa akselin.

<svg data-fig="fy9-voimat-s3-graph" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: vaunun kiihtyvyys a vetävän voiman F funktiona. Kuvaajassa on seitsemän mustaa pistettä. Voimat ovat 0,40–1,60 N. Pisteisiin on sovitettu nouseva suora. Suoraa on jatkettu katkoviivana alas vaaka-akselille asti. Suora kulkee pisteiden (0,40 N; 0,19 m/s²) ja (1,60 N; 1,60 m/s²) kautta. Nämä kaksi suoran pistettä on ympyröity. Suora leikkaa vaaka-akselin noin kohdassa F = 0,24 N. Suora ei kulje origon kautta." style="max-width:100%;font-size:24px">
  <line x1="141" y1="380" x2="141" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186" y1="380" x2="186" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="380" x2="230.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275.5" y1="380" x2="275.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="380" x2="320.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="380" x2="365.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="380" x2="410" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455" y1="380" x2="455" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="380" x2="500" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="344.5" x2="500" y2="344.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="309" x2="500" y2="309" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="273.5" x2="500" y2="273.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="238" x2="500" y2="238" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="202" x2="500" y2="202" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="166.5" x2="500" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="131" x2="500" y2="131" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="95.5" x2="500" y2="95.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="60" x2="500" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="380" x2="514" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,380 L513,386 L513,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="381" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="141" y1="380" x2="141" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186" y1="380" x2="186" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="163.5" y="389.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}4$</div></foreignObject>
  <line x1="230.5" y1="380" x2="230.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="275.5" y1="380" x2="275.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="253" y="389.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}8$</div></foreignObject>
  <line x1="320.5" y1="380" x2="320.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365.5" y1="380" x2="365.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="343" y="389.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}2$</div></foreignObject>
  <line x1="410" y1="380" x2="410" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="455" y1="380" x2="455" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="432.5" y="389.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}6$</div></foreignObject>
  <line x1="500" y1="380" x2="500" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="344.5" x2="96" y2="344.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="309" x2="96" y2="309" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="294.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}4$</div></foreignObject>
  <line x1="89" y1="273.5" x2="96" y2="273.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="238" x2="96" y2="238" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="223.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}8$</div></foreignObject>
  <line x1="89" y1="202" x2="96" y2="202" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="166.5" x2="96" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="152" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}2$</div></foreignObject>
  <line x1="89" y1="131" x2="96" y2="131" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="95.5" x2="96" y2="95.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="81" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}6$</div></foreignObject>
  <line x1="89" y1="60" x2="96" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="66" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="532" y="365.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{N})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a\ (\text{m/s}^2)$</div></foreignObject>
  <polyline points="186,346.5 455,95.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="149.5,380 186,346.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="186" cy="344.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="230.5" cy="307" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="275.5" cy="261" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="320.5" cy="223.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="365.5" cy="177.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="410" cy="140" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="455" cy="94" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="186" cy="346" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="455" cy="95.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="149.5" cy="380" r="7" fill="#e8590c"/>
  <foreignObject x="159.5" y="337.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$F_0 \approx 0{,}24\,\text{N}$</div></foreignObject>
  <foreignObject x="189" y="107.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$k \approx 1{,}18\,\tfrac{1}{\text{kg}}$</div></foreignObject>
</svg>

Ympyröidyt kohdat ovat ne kaksi suoran pistettä, joista b-kohdan kulmakerroin luetaan. Katkoviiva on suoran jatke vaaka-akselille.

**Mallivastaus:** Pisteet ovat melkein suoralla. Kiihtyvyys siis kasvaa tasaisesti, kun vetävä voima kasvaa. Pisteisiin sovitetaan yksi suora, joka kulkee pisteiden lomitse eli niiden välistä. Pisteitä ei yhdistetä murtoviivaksi. Todellisissa mittauksissa pisteet eivät yleensä ole täsmälleen samalla suoralla, koska mittauksessa on aina epävarmuutta. Suora ei kulje origon kautta. Se leikkaa vaaka-akselin noin kohdassa $0{,}24\,\text{N}$. Siksi suoraa ei pakoteta kulkemaan origon kautta. Sitä jatketaan vaaka-akselille, koska b-kohdassa tarvitaan tätä kohtaa.

### b)
**Annettu:** a-kohdan kuvaaja ja suoralta luetut pisteet
**Kysytty:** vaunun massa $m$ ja kitkavoima $F_\mu$
**Periaate:** Vaunuun vaikuttaa vaakasuunnassa kaksi voimaa: langan veto $F$ eteenpäin ja kitka $F_\mu$ taaksepäin. Newtonin toisen lain mukaan $F - F_\mu = ma$. Siitä saadaan $a = \tfrac{1}{m}F - \tfrac{F_\mu}{m}$. Tämä on suoran yhtälö. Kulmakerroin on $\tfrac{1}{m}$. Suora leikkaa vaaka-akselin kohdassa $F = F_\mu$. Siinä kohdassa veto juuri ja juuri kumoaa kitkan. Siksi suora ei kulje origon kautta (luku *Newtonin toinen laki*).
**Kuvaajan lukeminen:** Suoralta luetaan kaksi pistettä, jotka ovat kaukana toisistaan. Ne eivät ole mittauspisteitä: $(0{,}40\,\text{N};\ 0{,}19\,\text{m/s}^2)$ ja $(1{,}60\,\text{N};\ 1{,}60\,\text{m/s}^2)$. Suora leikkaa vaaka-akselin noin kohdassa $F_0 = 0{,}24\,\text{N}$.
**Kaava:** $k = \dfrac{\Delta a}{\Delta F} = \dfrac{1}{m}$, joten $m = \dfrac{1}{k}$. Lisäksi $F_\mu = F_0 = F_1 - \dfrac{a_1}{k}$
**Muunnokset:** $1\,\tfrac{\text{m/s}^2}{\text{N}} = 1\,\tfrac{\text{m/s}^2}{\text{kg} \cdot \text{m/s}^2} = 1\,\tfrac{1}{\text{kg}}$. Kulmakertoimen käänteisluku on siis kilogrammoja.
**Sijoitus:** $k = \dfrac{1{,}60\,\text{m/s}^2 - 0{,}19\,\text{m/s}^2}{1{,}60\,\text{N} - 0{,}40\,\text{N}} = \dfrac{1{,}41\,\text{m/s}^2}{1{,}20\,\text{N}} = 1{,}175\,\tfrac{1}{\text{kg}}$, joten $m = \dfrac{1}{1{,}175\,\tfrac{1}{\text{kg}}} = 0{,}851\,\text{kg}$ ja $F_\mu = 0{,}40\,\text{N} - \dfrac{0{,}19\,\text{m/s}^2}{1{,}175\,\tfrac{1}{\text{kg}}} = 0{,}238\,\text{N}$
**Vastaus:** $m \approx 0{,}85\,\text{kg}$ ja $F_\mu \approx 0{,}24\,\text{N}$. Tuloksissa on kaksi merkitsevää numeroa, koska suoralta luettu kulmakerroin on noin $\pm 0{,}03\,\tfrac{1}{\text{kg}}$ tarkka.
**Järkevyys:** Laboratoriovaunun massa on yleensä alle kilogramman. Pienimmän neliösumman suora antaa saman tuloksen: $k = 1{,}175\,\tfrac{1}{\text{kg}}$, ja leikkauskohta on $0{,}239\,\text{N}$. Kitka on pieni verrattuna vetoon. Näin pitää olla, kun vaunu kulkee pyörillä.

### c)
**Kysytty:** vaunun voimakuvio, kun $F = 1{,}20\,\text{N}$, ja kuvion yhteys b-kohdan malliin
**Periaate:** Vaunuun vaikuttavat Maa (paino), rata (tukivoima ja kitka) ja lanka (veto). Lanka on vaakasuora. Siksi pystysuunnassa vaikuttavat vain paino ja tukivoima, ja ne kumoavat toisensa.
**Mallivastaus:** Vaunu piirretään suorakulmioksi. Paino $\overline{G}$ lähtee keskipisteestä alas, ja tukivoima $\overline{N}$ lähtee alapinnasta ylös. Ne ovat yhtä pitkät. Langan veto $\overline{T}$ lähtee kiinnityskohdasta eteenpäin. Kitka $\overline{F}_\mu$ lähtee alapinnan takakulmasta taaksepäin. Kitka on noin viidesosa vedosta. Kiihtyvyys merkitään erikseen kuvion viereen. Vaakasuorat voimat on piirretty omassa mittakaavassaan, koska ne ovat paljon pienempiä kuin paino.
```voimakuvio
pinta 0
G 8,35
N 8,35
T 1,20 0
F_mu 0,24 vasen
a oikea
```
Kuviosta saadaan vaakasuunnan liikeyhtälö $T - F_\mu = ma$. Se on sama kuin b-kohdan suoran yhtälö, kun $T = F$. Kuvion kokonaisvoima on $1{,}20\,\text{N} - 0{,}24\,\text{N} = 0{,}96\,\text{N}$. Se antaa kiihtyvyyden $0{,}96\,\text{N} : 0{,}851\,\text{kg} \approx 1{,}13\,\text{m/s}^2$. Tämä on lähellä mitattua arvoa $1{,}14\,\text{m/s}^2$.

### d)
**Annettu:** b-kohdasta $m = 0{,}851\,\text{kg}$ ja $F_\mu = 0{,}238\,\text{N}$; lisäpunnus $m_\text{x} = 0{,}500\,\text{kg}$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** kerroin $\mu = \tfrac{F_\mu}{N}$ ja se, miten suora muuttuu lisäpunnuksen kanssa
**Periaate:** Lanka on vaakasuora. Siksi pystysuunnassa vaikuttavat vain paino ja tukivoima, ja $N = mg$ (luku *Paino, kitka ja kalteva taso*). Mallissa kitka on verrannollinen tukivoimaan.
**Kaava:** $\mu = \dfrac{F_\mu}{N} = \dfrac{F_\mu}{mg}$; lisäpunnuksella $m' = m + m_\text{x}$, suoran kulmakerroin on $k' = \dfrac{1}{m'}$ ja leikkauskohta vaaka-akselilla $F_0' = \mu m' g$
**Muunnokset:** Ei tarvita. Suureet ovat perusyksiköissä.
**Sijoitus:** $\mu = \dfrac{0{,}238\,\text{N}}{0{,}851\,\text{kg} \cdot 9{,}81\,\text{m/s}^2} = \dfrac{0{,}238\,\text{N}}{8{,}35\,\text{N}} = 0{,}0285$
**Vastaus:** $\mu \approx 0{,}029$. Tuloksessa on kaksi merkitsevää numeroa, kuten $F_\mu$:ssä. Kertoimella ei ole yksikköä. Lisäpunnuksen kanssa massa on $1{,}351\,\text{kg}$. Silloin suora loivenee. Kulmakerroin on $\tfrac{1}{1{,}351\,\text{kg}} \approx 0{,}74\,\tfrac{1}{\text{kg}}$. Leikkauskohta siirtyy oikealle kohtaan $0{,}029 \cdot 1{,}351\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \approx 0{,}38\,\text{N}$.
**Järkevyys:** Pyörillä kulkevan vaunun vierimisvastus on paljon pienempi kuin liukuvan kappaleen kitka. Liukuvan kappaleen kitkakerroin on yleensä $0{,}2\text{–}0{,}6$. Siksi $0{,}03$ on uskottava arvo. Ennuste perustuu malliin, jossa kitka ei riipu nopeudesta. Ennuste kannattaa tarkistaa: toista mittaus punnuksen kanssa.

### Yleisiä virheitä
- Suora pakotetaan kulkemaan origon kautta. Silloin kulmakerroin ja massa ovat väärin, eikä kitkaa saada.
- Kulmakerroin luetaan kahdesta vierekkäisestä mittauspisteestä eikä sovitetusta suorasta.
- Massaksi otetaan kulmakerroin itse ($1{,}18\,\text{kg}$). Kulmakerroin on kuitenkin massan käänteisluku.
- c-kohdassa voimakuvioon piirretään punnusten paino vaunuun. Vaunua vetää kuitenkin lanka.

### Hyväksytään myös
- b-kohdassa silmämääräisesti sovitetun suoran kulmakerroin $1{,}14\text{–}1{,}22\,\tfrac{1}{\text{kg}}$ eli massa $0{,}82\text{–}0{,}88\,\text{kg}$, ja leikkauskohta $0{,}21\text{–}0{,}27\,\text{N}$; d-kohdassa niistä laskettu $\mu \approx 0{,}025\text{–}0{,}032$.
- Suoran sovitus laskimella tai taulukkolaskennalla ($a = 1{,}175\,\tfrac{1}{\text{kg}} \cdot F - 0{,}281\,\text{m/s}^2$).

## fy9-voimat-s4

### a)
**Kysytty:** mikä voima kiihdyttää kävelijää eteenpäin ja miksi peilijäällä on vaikeaa lähteä liikkeelle
**Periaate:** Kappaleen liiketilaa muuttavat vain ulkoiset voimat, jotka vaikuttavat siihen (Newtonin toinen laki). Voima ja vastavoima vaikuttavat eri kappaleisiin (kolmas laki). Lepokitka on enintään $\mu_0 N$.
**Mallivastaus:** Kun Ella astuu, hänen jalkansa työntää maata taaksepäin. Kolmannen lain mukaan maa työntää jalkaa eteenpäin yhtä suurella voimalla. Tämä voima on maan lepokitka. Jalka pyrkii liukumaan taaksepäin maan suhteen, ja kitka estää sen. Lepokitka on ainoa vaakasuora ulkoinen voima. Siksi juuri se kiihdyttää Ellaa eteenpäin. Ellan lihasten voimat ovat hänen sisäisiä voimiaan. Ne eivät yksin voi muuttaa koko kehon liiketilaa. Peilijäällä lepokitkakerroin on pieni. Siksi kitkan yläraja $\mu_0 N$ on pieni. Jos jalka työntää taaksepäin lujemmin kuin kitka pystyy vastustamaan, jalka liukuu. Siksi suurin mahdollinen kiihtyvyys jää pieneksi. Jäällä kävellään lyhyin askelin, ja jalka asetetaan melkein pystysuoraan.

### b)
**Kysytty:** pitääkö väite ”moottori työntää autoa eteenpäin” paikkansa
**Periaate:** Auton liikettä muuttavat vain ulkoiset voimat, jotka vaikuttavat autoon. Moottori on auton osa. Siksi sen voimat pyöriin ja koriin ovat sisäisiä voimia, jotka kumoavat toisensa (kolmas laki).
**Mallivastaus:** Väite on vain osittain oikein. Moottori pyörittää etupyöriä. Moottori ei kuitenkaan voi yksin työntää koko autoa, koska se on auton sisällä. Pyörivä rengas pyrkii liukumaan taaksepäin tien pinnan suhteen. Tien lepokitka vastustaa tätä liukumista, ja siksi kitka osoittaa eteenpäin. Tämä tien voima vetäviin pyöriin on ulkoinen voima, joka kiihdyttää autoa. Siksi auto ei pääse liikkeelle peilijäällä, vaikka moottori kävisi täysillä. Pyörät vain sutivat eli pyörivät paikallaan, koska kitka ei riitä.

### c)
**Kysytty:** kiihtyvän auton voimakuvio, kun ilmanvastus ja vierimisvastus otetaan huomioon
**Periaate:** Autoon vaikuttavat Maa (paino), tie (tukivoima, lepokitka vetäviin pyöriin ja vierimisvastus) ja ilma (ilmanvastus). Auto kiihtyy, joten kokonaisvoima osoittaa eteenpäin.
**Mallivastaus:** Auto piirretään suorakulmioksi. Paino $\overline{G}$ lähtee keskipisteestä alas, ja tukivoima $\overline{N}$ lähtee alapinnasta ylös. Ne ovat yhtä pitkät. Tien lepokitka vetäviin pyöriin $\overline{F}_\mu$ lähtee alapinnan etukulmasta eteenpäin. Vierimisvastus $\overline{F}_\text{r}$ ja ilmanvastus $\overline{F}_\text{v}$ osoittavat taaksepäin. Eteenpäin osoittava kitka on suurempi kuin vastukset, koska auto kiihtyy. Nopeus ja kiihtyvyys merkitään kuvion viereen. Suuruudet ovat vain esimerkkejä. Vaakasuorat voimat on piirretty omassa mittakaavassaan. Tukivoiman voi jakaa myös kahdeksi tukivoimaksi: etupyörien $\overline{N}_1$ ja takapyörien $\overline{N}_2$.
```voimakuvio
pinta 0
G 100
N 100
F_mu 30 oikea
F_r 6 vasen @vasen
F_v 10 vasen
a oikea
v oikea
```

### d)
**Kysytty:** suurin kiihtyvyys, jonka tie antaa asfaltilla ja jäällä, ja miksi etuvetoisella autolla se on pienempi
**Periaate:** Kiihdyttävä voima on tien lepokitka. Se on enintään $\mu_0 N$. Jos kaikki pyörät vetävät, tukivoima on koko auton paino, $N = mg$.
**Mallivastaus:** Suurin kiihdyttävä voima on $\mu_0 mg$. Siksi $ma_\text{max} = \mu_0 mg$ ja $a_\text{max} = \mu_0 g$. Massa supistuu. Asfaltilla $a_\text{max} \approx 0{,}8 \cdot 9{,}81\,\text{m/s}^2 \approx 8\,\text{m/s}^2$, ja jäällä $0{,}1 \cdot 9{,}81\,\text{m/s}^2 \approx 1\,\text{m/s}^2$, kun vastuksia ei oteta huomioon. Etuvetoisessa autossa eteenpäin vievä lepokitka vaikuttaa vain vetäviin etupyöriin. Niiden tukivoima on vain osa auton painosta, esimerkiksi noin puolet. Silloin suurin kiihdyttävä voima on $\mu_0 N_\text{etu} < \mu_0 mg$, ja suurin kiihtyvyys on pienempi. Jäällä etuvetoinen auto voi siis kiihtyä enintään alle $1\,\text{m/s}^2$.

### Yleisiä virheitä
- Kävelijää tai autoa ”työntävät” lihakset tai moottori. Silloin sisäinen voima esitetään ulkoisena voimana.
- Voima ja vastavoima (jalka työntää maata, maa työntää jalkaa) piirretään samaan voimakuvioon.
- Kitka piirretään aina liikettä vastaan, myös vetäviin pyöriin.
- d-kohdassa kiihtyvyydeksi lasketaan $\mu_0 N$, eikä sitä jaeta massalla. Tai jäätä ja asfalttia verrataan ilman lukuja.

## fy9-voimat-s5

### a)
**Annettu:** rajakulmat $22^\circ$, $24^\circ$, $21^\circ$, $23^\circ$ ja $33^\circ$; mittauksessa 5 kirjaa nostettiin nykäisten
**Kysytty:** lepokitkakerroin $\mu_0$ ja sen epävarmuus
**Periaate:** Rajakulmalla painon kannen suuntainen komponentti on yhtä suuri kuin lepokitkan suurin arvo. Tukivoima on painon kohtisuora komponentti (luku *Paino, kitka ja kalteva taso*). Mittaus 5 jätetään pois, koska raporttiin on kirjattu karkea virhe eli selvä virhe mittauksen tekemisessä. Nopea nosto painaa kantta hetken puhelinta vasten. Silloin tukivoima ja lepokitkan yläraja kasvavat hetkeksi. Lisäksi kulma luetaan liian myöhään. Siksi $33^\circ$ ei ole liukumisen raja. Tulosta ei poistettaisi pelkästään siksi, että se poikkeaa muista.
**Kaava:** $mg\sin\alpha_0 = \mu_0 mg\cos\alpha_0$, joten $\mu_0 = \tan\alpha_0$. Rajakulmana käytetään hyväksyttyjen mittausten keskiarvoa $\alpha_\text{ka} = \dfrac{\alpha_1 + \alpha_2 + \alpha_3 + \alpha_4}{4}$, joten $\mu_0 = \tan\alpha_\text{ka}$. Epävarmuus on puolet vaihteluvälistä: $\Delta\mu_0 = \dfrac{\tan\alpha_\text{max} - \tan\alpha_\text{min}}{2}$.
**Muunnokset:** Ei tarvita. Kulmat ovat asteina, eikä kertoimella ole yksikköä.
**Sijoitus:** $\alpha_\text{ka} = \dfrac{22^\circ + 24^\circ + 21^\circ + 23^\circ}{4} = 22{,}5^\circ$ ja $\mu_0 = \tan 22{,}5^\circ = 0{,}414$. Hajonnan rajat: $\tan 21^\circ = 0{,}384$ ja $\tan 24^\circ = 0{,}445$
**Vastaus:** $\mu_0 \approx 0{,}41 \pm 0{,}03$. Tuloksessa on kaksi merkitsevää numeroa, koska kulmat on luettu asteen tarkkuudella ja niiden hajonta on noin $\pm 1{,}5^\circ$. Epävarmuus on puolet tulosten vaihteluvälistä ($0{,}384\text{–}0{,}445$). Tämä on tässä valittu yksinkertainen arvio.
**Järkevyys:** Silikoni on pitävä materiaali eli se ei liu'u helposti. Siksi kerroin $0{,}4$ on uskottava. Mittausten mukaan rajakulma on noin $22^\circ$, ja $\tan 22{,}5^\circ \approx 0{,}41$ sopii siihen. Raportin arvo $0{,}54$ vastaisi rajakulmaa $28^\circ$. Yksikään huolellinen mittaus ei antanut tätä kulmaa.

### b)
**Kysytty:** raportin menetelmän ja johtopäätöksen virheet ja puutteet
**Periaate:** Luotettava tulos vaatii neljä asiaa: oikean mallin, kaikkien mittausten perustellun käsittelyn, epävarmuuden arvion ja johtopäätöksen, joka ei mene aineiston ulkopuolelle.
**Mallivastaus:** *Malli.* Kaava $\mu_0 = \sin\alpha_0$ on väärä. Liukumisen rajalla $mg\sin\alpha_0 = \mu_0 mg\cos\alpha_0$, joten $\mu_0 = \tan\alpha_0$.

*Tulosten käsittely.* Ryhmä valitsi suurimman kulman. Juuri siinä mittauksessa on kuitenkin kirjattu karkea virhe. Oikein olisi laskea keskiarvo huolellisista mittauksista ja kertoa, miksi mittaus 5 jätettiin pois. Raportissa ei ole epävarmuutta, vaikka kulmat vaihtelevat $21^\circ$:sta $24^\circ$:seen.

*Menetelmä.* Käsin nostaminen ei ole tasaista. Kulman lukeminen juuri liukumisen hetkellä on vaikeaa. Videokuvaus on hyvä. Kulmamittarin pitäisi kuitenkin olla kiinni kirjassa. Kirjaa pitäisi nostaa hitaasti ja tasaisesti, esimerkiksi ruuvilla tai kirjapinon avulla.

*Johtopäätös.* Tulos koskee vain tätä kuorta ja tätä kirjan kantta. Se ei koske kaikkia pintoja. Lisäksi oikealla kaavalla rajakulma on noin $22^\circ$, ei $33^\circ$. Puhelin lähtee liukumaan jo noin $22^\circ$:n kulmassa.

### c)
**Kysytty:** koe, jolla samoille pinnoille määritetään liikekitkakerroin
**Periaate:** Liikekitka vaikuttaa liukuvaan kappaleeseen. Sen suuruus saadaan Newtonin laeista. Mitataan joko veto tasaisella nopeudella tai kiihtyvyys rinteessä.
**Mallivastaus:** *Menetelmä 1, veto.* Kirja on vaakasuoralla pöydällä. Puhelimeen kiinnitetään lanka ja voima-anturi (tai jousivaaka). Puhelinta vedetään vaakasuoraan tasaisella nopeudella. Silloin veto on yhtä suuri kuin liikekitka, ja tukivoima on yhtä suuri kuin paino: $\mu = \dfrac{F}{mg}$. Puhelimen massa punnitaan vaa'alla. Massaa muutetaan lisäämällä puhelimen päälle punnuksia. $(N, F_\mu)$-pisteisiin sovitetaan suora, joka kulkee origon kautta. Suoran kulmakerroin on $\mu$.

*Menetelmä 2, kiihtyvyys.* Kantta kallistetaan jyrkemmäksi kuin rajakulma, esimerkiksi $30^\circ$:een. Puhelin päästetään liukumaan levosta. Kiihtyvyys mitataan videolta tai puhelimen omalla kiihtyvyysanturilla. Voimakuviosta saadaan $\mu = \dfrac{g\sin\alpha - a}{g\cos\alpha}$.

*Luotettavuus.* Jokainen mittaus toistetaan monta kertaa. Tuloksista lasketaan keskiarvo ja hajonta. Pinnat puhdistetaan joka kerta samalla tavalla. Vedossa nopeuden on oltava tasainen. Sen näkee siitä, että anturin lukema pysyy tasaisena.

### Yleisiä virheitä
- Mittaus 5 poistetaan vain siksi, että se poikkeaa muista. Tai se otetaan mukaan keskiarvoon, vaikka karkea virhe on kirjattu.
- Kerroin lasketaan sinillä tai kosinilla, vaikka pitäisi käyttää tangenttia.
- Kertoimelle annetaan yksikkö.
- c-kohdassa vetoa ei tehdä tasaisella nopeudella. Silloin veto ei ole yhtä suuri kuin kitka. Tai liikekitkaa yritetään mitata rajakulmasta, vaikka rajakulma antaa lepokitkan.

### Hyväksytään myös
- a-kohdassa lasketaan kunkin kulman tangentti erikseen ja niiden keskiarvo ($0{,}415$).
- Epävarmuutena käytetään keskiarvon keskivirhettä, kun se on laskettu ja nimetty oikein.

## fy9-voimat-s6

### a)
**Annettu:** rinteen pituus $L = 40\,\text{m}$, kaltevuuskulma $\alpha = 12^\circ$, liikekitkakerroin $\mu = 0{,}080$, alkunopeus $0$, $g = 9{,}81\,\text{m/s}^2$; ilmanvastusta ei oteta huomioon
**Kysytty:** nopeus $v$ rinteen alapäässä
**Periaate:** Laskijaan vaikuttavat paino, rinteen tukivoima ja liikekitka rinnettä ylös. Voimat ovat vakiot, joten kiihtyvyys on vakio (luku *Paino, kitka ja kalteva taso*). Siksi tasaisesti kiihtyvän liikkeen yhtälöt pätevät eli ovat voimassa (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*).
**Voimakuvio:** Laskija on rinteen suuntainen suorakulmio. $x$-akseli osoittaa rinnettä alas. Paino $\overline{G}$ lähtee keskipisteestä suoraan alas. Tukivoima $\overline{N}$ on kohtisuorassa rinnettä vastaan ja osoittaa rinteestä ulos. Liikekitka $\overline{F}_\mu$ lähtee alapinnan ylemmästä kulmasta rinnettä ylös. Painon komponentit piirretään katkoviivoilla.
```voimakuvio
pinta -12
G 100
N 97,81
F_mu 7,82 ylös
a alas
akselit -12
komponentit G
```
**Kaava:** $y$: $N = mg\cos\alpha$; $x$: $mg\sin\alpha - \mu mg\cos\alpha = ma_1$, joten $a_1 = g(\sin\alpha - \mu\cos\alpha)$. Kun laskija lähtee levosta, $v^2 = 2a_1 L$, joten $v = \sqrt{2gL(\sin\alpha - \mu\cos\alpha)}$
**Muunnokset:** Ei tarvita. Suureet ovat perusyksiköissä.
**Sijoitus:** $a_1 = 9{,}81\,\text{m/s}^2 \cdot (\sin 12^\circ - 0{,}080 \cdot \cos 12^\circ) = 9{,}81\,\text{m/s}^2 \cdot (0{,}2079 - 0{,}0783) = 1{,}272\,\text{m/s}^2$ ja $v = \sqrt{2 \cdot 1{,}272\,\text{m/s}^2 \cdot 40\,\text{m}} = \sqrt{101{,}76\,\text{m}^2/\text{s}^2} = 10{,}09\,\text{m/s}$
**Vastaus:** $v \approx 10\,\text{m/s}$. Tuloksessa on kaksi merkitsevää numeroa, kuten rinteen pituudessa $40\,\text{m}$.
**Järkevyys:** $10{,}09\,\text{m/s} = 10{,}09 \cdot 3{,}6\,\text{km/h} \approx 36\,\text{km/h}$. Se on liukurille nopea mutta mahdollinen nopeus. Lasku kestää $t = v : a_1 \approx 7{,}9\,\text{s}$. Ilman kitkaa nopeus olisi $\sqrt{2gL\sin\alpha} \approx 12{,}8\,\text{m/s}$. Kitka siis pienentää nopeutta selvästi.

### b)
**Annettu:** a-kohdasta $v = 10{,}09\,\text{m/s}$, $\mu = 0{,}080$, loppunopeus $0$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** liukumatka $s_2$ pellolla
**Periaate:** Rinteen ja pellon välinen kohta on loiva. Siksi nopeus pellon alussa on a-kohdan nopeus. Vaakasuoralla pellolla tukivoima on yhtä suuri kuin paino. Ainoa vaakasuora voima on liikekitka taaksepäin. Hidastuvuus on vakio, joten tasaisesti kiihtyvän liikkeen yhtälöt pätevät.
**Voimakuvio:** Laskija on suorakulmio. Paino $\overline{G}$ osoittaa alas, tukivoima $\overline{N}$ ylös ja liikekitka $\overline{F}_\mu$ taaksepäin. Kiihtyvyys osoittaa taaksepäin ja nopeus eteenpäin.
```voimakuvio
pinta 0
G 100
N 100
F_mu 8 vasen
a vasen
v oikea
```
**Kaava:** $-\mu mg = ma_2$, joten $a_2 = -\mu g$. Yhtälöstä $0 - v^2 = 2a_2 s_2$ saadaan $s_2 = \dfrac{v^2}{2\mu g}$
**Muunnokset:** Ei tarvita. Suureet ovat perusyksiköissä.
**Sijoitus:** $s_2 = \dfrac{101{,}76\,\text{m}^2/\text{s}^2}{2 \cdot 0{,}080 \cdot 9{,}81\,\text{m/s}^2} = \dfrac{101{,}76\,\text{m}^2/\text{s}^2}{1{,}5696\,\text{m/s}^2} = 64{,}83\,\text{m}$
**Vastaus:** $s_2 \approx 65\,\text{m}$. Tuloksessa on kaksi merkitsevää numeroa, kuten rinteen pituudessa ja kitkakertoimessa.
**Järkevyys:** Pellolla hidastuvuus $0{,}785\,\text{m/s}^2$ on pienempi kuin rinteen kiihtyvyys $1{,}272\,\text{m/s}^2$. Siksi pysähtymismatka on rinnettä pidempi samassa suhteessa: $40\,\text{m} \cdot 1{,}272 : 0{,}785 \approx 65\,\text{m}$. Matka on pitkä, mutta tamppautuneella eli tiiviiksi painetulla lumella se on mahdollinen.

### c)
**Kysytty:** liukuuko raskas isä pidemmälle kuin kevyet lapset mallissa ja silloin, kun ilmanvastus otetaan huomioon
**Periaate:** Mallissa kaikki voimat ovat verrannollisia massaan. Siksi massa supistuu liikeyhtälöistä. Ilmanvastus riippuu nopeudesta sekä laskijan koosta ja asennosta. Se ei riipu massasta (luku *Ilmanvastus ja putoaminen ilmassa*).
**Mallivastaus:** a- ja b-kohdan mallissa $a_1 = g(\sin\alpha - \mu\cos\alpha)$ ja $a_2 = -\mu g$. Massa ei siis vaikuta nopeuteen eikä liukumatkaan. Isä ja lapset pysähtyvät samaan kohtaan. Todellisuudessa ilmanvastus $F_\text{v}$ hidastaa jokaista lisää. Se muuttaa laskijan kiihtyvyyttä määrällä $F_\text{v} : m$. Isä on suurempi kuin lapsi. Siksi isän ilmanvastus on samalla nopeudella vähän suurempi. Isän massa on kuitenkin paljon suurempi. Siksi ilmanvastus on pienempi osa hänen painostaan. Isän hidastuvuus kasvaa siis vähemmän, ja hän liukuu todennäköisesti pidemmälle. Väite voi siis pitää paikkansa. Syy on kuitenkin ilmanvastus. Syy ei ole se, että raskas laskija painaisi liukuria eteenpäin. Myös asento, liukurin pohja ja lumen kohta vaikuttavat tulokseen.

### Yleisiä virheitä
- Rinteessä kitkaksi otetaan $\mu mg$, vaikka $N = mg\cos\alpha$.
- Pellolla käytetään rinteen kiihtyvyyttä. Tai nopeus lasketaan kaavalla $v = a t$, vaikka aikaa ei tiedetä.
- Kitka unohdetaan rinteessä. Silloin nopeudesta tulee liian suuri.
- c-kohdassa väitetään, että mallin mukaan raskas laskija liukuu pidemmälle, koska hänen painonsa on suurempi.

### Hyväksytään myös
- a- ja b-kohdan ratkaisu työn ja energian avulla, kun tulokset ovat samat ($v^2 = 2gL(\sin\alpha - \mu\cos\alpha)$ ja $\mu mg s_2 = \tfrac{1}{2}mv^2$).
