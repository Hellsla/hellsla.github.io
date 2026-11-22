# Ympyrärata: jaksonaika ja ratanopeus

> **Miksi** karusellin reunalla seisova lapsi kiitää paljon lujempaa kuin keskitangon vieressä seisova, vaikka molemmat tekevät kierroksen yhtä nopeasti?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: leikkikentän karuselli pyörii kesäpäivänä. Toinen lapsi seisoo karusellin reunalla, toinen lähellä keskitankoa. Kummankin kohdalla on sininen nuoli liikkeen suuntaan radan tangentin suuntaisesti; reunalla seisovan lapsen nuoli on kaksi kertaa niin pitkä kuin keskellä seisovan." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Kappale on **ympyräliikkeessä**, kun sen rata on ympyrä: kappale pysyy koko ajan samalla etäisyydellä radan keskipisteestä. Tämä etäisyys on radan säde $r$. Karusellissa seisova lapsi, liikenneympyrää kiertävä auto ja Maata kiertävä satelliitti ovat ympyräliikkeessä tai lähes siinä. Jos kappale kulkee jokaisessa yhtä pitkässä ajassa yhtä pitkän matkan, sen nopeuden suuruus eli vauhti pysyy samana. Silloin liike on **tasaista ympyräliikettä**. Tässä luvussa tarkastellaan vain tasaista ympyräliikettä.

### Nopeus osoittaa tangentin suuntaan
Nopeus on vektori $\overline{v}$, jolla on suuruus ja suunta. Nopeus osoittaa joka hetki siihen suuntaan, johon kappale on juuri sillä hetkellä liikkumassa. Ympyräradalla tämä suunta on radan **tangentin** suunta, joka on kohtisuorassa keskipisteestä piirrettyä sädettä vastaan. Kun kappale kiertää, tangentin suunta kääntyy koko ajan. Tasaisessa ympyräliikkeessä nopeusvektorit ovat siis kaikki yhtä pitkiä, mutta ne osoittavat eri suuntiin: nopeuden suuruus pysyy samana, mutta nopeus muuttuu.

<svg data-fig="tangent" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva: kappale kiertää ympyrärataa vastapäivään. Neljässä kohdassa on piirretty sininen nopeusvektori: kaikki ovat yhtä pitkiä ja radan tangentin suuntaisia, kohtisuorassa keskipisteestä piirrettyä sädettä vastaan. Oikealla lukee, että nopeuksien suuruudet ovat yhtä suuret mutta vektorit erisuuret." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-3-tangent.webp" x="0" y="1.2" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="302" y="95.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <foreignObject x="35" y="35.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <foreignObject x="64" y="267.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_3$</div></foreignObject>
  <foreignObject x="264" y="319.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_4$</div></foreignObject>
  <foreignObject x="222" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="380" y="135.5" width="206" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v_1 = v_2 = v_3 = v_4$</div></foreignObject>
  <foreignObject x="380" y="207.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\overline{v}_1 \neq \overline{v}_2$</div></foreignObject>
</svg>

```pysahdy
Kappale kiertää ympyrää vastapäivään, ja se on juuri radan ylimmässä kohdassa. Mihin suuntaan sen nopeus osoittaa?
---
Vasemmalle. Nopeus on radan tangentin suuntainen eli kohtisuorassa pystysuoraa sädettä vastaan, joten se on vaakasuora ja osoittaa kiertosuuntaan.
```

### Kun naru katkeaa
Naruun sidottu kiekko kiertää jäällä tappia. Naru vetää kiekkoa kohti tappia ja kääntää sen liikkeen suuntaa koko ajan. Jos naru katkeaa, kiekkoon ei enää vaikuta vaakasuunnassa voimaa: jään kitka oletetaan pieneksi, ja pystysuorat voimat, paino ja jään tukivoima, kumoavat toisensa. Newtonin ensimmäisen lain mukaan kiekko jatkaa silloin tasaista suoraviivaista liikettä sillä nopeudella, joka sillä oli katkeamishetkellä. Kiekko lähtee siis radan tangentin suuntaan, ei suoraan poispäin tapista. Samoin pyöritetyn sateenvarjon reunasta irtoavat vesipisarat lähtevät tangentin suuntaan.

<svg data-fig="release" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva: naruun sidottu kiekko kiertää tappia vastapäivään katkoviivalla piirrettyä ympyrärataa. Radan alimmassa kohdassa naru katkeaa, ja kiekko jatkaa suoraan oikealle radan tangentin suuntaan. Kiekon paikat on merkitty yhtä pitkin aikavälein: välit ovat yhtä pitkät, joten vauhti pysyy samana." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-3-release.webp" x="1.2" y="1.2" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="510.5" y="219.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="95.5" y="275.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{naru katkeaa}$</div></foreignObject>
  <foreignObject x="292" y="275.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{suoraan, tasaisesti}$</div></foreignObject>
</svg>

### Suunnan muutos on nopeuden muutos
Nopeuden muutos $\Delta\overline{v}$ nähdään, kun kaksi peräkkäistä nopeusvektoria piirretään alkamaan samasta pisteestä. Muutos $\Delta\overline{v}$ on se vektori, joka on lisättävä vektoriin $\overline{v}_1$, jotta saadaan $\overline{v}_2$. Ympyräradalla vektorit ovat yhtä pitkiä, mutta niiden suunnat eroavat, joten $\Delta\overline{v}$ ei ole nolla, kun aikaväli on lyhyempi kuin yksi kierros. Kiihtyvyys tarkoittaa nopeuden muutosta, ei pelkästään vauhdin muutosta. Tasaisessa ympyräliikkeessä kappale on siis kiihtyvässä liikkeessä, ja Newtonin toisen lain mukaan siihen vaikuttaa kokonaisvoima, joka ei ole nolla. Tämä kokonaisvoima osoittaa ympyrän keskipisteen puolelle eli radan sisäpuolelle, ei ulospäin. Kiihtyvyyden suuruus lasketaan luvussa *Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö*.

<svg data-fig="dv" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva: vasemmalla ympyräradan kaari ja kappaleen kaksi peräkkäistä paikkaa, joissa nopeudet ovat yhtä pitkät mutta eri suuntiin. Oikealla samat vektorit on siirretty alkamaan samasta pisteestä, ja musta nuoli ensimmäisen kärjestä toisen kärkeen on nopeuden muutos. Toinen nopeus on ensimmäinen nopeus plus nopeuden muutos." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-3-dv.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="221" y="96" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <foreignObject x="-3" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <foreignObject x="490" y="137" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <foreignObject x="375" y="233.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <foreignObject x="394" y="166.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\Delta\overline{v}$</div></foreignObject>
  <foreignObject x="366" y="297.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{v}_2 = \overline{v}_1 + \Delta\overline{v}$</div></foreignObject>
</svg>

```pysahdy
Kappale kiertää ympyrää tasaisella vauhdilla. Onko sen kiihtyvyys nolla?
---
Ei ole. Vauhti pysyy samana, mutta nopeuden suunta muuttuu koko ajan, joten nopeus muuttuu ja kappale kiihtyy.
```

## Kaava: Ratanopeus
Tasaista ympyräliikettä kuvaa **kierrosaika** $T$, joka on aika, jossa kappale kiertää radan kerran. Sen käänteisluku on **pyörimistaajuus** $f$, joka kertoo, kuinka monta kierrosta kappale tekee aikayksikössä:
```kaavat
kierrostaajuus :: f = \frac{1}{T}
```
missä $f$ on pyörimistaajuus ($\tfrac{1}{\text{s}}$) ja $T$ kierrosaika ($\text{s}$). Kun kierrosaika on $T = 0{,}50\,\text{s}$, kappale tekee $2{,}0$ kierrosta sekunnissa eli $f = 2{,}0\,\tfrac{1}{\text{s}}$. Pyörimistaajuus ilmoitetaan usein myös kierroksina minuutissa. Esimerkiksi $45\,\tfrac{1}{\text{min}}$ muunnetaan sijoittamalla $1\,\text{min} = 60\,\text{s}$, jolloin $45\,\tfrac{1}{\text{min}} = \tfrac{45}{60\,\text{s}} = 0{,}75\,\tfrac{1}{\text{s}}$.

<figure class="unit-photo"><img src="pics/fy5/playground-carousel.webp" alt="Punainen käsin pyöritettävä karuselli leikkipuistossa. Pyöreän lattian reunalla on kaiteet ja keskellä akseli."><figcaption>Leikkipuiston karuselli. Kaikki karusellin kohdat tekevät kierroksen yhtä nopeasti, mutta reunalla kuljettu matka on pidempi kuin akselin lähellä.</figcaption></figure>

Yhdellä kierroksella kappale kulkee ympyrän kehän pituisen matkan $2\pi r$, ja siihen kuluu kierrosaika $T$. Koska vauhti on tasainen, nopeuden suuruus ympyräradalla eli **ratanopeus** on kuljettu matka jaettuna ajalla:
```latex
v = \frac{2\pi r}{T} = 2\pi r f
```
missä $v$ on ratanopeus ($\text{m/s}$), $r$ radan säde ($\text{m}$), $T$ kierrosaika ($\text{s}$) ja $f$ pyörimistaajuus ($\tfrac{1}{\text{s}}$). Jälkimmäinen muoto saadaan, kun $\tfrac{1}{T}$ korvataan pyörimistaajuudella $f$.

Kaavasta näkyy alun kysymyksen vastaus. Karusellin kaikki kohdat tekevät kierroksen samassa ajassa $T$, mutta reunalla seisova lapsi kiertää suurempaa ympyrää. Ratanopeus on suoraan verrannollinen säteeseen, kun kierrosaika on sama: kaksi kertaa kauempana keskipisteestä seisova lapsi kulkee samassa ajassa kaksi kertaa pidemmän matkan, joten hänen ratanopeutensa on kaksinkertainen. Samalla säteellä taas kierrosajan puolittaminen kaksinkertaistaa ratanopeuden.

<svg data-fig="two-radii" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva ylhäältä: kaksi kohtaa A ja B ovat samalla säteellä pyörivässä karusellissa, A etäisyydellä r ja B etäisyydellä 2r keskipisteestä. Samassa ajassa kumpikin kiertyy yhtä suuren osan kierroksesta, mutta B:n kulkema kaari on kaksi kertaa niin pitkä, ja B:n sininen nopeusvektori on kaksi kertaa niin pitkä kuin A:n. Mittasuhteet ovat oikeat." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-3-two-radii.webp" x="-1.2" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="240" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="380" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <foreignObject x="146" y="333.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="286" y="333.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="168" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{A}$</div></foreignObject>
  <foreignObject x="241.5" y="38" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{B}$</div></foreignObject>
  <foreignObject x="240" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s_\text{A}$</div></foreignObject>
  <foreignObject x="370" y="208" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s_\text{B}$</div></foreignObject>
  <foreignObject x="440" y="105.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sama } T$</div></foreignObject>
  <foreignObject x="440" y="161.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s_\text{B} = 2\,s_\text{A}$</div></foreignObject>
  <foreignObject x="440" y="217.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v_\text{B} = 2\,v_\text{A}$</div></foreignObject>
</svg>

```pysahdy
Kappale kiertää ympyrää, jonka säde on $2{,}0\,\text{m}$, ja yksi kierros kestää $4{,}0\,\text{s}$. Mikä on sen ratanopeus?
---
Ratanopeus on $v = \tfrac{2\pi r}{T}$. Se on $\tfrac{2\pi \cdot 2{,}0\,\text{m}}{4{,}0\,\text{s}} \approx 3{,}1\,\text{m/s}$.
```

## Esimerkki
Pesukoneen rummun halkaisija on $46\,\text{cm}$. Linkouksessa rumpu pyörii $1200$ kierrosta minuutissa. Kuinka suuri on rummun seinää vasten painuneen sukan ratanopeus?

<!-- vaihe -->

**Tunnetut ja kysytty.** Rummun halkaisija $d = 46\,\text{cm}$ ja pyörimistaajuus $f = 1200\,\tfrac{1}{\text{min}}$.

Kysytään sukan ratanopeutta $v$.

<!-- vaihe -->

**Periaate.** Sukka pyörii rummun seinällä rummun mukana, joten se on tasaisessa ympyräliikkeessä, jonka säde on rummun säde $r = \tfrac{d}{2}$. Yhdellä kierroksella sukka kulkee kehän pituisen matkan $2\pi r$, ja kierroksia on $f$ aikayksikössä, joten ratanopeus on $v = 2\pi r f$.

<!-- vaihe -->

**Kaava ratkaistuna.** Sijoitetaan säde halkaisijan avulla:
```latex
\begin{aligned}
&v = 2\pi r f, \quad r = \frac{d}{2} \\
&v = \pi d f
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Halkaisija on $46\,\text{cm} = 46 \cdot 0{,}01\,\text{m} = 0{,}46\,\text{m}$. Pyörimistaajuus on $f = 1200\,\tfrac{1}{\text{min}} = \tfrac{1200}{60\,\text{s}} = 20\,\tfrac{1}{\text{s}}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
v &= \pi d f \\
&= \pi \cdot 0{,}46\,\text{m} \cdot 20\,\tfrac{1}{\text{s}} \\
&= 28{,}90\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Sukan ratanopeus on noin $29\,\text{m/s}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska halkaisija $46\,\text{cm}$ on annettu kahdella numerolla.

<!-- vaihe -->

**Järkevyys.** Rummun kehä on $\pi \cdot 0{,}46\,\text{m} \approx 1{,}45\,\text{m}$, ja rumpu pyörii $20$ kierrosta sekunnissa, joten sukka kulkee sekunnissa noin $20 \cdot 1{,}45\,\text{m} \approx 29\,\text{m}$. Kierrosaika on $T = \tfrac{1}{f} = 0{,}050\,\text{s}$, ja kaava $v = \tfrac{2\pi r}{T} = \tfrac{2\pi \cdot 0{,}23\,\text{m}}{0{,}050\,\text{s}}$ antaa saman $28{,}9\,\text{m/s}$. Se on noin $29 \cdot 3{,}6\,\tfrac{\text{km}}{\text{h}} \approx 104\,\tfrac{\text{km}}{\text{h}}$, moottoritien nopeuden luokkaa, mikä sopii nopeaan linkoukseen.

## Yleinen virhekäsitys
Moni ajattelee, että tasaisessa ympyräliikkeessä nopeus ei muutu, koska nopeusmittari näyttää koko ajan samaa lukemaa. Mittari näyttää kuitenkin vain nopeuden suuruuden eli vauhdin. Nopeus on vektori, ja sen suunta kääntyy koko ajan, joten nopeus muuttuu ja kappale on kiihtyvässä liikkeessä. Ilman kokonaisvoimaa kappale ei pysyisi ympyräradalla vaan jatkaisi suoraan.

Toinen virhe on luulla, että narun katketessa kappale lentää suoraan poispäin keskipisteestä. Mikään voima ei työnnä kappaletta ulospäin. Kun naru lakkaa vetämästä, kappale jatkaa sen hetkisen nopeutensa suuntaan eli radan tangentin suuntaan.

Laskuissa tavallisia virheitä ovat halkaisijan sijoittaminen säteen paikalle kaavaan $v = \tfrac{2\pi r}{T}$ ja pyörimistaajuuden sijoittaminen kierroksina minuutissa muuntamatta sitä kierroksiksi sekunnissa.

## Tiivistelmä
- Ympyräliikkeessä kappaleen rata on ympyrä, jonka säde on $r$. Tasaisessa ympyräliikkeessä vauhti pysyy samana.
- Nopeus $\overline{v}$ on joka hetki radan tangentin suuntainen. Suunta muuttuu koko ajan, joten nopeus muuttuu ja kappale on kiihtyvässä liikkeessä, vaikka vauhti on vakio.
- Kun kappaleeseen ei enää vaikuta kokonaisvoimaa, se jatkaa suoraviivaisesti radan tangentin suuntaan.
- Kierrosaika $T$ on yhden kierroksen aika, ja pyörimistaajuus $f = \tfrac{1}{T}$ on kierrosten määrä aikayksikössä.
- Ratanopeus $v = \tfrac{2\pi r}{T} = 2\pi r f$ on suoraan verrannollinen säteeseen, kun kierrosaika on sama.
