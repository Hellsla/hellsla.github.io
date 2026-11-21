# Kappaleen tasapaino: voimat ja momentit

> **Miksi** maalauspukkien päällä olevan lankun ulokkeelle voi nostaa maalipurkin, mutta vain tiettyyn kohtaan asti ennen kuin lankku kaatuu?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: maalari maalaa talon seinää punaiseksi. Seinän edessä on kaksi maalauspukkia. Niiden päällä on pitkä lankku. Maalari seisoo lankulla pukkien välissä ja maalaa siveltimellä seinän yläosaa. Lankun oikea pää ulottuu pitkälle oikean pukin yli. Tämän ulokkeen päällä on iso maalipurkki. Ulokkeen alla ei ole tukea. Kuvasta herää kysymys: kuinka kauas ulokkeelle purkin voi viedä ennen kuin lankku kaatuu?" class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Kaksi tasapainoehtoa
Luvussa *Momentti: voiman kiertävä vaikutus* opittiin, että voima kiertää kappaletta sitä enemmän, mitä suurempi on voiman momentti $M = Fr$. Levossa olevalle kappaleelle ei riitä, että voimat kumoavat toisensa. Kappale on **tasapainossa**, kun se ei lähde liikkeelle eikä kiertymään. Liikkeen suhteen ehto on tuttu Newtonin laeista: voimien summa on nolla. Kiertymisen suhteen ehto on uusi: voimien momenttien summa on nolla. Kuvassa viivaimeen vaikuttaa kahdessa tapauksessa kaksi yhtä suurta ja vastakkaista voimaa. Siksi voimien summa on nolla. Vasemmalla voimat ovat samalla suoralla, eivätkä ne kierrä viivainta. Oikealla voimat ovat eri suorilla, ja niiden momentit kiertävät viivainta samaan suuntaan. Viivain alkaa kiertyä, vaikka sen keskipiste ei lähde liikkeelle.

<svg data-fig="pari" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva, viivain pöydällä ylhäältä katsottuna, kaksi tapausta. Vasemmalla yhtä suuret ja vastakkaiset voimat F1 ja F2 vetävät viivaimen päistä viivaimen suuntaisesti samalla suoralla: voimien summa ja momenttien summa ovat nolla, eikä viivain kierry. Oikealla yhtä suuret ja vastakkaiset voimat vaikuttavat viivaimen päihin kohtisuoraan sitä vastaan eri suorilla: voimien summa on nolla, mutta momenttien summa ei, ja viivain alkaa kiertyä, mitä kuvaa kaareva nuoli." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-pari.webp" x="0" y="0" width="600" height="340" preserveAspectRatio="none"/>
  <foreignObject x="96" y="11.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ei kierry}$</div></foreignObject>
  <foreignObject x="402.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kiertyy}$</div></foreignObject>
  <foreignObject x="5.5" y="129.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{1}$</div></foreignObject>
  <foreignObject x="263.5" y="129.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{2}$</div></foreignObject>
  <foreignObject x="323.5" y="79.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{1}$</div></foreignObject>
  <foreignObject x="531.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{2}$</div></foreignObject>
  <foreignObject x="108.5" y="253.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Sigma\overline{F} = \overline{0}$</div></foreignObject>
  <foreignObject x="121" y="289.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Sigma M = 0$</div></foreignObject>
  <foreignObject x="408.5" y="253.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Sigma\overline{F} = \overline{0}$</div></foreignObject>
  <foreignObject x="421" y="289.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\Sigma M \neq 0$</div></foreignObject>
</svg>

### Painopiste
Maan vetovoima vaikuttaa kappaleen jokaiseen osaan. Painon momenttia laskettaessa koko paino voidaan kuitenkin ajatella yhteen pisteeseen. Se on kappaleen **painopiste**. Tasa-aineisen ja symmetrisen kappaleen, kuten tasapaksun lankun, painopiste on keskellä. Siksi voimakuviossa paino piirretään lähtemään painopisteestä. Kahden kappaleen yhteinen painopiste on niiden painopisteiden välissä, lähempänä raskaampaa kappaletta. Jos kappale tuetaan yhdestä kohdasta, se pysyy paikallaan vain, kun painopiste on tukikohdan pystysuoralla. Muuten painon momentti tukikohdan suhteen kiertää kappaletta.

```pysahdy
Tasapaksua lankkua kannatellaan yhdestä kohdasta. Mihin kohtaan tuen pitää osua, jotta lankku pysyy vaakasuorassa? Miksi?
---
Tuen pitää olla lankun keskellä eli painopisteen alla. Silloin painon varsi on nolla. Paino ei silloin kierrä lankkua.
```

### Milloin kappale kaatuu
Paikallaan olevan kappaleen **tukipinta** on alue, jonka kappaleen ja alustan kosketuskohdat rajaavat. Laatikolla se on laatikon pohja. Tuolilla se on alue jalkojen välissä. Kaatumista arvioidaan pystysuoralla suoralla, joka kulkee painopisteen kautta. Kun suora osuu tukipinnan kohdalle, painon momentti tukipinnan reunan suhteen kääntää kappaleen takaisin alustan varaan. Silloin kappale pysyy pystyssä. Jos suora osuu tukipinnan ulkopuolelle, painon momentti alemman reunan suhteen kiertää kappaletta reunan yli. Silloin kappale kaatuu. Siksi matala ja leveä kappale kestää suuremman kallistuksen kuin korkea ja kapea. Kaatuminen on kiertymistä reunan ympäri. Liukuminen on sitä, että koko kappale siirtyy alustaa pitkin. Kitka estää liukumisen. Kuvan laatikot ovat samalla kaltevalla tasolla, ja kitka estää niitä liukumasta. Ne voivat siis vain pysyä paikallaan tai kaatua.

<svg data-fig="kaatuu" viewBox="0 0 600 372" role="img" aria-label="Kaavakuva mittakaavassa: kaksi laatikkoa samalla 30 asteen kaltevalla tasolla, kitka estää liukumisen. Matala laatikko on 0,60 m leveä ja 0,60 m korkea, korkea laatikko 0,30 m leveä ja 0,80 m korkea. Kummankin painopisteestä lähtee pystysuora katkoviiva alas tasoon. Matalan laatikon viiva osuu laatikon pohjan kohdalle, joten se pysyy pystyssä. Korkean laatikon viiva osuu tasoon pohjan alemman reunan ulkopuolelle, joten se kaatuu, mitä kuvaa kaareva nuoli." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-kaatuu.webp" x="1.2" y="0" width="597" height="380.6" preserveAspectRatio="none"/>
  <foreignObject x="132" y="305.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$30^\circ$</div></foreignObject>
  <foreignObject x="116.5" y="120.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{pysyy}$</div></foreignObject>
  <foreignObject x="431.5" y="33.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{kaatuu}$</div></foreignObject>
</svg>

```pysahdy
Kaltevalla tasolla oleva laatikko kaatuu, vaikka kitka estää sen liukumisen. Mistä riippuu, kaatuuko laatikko?
---
Laatikko kaatuu, jos painopisteen kautta kulkeva pystysuora osuu tukipinnan ulkopuolelle. Silloin painon momentti kiertää laatikon alemman reunan yli.
```

## Kaava: Tasapainoehdot
Kappale on tasapainossa, kun voimien summa on nolla ja voimien momenttien summa on nolla:
```latex
\begin{aligned}
&\Sigma\overline{F} = \overline{0} \\
&\Sigma M = 0
\end{aligned}
```
Tässä $\Sigma\overline{F}$ on kappaleeseen vaikuttavien voimien vektorisumma ($\text{N}$). $\Sigma M$ on voimien momenttien summa jonkin pisteen suhteen ($\text{Nm}$). Ensimmäinen on **tasapainoehto liikkeen suhteen**. Toinen on **momenttiehto** eli tasapainoehto kiertymisen suhteen. Komponenteittain ensimmäinen ehto on $\Sigma F_x = 0$ ja $\Sigma F_y = 0$. Momentit lasketaan kuten luvussa *Momentti: voiman kiertävä vaikutus*: $M = Fr$, missä $r$ on voiman varsi. Etumerkki kertoo kiertosuunnan. Tässä luvussa vastapäivään kiertävä momentti on positiivinen.

### Momenttipisteen valinta
Levossa oleva kappale ei kierry minkään pisteen ympäri. Siksi momenttiehto pätee jokaisen pisteen suhteen. Momenttipisteeksi kannattaa valita tuntemattoman voiman vaikutuspiste. Silloin sen voiman varsi on nolla, eikä voima näy momenttiehdossa. Jos voima ei ole kohtisuorassa sauvamaista kappaletta (lankku, tanko) vastaan, se jaetaan komponentteihin. Kun momenttipiste on sauvan suoralla, momentin antaa sauvaa vastaan kohtisuora komponentti kerrottuna etäisyydellä momenttipisteestä. Kuvassa tangon päähän vaikuttava voima $\overline{F}$ muodostaa tangon kanssa kulman $\alpha$. Tangon suuntainen komponentti $F\cos\alpha$ kulkee saranan kautta eikä kierrä tankoa. Kohtisuora komponentti $F\sin\alpha$ antaa momentin $M = F\sin\alpha \cdot r$.

<svg data-fig="komponentit" viewBox="0 0 600 290" role="img" aria-label="Kaavakuva: vaakasuora tanko on saranalla seinässä. Tangon uloimpaan päähän vaikuttaa voima F, joka osoittaa vinosti ylös kohti seinää ja muodostaa kulman alfa tangon kanssa. Voima on jaettu katkoviivanuolilla tangon suuntaiseen komponenttiin, joka kulkee saranan kautta eikä kierrä tankoa, ja tankoa vastaan kohtisuoraan komponenttiin F sin alfa, joka antaa momentin saranan suhteen. Momentin varsi on tangon pituus r." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-komponentit.webp" x="2.5" y="6.3" width="606.1" height="305.6" preserveAspectRatio="none"/>
  <foreignObject x="328" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="262" y="81.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="444" y="132.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F\sin\alpha$</div></foreignObject>
  <foreignObject x="326" y="215.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$F\cos\alpha$</div></foreignObject>
  <foreignObject x="250" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="96" y="209.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sarana}$</div></foreignObject>
</svg>

### Kaksi tukea
Kuvan lankku on kahden tuen varassa. Lasketaan momentit painopisteen suhteen. Painon $\overline{G}$ varsi on nolla. Tukivoima $\overline{N}_1$ kiertää lankkua myötäpäivään ja $\overline{N}_2$ vastapäivään. Momenttiehdosta $N_2 r_2 - N_1 r_1 = 0$ saadaan
```latex
N_1 r_1 = N_2 r_2
```
Tässä $N_1$ ja $N_2$ ovat tukivoimat ($\text{N}$) ja $r_1$ ja $r_2$ ovat tukien etäisyydet painopisteestä ($\text{m}$). Painopistettä lähempänä oleva tuki kantaa siis suuremman osan painosta. Liikkeen suhteen ehdosta saadaan, että tukivoimien summa on $N_1 + N_2 = G$.

<svg data-fig="lankku" viewBox="0 0 600 290" role="img" aria-label="Voimakuvio: tasa-aineinen lankku kahden tuen varassa, suorakulmiona. Paino G lähtee lankun keskeltä painopisteestä alas. Tukivoimat N1 ja N2 osoittavat ylös ja päättyvät lankun alapintaan tukien kohdalla. Tuki 1 on etäisyydellä r1 painopisteestä ja tuki 2 lyhyemmällä etäisyydellä r2. Nuolten pituudet ovat mittakaavassa: N2 on pidempi kuin N1, ja yhdessä ne ovat yhtä pitkät kuin G." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-lankku.webp" x="17.9" y="14.4" width="574.2" height="285.9" preserveAspectRatio="none"/>
  <foreignObject x="309.5" y="227" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="112.5" y="191.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_{1}$</div></foreignObject>
  <foreignObject x="387.5" y="236.7" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_{2}$</div></foreignObject>
  <foreignObject x="201" y="39.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r_1$</div></foreignObject>
  <foreignObject x="338.5" y="39.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r_2$</div></foreignObject>
  <foreignObject x="428.5" y="77.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lankku}$</div></foreignObject>
</svg>

```pysahdy
Tasa-aineinen lankku on kahden tuen varassa. Tuet ovat $0{,}40\,\text{m}$ ja $1{,}20\,\text{m}$:n päässä painopisteestä. Kantaako kumpikin tuki puolet painosta?
---
Ei kanna. Pätee $N_1 r_1 = N_2 r_2$. Lähempi tuki kantaa kolminkertaisen voiman eli $\tfrac{3}{4}$ painosta. Kauempi tuki kantaa $\tfrac{1}{4}$.
```

### Yhteinen painopiste
Kahden kappaleen massat ovat $m_1$ ja $m_2$. Niiden yhteinen painopiste on kohdassa
```kaavat
massakeskipiste :: x_\text{pp} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}
```
Tässä $x_1$ ja $x_2$ ovat kappaleiden painopisteiden paikat ($\text{m}$) samalla akselilla. Kaava seuraa momenttiehdosta. Jos kappaleet tuetaan kohdasta $x_\text{pp}$, painojen momentit tukikohdan suhteen kumoavat toisensa. Kahden tuen varassa oleva kuormitettu lankku kaatuu, kun lankun ja kuorman yhteinen painopiste siirtyy tukien välin ulkopuolelle.

## Esimerkki
Kaksi kantajaa kantaa vaakasuorassa tasa-aineista hirttä. Hirren pituus on $4{,}00\,\text{m}$ ja massa $60{,}0\,\text{kg}$. Kantaja A kannattelee hirren etupäätä. Kantaja B on $1{,}00\,\text{m}$:n päässä takapäästä. Kuinka suurella voimalla kumpikin kantaja kannattelee hirttä? Kantajat tukevat hirttä pystysuoraan ylöspäin.

<svg data-fig="hirsi" viewBox="0 0 600 330" role="img" aria-label="Voimakuvio: tasa-aineinen hirsi suorakulmiona. Kantaja A on hirren vasemmassa päässä ja kantaja B 1,00 m:n päässä oikeasta päästä. Paino G lähtee hirren keskeltä alas. Kantajien voimat NA ja NB osoittavat ylös ja päättyvät hirren alapintaan. Etäisyydet: A:sta painopisteeseen 2,00 m, painopisteestä B:hen 1,00 m. Momenttipisteeksi on merkitty A ja positiiviseksi kiertosuunnaksi vastapäivään. Nuolten pituudet ovat mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-hirsi.webp" x="1.2" y="2.5" width="600" height="337.5" preserveAspectRatio="none"/>
  <foreignObject x="309.5" y="259" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="66.5" y="215.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_\text{A}$</div></foreignObject>
  <foreignObject x="387.5" y="255" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_\text{B}$</div></foreignObject>
  <foreignObject x="148.5" y="73.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}00\,\text{m}$</div></foreignObject>
  <foreignObject x="313.5" y="73.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}00\,\text{m}$</div></foreignObject>
  <foreignObject x="423.5" y="73.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}00\,\text{m}$</div></foreignObject>
  <foreignObject x="46" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="440" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <foreignObject x="156" y="269.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
</svg>

<!-- vaihe -->

**Tunnetut ja kysytty.** Hirsi: $L = 4{,}00\,\text{m}$, $m = 60{,}0\,\text{kg}$, $g = 9{,}81\,\text{m/s}^2$. Painopiste on keskellä, $2{,}00\,\text{m}$:n päässä A:sta. B on $3{,}00\,\text{m}$:n päässä A:sta.

Kysytään kantajien voimia $N_\text{A}$ ja $N_\text{B}$.

<!-- vaihe -->

**Periaate.** Hirsi on levossa. Siksi se on tasapainossa sekä liikkeen että kiertymisen suhteen. Kappaleeksi valitaan hirsi. Voimakuviossa siihen vaikuttavat paino $\overline{G}$ painopisteestä alas sekä kantajien voimat $\overline{N}_\text{A}$ ja $\overline{N}_\text{B}$ ylös. Momenttipisteeksi valitaan A. Silloin $N_\text{A}$:n varsi on nolla. Vastapäivään kiertävä momentti on positiivinen. Tuntematon $N_\text{B}$ saadaan momenttiehdosta. Sen jälkeen $N_\text{A}$ saadaan voimien summasta.

<!-- vaihe -->

**Kaava ratkaistuna.** Momenttiehto A:n suhteen ja ehto $\Sigma F_y = 0$, kun ylöspäin on positiivinen:
```latex
\begin{aligned}
&N_\text{B} r_\text{B} - G r_G = 0 \\
&N_\text{B} = \frac{m g r_G}{r_\text{B}} \\[6pt]
&N_\text{A} + N_\text{B} - G = 0 \\
&N_\text{A} = m g - N_\text{B}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita: massa on kilogrammoina ja pituudet metreinä. Voimien varret ovat $r_G = 2{,}00\,\text{m}$ ja $r_\text{B} = 3{,}00\,\text{m}$, koska voimat ovat pystysuoria ja hirsi on vaakasuora.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&G = m g \\
&= 60{,}0\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \\
&= 588{,}6\,\text{N} \\[6pt]
&N_\text{B} = \frac{G r_G}{r_\text{B}} \\
&= \frac{588{,}6\,\text{N} \cdot 2{,}00\,\text{m}}{3{,}00\,\text{m}} \\
&= 392{,}4\,\text{N} \\[6pt]
&N_\text{A} = G - N_\text{B} \\
&= 588{,}6\,\text{N} - 392{,}4\,\text{N} \\
&= 196{,}2\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kantaja A kannattelee hirttä voimalla $196\,\text{N}$ ja kantaja B voimalla $392\,\text{N}$. Tulokset ilmoitetaan kolmella merkitsevällä numerolla, kuten massa $60{,}0\,\text{kg}$ ja pituudet.

<!-- vaihe -->

**Järkevyys.** Voimien summa on $196\,\text{N} + 392\,\text{N} = 588\,\text{N}$. Se on hirren paino. B on painopisteestä $1{,}00\,\text{m}$:n päässä ja A $2{,}00\,\text{m}$:n päässä. Siksi B kantaa kaksi kertaa niin paljon kuin A. Näin painopisteen suhteen lasketun momenttiehdon pitääkin olla: $196\,\text{N} \cdot 2{,}00\,\text{m} = 392\,\text{N} \cdot 1{,}00\,\text{m}$.

## Yleinen virhekäsitys
Moni ajattelee, että kaksi tukea kantavat aina puolet painosta. Moni ajattelee myös, että kauempana oleva tuki kantaa enemmän, koska sen ”vipuvarsi” on pidempi. Momenttiehto painopisteen suhteen näyttää, että asia on päinvastoin: $N_1 r_1 = N_2 r_2$. Siksi painopistettä *lähempänä* oleva tuki kantaa enemmän. Kumpikin tuki kantaa puolet painosta vain, kun tuet ovat yhtä kaukana painopisteestä.

Toinen virhe on luulla, että kuormitettu lankku kaatuu heti, kun kuorma on tuen ohi. Lankku kaatuu vasta, kun lankun ja kuorman *yhteinen* painopiste on tuen ohi. Siihen asti lankun oma paino tukien välissä kumoaa kuorman momentin.

Kolmas virhe on uskoa, että momentit pitää laskea vain painopisteen tai tuen suhteen. Momenttiehto pätee minkä tahansa pisteen suhteen. Eri pisteistä laskettuna saadaan samat voimat. Hyvä valinta vain lyhentää laskua.

## Tiivistelmä
- Kappale on tasapainossa, kun voimien summa on nolla, $\Sigma\overline{F} = \overline{0}$ (liikkeen suhteen), ja voimien momenttien summa on nolla, $\Sigma M = 0$ (kiertymisen suhteen).
- Momenttiehto pätee minkä tahansa pisteen suhteen. Momenttipisteeksi kannattaa valita tuntemattoman voiman vaikutuspiste.
- Paino vaikuttaa painopisteessä. Tasa-aineisen symmetrisen kappaleen painopiste on keskellä. Kahden tuen varassa olevalle lankulle pätee $N_1 r_1 = N_2 r_2$: painopistettä lähempänä oleva tuki kantaa enemmän.
- Tuettu kappale pysyy pystyssä, kun painopisteen kautta kulkeva pystysuora osuu tukipinnan kohdalle. Muuten se kaatuu.
