# Soveltava tunti: hissi, laskuvarjo ja kelkkamäki

> **Miksi** kaksi pulkkaa voi pysähtyä yhtä kauas mäen huipusta, vaikka toinen laskee jyrkkää ja toinen loivaa rinnettä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvinen pulkkamäki. Mäen huipulla seisoo kaksi lasta, ja toisen pulkka odottaa lähtöä. Mäen vasen rinne on jyrkkä ja lyhyt, oikea rinne loiva ja pitkä, ja kummankin rinteen juurelta jatkuu tasainen lumikenttä. Kummallakin puolella pulkan jäljet kulkevat rinnettä alas ja tasaista pitkin pulkkaan, joka on pysähtynyt lapsi kyydissään punaisen merkkilipun kohdalle. Vasemmalla jyrkältä puolelta laskenut pulkka on liukunut tasaisella pitkälle, oikealla loivalta puolelta laskenut vain vähän, ja molemmat liput ovat yhtä kaukana mäen huipusta vaakasuunnassa mitattuna. Taustalla metsää, punainen mökki ja lumisia kumpuja. Mäen korkeus ja matkat on piirretty mittakaavaan. Lapset ja pulkat on piirretty suurempina." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-16-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Ensin voimakuvio, sitten työkalu
Tämän luvun tehtävät ratkeavat kahdella työkalulla. Kumpikin alkaa samasta kohdasta. Moduulissa on myös kolmas työkalu. Törmäyksissä ja lyhyissä iskuissa käytetään impulssiperiaatetta ja liikemäärän säilymistä (luku *Liikemäärän säilyminen ja yksiulotteiset törmäykset*). Ensin valitaan kappale ja piirretään sen voimakuvio, kuten luvussa *Voimakuvio ja voimien yhteisvaikutus*. Voimakuvio on piirros, jossa näkyvät kappaleeseen vaikuttavat voimat ja niiden suunnat. Sitten valitaan työkalu sen mukaan, mitä kysytään. Kun kysytään voimaa tai kiihtyvyyttä jollakin hetkellä, kirjoitetaan liikeyhtälö (luku *Newtonin toinen laki*). Kun kysytään nopeutta jossakin kohdassa tai energian muutosta jollakin matkalla, käytetään energiaperiaatetta (luku *Mekaanisen energian säilyminen ja energiaperiaate*). Silloinkin tarvitaan voimakuvio, koska siitä nähdään, mitkä voimat tekevät työtä.

<svg data-fig="kolme" viewBox="0 0 600 460" role="img" aria-label="Kolme tilannetta. Ylhäällä ovat tilannekuvat ja katkoviivan alla voimakuviot, joissa valittu kappale on suorakulmio ja voimat ovat kunkin kuvion sisällä mittakaavassa. Vasemmalla hissi lähtee ylös: ihminen seisoo hissikorin lattialla, ja sininen nopeusnuoli osoittaa ylös. Ihmisen voimakuviossa paino G keskipisteestä alas ja lattian tukivoima N alapinnasta ylös, painoa pidempänä, ja oranssi kiihtyvyysnuoli ylös. Keskellä laskuvarjohyppääjä laskeutuu varjon varassa tasaisella nopeudella: nopeusnuoli alas. Voimakuviossa paino G alas ja ilmanvastus F_v yläpinnasta ylös, yhtä pitkinä, kiihtyvyys nolla. Oikealla pulkka liukuu rinnettä alas vasemmalle: nopeusnuoli rinnettä alas. Voimakuviossa pulkka on rinteen suuntaisesti kallistettu suorakulmio: paino G keskipisteestä suoraan alas, tukivoima N alapinnasta kohtisuoraan rinteestä ulos ja liukukitka F_mu alapinnan ylemmästä kulmasta rinnettä ylös, lyhyenä. Kiihtyvyysnuoli rinnettä alas." style="max-width:100%;font-size:26px">
  <image href="pics/fy4/fy4-16-kolme.webp" x="0" y="0" width="600" height="466.2" preserveAspectRatio="none"/>
  <foreignObject x="62" y="6.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#6b7480">$\text{hissi}$</div></foreignObject>
  <foreignObject x="228.5" y="6.5" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#6b7480">$\text{laskuvarjo}$</div></foreignObject>
  <foreignObject x="428.5" y="6.5" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#6b7480">$\text{kelkkamäki}$</div></foreignObject>
  <foreignObject x="170.5" y="109.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="94.5" y="343" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="36.5" y="242.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="160.5" y="246.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="360.5" y="114.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="217.5" y="226" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="290.5" y="363" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="341.5" y="284.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="429.5" y="79.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="464.5" y="404.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="458.5" y="221.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="535" y="317.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="387" y="232" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

### Hissi: vaaka mittaa tukivoimaa
Kylpyhuonevaaka ei mittaa painoa vaan tukivoimaa $N$. Tukivoima on voima, jolla vaaka työntää seisojaa ylöspäin. Lukema näkyy kilogrammoina, koska vaaka jakaa voiman luvulla $9{,}81\,\text{m/s}^2$. Hississä paikallaan seisovaan ihmiseen vaikuttavat vain paino ja tukivoima. Kun positiivinen suunta on ylös, liikeyhtälö on $N - mg = ma$, joten $N = m(g + a)$. Oletetaan, että hissi lähtee ylös ja kiihtyy $1{,}0\,\text{m/s}^2$. Silloin $60{,}0\,\text{kg}$:n ihmisen tukivoima on $649\,\text{N}$. Pyöristettynä se on $650\,\text{N}$ kuten kuvaajassa, ja vaaka näyttää $66\,\text{kg}$. Tasaisella nopeudella $a = 0$, ja vaaka näyttää saman kuin kotona. Näin on, liikkuipa hissi ylös tai alas. Lukema riippuu siis kiihtyvyydestä, ei nopeudesta.

```pysahdy
Hissi liikkuu ylöspäin tasaisella nopeudella $2{,}0\,\text{m/s}$. Näyttääkö vaaka silloin enemmän, vähemmän vai saman kuin paikallaan seisoessa? Perustele.
---
Saman. Nopeus on vakio, joten $a = 0$ ja $N = mg$. Vaa'an lukema riippuu kiihtyvyydestä, ei nopeudesta.
```

### Laskuvarjo: rajanopeudella mekaaninen energia pienenee
Varjon varassa laskeutuva hyppääjä putoaa pian rajanopeudella eli tasaisella nopeudella (luku *Ilmanvastus ja putoaminen ilmassa*). Liikeyhtälön mukaan kiihtyvyys on nolla, joten ilmanvastus on yhtä suuri kuin paino, $F_\text{v} = mg$. Katsotaan sitten energiaa. Liike-energia ei muutu, mutta potentiaalienergia pienenee koko ajan. Energiaperiaatteen mukaan mekaanisen energian muutos on ilmanvastuksen tekemä työ. Työ on negatiivinen, koska ilmanvastus osoittaa liikettä vastaan. Korkeuden $h$ matkalla $W_\text{v} = -F_\text{v} h = -mgh$. Kun $80\,\text{kg}$:n hyppääjä laskeutuu $100\,\text{m}$, noin $78\,\text{kJ}$ mekaanista energiaa muuttuu ilman liikkeeksi ja lopulta sisäenergiaksi. Kumpikin työkalu kertoo saman asian omalla tavallaan.

```pysahdy
Hyppääjän liike-energia ei muutu rajanopeudella. Mihin mekaaninen energia silloin menee?
---
Potentiaalienergia pienenee korkeuden mukana. Ilmanvastus tekee negatiivisen työn, ja energia muuttuu ilman liikkeeksi ja lopulta sisäenergiaksi.
```

### Kelkkamäki: kitka vie energiaa koko matkalla
Pulkka liukuu suoraa rinnettä alas. Voimakuvio näyttää, että painon rinnettä vastaan kohtisuora komponentti ja tukivoima kumoavat toisensa. Siksi $N = mg\cos\alpha$, kuten luvussa *Paino, kitka ja kalteva taso*. Liukukitka on silloin $F_\mu = \mu mg\cos\alpha$. Liukukitka on kitka, joka vastustaa liukumista. Tukivoima ei tee työtä, koska se on kohtisuorassa liikettä vastaan. Paino tekee rinteessä työn $mgh$. Kitka tekee negatiivisen työn $-F_\mu L$, kun rinteen pituus on $L$. Otetaan kaksi yhtä korkeaa mäkeä. Jyrkässä rinteessä tukivoima ja kitka ovat pienempiä, ja rinne on lyhyempi. Siksi kitka vie vähemmän energiaa, ja pulkka on juurella nopeampi. Tasaisella pulkka liukuu, kunnes kitka on muuttanut kaiken liike-energian sisäenergiaksi.

```pysahdy
Kaksi pulkkaa lähtee yhtä korkealta, toinen jyrkältä ja toinen loivalta rinteeltä. Kummassa rinteessä kitka tekee suuremman työn ja miksi?
---
Loivassa. Rinne on pidempi, joten kitka vaikuttaa pitemmän matkan ja vie enemmän energiaa kuin jyrkässä rinteessä.
```

## Kaava: Liikeyhtälö ja energiaperiaate
Soveltavan tehtävän ensimmäinen työkalu on Newtonin toinen laki:
```kaavat
Newtonin 2. laki (dynamiikan peruslaki) :: \Sigma\overline{F} = m\overline{a}
```
missä $\Sigma\overline{F}$ on kappaleeseen vaikuttavien voimien summa eli kokonaisvoima ($\text{N}$), $m$ kappaleen massa ($\text{kg}$) ja $\overline{a}$ sen kiihtyvyys ($\text{m/s}^2$). Laki kirjoitetaan voimakuviosta komponenteittain, $\Sigma F_x = ma_x$ ja $\Sigma F_y = ma_y$. Ensin valitaan akselit ja positiiviset suunnat. Toinen työkalu on mekaniikan energiaperiaate:
```kaavat
mekaniikan energiaperiaate :: E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}
```
missä indeksi $0$ tarkoittaa alkutilannetta. Suure ilman indeksiä tarkoittaa lopputilannetta. Liike-energia on $E_\text{k} = \tfrac12 mv^2$, ja potentiaalienergia on $E_\text{p} = mgh$ valitusta nollatasosta. Työ $W$ on muiden voimien kuin painon tekemä työ ($\text{J}$). Energiaperiaatteessa ei tarvita kiihtyvyyttä eikä aikaa. Siksi se sopii, kun kysytään nopeutta tietyssä kohdassa.

### Kitkan työ riippuu vaakasuorasta matkasta
Oletetaan suora rinne, jonka kaltevuuskulma on $\alpha$ ja pituus $L$. Liukukitka on $\mu mg\cos\alpha$, ja sen tekemä työ on $-\mu mg\cos\alpha \cdot L$. Kuvasta nähdään, että $L\cos\alpha$ on rinteen vaakasuora pituus $x_1$. Tasaisella $N = mg$, ja kitkan työ matkalla $x_2$ on $-\mu mg x_2$. Kummassakin tapauksessa liukukitkan työ on
```latex
W_\mu = -\mu m g x
```
missä $\mu$ on liukukitkakerroin, $m$ massa ($\text{kg}$), $g$ putoamiskiihtyvyys ($\text{m/s}^2$) ja $x$ kuljetun matkan vaakasuora pituus ($\text{m}$). Tulos pätee vain tietyillä ehdoilla. Pinnan on oltava suora, ja kitkakertoimen on oltava sama koko matkalla. Lisäksi pintaa vastaan kohtisuorassa saavat vaikuttaa vain paino ja tukivoima. Pulkkaa ei siis esimerkiksi vedetä narusta.

<svg data-fig="kitkatyo" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva (ei mittakaavassa): pulkka lähtee levosta mäen huipulta, liukuu suoraa rinnettä alas ja jatkaa tasaista pitkin, kunnes pysähtyy. Rinteen pituus on L ja korkeus h, ja rinne on kulmassa alfa vaakatasoon nähden. Rinteen vaakasuora pituus on x 1 eli L kertaa kosini alfa, ja tasaisella pulkka liukuu matkan x 2. Kummallakin pulkka on piirretty paikallaan, nopeus nolla." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-16-kitkatyo.webp" x="0" y="-2.5" width="600" height="337.5" preserveAspectRatio="none"/>
  <foreignObject x="25" y="29.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$v_1 = 0$</div></foreignObject>
  <foreignObject x="491" y="163.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$v_2 = 0$</div></foreignObject>
  <foreignObject x="217" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L$</div></foreignObject>
  <foreignObject x="92" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="252.5" y="178.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="163.5" y="273.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_1 = L\cos\alpha$</div></foreignObject>
  <foreignObject x="406.5" y="273.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_2$</div></foreignObject>
</svg>

### Miksi pulkat pysähtyvät yhtä kauas
Pulkka lähtee levosta korkeudelta $h$, laskee rinteen ja pysähtyy tasaiselle. Nollataso valitaan tasaisen kohdalle. Silloin energiaperiaatteesta saadaan $mgh - \mu mg(x_1 + x_2) = 0$. Massa supistuu pois. Pulkan koko vaakasuora matka huipulta pysähtymiskohtaan on
```latex
x_1 + x_2 = \frac{h}{\mu}
```
Kaltevuuskulma ei näy tuloksessa. Jyrkältä puolelta laskeva pulkka kulkee rinteessä lyhyen vaakamatkan, joten sille jää enemmän matkaa tasaisella. Loivalta puolelta laskeva käyttää suuremman osan vaakamatkasta rinteessä. Tämä vastaa alun kysymykseen. Malli olettaa kolme asiaa: kitkakerroin on sama koko matkalla, ilmanvastus on pieni ja rinteen juuren mutka on lyhyt. Jyrkässä mutkassa tukivoima ja kitka kasvavat hetkeksi. Siksi todellinen pulkka pysähtyy jyrkän mäen alla vähän aikaisemmin. Lisäksi rinteen on oltava niin jyrkkä, että pulkka liukuu: $\tan\alpha > \mu$.

### Ratkaisun vaiheet
1. Valitse kappale ja piirrä sen voimakuvio. Kirjoita jokaiselle voimalle aiheuttaja ja suunta.
2. Päätä työkalu: hetken voima tai kiihtyvyys saadaan liikeyhtälöstä, nopeus tietyssä kohdassa energiaperiaatteesta.
3. Liikeyhtälöön valitse akselit ja positiiviset suunnat. Energiaperiaatteeseen valitse nollataso ja kirjoita muiden voimien työ etumerkkeineen. Liikettä vastustava voima tekee negatiivista työtä. Liikettä vastaan kohtisuora voima ei tee työtä.
4. Ratkaise kysytty suure ensin symbolein ja sijoita luvut vasta sitten. Tarkista tulos rajatapauksella, esimerkiksi ilman kitkaa.

## Esimerkki
Lapsi ja pulkka ovat yhteensä $32{,}0\,\text{kg}$. He lähtevät levosta suoran rinteen ylimmästä kohdasta. Rinteen pituus on $25{,}0\,\text{m}$, kaltevuuskulma $20{,}0^\circ$ ja pulkan ja lumen välinen liukukitkakerroin $0{,}200$. Kuinka suuri on pulkan nopeus rinteen juurella? Ilmanvastus jätetään huomiotta.

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 32{,}0\,\text{kg}$, $L = 25{,}0\,\text{m}$, $\alpha = 20{,}0^\circ$, $\mu = 0{,}200$, alkunopeus $v_1 = 0$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään nopeutta $v_2$ rinteen juurella.

<!-- vaihe -->

**Periaate.** Kysytään nopeutta tietyssä kohdassa, joten käytetään energiaperiaatetta. Kappaleeksi valitaan pulkka ja lapsi yhdessä. Paino tekee työtä, ja energiaperiaate ottaa sen huomioon potentiaalienergian muutoksena. Tukivoima ei tee työtä, koska se on kohtisuorassa liikettä vastaan. Liukukitka osoittaa liikettä vastaan ja tekee negatiivisen työn $W = -F_\mu L$. Kitkavoima saadaan voimakuviosta.

<!-- vaihe -->

**Voimakuvio.** Pulkka piirretään suorakulmiona rinteen suuntaisesti. Siihen vaikuttavat Maa (paino $\overline{G}$), lumi (tukivoima $\overline{N}$) ja lumen liukukitka $\overline{F}_\mu$. Kitka osoittaa rinnettä ylös, koska pulkka liukuu alas. Akselit valitaan niin, että $x$ osoittaa rinnettä alas ja $y$ kohtisuoraan rinteestä ulos. Suunnassa $y$ pulkka ei kiihdy, joten $N - mg\cos\alpha = 0$ ja $F_\mu = \mu N = \mu mg\cos\alpha$.

<svg data-fig="esimerkki" viewBox="0 0 600 400" role="img" aria-label="Vasemmalla tilannekuva: pulkka ja lapsi liukuvat lumista rinnettä alas vasemmalle, ja pulkan yllä sininen nopeusnuoli osoittaa rinnettä alas. Rinne nousee oikealle kulmassa 20 astetta. Oikealla pulkan voimakuvio, pulkka suorakulmiona rinteen suuntaisesti kallistettuna, voimat mittakaavassa. Paino G keskipisteestä suoraan alas. Tukivoima N alapinnasta kohtisuoraan rinteestä ulos, vähän painoa lyhyempänä. Liukukitka F_mu alapinnan ylemmästä kulmasta rinnettä ylös, lyhyenä. Painon komponentit katkoviivoin keskipisteestä: G x rinnettä alas, kitkaa pidempänä, ja G y kohtisuoraan rinnettä kohti. Erillään oranssi kiihtyvyysnuoli rinnettä alas. Nurkassa akselit: x rinnettä alas ja y kohtisuoraan rinteestä ulos." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy416-ex-snow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy416-ex-s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient></defs>
  <foreignObject x="37.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="333.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <path d="M18,300 L215.5,228 V300 Z" fill="url(#fy416-ex-snow)" stroke="#4f8fbf" stroke-width="2.5" stroke-linejoin="round"/>
  <g transform="translate(138.5,256) rotate(-20) scale(-0.8,0.8)">
  <path d="M-46,-4 Q-48,0 -40,0 H34 Q52,0 56,-22 L48,-24 Q44,-10 30,-10 H-38 Z" fill="url(#fy416-ex-s)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M-40,-6 H28" fill="none" stroke="#f2a69c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <path d="M6,-14 Q26,-16 40,-20" fill="none" stroke="#1f2933" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M-22,-12 Q-26,-46 -6,-50 Q8,-50 10,-14 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M2,-40 L22,-24" fill="none" stroke="#1971c2" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="-8" cy="-62" r="11" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M-20,-62 Q-20,-78 -8,-78 Q4,-78 4,-62 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="-8" cy="-80" r="4" fill="#ffffff" stroke="#1f2933" stroke-width="1.5"/>
  </g>
  <line x1="107.5" y1="170.5" x2="53" y2="190" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M61,180.5 L51,191 L65.5,192.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="58.5" y="148" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <path d="M88,300 A70,70 0 0 0 84,276" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="90" y="269" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20^\circ$</div></foreignObject>
  <line x1="234" y1="36" x2="234" y2="388" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="358" y="154" width="104" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-20 410 176)"/>
  <line x1="410" y1="176" x2="410" y2="291" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M410,308 L402,290 L418,290 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="375.5" y="311.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="436.5" y1="190" x2="400" y2="89.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M394,73.5 L407.5,87.5 L392.5,93 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="363.5" y="47" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="466.5" y1="179" x2="473.5" y2="176" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M489.5,170.5 L475.5,184 L470,169 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="477" y="176" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="410" y1="176" x2="369.5" y2="190.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M377.5,181 L367.5,191.5 L382,193" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="323" y="189" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <line x1="410" y1="176" x2="451.5" y2="290.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M442,282.5 L452.5,292.5 L454,278" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="458" y="280" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <line x1="300" y1="120" x2="249.5" y2="138.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M257.5,128.5 L247.5,139 L262,141" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="227" y="106.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="540" y1="330" x2="507" y2="342" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M498.5,345 L506.5,337.5 L509.5,346 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="540" y1="330" x2="528" y2="297" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M525,288.5 L532.5,296.5 L524,299.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="475.5" y="335.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="510" y="261" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Nollataso valitaan rinteen juurelle. Alussa $E_\text{p,1} = mgh$, missä $h = L\sin\alpha$, ja lopussa $E_\text{p,2} = 0$. Nopeus ratkaistaan energiaperiaatteesta:
```latex
\begin{aligned}
&mgL\sin\alpha - \mu mg\cos\alpha \cdot L \\
&\quad = \tfrac12 mv_2^2 \\
&v_2 = \sqrt{2gL(\sin\alpha - \mu\cos\alpha)}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita. Suureet ovat SI-yksiköissä, ja kitkakerroin on yksikötön. Kulma on asteina, ja laskin on asteasetuksella.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin sulkulauseke ja sitten nopeus:
```latex
\begin{aligned}
&\sin 20{,}0^\circ - 0{,}200\cdot\cos 20{,}0^\circ \\
&\quad \approx 0{,}3420 - 0{,}1879 = 0{,}1541 \\
&v_2 = \sqrt{2\cdot 9{,}81\cdot 25{,}0\cdot 0{,}1541}\,\tfrac{\text{m}}{\text{s}} \\
&\phantom{v_2} \approx 8{,}694\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Pulkan nopeus rinteen juurella on $8{,}69\,\text{m/s}$ eli noin $31\,\text{km/h}$. Tuloksessa on kolme merkitsevää numeroa, kuten lähtöarvoissa: rinteen pituus $25{,}0\,\text{m}$, kulma $20{,}0^\circ$ ja kitkakerroin $0{,}200$.

<!-- vaihe -->

**Järkevyys.** Ilman kitkaa nopeus olisi $\sqrt{2gh} = \sqrt{2\cdot 9{,}81\cdot 8{,}55}\,\tfrac{\text{m}}{\text{s}} \approx 13{,}0\,\text{m/s}$. Kitka pienentää nopeutta, kuten pitääkin. Sama tulos saadaan liikeyhtälöllä. Suunnassa $x$ pätee $mg\sin\alpha - \mu mg\cos\alpha = ma$, joten $a \approx 1{,}51\,\text{m/s}^2$. Luvun *Mekaanisen energian säilyminen ja energiaperiaate* tuloksesta $aL = \tfrac12 v_2^2$ saadaan $v_2^2 \approx 75{,}6\,\text{m}^2/\text{s}^2$ kuten edellä. Massa supistui pois. Raskaampi ja kevyempi pulkka ovat siis juurella yhtä nopeita, kun kitkakerroin on sama.

## Yleinen virhekäsitys
Moni ajattelee, että hississä vaaka näyttää enemmän, koska hissi liikkuu ylöspäin. Lukema riippuu kuitenkin kiihtyvyydestä, ei nopeudesta. Tasaisesti ylös tai alas liikkuvassa hississä vaaka näyttää saman kuin kotona. Ylös liikkuvassa hississä, joka hidastaa pysähtyäkseen, vaaka näyttää vähemmän.

Toinen virhe on ajatella, että rajanopeudella mekaaninen energia säilyy, koska nopeus ei muutu. Liike-energia pysyy samana, mutta potentiaalienergia pienenee. Ilmanvastuksen negatiivinen työ muuttaa sen muiksi energiamuodoiksi. Kolmas virhe on kirjoittaa rinteessä kitkavoimaksi $\mu mg$. Rinteessä tukivoima on $mg\cos\alpha$, joten kitkavoima on $\mu mg\cos\alpha$. Kitkan työ on $-\mu mg$ kertaa vaakasuora matka, ei kertaa rinteen pituus.

## Tiivistelmä
- Mekaniikan tehtävä alkaa aina kappaleen valinnasta ja voimakuviosta. Hetken voima tai kiihtyvyys saadaan liikeyhtälöstä $\Sigma\overline{F} = m\overline{a}$. Nopeus tietyssä kohdassa saadaan energiaperiaatteesta.
- Hississä vaaka mittaa tukivoimaa $N = m(g + a)$, kun positiivinen suunta on ylös. Lukema riippuu kiihtyvyydestä, ei nopeudesta.
- Rajanopeudella $F_\text{v} = mg$, ja ilmanvastuksen työ on $-mgh$. Mekaaninen energia pienenee, vaikka nopeus ei muutu.
- Suoralla rinteellä $N = mg\cos\alpha$, ja liukukitkan työ on $W_\mu = -\mu mgx$. Tässä $x$ on vaakasuora matka. Pulkka lähtee levosta korkeudelta $h$. Se pysähtyy vaakamatkan $h/\mu$ päähän huipusta, kun kitkakerroin on sama koko matkan.
- Kun kappale liukuu paikallaan olevaa pintaa pitkin, tukivoima ei tee työtä. Se on kohtisuorassa liikettä vastaan. Liikkuvassa hississä lattian tukivoima on liikkeen suuntainen, joten se tekee työtä. Työ on positiivista, kun hissi nousee, ja negatiivista, kun hissi laskeutuu.
