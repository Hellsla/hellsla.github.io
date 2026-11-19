## fy9-voimat-s1

### a)
**Kysytty:** veneen voimakuvio, kun vinssi vetää venettä luiskaa ylös tasaisella nopeudella
**Periaate:** Valitaan kappaleeksi vene ja etsitään sen vuorovaikutukset: Maa (paino), luiskan liukulistat (tukivoima ja kitka) ja vaijeri (jännitysvoima). Vene liukuu luiskaa ylös, joten liukukitka osoittaa luiskaa alas. Nopeus on vakio, joten voimien summa on nolla.
**Mallivastaus:** Vene piirretään luiskan suuntaiseksi suorakulmioksi.
- Paino $\overline{G}$ lähtee keskipisteestä suoraan alas, ei kohtisuoraan luiskaa vastaan.
- Tukivoima $\overline{N}$ lähtee pohjasta kohtisuoraan luiskasta ulospäin. Se on yhtä suuri kuin painon luiskaa vastaan kohtisuora komponentti, joten se on hieman painoa pienempi.
- Liukukitka $\overline{F}_\mu$ lähtee pohjan alemmasta kulmasta luiskaa alas.
- Vaijerin jännitysvoima $\overline{T}$ lähtee keulasta luiskaa ylös.

Nuolten pituudet: $\overline{T}$ on yhtä pitkä kuin kitka ja painon luiskan suuntainen komponentti yhteensä, koska kokonaisvoima on nolla. Nopeuden saa merkitä erikseen kuvion viereen, mutta ei voimaksi.
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
**Annettu:** massa $m = 280\,\text{kg}$, luiskan kaltevuuskulma $\alpha = 14^\circ$, liukukitkakerroin $\mu = 0{,}25$, nopeus vakio, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** vaijerin jännitysvoima $T$
**Periaate:** Nopeus on vakio, joten Newtonin ensimmäisen lain mukaan voimien summa on nolla sekä luiskan suunnassa että sitä vastaan kohtisuorassa. Vene liukuu, joten kitka on liukukitkaa $\mu N$, ja kohtisuorassa suunnassa vaikuttavat vain painon komponentti ja tukivoima (luku *Paino, kitka ja kalteva taso*).
**Voimakuvio:** a-kohdan kuvio; $x$-akseli luiskaa ylös ja $y$-akseli kohtisuoraan luiskasta ulos. Painon komponentit ovat $G_x = mg\sin\alpha$ luiskaa alas ja $G_y = mg\cos\alpha$ luiskaa kohti.
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
**Muunnokset:** Ei tarvita, suureet ovat perusyksiköissä.
**Sijoitus:** $$
\begin{aligned}
T &= 280\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \\
&\cdot (\sin 14^\circ + 0{,}25 \cdot \cos 14^\circ) \\
&= 2746{,}8\,\text{N} \\
&\cdot (0{,}2419 + 0{,}2426) \\
&= 1330{,}8\,\text{N}
\end{aligned}
$$
**Vastaus:** $T \approx 1{,}3\,\text{kN}$, kaksi merkitsevää numeroa kuten kulmassa $14^\circ$ ja kitkakertoimessa $0{,}25$.
**Järkevyys:** Painon luiskan suuntainen komponentti on $665\,\text{N}$ ja kitka $666\,\text{N}$, joten vinssi tekee kitkaa vastaan lähes yhtä paljon kuin nostaa venettä. Veto on noin puolet painosta $2{,}7\,\text{kN}$: luiska pienentää tarvittavaa voimaa, ei työtä, mutta kitka syö siitä hyödystä paljon.

### c)
**Annettu:** $m = 280\,\text{kg}$, $\alpha = 14^\circ$, lepokitkakerroin $\mu_0 = 0{,}35$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** pysyykö vene levossa, ja pienin kaltevuuskulma $\alpha_0$, jolla vene lähtee itsestään liukumaan
**Periaate:** Vaijerin löystyttyä veneeseen vaikuttavat paino, tukivoima ja lepokitka, joka osoittaa luiskaa ylös. Lepokitka on vain niin suuri kuin tilanne vaatii, enintään $\mu_0 N$. Vene pysyy paikallaan, jos tarvittava lepokitka $mg\sin\alpha$ ei ylitä tätä ylärajaa (luku *Paino, kitka ja kalteva taso*).
**Voimakuvio:** Vene luiskan suuntaisena suorakulmiona: paino keskipisteestä alas, tukivoima pohjasta kohtisuoraan luiskasta ulos ja lepokitka pohjan ylemmästä kulmasta luiskaa ylös, yhtä suurena kuin painon luiskan suuntainen komponentti.
```voimakuvio
pinta 14
G 2746,8
N 2665,2
F_mu 664,5 ylös
a 0
```
**Kaava:** Vene pysyy, kun $mg\sin\alpha \le \mu_0 mg\cos\alpha$ eli $\tan\alpha \le \mu_0$. Rajakulmalla $\tan\alpha_0 = \mu_0$, joten $\alpha_0 = \arctan\mu_0$
**Muunnokset:** Ei tarvita. Massa supistuu.
**Sijoitus:** Tarvittava lepokitka $mg\sin\alpha = 2746{,}8\,\text{N} \cdot \sin 14^\circ = 664{,}5\,\text{N}$ ja yläraja $$
\begin{aligned}
\mu_0 mg\cos\alpha &= 0{,}35 \cdot 2746{,}8\,\text{N} \\
&\cdot \cos 14^\circ \\
&= 932{,}8\,\text{N}
\end{aligned}
$$; rajakulma $\alpha_0 = \arctan 0{,}35 = 19{,}29^\circ$
**Vastaus:** Vene pysyy paikallaan, koska $664{,}5\,\text{N} < 932{,}8\,\text{N}$ (yhtä hyvin $\tan 14^\circ \approx 0{,}25 < 0{,}35$). Itsestään se lähtisi liukumaan, jos luiska olisi vähintään noin $19^\circ$:n kulmassa; kaksi merkitsevää numeroa kuten kitkakertoimessa $0{,}35$.
**Järkevyys:** Rajakulma ei riipu massasta, koska sekä alas vievä komponentti että kitkan yläraja ovat verrannollisia massaan. Märkä, liukas tai jäinen lista voi pienentää lepokitkakerrointa, jolloin vene voi lähteä liikkeelle loivemmallakin luiskalla: venettä ei kannata jättää pelkän kitkan varaan.

### Yleisiä virheitä
- Voimakuvioon piirretään luiskaa ylös vievä ”liikkeen voima” vaijerin voiman lisäksi, tai painon komponentit omiksi voimikseen painon lisäksi.
- Tukivoimaksi otetaan $N = mg$, vaikka luiskalla $N = mg\cos\alpha$.
- Kitka piirretään luiskaa ylös, vaikka vene liukuu ylös ja liukukitka vastustaa liukumista.
- c-kohdassa lepokitkaksi otetaan suoraan $\mu_0 N$, vaikka se on vain yläraja; tai liukumisehto kirjoitetaan sinin avulla, $\sin\alpha_0 = \mu_0$.

### Hyväksytään myös
- c-kohdassa vertailu $\tan 14^\circ \approx 0{,}25 < \mu_0 = 0{,}35$ ilman voimien lukuarvoja.

## fy9-voimat-s2

### a)
**Kysytty:** reen A ja reen B voimakuviot kiihdytyksen aikana
**Periaate:** Kytketyistä kappaleista kumpikin valitaan vuorollaan kappaleeksi, ja kummallekin piirretään oma kuvio, jossa ovat vain siihen vaikuttavat voimat. Köysi vetää kumpaakin rekeä itseään kohti: köysi 2 vetää A:ta taaksepäin ja B:tä eteenpäin samansuuruisella voimalla, koska köysi on kevyt.
**Mallivastaus:** Kumpikin reki piirretään omaksi suorakulmiokseen.
- Reki A: paino $\overline{G}_\text{A}$ alas, tukivoima $\overline{N}_\text{A}$ ylös, köyden 1 voima $\overline{T}_1$ eteenpäin, köyden 2 voima $\overline{T}_2$ taaksepäin ja liukukitka $\overline{F}_{\mu\text{A}}$ taaksepäin.
- Reki B: paino $\overline{G}_\text{B}$ alas, tukivoima $\overline{N}_\text{B}$ ylös, köyden 2 voima $\overline{T}_2$ eteenpäin ja liukukitka $\overline{F}_{\mu\text{B}}$ taaksepäin.

Kummankin reen kokonaisvoima osoittaa eteenpäin, koska reet kiihtyvät. Kiihtyvyys merkitään kuvioiden viereen omalla värillään. Kelkkaa ei piirretä, eikä B:n voimaa köyteen piirretä B:n kuvioon. Vaakasuorat voimat on piirretty omassa mittakaavassaan, koska ne ovat paljon painoja pienempiä.
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
**Annettu:** $m_\text{B} = 80\,\text{kg}$, liukukitkakerroin $\mu = 0{,}10$, kiihtyvyys $a = 0{,}50\,\text{m/s}^2$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** köyden 2 jännitysvoima $T_2$
**Periaate:** Reen B vaakasuorat voimat ovat köyden 2 veto eteenpäin ja kitka taaksepäin. Newtonin toisen lain mukaan niiden summa on $m_\text{B} a$. Pystysuunnassa ei ole kiihtyvyyttä, joten $N_\text{B} = m_\text{B} g$ ja kitka on $\mu m_\text{B} g$ (luku *Liikeyhtälö kytketyille kappaleille*).
**Kaava:** $T_2 - \mu m_\text{B} g = m_\text{B} a$, joten $T_2 = m_\text{B}(a + \mu g)$
**Muunnokset:** Ei tarvita, suureet ovat perusyksiköissä.
**Sijoitus:** $$
\begin{aligned}
T_2 &= 80\,\text{kg} \cdot (0{,}50\,\text{m/s}^2 \\
&+ 0{,}10 \cdot 9{,}81\,\text{m/s}^2) \\
&= 80\,\text{kg} \cdot 1{,}481\,\text{m/s}^2 \\
&= 118{,}48\,\text{N}
\end{aligned}
$$
**Vastaus:** $T_2 \approx 120\,\text{N}$, kaksi merkitsevää numeroa kuten kiihtyvyydessä $0{,}50\,\text{m/s}^2$ ja kitkakertoimessa $0{,}10$.
**Järkevyys:** B:n kitka on $$
\begin{aligned}
&0{,}10 \cdot 80\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \\
&\approx 78\,\text{N}
\end{aligned}
$$ ja kiihdyttämiseen tarvitaan $80\,\text{kg} \cdot 0{,}50\,\text{m/s}^2 = 40\,\text{N}$; yhteensä noin $118\,\text{N}$, kuten pitää.

### c)
**Annettu:** $m_\text{A} = 120\,\text{kg}$, $m_\text{B} = 80\,\text{kg}$, $\mu = 0{,}10$, $a = 0{,}50\,\text{m/s}^2$, b-kohdasta $T_2 = 118{,}48\,\text{N}$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** köyden 1 jännitysvoima $T_1$
**Periaate:** Reen A vaakasuorat voimat ovat köyden 1 veto eteenpäin sekä köyden 2 veto ja kitka taaksepäin, ja niiden summa on $m_\text{A} a$. Saman tuloksen antaa molempien rekien systeemi, jossa köyden 2 voimat ovat sisäisiä ja kumoavat toisensa.
**Kaava:** $T_1 - T_2 - \mu m_\text{A} g = m_\text{A} a$, joten $T_1 = T_2 + m_\text{A}(a + \mu g) = (m_\text{A} + m_\text{B})(a + \mu g)$
**Muunnokset:** Ei tarvita, suureet ovat perusyksiköissä.
**Sijoitus:** $$
\begin{aligned}
T_1 &= 118{,}48\,\text{N} \\
&+ 120\,\text{kg} \cdot 1{,}481\,\text{m/s}^2 \\
&= 118{,}48\,\text{N} + 177{,}72\,\text{N} \\
&= 296{,}2\,\text{N}
\end{aligned}
$$
**Vastaus:** $T_1 \approx 300\,\text{N}$ ($296\,\text{N}$), kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Systeemin tarkistus: $$
\begin{aligned}
&(120 + 80)\,\text{kg} \cdot 1{,}481\,\text{m/s}^2 \\
&= 296{,}2\,\text{N}
\end{aligned}
$$, sama tulos. Etummainen köysi on kireämpi, koska se kiihdyttää ja vetää molempia rekiä.

### d)
**Kysytty:** pitääkö väite ”takimmaisen köyden voima on puolet etummaisen voimasta” paikkansa
**Periaate:** Kumpikin köysi vetää kaikkia niitä rekiä, jotka ovat sen takana. Kun kitkakerroin on sama, jokainen reki tarvitsee vetoa $m(a + \mu g)$, eli vedon tarve on verrannollinen massaan.
**Mallivastaus:** Väite ei pidä. Köysi 2 vetää vain rekeä B, köysi 1 molempia rekiä. b- ja c-kohdan tuloksista $$
\begin{aligned}
&T_2 : T_1 \\
&= 118\,\text{N} : 296\,\text{N} \\
&= 0{,}40
\end{aligned}
$$, mikä on sama kuin massojen suhde $80\,\text{kg} : 200\,\text{kg}$. Suhde riippuu siis rekien massoista, ei niiden lukumäärästä. Puolet se olisi vain, jos reet olisivat yhtä raskaat ja niillä olisi sama kitkakerroin.

### Yleisiä virheitä
- Molemmat reet piirretään yhteen kuvioon, tai kelkan voima piirretään suoraan rekeen B.
- Reen A kuviosta puuttuu köyden 2 taaksepäin vetävä voima, jolloin $T_1$ saadaan liian pieneksi ($T_1 = m_\text{A}(a + \mu g) \approx 178\,\text{N}$).
- Kitka unohdetaan, ja jännitysvoimaksi lasketaan pelkkä $ma$.
- Köyden voimat $\overline{T}_1$ ja $\overline{T}_2$ nimetään samalla symbolilla, jolloin yhtälöistä ei näe, kumpi köysi on kyseessä.

### Hyväksytään myös
- c-kohdassa molempien rekien käsittely yhtenä kappaleena, kun ratkaisussa todetaan, että köyden 2 voimat ovat systeemin sisäisiä.

## fy9-voimat-s3

### a)
**Kysytty:** vaunun kiihtyvyys vetävän voiman funktiona kuvaajana ja siihen sovitettu malli
**Kuvaaja:** Vaaka-akselilla on vetävä voima $F\ (\text{N})$ ja pystyakselilla kiihtyvyys $a\ (\text{m/s}^2)$. Vaaka-akseli alkaa nollasta, jotta suoran ja akselin leikkauskohta näkyy.

<svg data-fig="fy9-voimat-s3-graph" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: vaunun kiihtyvyys a vetävän voiman F funktiona. Seitsemän mustaa pistettä voimilla 0,40–1,60 N. Pisteisiin on sovitettu nouseva suora, jota on jatkettu katkoviivana alas vaaka-akselille asti. Suora kulkee pisteiden (0,40 N; 0,19 m/s²) ja (1,60 N; 1,60 m/s²) kautta; nämä kaksi suoran pistettä on ympyröity. Suora leikkaa vaaka-akselin noin kohdassa F = 0,24 N, eikä se kulje origon kautta." style="max-width:100%;font-size:24px">
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

**Mallivastaus:** Pisteet ovat lähes suoralla, joten kiihtyvyys kasvaa tasaisesti vetävän voiman kasvaessa. Pisteisiin sovitetaan yksi suora, joka kulkee pisteiden lomitse, eikä pisteitä yhdistetä murtoviivaksi. Todellisissa mittaussarjoissa mittauspisteet eivät yleensä sijaitse täsmälleen samalla suoralla mittausepävarmuuden vuoksi. Suora ei kulje origon kautta: se leikkaa vaaka-akselin noin kohdassa $0{,}24\,\text{N}$. Siksi suoraa ei pakoteta origon kautta, vaan sitä jatketaan vaaka-akselille b-kohtaa varten.

### b)
**Annettu:** a-kohdan kuvaaja ja suoralta luetut pisteet
**Kysytty:** vaunun massa $m$ ja kitkavoima $F_\mu$
**Periaate:** Vaunuun vaikuttavat vaakasuunnassa langan veto $F$ eteenpäin ja kitka $F_\mu$ taaksepäin. Newtonin toisen lain mukaan $F - F_\mu = ma$, joten $a = \tfrac{1}{m}F - \tfrac{F_\mu}{m}$ on suoran yhtälö: kulmakerroin on $\tfrac{1}{m}$, ja suora leikkaa vaaka-akselin kohdassa $F = F_\mu$, jossa veto juuri ja juuri kumoaa kitkan. Siksi suora ei kulje origon kautta (luku *Newtonin toinen laki*).
**Kuvaajan lukeminen:** Suoralta luetaan kaksi kaukana toisistaan olevaa pistettä, ei mittauspisteitä: $(0{,}40\,\text{N};\ 0{,}19\,\text{m/s}^2)$ ja $(1{,}60\,\text{N};\ 1{,}60\,\text{m/s}^2)$. Suora leikkaa vaaka-akselin noin kohdassa $F_0 = 0{,}24\,\text{N}$.
**Kaava:** $k = \dfrac{\Delta a}{\Delta F} = \dfrac{1}{m}$, joten $m = \dfrac{1}{k}$; ja $F_\mu = F_0 = F_1 - \dfrac{a_1}{k}$
**Muunnokset:** $1\,\tfrac{\text{m/s}^2}{\text{N}} = 1\,\tfrac{\text{m/s}^2}{\text{kg} \cdot \text{m/s}^2} = 1\,\tfrac{1}{\text{kg}}$, joten kulmakertoimen käänteisluku on kilogrammoja.
**Sijoitus:** $k = \dfrac{1{,}60\,\text{m/s}^2 - 0{,}19\,\text{m/s}^2}{1{,}60\,\text{N} - 0{,}40\,\text{N}} = \dfrac{1{,}41\,\text{m/s}^2}{1{,}20\,\text{N}} = 1{,}175\,\tfrac{1}{\text{kg}}$, joten $m = \dfrac{1}{1{,}175\,\tfrac{1}{\text{kg}}} = 0{,}851\,\text{kg}$ ja $F_\mu = 0{,}40\,\text{N} - \dfrac{0{,}19\,\text{m/s}^2}{1{,}175\,\tfrac{1}{\text{kg}}} = 0{,}238\,\text{N}$
**Vastaus:** $m \approx 0{,}85\,\text{kg}$ ja $F_\mu \approx 0{,}24\,\text{N}$, kaksi merkitsevää numeroa, koska suoralta luettu kulmakerroin on noin $\pm 0{,}03\,\tfrac{1}{\text{kg}}$ tarkka.
**Järkevyys:** Laboratoriovaunun massa on tyypillisesti alle kilogramman. Pienimmän neliösumman suora antaa saman: $k = 1{,}175\,\tfrac{1}{\text{kg}}$ ja leikkauskohta $0{,}239\,\text{N}$. Kitka on pieni verrattuna vetoon, kuten pyörillä kulkevalla vaunulla pitää.

### c)
**Kysytty:** vaunun voimakuvio, kun $F = 1{,}20\,\text{N}$, ja sen yhteys b-kohdan malliin
**Periaate:** Vaunuun vaikuttavat Maa (paino), rata (tukivoima ja kitka) ja lanka (veto). Lanka on vaakasuora, joten pystysuunnassa vaikuttavat vain paino ja tukivoima, ja ne kumoavat toisensa.
**Mallivastaus:** Vaunu piirretään suorakulmioksi. Paino $\overline{G}$ keskipisteestä alas ja tukivoima $\overline{N}$ alapinnasta ylös, yhtä pitkinä. Langan veto $\overline{T}$ lähtee kiinnityskohdasta eteenpäin, ja kitka $\overline{F}_\mu$ alapinnan takakulmasta taaksepäin, noin viidesosa vedosta. Kiihtyvyys merkitään erikseen kuvion viereen.

Vaakasuorat voimat on piirretty omassa mittakaavassaan, koska ne ovat paljon painoa pienempiä.
```voimakuvio
pinta 0
G 8,35
N 8,35
T 1,20 0
F_mu 0,24 vasen
a oikea
```
Vaakasuunnan liikeyhtälö kuviosta on $T - F_\mu = ma$, sama kuin b-kohdan suoran yhtälö, kun $T = F$. Kuvion kokonaisvoima $1{,}20\,\text{N} - 0{,}24\,\text{N} = 0{,}96\,\text{N}$ antaa kiihtyvyyden $0{,}96\,\text{N} : 0{,}851\,\text{kg} \approx 1{,}13\,\text{m/s}^2$, joka on lähellä mitattua $1{,}14\,\text{m/s}^2$.

### d)
**Annettu:** b-kohdasta $m = 0{,}851\,\text{kg}$ ja $F_\mu = 0{,}238\,\text{N}$; lisäpunnus $m_\text{x} = 0{,}500\,\text{kg}$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** kerroin $\mu = \tfrac{F_\mu}{N}$ ja suoran muutos lisäpunnuksella
**Periaate:** Lanka on vaakasuora, joten pystysuunnassa vaikuttavat vain paino ja tukivoima, ja $N = mg$ (luku *Paino, kitka ja kalteva taso*). Mallissa kitka on verrannollinen tukivoimaan.
**Kaava:** $\mu = \dfrac{F_\mu}{N} = \dfrac{F_\mu}{mg}$; lisäpunnuksella $m' = m + m_\text{x}$, suoran kulmakerroin on $k' = \dfrac{1}{m'}$ ja leikkauskohta vaaka-akselilla $F_0' = \mu m' g$
**Muunnokset:** Ei tarvita, suureet ovat perusyksiköissä.
**Sijoitus:** $\mu = \dfrac{0{,}238\,\text{N}}{0{,}851\,\text{kg} \cdot 9{,}81\,\text{m/s}^2} = \dfrac{0{,}238\,\text{N}}{8{,}35\,\text{N}} = 0{,}0285$
**Vastaus:** $\mu \approx 0{,}029$, kaksi merkitsevää numeroa kuten $F_\mu$; kertoimella ei ole yksikköä. Lisäpunnuksella massa on $1{,}351\,\text{kg}$: suora loivenee, kulmakerroin $\tfrac{1}{1{,}351\,\text{kg}} \approx 0{,}74\,\tfrac{1}{\text{kg}}$, ja leikkauskohta siirtyy oikealle, kohtaan $$
\begin{aligned}
&0{,}029 \cdot 1{,}351\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \\
&\approx 0{,}38\,\text{N}
\end{aligned}
$$.
**Järkevyys:** Pyörillä kulkevan vaunun vierimisvastus on paljon pienempi kuin liukuvan kappaleen kitka, jonka kerroin on tyypillisesti $0{,}2\text{–}0{,}6$, joten $0{,}03$ on uskottava. Ennuste perustuu malliin, jossa kitka ei riipu nopeudesta; se kannattaa tarkistaa toistamalla mittaus punnuksen kanssa.

### Yleisiä virheitä
- Suora pakotetaan origon kautta, jolloin kulmakerroin ja massa tulevat väärin eikä kitkaa saada.
- Kulmakerroin luetaan kahdesta vierekkäisestä mittauspisteestä eikä sovitetusta suorasta.
- Massaksi otetaan kulmakerroin itse ($1{,}18\,\text{kg}$), vaikka kulmakerroin on massan käänteisluku.
- c-kohdassa voimakuvioon piirretään punnusten paino vaunuun, vaikka vaunua vetää lanka.

### Hyväksytään myös
- b-kohdassa silmämääräisesti sovitetun suoran kulmakerroin $1{,}14\text{–}1{,}22\,\tfrac{1}{\text{kg}}$ eli massa $0{,}82\text{–}0{,}88\,\text{kg}$, ja leikkauskohta $0{,}21\text{–}0{,}27\,\text{N}$; d-kohdassa niistä laskettu $\mu \approx 0{,}025\text{–}0{,}032$.
- Laskimen tai taulukkolaskennan suoran sovitus ($a = 1{,}175\,\tfrac{1}{\text{kg}} \cdot F - 0{,}281\,\text{m/s}^2$).

## fy9-voimat-s4

### a)
**Kysytty:** mikä voima kiihdyttää kävelijää eteenpäin ja miksi peilijäällä on vaikeaa lähteä liikkeelle
**Periaate:** Kappaleen liiketilaa muuttavat vain siihen kohdistuvat ulkoiset voimat (Newtonin toinen laki). Voima ja vastavoima vaikuttavat eri kappaleisiin (kolmas laki). Lepokitka on enintään $\mu_0 N$.
**Mallivastaus:** Kun Ella astuu, hänen jalkansa työntää maata taaksepäin. Kolmannen lain mukaan maa työntää jalkaa yhtä suurella voimalla eteenpäin. Tämä voima on maan lepokitka: jalka pyrkii liukumaan taaksepäin maan suhteen, ja kitka estää sen. Se on ainoa vaakasuora ulkoinen voima, joten juuri se kiihdyttää Ellaa eteenpäin.

Ellan lihakset ovat hänen sisäisiä voimiaan, eivätkä ne yksin voi muuttaa koko kehon liiketilaa. Peilijäällä lepokitkakerroin on pieni, joten kitkan yläraja $\mu_0 N$ on pieni. Jos jalka työntää taaksepäin lujemmin kuin kitka pystyy vastustamaan, jalka liukuu. Siksi suurin mahdollinen kiihtyvyys jää pieneksi, ja jäällä kävellään lyhyin askelin jalka lähes pystysuoraan asetettuna.

### b)
**Kysytty:** pitääkö väite ”moottori työntää autoa eteenpäin” paikkansa
**Periaate:** Auton liikkeen muuttavat vain autoon kohdistuvat ulkoiset voimat. Moottori on auton osa, joten sen voimat pyöriin ja koriin ovat sisäisiä voimia, jotka kumoavat toisensa (kolmas laki).
**Mallivastaus:** Väite on vain osittain oikein. Moottori pyörittää etupyöriä, mutta se ei voi yksin työntää koko autoa, koska se on auton sisällä. Pyörivä rengas pyrkii liukumaan taaksepäin tien pinnan suhteen, ja tien lepokitka vastustaa tätä liukumista osoittamalla eteenpäin.

Tämä tien voima vetäviin pyöriin on ulkoinen voima, joka kiihdyttää autoa. Siksi auto ei pääse liikkeelle peilijäällä, vaikka moottori kävisi täysillä: pyörät vain sutivat, koska kitka ei riitä.

### c)
**Kysytty:** kiihtyvän auton voimakuvio, kun ilmanvastus ja vierimisvastus otetaan huomioon
**Periaate:** Autoon vaikuttavat Maa (paino), tie (tukivoima, lepokitka vetäviin pyöriin ja vierimisvastus) ja ilma (ilmanvastus). Auto kiihtyy, joten kokonaisvoima osoittaa eteenpäin.
**Mallivastaus:** Auto piirretään suorakulmioksi. Paino $\overline{G}$ keskipisteestä alas ja tukivoima $\overline{N}$ alapinnasta ylös, yhtä pitkinä. Tien lepokitka vetäviin pyöriin $\overline{F}_\mu$ lähtee alapinnan etukulmasta eteenpäin. Vierimisvastus $\overline{F}_\text{r}$ ja ilmanvastus $\overline{F}_\text{v}$ osoittavat taaksepäin.

Eteenpäin osoittava kitka on vastuksia suurempi, koska auto kiihtyy. Nopeus ja kiihtyvyys merkitään kuvion viereen. Suuruudet ovat havainnollistavia, ja vaakasuorat voimat on piirretty omassa mittakaavassaan. Tukivoiman voi jakaa myös etu- ja takapyörien tukivoimiksi $\overline{N}_1$ ja $\overline{N}_2$.
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
**Kysytty:** suurin tien antama kiihtyvyys asfaltilla ja jäällä sekä miksi etuvetoisella autolla se on pienempi
**Periaate:** Kiihdyttävä voima on tien lepokitka, joka on enintään $\mu_0 N$. Jos kaikki pyörät vetävät, tukivoima on koko auton paino, $N = mg$.
**Mallivastaus:** Suurin kiihdyttävä voima on $\mu_0 mg$, joten $ma_\text{max} = \mu_0 mg$ ja $a_\text{max} = \mu_0 g$; massa supistuu. Asfaltilla $$
\begin{aligned}
a_\text{max} &\approx 0{,}8 \cdot 9{,}81\,\text{m/s}^2 \\
&\approx 8\,\text{m/s}^2
\end{aligned}
$$ ja jäällä $0{,}1 \cdot 9{,}81\,\text{m/s}^2 \approx 1\,\text{m/s}^2$, kun vastukset jätetään huomiotta.

Etuvetoisessa autossa eteenpäin vievä lepokitka vaikuttaa vain vetäviin etupyöriin, ja niiden tukivoima on vain osa auton painosta, esimerkiksi noin puolet. Silloin suurin kiihdyttävä voima on $\mu_0 N_\text{etu} < \mu_0 mg$, ja suurin kiihtyvyys on pienempi. Jäällä etuvetoinen auto voi siis kiihtyä enintään alle $1\,\text{m/s}^2$.

### Yleisiä virheitä
- Kävelijää tai autoa ”työntävät” lihakset tai moottori, eli sisäinen voima esitetään ulkoisena.
- Voima ja vastavoima (jalka työntää maata, maa työntää jalkaa) piirretään samaan voimakuvioon.
- Kitka piirretään aina liikettä vastaan, myös vetäviin pyöriin.
- d-kohdassa kiihtyvyydeksi lasketaan $\mu_0 N$ ilman massalla jakamista, tai jäätä ja asfalttia verrataan ilman lukuja.

## fy9-voimat-s5

### a)
**Annettu:** rajakulmat $22^\circ$, $24^\circ$, $21^\circ$, $23^\circ$ ja $33^\circ$; mittauksessa 5 kirjaa nostettiin nykäisten
**Kysytty:** lepokitkakerroin $\mu_0$ ja sen epävarmuus
**Periaate:** Rajakulmalla painon kannen suuntainen komponentti on yhtä suuri kuin lähtökitka eli täysin kehittynyt lepokitka, ja tukivoima on painon kohtisuora komponentti (luku *Paino, kitka ja kalteva taso*).

Mittaus 5 jätetään pois, koska raporttiin on kirjattu karkea virhe: nopea nosto painaa kantta hetkellisesti puhelinta vasten, jolloin tukivoima ja lepokitkan yläraja kasvavat hetkeksi, ja kulma luetaan myöhässä. Siksi $33^\circ$ ei ole liukumisen raja. Tulosta ei poistettaisi pelkästään siksi, että se poikkeaa muista.
**Kaava:** $mg\sin\alpha_0 = \mu_0 mg\cos\alpha_0$, joten $\mu_0 = \tan\alpha_0$. Rajakulmana käytetään hyväksyttyjen mittausten keskiarvoa $\alpha_\text{ka} = \dfrac{\alpha_1 + \alpha_2 + \alpha_3 + \alpha_4}{4}$, joten $\mu_0 = \tan\alpha_\text{ka}$, ja epävarmuus on puolet vaihteluvälistä, $\Delta\mu_0 = \dfrac{\tan\alpha_\text{max} - \tan\alpha_\text{min}}{2}$
**Muunnokset:** Ei tarvita. Kulmat ovat asteina, ja kertoimella ei ole yksikköä.
**Sijoitus:** $\alpha_\text{ka} = \dfrac{22^\circ + 24^\circ + 21^\circ + 23^\circ}{4} = 22{,}5^\circ$ ja $\mu_0 = \tan 22{,}5^\circ = 0{,}414$. Hajonnan rajat: $\tan 21^\circ = 0{,}384$ ja $\tan 24^\circ = 0{,}445$
**Vastaus:** $\mu_0 \approx 0{,}41 \pm 0{,}03$, kaksi merkitsevää numeroa, koska kulmat on luettu asteen tarkkuudella ja niiden hajonta on noin $\pm 1{,}5^\circ$. Epävarmuus on puolet tulosten vaihteluvälistä ($0{,}384\text{–}0{,}445$), mikä on tässä valittu yksinkertainen arvio.
**Järkevyys:** Silikoni on tunnetusti pitävä materiaali, joten kerroin $0{,}4$ on uskottava. Rajakulma on mittausten mukaan noin $22^\circ$, ja $\tan 22{,}5^\circ \approx 0{,}41$ on johdonmukainen sen kanssa. Raportin arvo $0{,}54$ vastaisi rajakulmaa $28^\circ$, jota yksikään huolellinen mittaus ei antanut.

### b)
**Kysytty:** raportin menetelmän ja johtopäätöksen virheet ja puutteet
**Periaate:** Luotettava tulos vaatii oikean mallin, kaikkien mittausten perustellun käsittelyn, epävarmuuden arvion ja johtopäätöksen, joka ei ulotu aineiston ulkopuolelle.
**Mallivastaus:** *Malli.* Kaava $\mu_0 = \sin\alpha_0$ on väärä. Liukumisen rajalla $mg\sin\alpha_0 = \mu_0 mg\cos\alpha_0$, joten $\mu_0 = \tan\alpha_0$.

*Tulosten käsittely.* Ryhmä valitsi suurimman kulman, vaikka juuri se on mittaus, jossa on kirjattu karkea virhe. Oikein olisi laskea keskiarvo huolellisista mittauksista ja kertoa, miksi mittaus 5 jätettiin pois. Raportissa ei ole epävarmuutta, vaikka kulmat vaihtelevat $21^\circ$:sta $24^\circ$:seen.

*Menetelmä.* Käsin nostaminen ei ole tasaista, ja kulman lukeminen juuri liukumisen hetkellä on vaikeaa. Videokuvaus on hyvä, mutta kulmamittarin pitäisi olla kiinni kirjassa, ja kirjaa pitäisi nostaa hitaasti ja tasaisesti, esimerkiksi ruuvilla tai kirjapinon avulla.

*Johtopäätös.* Tulos koskee vain tätä kuorta ja tätä kirjan kantta, ei kaikkia pintoja. Lisäksi rajakulma on oikealla kaavalla noin $22^\circ$, ei $33^\circ$: puhelin lähtee liukumaan jo noin $22^\circ$:n kulmassa.

### c)
**Kysytty:** koe, jolla samoille pinnoille määritetään liukukitkakerroin
**Periaate:** Liukukitka vaikuttaa liukuvaan kappaleeseen, ja sen suuruus saadaan Newtonin laeista, kun mitataan joko veto tasaisella nopeudella tai kiihtyvyys rinteessä.
**Mallivastaus:** *Menetelmä 1, veto.* Kirja on vaakasuoralla pöydällä, ja puhelimeen kiinnitetään lanka ja voima-anturi (tai jousivaaka). Puhelinta vedetään vaakasuoraan tasaisella nopeudella, jolloin veto on yhtä suuri kuin liukukitka ja tukivoima yhtä suuri kuin paino: $\mu = \dfrac{F}{mg}$. Puhelimen massa punnitaan vaa'alla. Massaa muutetaan lisäämällä puhelimen päälle punnuksia, ja $(N, F_\mu)$-pisteisiin sovitetun origon kautta kulkevan suoran kulmakerroin on $\mu$.

*Menetelmä 2, kiihtyvyys.* Kantta kallistetaan rajakulmaa jyrkemmäksi, esimerkiksi $30^\circ$:een, ja puhelin päästetään liukumaan levosta. Kiihtyvyys mitataan videolta tai puhelimen omalla kiihtyvyysanturilla. Voimakuviosta $\mu = \dfrac{g\sin\alpha - a}{g\cos\alpha}$.

*Luotettavuus.* Jokainen mittaus toistetaan useita kertoja, ja tuloksista lasketaan keskiarvo ja hajonta. Pinnat puhdistetaan samalla tavalla joka kerta. Vedossa nopeuden on oltava tasainen, mikä näkyy anturin lukeman tasaisuutena.

### Yleisiä virheitä
- Mittaus 5 poistetaan vain siksi, että se poikkeaa muista, tai se otetaan mukaan keskiarvoon, vaikka karkea virhe on kirjattu.
- Kerroin lasketaan sinillä tai kosinilla tangentin sijaan.
- Kertoimelle annetaan yksikkö.
- c-kohdassa vetoa ei tehdä tasaisella nopeudella, jolloin veto ei ole yhtä suuri kuin kitka, tai liukukitkaa yritetään mitata rajakulmasta, joka antaa lepokitkan.

### Hyväksytään myös
- a-kohdassa kunkin kulman tangentti erikseen ja niiden keskiarvo ($0{,}415$).
- Epävarmuudeksi keskiarvon keskivirhe, kun se on laskettu ja nimetty oikein.

## fy9-voimat-s6

### a)
**Annettu:** rinteen pituus $L = 40\,\text{m}$, kaltevuuskulma $\alpha = 12^\circ$, liukukitkakerroin $\mu = 0{,}080$, alkunopeus $0$, $g = 9{,}81\,\text{m/s}^2$; ilmanvastus jätetään pois
**Kysytty:** nopeus $v$ rinteen alapäässä
**Periaate:** Laskijaan vaikuttavat paino, rinteen tukivoima ja liukukitka rinnettä ylös. Voimat ovat vakiot, joten kiihtyvyys on vakio (luku *Paino, kitka ja kalteva taso*), ja tasaisesti kiihtyvän liikkeen yhtälöt pätevät (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*).
**Voimakuvio:** Laskija rinteen suuntaisena suorakulmiona, $x$-akseli rinnettä alas. Paino $\overline{G}$ keskipisteestä suoraan alas, tukivoima $\overline{N}$ kohtisuoraan rinteestä ulos ja liukukitka $\overline{F}_\mu$ alapinnan ylemmästä kulmasta rinnettä ylös. Painon komponentit katkoviivoin.
```voimakuvio
pinta -12
G 100
N 97,81
F_mu 7,82 ylös
a alas
akselit -12
komponentit G
```
**Kaava:** $y$: $N = mg\cos\alpha$; $x$: $mg\sin\alpha - \mu mg\cos\alpha = ma_1$, joten $a_1 = g(\sin\alpha - \mu\cos\alpha)$. Levosta lähtevälle $v^2 = 2a_1 L$, joten $v = \sqrt{2gL(\sin\alpha - \mu\cos\alpha)}$
**Muunnokset:** Ei tarvita, suureet ovat perusyksiköissä.
**Sijoitus:** $$
\begin{aligned}
a_1 &= 9{,}81\,\text{m/s}^2 \\
&\cdot (\sin 12^\circ - 0{,}080 \cdot \cos 12^\circ) \\
&= 9{,}81\,\text{m/s}^2 \\
&\cdot (0{,}2079 - 0{,}0783) \\
&= 1{,}272\,\text{m/s}^2
\end{aligned}
$$ ja $v = \sqrt{2 \cdot 1{,}272\,\text{m/s}^2 \cdot 40\,\text{m}} = \sqrt{101{,}76\,\text{m}^2/\text{s}^2} = 10{,}09\,\text{m/s}$
**Vastaus:** $v \approx 10\,\text{m/s}$, kaksi merkitsevää numeroa kuten rinteen pituudessa $40\,\text{m}$.
**Järkevyys:** $10{,}09\,\text{m/s} = 10{,}09 \cdot 3{,}6\,\text{km/h} \approx 36\,\text{km/h}$, liukurille nopea mutta mahdollinen. Lasku kestää $t = v : a_1 \approx 7{,}9\,\text{s}$. Ilman kitkaa nopeus olisi $\sqrt{2gL\sin\alpha} \approx 12{,}8\,\text{m/s}$, joten kitka pienentää sitä selvästi.

### b)
**Annettu:** a-kohdasta $v = 10{,}09\,\text{m/s}$, $\mu = 0{,}080$, loppunopeus $0$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** liukumatka $s_2$ pellolla
**Periaate:** Rinteen ja pellon välinen kohta on loiva, joten pellon alkunopeus on a-kohdan nopeus. Vaakasuoralla pellolla tukivoima on painon suuruinen, ja ainoa vaakasuora voima on liukukitka taaksepäin. Hidastuvuus on vakio, joten tasaisesti kiihtyvän liikkeen yhtälöt pätevät.
**Voimakuvio:** Laskija suorakulmiona: paino $\overline{G}$ alas, tukivoima $\overline{N}$ ylös ja liukukitka $\overline{F}_\mu$ taaksepäin. Kiihtyvyys osoittaa taaksepäin ja nopeus eteenpäin.
```voimakuvio
pinta 0
G 100
N 100
F_mu 8 vasen
a vasen
v oikea
```
**Kaava:** $-\mu mg = ma_2$, joten $a_2 = -\mu g$. Yhtälöstä $0 - v^2 = 2a_2 s_2$ saadaan $s_2 = \dfrac{v^2}{2\mu g}$
**Muunnokset:** Ei tarvita, suureet ovat perusyksiköissä.
**Sijoitus:** $s_2 = \dfrac{101{,}76\,\text{m}^2/\text{s}^2}{2 \cdot 0{,}080 \cdot 9{,}81\,\text{m/s}^2} = \dfrac{101{,}76\,\text{m}^2/\text{s}^2}{1{,}5696\,\text{m/s}^2} = 64{,}83\,\text{m}$
**Vastaus:** $s_2 \approx 65\,\text{m}$, kaksi merkitsevää numeroa kuten rinteen pituudessa ja kitkakertoimessa.
**Järkevyys:** Pellolla hidastuvuus $0{,}785\,\text{m/s}^2$ on pienempi kuin rinteen kiihtyvyys $1{,}272\,\text{m/s}^2$, joten pysähtymismatka on rinnettä pidempi samassa suhteessa: $$
40\,\text{m} \cdot 1{,}272 : 0{,}785 \approx 65\,\text{m}
$$. Matka on tamppautuneella lumella pitkä mutta mahdollinen.

### c)
**Kysytty:** liukuuko raskas isä pidemmälle kuin kevyet lapset mallissa ja kun ilmanvastus otetaan huomioon
**Periaate:** Mallissa kaikki voimat ovat verrannollisia massaan, joten massa supistuu liikeyhtälöistä. Ilmanvastus riippuu nopeudesta, laskijan koosta ja asennosta, mutta ei massasta (luku *Ilmanvastus ja putoaminen ilmassa*).
**Mallivastaus:** a- ja b-kohdan mallissa $a_1 = g(\sin\alpha - \mu\cos\alpha)$ ja $a_2 = -\mu g$, joten massa ei vaikuta nopeuteen eikä liukumatkaan: isä ja lapset pysähtyvät samaan kohtaan. Todellisuudessa ilmanvastus $F_\text{v}$ hidastaa jokaista lisää. Laskijan kiihtyvyyteen se vaikuttaa määrällä $F_\text{v} : m$. Isä on lasta suurempi, joten hänen ilmanvastuksensa on samalla nopeudella vähän suurempi, mutta hänen massansa on paljon suurempi, joten ilmanvastus on pienempi osa hänen painostaan.

Isän hidastuvuus kasvaa siksi vähemmän, ja hän todennäköisesti liukuu pidemmälle. Väite voi siis pitää paikkansa, mutta syy on ilmanvastus eikä se, että raskas laskija painaisi liukuria eteenpäin. Myös asento, liukurin pohja ja lumen kohta vaikuttavat tulokseen.

### Yleisiä virheitä
- Rinteessä kitkaksi otetaan $\mu mg$, vaikka $N = mg\cos\alpha$.
- Pellolla käytetään rinteen kiihtyvyyttä, tai nopeus lasketaan kaavalla $v = a t$ ilman aikaa.
- Kitka unohdetaan rinteessä, jolloin nopeus on liian suuri.
- c-kohdassa väitetään, että raskas laskija liukuu mallin mukaan pidemmälle, koska paino on suurempi.

### Hyväksytään myös
- a- ja b-kohdan ratkaisu työn ja energian avulla, kun tulokset ovat samat ($v^2 = 2gL(\sin\alpha - \mu\cos\alpha)$ ja $\mu mg s_2 = \tfrac{1}{2}mv^2$).

## fy9-voimat-s7

### a)
**Annettu:** kuvaajan pisteet $(0\,\text{s};\ 0\,\text{m/s})$, $(2\,\text{s};\ 18{,}6\,\text{m/s})$, $(6\,\text{s};\ 40{,}4\,\text{m/s})$ ja $(10\,\text{s};\ 46{,}4\,\text{m/s})$; nopeus alaspäin, positiivinen suunta alas
**Kysytty:** keskikiihtyvyydet $a_1$ ($0\ldots 2\,\text{s}$) ja $a_2$ ($6\ldots 10\,\text{s}$)
**Periaate:** Kiihtyvyys on nopeuden muutos jaettuna ajalla (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*). Keskikiihtyvyys on $(t,v)$-kuvaajan pisteitä yhdistävän suoran kulmakerroin.
**Kuvaajan lukeminen:** Pisteet ovat kaukana toisistaan, joten niistä luetaan nopeudet: $0\ldots 2\,\text{s}$: $0$ ja $18{,}6\,\text{m/s}$; $6\ldots 10\,\text{s}$: $40{,}4\,\text{m/s}$ ja $46{,}4\,\text{m/s}$.
**Kaava:** $$
\begin{aligned}
a &= \dfrac{\Delta v}{\Delta t} \\
&= \dfrac{v_2 - v_1}{t_2 - t_1}
\end{aligned}
$$
**Muunnokset:** Ei tarvita: nopeudet ovat yksikössä $\text{m/s}$ ja ajat sekunteina.
**Sijoitus:** $$
\begin{aligned}
a_1 &= \dfrac{18{,}6\,\text{m/s} - 0}{2\,\text{s} - 0} \\
&= 9{,}3\,\text{m/s}^2
\end{aligned}
$$ ja $$
\begin{aligned}
a_2 &= \dfrac{46{,}4\,\text{m/s} - 40{,}4\,\text{m/s}}{10\,\text{s} - 6\,\text{s}} \\
&= \dfrac{6{,}0\,\text{m/s}}{4\,\text{s}} \\
&= 1{,}5\,\text{m/s}^2
\end{aligned}
$$
**Vastaus:** $a_1 \approx 9{,}3\,\text{m/s}^2$ ja $a_2 \approx 1{,}5\,\text{m/s}^2$, kaksi merkitsevää numeroa kuten luetuissa nopeuksissa.
**Järkevyys:** Heti hypyn jälkeen kiihtyvyys on lähellä putoamiskiihtyvyyttä $9{,}81\,\text{m/s}^2$, koska ilmanvastus on vielä pieni. Myöhemmin ilmanvastus on kasvanut lähelle painoa ja kiihtyvyys on pieni; kuvaaja loivenee, mikä sopii tähän.

### b)
**Annettu:** $m = 75{,}0\,\text{kg}$, $a_2 = 1{,}5\,\text{m/s}^2$ välillä $6\ldots 10\,\text{s}$ eli keskiarvona hetkellä $8\,\text{s}$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** ilmanvastus $F_\text{v}$ hetkellä $8\,\text{s}$
**Periaate:** Hyppääjään vaikuttavat paino alas ja ilmanvastus ylös. Newtonin toisen lain mukaan kokonaisvoima on massa kertaa kiihtyvyys (luku *Newtonin toinen laki*, luku *Ilmanvastus ja putoaminen ilmassa*).
**Voimakuvio:** Hyppääjä suorakulmiona, $y$-akseli alas. Paino $\overline{G}$ keskipisteestä alas, ilmanvastus $\overline{F}_\text{v}$ alapinnasta ylös ja hieman painoa lyhyempi, kiihtyvyys ja nopeus alas.
```voimakuvio
G 735,8
F_v 623,3 ylös työntö @ala
a alas
v alas
```
**Kaava:** Alas positiivinen: $mg - F_\text{v} = ma$, joten $F_\text{v} = m(g - a)$
**Muunnokset:** Ei tarvita, suureet ovat perusyksiköissä.
**Sijoitus:** $$
\begin{aligned}
F_\text{v} &= 75{,}0\,\text{kg} \\
&\quad \cdot (9{,}81\,\text{m/s}^2 \\
&\qquad - 1{,}5\,\text{m/s}^2) \\
&= 75{,}0\,\text{kg} \cdot 8{,}31\,\text{m/s}^2 \\
&= 623\,\text{N}
\end{aligned}
$$
**Vastaus:** $$
\begin{aligned}
F_\text{v} &\approx 6{,}2 \cdot 10^2\,\text{N}
\end{aligned}
$$, kaksi merkitsevää numeroa kuten kiihtyvyydessä.
**Järkevyys:** Paino on $mg = 736\,\text{N}$, ja $$
\begin{aligned}
623\,\text{N} : 736\,\text{N} &\approx 0{,}85
\end{aligned}
$$. Ilmanvastus on siis noin $85\,\%$ painosta, mikä sopii pieneen kiihtyvyyteen $1{,}5\,\text{m/s}^2$. Jos ilmanvastus olisi nolla, kiihtyvyys olisi $9{,}81\,\text{m/s}^2$.

### c)
**Annettu:** $F_\text{v} = 623{,}25\,\text{N}$ nopeudella $v = 44{,}5\,\text{m/s}$ (kuvaajan piste hetkellä $8\,\text{s}$), $mg = 735{,}75\,\text{N}$, $F_\text{v} = kv^2$
**Kysytty:** rajanopeus $v_\text{r}$
**Periaate:** Rajanopeudella kiihtyvyys on nolla, joten ilmanvastus on yhtä suuri kuin paino (luku *Ilmanvastus ja putoaminen ilmassa*). Kerroin $k$ pysyy samana, koska asento on sama.
**Voimakuvio:** Hyppääjä suorakulmiona: paino $\overline{G}$ alas ja ilmanvastus $\overline{F}_\text{v}$ ylös, yhtä pitkät; kiihtyvyys on nolla ja nopeus alas.
```voimakuvio
G 735,8
F_v 735,8 ylös työntö @ala
a 0
v alas
```
**Kaava:** Hetkellä $8\,\text{s}$: $F_\text{v} = kv^2$, joten $k = \dfrac{F_\text{v}}{v^2}$. Rajanopeudella: $kv_\text{r}^2 = mg$, joten $$
\begin{aligned}
v_\text{r} &= \sqrt{\dfrac{mg}{k}} \\
&= v\sqrt{\dfrac{mg}{F_\text{v}}}
\end{aligned}
$$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $$
\begin{aligned}
v_\text{r} &= 44{,}5\,\text{m/s} \cdot \sqrt{\dfrac{735{,}75\,\text{N}}{623{,}25\,\text{N}}} \\
&= 44{,}5\,\text{m/s} \cdot 1{,}0865 \\
&= 48{,}4\,\text{m/s}
\end{aligned}
$$
**Vastaus:** $v_\text{r} \approx 48\,\text{m/s}$, kaksi merkitsevää numeroa kuten luetussa nopeudessa.
**Järkevyys:** Kuvaajassa nopeus on hetkellä $12\,\text{s}$ jo $47{,}3\,\text{m/s}$ ja kasvaa yhä hitaasti ($0{,}9\,\text{m/s}$ kahdessa sekunnissa), joten rajanopeus on hieman tätä suurempi. Arvio $$
\begin{aligned}
48\,\text{m/s} &\approx 174\,\text{km/h}
\end{aligned}
$$ on vatsa alaspäin putoavalle hyppääjälle oikean suuruinen.

### d)
**Annettu:** $m' = 100\,\text{kg}$, $m = 75{,}0\,\text{kg}$, b- ja c-kohdan arvoista $$
\begin{aligned}
k &= \dfrac{623{,}25\,\text{N}}{(44{,}5\,\text{m/s})^2} \\
&= 0{,}3147\,\text{kg/m}
\end{aligned}
$$
**Kysytty:** toisen hyppääjän rajanopeus $v_\text{r}'$ ja vertailu
**Periaate:** Rajanopeudella ilmanvastus on yhtä suuri kuin paino, $kv_\text{r}^2 = mg$. Asento ja varusteet ovat samat, joten $k$ on sama. Ilmanvastus riippuu nopeudesta ja asennosta, ei massasta, joten raskaampi hyppääjä tarvitsee suuremman nopeuden saadakseen ilmanvastuksen yhtä suureksi kuin painonsa.
**Mallivastaus:** Rajanopeudelle pätee $v_\text{r} = \sqrt{\dfrac{mg}{k}}$, joten $$
\begin{aligned}
v_\text{r}' &= \sqrt{\dfrac{m'g}{k}} \\
&= \sqrt{\dfrac{100\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{0{,}3147\,\text{kg/m}}} \\
&= \sqrt{3117\,\text{m}^2/\text{s}^2} \\
&= 55{,}8\,\text{m/s}
\end{aligned}
$$ Suhde on $$
\begin{aligned}
\dfrac{v_\text{r}'}{v_\text{r}} &= \sqrt{\dfrac{m'}{m}} \\
&= \sqrt{\dfrac{100\,\text{kg}}{75{,}0\,\text{kg}}} \\
&= 1{,}155
\end{aligned}
$$. Raskaamman hyppääjän rajanopeus on noin $56\,\text{m/s}$ eli noin $15\,\%$ suurempi, vaikka massa on $33\,\%$ suurempi, koska rajanopeus kasvaa massan neliöjuuren mukana. Raskaampi saavuttaa rajanopeuden myös hitaammin, koska hänen painonsa on suurempi ja ilmanvastuksen on kasvettava suuremmaksi.

### Yleisiä virheitä
- Kiihtyvyys luetaan yhdestä pisteestä tai nopeuden arvosta; kiihtyvyys on nopeuden muutos jaettuna ajalla, ei nopeus.
- Ilmanvastukseksi otetaan $mg$ tai $ma$; ilmanvastus on $m(g - a)$, koska paino ja ilmanvastus vaikuttavat yhdessä.
- Rajanopeudeksi otetaan kuvaajan viimeinen piste $47{,}3\,\text{m/s}$, vaikka nopeus kasvaa vielä.
- d-kohdassa väitetään, että rajanopeus on verrannollinen massaan ($100 : 75 \cdot 48\,\text{m/s} \approx 64\,\text{m/s}$), vaikka $v_\text{r} \propto \sqrt{m}$.

### Hyväksytään myös
- a- ja b-kohdan luvut luetuilla arvoilla, jotka poikkeavat vähän (esim. $v_\text{8\,s} = 44{,}6\,\text{m/s}$); tulos $a_2$ välillä $1{,}4\ldots 1{,}6\,\text{m/s}^2$ ja $F_\text{v}$ välillä $600\ldots 650\,\text{N}$.

## fy9-voimat-s8

### a)
**Annettu:** $m = 75{,}0\,\text{kg}$, lukema $N = 650\,\text{N}$ aikavälillä $1{,}0\ldots 3{,}0\,\text{s}$ (kuvaajan vaakasuora kohta), $g = 9{,}81\,\text{m/s}^2$; ylös positiivinen
**Kysytty:** kiihtyvyys $a$
**Periaate:** Henkilöön vaikuttavat paino alas ja levyn tukivoima ylös; levyn lukema on tukivoima. Newtonin toisen lain mukaan kokonaisvoima on massa kertaa kiihtyvyys (luku *Newtonin toinen laki*, luku *Soveltava tunti: hissi, laskuvarjo ja kelkkamäki*).
**Kuvaajan lukeminen:** Aikavälillä $1{,}0\ldots 3{,}0\,\text{s}$ lukema on vakio $650\,\text{N}$, ja ennen sitä ja sen jälkeen $736\,\text{N}$.
**Voimakuvio:** Henkilö suorakulmiona, $y$-akseli ylös. Paino $\overline{G}$ keskipisteestä alas ja tukivoima $\overline{N}$ alapinnasta ylös, hieman painoa lyhyempi; kiihtyvyys osoittaa alas.
```voimakuvio
pinta 0
G 735,8
N 650
a alas
v alas
```
**Kaava:** Ylös positiivinen: $N - mg = ma$, joten $a = \dfrac{N - mg}{m}$
**Muunnokset:** Ei tarvita, suureet ovat perusyksiköissä.
**Sijoitus:** $$
\begin{aligned}
a &= \dfrac{650\,\text{N} - 75{,}0\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{75{,}0\,\text{kg}} \\
&= \dfrac{650\,\text{N} - 735{,}75\,\text{N}}{75{,}0\,\text{kg}} \\
&= -1{,}14\,\text{m/s}^2
\end{aligned}
$$
**Vastaus:** $a \approx -1{,}1\,\text{m/s}^2$, kaksi merkitsevää numeroa kuten lukemassa $650\,\text{N}$. Miinusmerkki kertoo, että kiihtyvyys osoittaa alas.
**Järkevyys:** Lukema on pienempi kuin paino $736\,\text{N}$, joten kokonaisvoima osoittaa alas. Kiihtyvyys $1{,}1\,\text{m/s}^2$ on noin $12\,\%$ putoamiskiihtyvyydestä, tavallinen hissin lähtökiihtyvyys.

### b)
**Annettu:** $a = -1{,}14\,\text{m/s}^2$ a-kohdasta, hissi levossa hetkellä $1{,}0\,\text{s}$ ja kiihtyvyys vakio aikavälillä $1{,}0\ldots 3{,}0\,\text{s}$
**Kysytty:** nopeus $v$ hetkellä $3{,}0\,\text{s}$
**Periaate:** Vakiokiihtyvyydellä nopeus muuttuu tasaisesti, $v = v_0 + a\,\Delta t$ (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*).
**Kuvaajan lukeminen:** Kiihtyvyys kestää hetkestä $1{,}0\,\text{s}$ hetkeen $3{,}0\,\text{s}$, joten $$
\begin{aligned}
\Delta t &= 3{,}0\,\text{s} - 1{,}0\,\text{s} \\
&= 2{,}0\,\text{s}
\end{aligned}
$$.
**Kaava:** $v = v_0 + a\,\Delta t$, ja $v_0 = 0$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $$
\begin{aligned}
v &= 0 + (-1{,}14\,\text{m/s}^2) \cdot 2{,}0\,\text{s} \\
&= -2{,}29\,\text{m/s}
\end{aligned}
$$
**Vastaus:** $v \approx -2{,}3\,\text{m/s}$, eli $2{,}3\,\text{m/s}$ alaspäin, kaksi merkitsevää numeroa kuten ajassa $2{,}0\,\text{s}$.
**Järkevyys:** Miinusmerkki sopii alaspäin kulkevaan hissiin. Nopeus $$
\begin{aligned}
2{,}3\,\text{m/s} &\approx 8{,}2\,\text{km/h}
\end{aligned}
$$ on tavallinen hissin matkanopeus, ja se pysyy samana välillä $3{,}0\ldots 6{,}0\,\text{s}$, koska lukema on silloin $736\,\text{N}$.

### c)
**Annettu:** $m = 75{,}0\,\text{kg}$, $N = 800\,\text{N}$ aikavälillä $6{,}0\ldots 8{,}7\,\text{s}$, $v = -2{,}29\,\text{m/s}$ hetkellä $6{,}0\,\text{s}$, $g = 9{,}81\,\text{m/s}^2$; ylös positiivinen
**Kysytty:** kiihtyvyys $a$ ja pysähtyykö hissi hetkellä $8{,}7\,\text{s}$
**Periaate:** Samoin kuin a-kohdassa: $N - mg = ma$. Lukema on nyt suurempi kuin paino, joten kokonaisvoima ja kiihtyvyys osoittavat ylös, vastakkaiseen suuntaan kuin nopeus (hissi hidastuu).
**Kuvaajan lukeminen:** Aikavälillä $6{,}0\ldots 8{,}7\,\text{s}$ lukema on $800\,\text{N}$; kesto on $$
\begin{aligned}
8{,}7\,\text{s} - 6{,}0\,\text{s} &= 2{,}7\,\text{s}
\end{aligned}
$$.
**Voimakuvio:** Henkilö suorakulmiona: paino $\overline{G}$ alas ja tukivoima $\overline{N}$ ylös, painoa pidempi; kiihtyvyys ylös, nopeus alas.
```voimakuvio
pinta 0
G 735,8
N 800
a ylös
v alas
```
**Kaava:** $a = \dfrac{N - mg}{m}$ ja nopeuden muutos $\Delta v = a\,\Delta t$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $$
\begin{aligned}
a &= \dfrac{800\,\text{N} - 735{,}75\,\text{N}}{75{,}0\,\text{kg}} \\
&= 0{,}857\,\text{m/s}^2
\end{aligned}
$$ ja $$
\begin{aligned}
v_\text{loppu} &= -2{,}29\,\text{m/s} \\
&\quad + 0{,}857\,\text{m/s}^2 \cdot 2{,}7\,\text{s} \\
&= -2{,}29\,\text{m/s} + 2{,}31\,\text{m/s} \\
&\approx 0
\end{aligned}
$$
**Vastaus:** $a \approx 0{,}86\,\text{m/s}^2$ ylöspäin. Nopeus on lopussa nolla ($0{,}02\,\text{m/s}$ on pyöristysero), joten hissi pysähtyy hetkellä $8{,}7\,\text{s}$.
**Järkevyys:** Hidastuvuus $0{,}86\,\text{m/s}^2$ on pienempi kuin lähtökiihtyvyys $1{,}1\,\text{m/s}^2$, ja jarrutus kestää siksi pidempään ($2{,}7\,\text{s}$ vs. $2{,}0\,\text{s}$): $$
\begin{aligned}
1{,}14 \cdot 2{,}0 &\approx 0{,}857 \cdot 2{,}7
\end{aligned}
$$.

### d)
**Annettu:** $|v| = 2{,}29\,\text{m/s}$ välillä $3{,}0\ldots 6{,}0\,\text{s}$; nopeus kasvaa nollasta hetkestä $1{,}0\,\text{s}$ hetkeen $3{,}0\,\text{s}$ ja pienenee nollaan hetkeen $8{,}7\,\text{s}$
**Kysytty:** hissin kulkema matka $s$ välillä $1{,}0\ldots 8{,}7\,\text{s}$
**Periaate:** $(t,v)$-kuvaajan ja aika-akselin väliin jäävä pinta-ala on kuljettu matka (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*). Nopeuden suuruuden kuvaaja on puolisuunnikas, koska kiihtyvyys on kolmella jaksolla vakio.
**Kuvaajan lukeminen:** Puolisuunnikkaan pitkä kanta on koko liike $$
\begin{aligned}
8{,}7\,\text{s} - 1{,}0\,\text{s} &= 7{,}7\,\text{s}
\end{aligned}
$$ ja lyhyt kanta tasaisen nopeuden jakso $$
\begin{aligned}
6{,}0\,\text{s} - 3{,}0\,\text{s} &= 3{,}0\,\text{s}
\end{aligned}
$$; korkeus on $|v| = 2{,}29\,\text{m/s}$.
**Kaava:** $s = \tfrac{1}{2}(t_1 + t_2)\,|v|$, jossa $t_1$ ja $t_2$ ovat puolisuunnikkaan yhdensuuntaiset sivut
**Muunnokset:** Ei tarvita.
**Sijoitus:** $$
\begin{aligned}
s &= \tfrac{1}{2} \cdot (7{,}7\,\text{s} + 3{,}0\,\text{s}) \cdot 2{,}29\,\text{m/s} \\
&= 5{,}35\,\text{s} \cdot 2{,}29\,\text{m/s} \\
&= 12{,}2\,\text{m}
\end{aligned}
$$
**Vastaus:** $s \approx 12\,\text{m}$ alaspäin, kaksi merkitsevää numeroa kuten nopeudessa.
**Järkevyys:** Tarkistus jaksoittain: $$
\begin{aligned}
s &= 2{,}29\,\text{m} + 6{,}87\,\text{m} \\
&\quad + 3{,}09\,\text{m} \\
&= 12{,}25\,\text{m}
\end{aligned}
$$ ($\tfrac{1}{2}\cdot 2{,}29\,\text{m/s} \cdot 2{,}0\,\text{s}$, $2{,}29\,\text{m/s} \cdot 3{,}0\,\text{s}$ ja $\tfrac{1}{2}\cdot 2{,}29\,\text{m/s} \cdot 2{,}7\,\text{s}$). Noin $12\,\text{m}$ vastaa noin neljää kerrosta, ja se sopii $7{,}7\,\text{s}$ kestävälle ajolle.

### e)
**Kysytty:** mitä levyn lukema mittaa ja miksi lukema on $736\,\text{N}$ levossa ja tasaisella nopeudella
**Periaate:** Levy mittaa voimaa, jolla se tukee henkilöä; painovoima on Maan vetovoima $mg$ ja riippuu vain massasta ja paikasta. Newtonin toisen lain mukaan kokonaisvoima määrää kiihtyvyyden, ei nopeutta (luku *Newtonin toinen laki*).
**Mallivastaus:** Lukema on tukivoima $N$. Painovoima $$
\begin{aligned}
mg &= 75{,}0\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \\
&= 736\,\text{N}
\end{aligned}
$$ ei muutu, kun hissi liikkuu. Levossa ja tasaisella nopeudella kiihtyvyys on nolla, joten $N - mg = 0$ ja $N = mg = 736\,\text{N}$; lukema ei riipu siitä, liikkuuko hissi, vaan siitä, kiihtyykö se.

Kun hissi lähtee alas, kiihtyvyys osoittaa alas ja $N - mg = ma < 0$, joten $N < mg$ ja lukema pienenee arvoon $650\,\text{N}$. Henkilön tunne siitä, että hän on kevyempi, on todellinen, mutta painovoima ei pienentynyt. Arkikielessä ”paino” tarkoittaa usein levyn lukemaa, ja se pienenee.

### Yleisiä virheitä
- Painovoimaksi otetaan levyn lukema $650\,\text{N}$, jolloin $a$-kohdan yhtälö antaa nollan.
- Kiihtyvyyden etumerkki sekoitetaan: valitaan ylös positiiviseksi mutta lasketaan $mg - N$, jolloin kiihtyvyys tulee positiivisena.
- Nopeus lasketaan kaavalla $v = a\,t$ ajalla $3{,}0\,\text{s}$, vaikka kiihtyvyys kestää vain välin $1{,}0\ldots 3{,}0\,\text{s}$ ($\Delta t = 2{,}0\,\text{s}$).
- Matkaksi lasketaan vain tasaisen nopeuden jakso ($2{,}29\,\text{m/s} \cdot 3{,}0\,\text{s}$), ja kiihtyvät jaksot unohdetaan.

### Hyväksytään myös
- Painovoima luetaan kuvaajasta ($736\,\text{N}$) laskun $75{,}0\,\text{kg} \cdot 9{,}81\,\text{m/s}^2$ sijaan; tulokset ovat samat kahden merkitsevän numeron tarkkuudella.
- d-kohdassa matka jaksoittain summaamalla, kun tulos on sama ($12\,\text{m}$).
