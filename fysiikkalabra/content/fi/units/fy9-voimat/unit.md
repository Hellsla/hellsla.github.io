# Newtonin lait ja voimakuvio

> **Miksi** auto saa peräkärryn liikkeelle, vaikka kärry vetää autoa taaksepäin yhtä suurella voimalla kuin auto vetää kärryä eteenpäin?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: syksyinen iltapäivä järven rannalla. Etualan tiellä punainen henkilöauto vetää perässään pientä peräkärryä, jossa on polttopuita. Auto ja kärry on yhdistetty vetoaisalla. Tien takana on järvi ja sen toisella rannalla metsää, tien varressa koivuja ja kuusia." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-voimat-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Kaikki tämän tunnin tehtävät ratkaistaan samalla tavalla: **ensin voimakuvio, sitten liikeyhtälö**. Valitse kappale, luettele sen vuorovaikutukset ja piirrä jokaisesta yksi voima. Kappale on voimakuviossa suorakulmio, ja jokainen voima lähtee vaikutuskohdastaan. Valitse sitten akselit ja kirjoita Newtonin toinen laki kunkin akselin suuntaan. Kokeessa voimakuvion pisteet menetetään puuttuvasta, ylimääräisestä tai väärään suuntaan piirretystä voimasta.

<svg data-fig="kartta" viewBox="0 0 380 888" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Aloita voimakuviosta ja katso, mikä tehtävän tunnusmerkki sopii. Vakionopeus tai levossa: kiihtyvyys on nolla, joten voimien summa on nolla. Lähtee levosta tai kiihtyy: kiihtyvyys ei ole nolla, joten voimien summa on massa kertaa kiihtyvyys. Tanko tai vipu pysyy paikallaan: myös momenttien summa on nolla. Kaksi kappaletta köydellä: oma liikeyhtälö kummallekin kappaleelle. Kitkaton pinta: ei kitkavoimaa. Liukuu karhealla pinnalla: liukukitka on kitkakerroin kertaa tukivoima. Pysyy paikallaan vaikka vedetään: lepokitka, enintään lähtökitkan suuruinen. Alkaa juuri liukua: täysin kehittynyt lepokitka eli lähtökitka on lepokitkakerroin kertaa tukivoima. Putoaa, ilmanvastus ja nopeus tasaantuu: voimat ovat tasapainossa ja ilmanvastus on yhtä suuri kuin paino." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="844" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{voimakuvio ensin, sitten tunnusmerkki}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{vakionopeus tai levossa}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ a = 0$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma\overline{F} = \overline{0}$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{lähtee levosta tai kiihtyy}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ a \neq 0$</div></foreignObject>
  <rect x="238" y="228" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="230" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma\overline{F} = m\overline{a}$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{tanko tai vipu pysyy paikallaan}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{myös momentit}$</div></foreignObject>
  <rect x="238" y="314" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="316" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma M = 0$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kaksi kappaletta köydellä}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{yhtälö kummallekin}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma F_i = m_i a_i$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kitkaton pinta}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{ei kitkavoimaa}$</div></foreignObject>
  <rect x="238" y="486" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="488" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\mu = 0$</div></foreignObject>
  <line x1="14" y1="564" x2="30" y2="564" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{liukuu karhealla pinnalla}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{liukukitka}$</div></foreignObject>
  <rect x="238" y="572" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="574" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\mu = \mu N$</div></foreignObject>
  <line x1="14" y1="650" x2="30" y2="650" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="614" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="624.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{pysyy paikallaan vaikka vedetään}$</div></foreignObject>
  <line x1="40" y1="654" x2="362" y2="654" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="659" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{lepokitka}$</div></foreignObject>
  <rect x="238" y="658" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="660" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F \le F_{\mu_0}$</div></foreignObject>
  <line x1="14" y1="747" x2="30" y2="747" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="700" width="342" height="94" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="710.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{alkaa juuri liukua}$</div></foreignObject>
  <line x1="40" y1="740" x2="362" y2="740" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="745" width="300" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{täysin kehittynyt lepokitka}$</div></foreignObject>
  <foreignObject x="44" y="767" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\text{eli lähtökitka}$</div></foreignObject>
  <rect x="238" y="766" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="768" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_{\mu_0} = \mu_0 N$</div></foreignObject>
  <line x1="14" y1="844" x2="30" y2="844" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="808" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="818.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{putoaa, ilmanvastus, nopeus tasaantuu}$</div></foreignObject>
  <line x1="40" y1="848" x2="362" y2="848" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="853" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{voimat tasapainossa}$</div></foreignObject>
  <rect x="238" y="852" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="854" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\text{v} = G$</div></foreignObject>
</svg>

Alun kysymyksen ratkaisee kappaleen valinta. Auto ja kärry vaikuttavat toisiinsa yhtä suurilla voimilla, mutta voimat vaikuttavat **eri kappaleisiin**, joten ne eivät kumoa toisiaan. Kärryn liikkeen ratkaisevat vain kärryyn vaikuttavat voimat: kiihdytettäessä vetoaisa vetää sitä eteenpäin enemmän kuin vierimisvastus jarruttaa.

```pysahdy
Auto vetää kärryä eteenpäin ja kärry autoa taaksepäin yhtä suurella voimalla. Miksi nämä voimat eivät kumoa toisiaan?
---
Ne vaikuttavat eri kappaleisiin. Kärryn liikkeen ratkaisevat vain kärryyn vaikuttavat voimat.
```

## Kaava: Newtonin lait ja voimat

### Newtonin lait

```kaavat
\Sigma\overline{F} = \overline{0} \ \Leftrightarrow\ \overline{v} = \text{vakio}
Newtonin 2. laki (dynamiikan peruslaki) :: \Sigma\overline{F} = m\overline{a}
\overline{F}_{AB} = -\overline{F}_{BA}
```

missä $\Sigma\overline{F}$ on kappaleeseen vaikuttavien voimien summa ($\text{N}$), $m$ massa ($\text{kg}$), $\overline{a}$ kiihtyvyys ($\text{m/s}^2$) ja $\overline{F}_{AB}$ voima, jolla A vaikuttaa B:hen. Laskussa toinen laki kirjoitetaan komponenteittain, $\Sigma F_x = ma_x$ ja $\Sigma F_y = ma_y$, ja vinon voiman komponentit ovat $F\cos\alpha$ ja $F\sin\alpha$. Kokonaisvoima osoittaa kiihtyvyyden suuntaan, ei aina nopeuden suuntaan.

```pysahdy
Kappale jarruttaa suoralla tiellä. Mihin suuntaan siihen vaikuttavien voimien summa osoittaa?
---
Kiihtyvyyden suuntaan eli nyt liikettä vastaan. Kokonaisvoima ei aina osoita nopeuden suuntaan.
```

### Paino, kitka ja rinne

```kaavat
kappaleeseen vaikuttava painovoima Maan pinnalla :: \overline{G} = m\overline{g}
liukukitka :: F_\mu = \mu N
lähtökitka, eli täysin kehittynyt lepokitka :: F_{\mu_0} = \mu_0 N
```

missä $\overline{g}$ on putoamiskiihtyvyys, $g = 9{,}81\,\text{m/s}^2$, joten painon suuruus on $G = mg$, $N$ on tukivoima ($\text{N}$), $\mu$ liukukitkakerroin ja $\mu_0$ lepokitkakerroin. Lepokitka on vain niin suuri kuin tilanne vaatii, enintään lähtökitkan $F_{\mu_0}$ suuruinen, ja se vastustaa pintojen liukumista toistensa suhteen, ei aina liikettä. Kaavat ovat kuivien pintojen kokeellisia malleja. Voimakuvioissa $\overline{F}_\mu$ tarkoittaa kumpaa tahansa kitkaa, lepo- tai liukukitkaa.

Rinteessä, jonka kaltevuuskulma on $\alpha$, painon komponentit ovat $G_x = mg\sin\alpha$ rinnettä alas ja $G_y = mg\cos\alpha$ rinnettä kohti. Kun pintaa vastaan kohtisuorassa vaikuttavat vain paino ja tukivoima, $N = mg\cos\alpha$. Komponentit eivät ole uusia voimia: ne piirretään katkoviivoin ja korvaavat painon laskussa.

<svg data-fig="kalteva" viewBox="0 0 600 380" role="img" aria-label="Kaksi kuvaa. Vasemmalla tilannekuva: muovipulkka liukuu lumista rinnettä alas vasemmalle. Rinne nousee oikealle kulmassa alfa vaakatasoon nähden. Pulkan yllä sininen nopeusnuoli ja oranssi kiihtyvyysnuoli osoittavat rinnettä alas. Oikealla pulkan voimakuvio, pulkka rinteen suuntaisesti kallistettuna suorakulmiona: paino G keskipisteestä suoraan alas, tukivoima N alapinnasta kohtisuoraan rinteestä ulospäin ja liukukitka F myy alapinnan ylemmästä kulmasta rinnettä ylös. Painon komponentit on piirretty katkoviivoin keskipisteestä: G x rinnettä alas ja G y kohtisuoraan rinnettä kohti. Komponentti G y on yhtä pitkä kuin tukivoima, ja G x on selvästi pidempi kuin kitka, joten voimien summa osoittaa rinnettä alas. Nuolten pituudet ovat mittakaavassa." style="max-width:100%;font-size:28px">
  <image href="pics/fy9/fy9-voimat-kalteva.webp" x="0" y="0" width="600" height="387.5" preserveAspectRatio="none"/>
  <foreignObject x="46" y="5" width="168" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="153.5" y="174.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="135" y="134.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="92.5" y="285" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$\alpha$</div></foreignObject>
  <foreignObject x="373" y="5" width="154" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <foreignObject x="409.5" y="326" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="388.5" y="45.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="509.5" y="142" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="338.5" y="189" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <foreignObject x="501.5" y="284" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <foreignObject x="450.5" y="223" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$\alpha$</div></foreignObject>
</svg>

```pysahdy
Kappale liukuu rinnettä, jonka kaltevuuskulma on $\alpha$, ja pintaa vastaan kohtisuorassa vaikuttavat vain paino ja tukivoima. Mikä on tukivoiman suuruus?
---
$N = mg\cos\alpha$, sillä tukivoima kumoaa painon pintaa vastaan kohtisuoran komponentin $G_y$. Se on pienempi kuin $mg$.
```

### Kytketyt kappaleet ja ilmanvastus

Kytketyille kappaleille piirretään kullekin oma voimakuvio ja kirjoitetaan oma liikeyhtälö. Kevyt, venymätön lanka ja kevyt, kitkaton väkipyörä antavat kappaleille saman kiihtyvyyden suuruuden ja samansuuruiset jännitysvoimat. Ilmanvastus $\overline{F}_\text{v}$ osoittaa nopeutta vastaan ja kasvaa nopeuden kasvaessa. Rajanopeudella kiihtyvyys on nolla, joten $F_\text{v} = G$.

## Yleisiä virheitä {Virheet}

- **Liikkeen suuntainen voima.** Liukuvaan kappaleeseen ei vaikuta mikään eteenpäin. Jokaisella voimalla on aiheuttaja, toinen kappale.
- **Voima ja vastavoima samassa kuviossa.** Ne vaikuttavat eri kappaleisiin eivätkä kumoa toisiaan.
- **$N = mg$ aina.** Rinteessä, vinossa vedossa ja kiihtyvässä hississä tukivoima on eri suuri kuin paino.
- **$F_\mu = \mu_0 N$ levossa.** Levossa kitka on vain niin suuri kuin tilanne vaatii; $\mu_0 N$ on sen yläraja.
- **Kytketyt: $T = m_2 g$.** Kun riippuva kappale kiihtyy alas, langan jännitysvoima on painoa pienempi.
- **Komponentit voimien lisäksi.** Jos sekä paino että sen komponentit ovat laskussa, paino tulee laskettua kahteen kertaan.

## Kertaa tarvittaessa {Kertaa}

- Ensimmäinen ja kolmas laki: [*Vuorovaikutus ja voima: Newtonin ensimmäinen ja kolmas laki*](fy4-3.html). Toinen laki: [*Newtonin toinen laki*](fy4-4.html).
- Voimakuvion kahdeksan vaihetta ja komponentit: [*Voimakuvio ja voimien yhteisvaikutus*](fy4-5.html).
- Paino, lepo- ja liukukitka ja rinne: [*Paino, kitka ja kalteva taso*](fy4-6.html).
- Lanka ja väkipyörä: [*Liikeyhtälö kytketyille kappaleille*](fy4-13.html). Rajanopeus: [*Ilmanvastus ja putoaminen ilmassa*](fy4-14.html).
