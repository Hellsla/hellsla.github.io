# Tuulivoimalan tutkiminen

> **Tutkimuskysymys:** Miten valitsemasi tekijä vaikuttaa tuulivoimalan pienoismallin tuottamaan sähkötehoon?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: työpöydän vasemmassa reunassa on puhallin, joka puhaltaa kohti tuulivoimalan pienoismallia. Ilmavirtaa kuvaavat katkoviivat kulkevat puhaltimesta roottoriin. Voimalan juurelta lähtevät johdot kulkevat säädettävään vastukseen ja kahteen yleismittariin. Puhaltimen ja voimalan välissä pöydällä on mittanauha, ja pöydällä on myös käsikäyttöinen tuulimittari ja vihko." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-tuulivoimala-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Tuulivoimala muuntaa liikkuvan ilman energiaa sähköksi. Kuinka paljon sähköä siitä saadaan, riippuu monesta asiasta: tuulesta, lavoista ja siitä, mitä voimalaan on kytketty. Tässä tutkimuksessa valitset yhden tekijän, muutat sitä hallitusti ja selvität mittaamalla, miten se vaikuttaa pienoismallin tuottamaan sähkötehoon. Suunnittele, mittaa ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** miten tuulivoimalan pienoismallin sähköteho riippuu yhdestä valitsemastasi tekijästä ja millä tekijän arvoilla teho on suurin mittausalueellasi, ovatko mittaamasi erot suurempia kuin mittausten epävarmuus, ja mistä järjestelmän energiahäviöt aiheutuvat.

Tutkittavaksi tekijäksi voit valita esimerkiksi tuulen nopeuden, lapojen lukumäärän, lapojen kulman, voimalan etäisyyden puhaltimesta tai sähköisen kuormituksen eli kuormitusvastuksen.

**Päätät itse** (molemmissa työtavoissa):

- tutkittavan tekijän ja sen arvot
- mittausten ja toistojen määrän
- miten pidät muut tekijät vakioina ja miten varmistat sen
- miten luet heiluvat mittarilukemat
- kuvaajan, josta tekijän vaikutus nähdään.

Osittain ohjatussa työtavassa sivu antaa näihin tukea ja neuvoo, miten epävarmuus arvioidaan.

::: tuki I
**Itsenäinen työtapa.** Valitset lisäksi epävarmuuden arviointitavan ja perustelet kaikki valintasi itse.

Laajennus, voimalan hyötysuhteen määrittäminen, kuuluu työhösi, jos käytössäsi on tuulimittari: vertaa tulostasi laajennuksessa kerrottuun ylärajaan.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Minkä tekijän valitsisit alustavasti? Voit vielä vaihtaa sen suunnitteluvaiheessa. Miten arvelet sähkötehon muuttuvan, kun tekijän arvo kasvaa? Luonnostele ennustamasi kuvaaja.
2. Kasvaako tai pieneneekö teho samaan suuntaan koko mittausalueella, vai voiko sillä olla suurin arvo jollakin tekijän arvolla? Perustele.
3. Vain osa voimalaa pyörittävän tuulen energiasta muuttuu sähköksi. Mihin loput energiasta joutuu?
4. Mitkä asiat voivat muuttua mittauksen aikana huomaamattasi, ja miten ne näkyisivät tuloksissa?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Tutkimuskysymyksessä on kaksi suuretta: valitsemasi tekijä ja sähköteho. Ennen kuin luet eteenpäin, kirjaa:

1. Mikä on muuttuja, jota muutat, ja miten muutat ja mittaat sen arvoa?
2. Mitä suureita mittaat jokaisella tekijän arvolla, jotta saat sähkötehon selville?
3. Mitkä muut tekijät vaikuttavat sähkötehoon, ja miten pidät ne vakioina?

## Teoriaa lyhyesti

Tuuli pyörittää voimalan roottoria, ja roottorin akseli pyörittää generaattoria, joka muuntaa pyörimisen energian sähköenergiaksi. Generaattoriin kytketty kuorma, tässä kuormitusvastus, muuntaa sähköenergian lämmöksi. Energiaketjun jokaisessa vaiheessa osa energiasta muuttuu muuksi kuin siksi, mitä seuraava vaihe tarvitsee. [[apua:fy4-15|Vesi- ja tuulivoima energian muuntajina]]

**Teho** kertoo, kuinka paljon energiaa muuntuu tai siirtyy aikayksikössä: $P = \dfrac{\Delta E}{\Delta t}$. Voimalan **sähköteho** on energia, jonka generaattori siirtää kuormaan sekunnissa. [[apua:fy2-3|Teho]]

Sähkötehoa ei yleensä lueta suoraan mittarista, vaan se lasketaan kahdesta mitattavasta suureesta. **Sähkövirta** $I$ kertoo, kuinka paljon sähkövarausta kulkee kuorman läpi sekunnissa. Sen yksikkö on ampeeri, $1\,\text{A} = 1\,\text{C/s}$, missä coulomb $\text{C}$ on varauksen yksikkö. **Jännite** $U$ kertoo, kuinka paljon energiaa varaus luovuttaa kuormaan varausyksikköä kohti. Sen yksikkö on voltti, $1\,\text{V} = 1\,\text{J/C}$. Kun jännite ja sähkövirta kerrotaan, saadaan kuormaan sekunnissa siirtyvä energia eli sähköteho:

```latex
P = UI
```

missä $P$ on sähköteho, $U$ kuorman napojen välinen jännite ja $I$ kuorman läpi kulkeva sähkövirta. Yksiköt sopivat yhteen: $\text{V} \cdot \text{A} = \dfrac{\text{J}}{\text{C}} \cdot \dfrac{\text{C}}{\text{s}} = \dfrac{\text{J}}{\text{s}} = \text{W}$. Sähkötehoa ja virtapiirejä käsitellään tarkemmin moduulissa FY6.

Jännitemittari kytketään **rinnan** kuorman kanssa eli kuorman napoihin. Virtamittari kytketään **sarjaan** kuorman kanssa, jolloin sama sähkövirta kulkee mittarin ja kuorman läpi. Kuvassa on yksi tapa kytkeä mittarit. Tarkista opettajalta, tuottaako pienoismallisi generaattori tasa- vai vaihtojännitettä, ja aseta mittarit sen mukaan. Vaihtojännitealueella mittarit näyttävät jännitteen ja sähkövirran tehollisarvot, ja vastuskuormalla niiden tulo $P = UI$ on silloinkin kuormaan siirtyvä keskimääräinen teho.

<svg data-fig="circuit" viewBox="0 0 600 290" role="img" aria-label="Kytkentäkaavio. Vasemmalla on generaattori G. Siitä lähtevässä yläjohtimessa on virtamittari A sarjassa, ja johdin jatkuu oikealle säädettävään kuormitusvastukseen, joka on piirretty suorakulmiona, jonka läpi kulkee vino nuoli. Jännitemittari V on kytketty kuormitusvastuksen rinnalle sen kumpaankin napaan. Alajohdin palaa vastukselta generaattorille. Yläjohtimeen on merkitty sähkövirta I ja jännitemittarin viereen jännite U." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-tuulivoimala-circuit.webp" x="8.6" y="4.9" width="591.1" height="293.1" preserveAspectRatio="none"/>
  <foreignObject x="80" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{G}$</div></foreignObject>
  <foreignObject x="235" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="139" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I$</div></foreignObject>
  <foreignObject x="510" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="554" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="132" y="187.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{generaattori}$</div></foreignObject>
  <foreignObject x="169" y="125.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{kuormitusvastus}$</div></foreignObject>
</svg>

::: tuki OO
Tarkista kirjauksesi tästä. Mittaat jokaisella tekijän arvolla kuorman jännitteen $U$ ja sähkövirran $I$ ja lasket niistä sähkötehon $P = UI$. Kaikki luettelon tekijät vaikuttavat tehoon, joten muuta vain yhtä kerrallaan ja pidä muut samoina:

| Tekijä | Miten muutat ja mittaat sitä | Mitä pidät vakiona |
|---|---|---|
| tuulen nopeus $v$ | puhaltimen nopeusasetus; mittaa $v$ tuulimittarilla voimalan kohdalta | lavat, lapakulma, kuorma, voimalan paikka |
| lapojen lukumäärä | vaihda lapoja, sijoita ne tasaisesti navan ympärille | lapojen muoto ja kulma, tuuli, kuorma, paikka |
| lapakulma | aseta kaikki lavat samaan kulmaan; lue kulma navan asteikosta tai astelevyllä | lapojen määrä, tuuli, kuorma, paikka |
| etäisyys puhaltimesta | mittaa etäisyys puhaltimen ritilästä roottoriin | puhaltimen asetus, lavat, kuorma, voimala puhaltimen keskilinjalla |
| kuormitusvastus $R$ | säädä vastusta; lue arvo vastuksen asteikolta tai laske mittauksistasi $R = \dfrac{U}{I}$ | tuuli, lavat, lapakulma, paikka |

Kuorman resistanssi $R = \dfrac{U}{I}$ kertoo, kuinka suuri jännite tarvitaan kuljettamaan kuorman läpi tietty sähkövirta. Sitä käsitellään moduulissa FY6.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä tekijää muutat, mitkä sen arvot valitset, mitä mittaat ja mitä pidät vakiona. Kokeile järjestelyä ensin: lähteekö roottori pyörimään kaikilla valitsemillasi arvoilla, ja kuinka paljon mittarilukemat heiluvat?

::: tuki OO
**Osittain ohjattu.** Valitse tekijä, jonka arvoa pystyt muuttamaan ainakin viidessä vaiheessa. Lapojen lukumäärässä riittää se, mitä välineistössä on. Päätä itse arvot, toistojen määrä ja lukutapa. Kirjaa päätöksesi perusteluineen.

Mieti ainakin näitä:

- Miten merkitset voimalan ja puhaltimen paikat, jotta ne pysyvät samoina koko mittauksen ajan, ellei juuri etäisyyttä tutkita?
- Kuinka kauan odotat jokaisen muutoksen jälkeen, ennen kuin luet mittarit?
- Lukemat heiluvat, koska puhaltimen ilmavirta on pyörteinen. Luetko useita lukemia ja lasket niistä keskiarvon, vai tallennatko jännitteen ja sähkövirran antureilla?
- Miten luet jännitteen ja sähkövirran samaan aikaan, kun ne ovat eri mittareissa?
:::

::: tuki OO
**Vihjeitä tekijöittäin.**

- **Kuormitusvastus.** Kun generaattorista otetaan sähkövirtaa, generaattori vastustaa roottorin pyörimistä. Käy läpi laaja resistanssialue, myös aivan pienet ja hyvin suuret arvot.
- **Tuulen nopeus.** Puhaltimessa on yleensä vain muutama nopeusasetus. Mittaa tuulen nopeus voimalan paikalta niin, että voimala on siirretty sivuun, koska roottori hidastaa ilmaa edessään. Ilmavirta ei ole tasainen: mittaa useasta kohdasta roottorin alueelta.
- **Etäisyys.** Etäisyyden muuttaminen muuttaa voimalaan osuvaa ilmavirtaa. Jos mittaat lisäksi tuulen nopeuden jokaisella etäisyydellä, voit tarkastella tehoa myös tuulen nopeuden funktiona.
- **Lapojen lukumäärä ja kulma.** Päätä, mistä lapakulma mitataan, esimerkiksi lavan ja roottorin pyörimistason välistä, ja käytä samaa tapaa koko ajan. Pidä roottori tasapainossa: epäsymmetrinen roottori tärisee.
:::

## Mittaa

Kirjaa alkuperäiset mittarilukemat taulukkoon heti mittauksen aikana. Laskemasi teho saa oman sarakkeensa mitattujen oikealle puolelle. Kirjaa myös vakioina pitämiesi tekijöiden arvot, esimerkiksi etäisyys ja puhaltimen asetus.

::: tuki OO
Voit käyttää esimerkiksi tällaista taulukkoa. Kirjaa jokainen toisto omalle rivilleen ja laske kunkin tekijän arvon tehoista keskiarvo $\overline{P}$ erilliseen taulukkoon, jossa on tekijän arvo, $\overline{P}$ ja sen epävarmuus $\Delta P$.

| tekijän arvo (yksikkö) | toisto | $U\ (\text{V})$ | $I\ (\text{A})$ | $P = UI\ (\text{W})$ |
|---|---|---|---|---|
| | 1. | | | |
| | 2. | | | |
| | 3. | | | |

Lue jännite ja sähkövirta mahdollisimman samaan aikaan, esimerkiksi niin, että kaksi ryhmäläistä lukee kumpikin oman mittarinsa sovitusta merkistä. Jos lukemat heiluvat, kirjaa myös heilahtelun pienin ja suurin arvo: heilahtelu on tässä työssä usein suurempi kuin mittarin lukematarkkuus.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti luet mittarit ja kuinka paljon lukemat vaihtelevat. [[apua:fy1-3|Mittausepävarmuus ja toistomittaukset]]

## Käsittele tulokset

Laske sähköteho jokaisella tekijän arvolla. Piirrä mittaustuloksista kuvaaja, josta näkyy, miten sähköteho riippuu tutkimastasi tekijästä. Merkitse akseleille suureet ja yksiköt. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla. Sovita pisteisiin suora tai käyrä vain, jos sille on fysikaaliset perusteet. [[apua:fy1-4|Kuvaajan laatiminen ja tulkinta]]

::: tuki OO
Valitse pystyakselille sähköteho $\overline{P}$ ja vaaka-akselille tutkimasi tekijä. Merkitse jokaiseen pisteeseen pystysuora virhejana, jonka pituus kumpaankin suuntaan on tehon epävarmuus $\Delta P$: silloin näet suoraan, ovatko pisteiden väliset erot epävarmuutta suurempia. Lapojen lukumäärällä on vain kokonaislukuarvoja, joten sen kuvaajassa pisteiden välille ei piirretä käyrää. Jos tutkit tuulen nopeutta, voit kokeilla, ovatko pisteet suoralla, kun vaaka-akselille valitaan $v^3$ (katso laajennus). Pisteiden pitäisi osua suoralle vain, jos hyötysuhde ei muutu tuulen nopeuden mukana.
:::

Vastaa:

1. Miten sähköteho muuttuu, kun tekijän arvo kasvaa? Onko teholla suurin arvo mittausalueellasi?
2. Millä tekijän arvoilla voimala toimii parhaiten, ja kuinka tarkasti voit sanoa sen kuvaajasta?
3. Ovatko pisteiden väliset erot suurempia kuin tehon epävarmuus?

Laskuihin ja kuvaajaan käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-kuvaaja|Mittauspisteiden kuvaaja]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Arvioi tehon epävarmuus $\Delta P$ jokaisessa mittauspisteessä, vähintään parhaassa pisteessä ja sen naapuripisteissä, jotta voit verrata pisteiden välisiä eroja epävarmuuteen. Ilmoita sähköteho epävarmuuksineen ainakin sillä tekijän arvolla, jolla voimala toimi parhaiten, muodossa $P = (P \pm \Delta P)\,\text{W}$, ja perustele, miten arvioit epävarmuuden.

::: tuki OO
Tehon epävarmuuden voit arvioida näin:

- **Jännitteen ja sähkövirran epävarmuus.** Käytä epävarmuutena $\Delta U$ ja $\Delta I$ suurempaa seuraavista: mittarin lukematarkkuus tai heilahtelun vaihteluvälin puolikas.
- **Tulon epävarmuus.** Kun suureet kerrotaan, niiden suhteelliset epävarmuudet lasketaan yhteen: $\dfrac{\Delta P}{P} = \dfrac{\Delta U}{U} + \dfrac{\Delta I}{I}$.
- **Toistot.** Jos teit toistoja, arvioi keskiarvon epävarmuus myös toistojen vaihteluvälin puolikkaana, $\Delta P = \dfrac{P_\text{max} - P_\text{min}}{2}$, ja käytä suurempaa näistä kahdesta arviosta.

Pyöristä $\Delta P$ yhteen merkitsevään numeroon ja $P$ samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä tekijät saattoivat muuttua, vaikka yritit pitää ne vakioina? Olivatko virheet satunnaisia vai systemaattisia, ja mihin suuntaan systemaattiset virheet olisivat muuttaneet tulosta? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Miten valitsemasi tekijä vaikutti sähkötehoon, ja millä käyttöalueella voimala toimi parhaiten? Mistä järjestelmän energiahäviöt aiheutuvat? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tutkimuskysymys ja hypoteesi:** valitsemasi tekijä ja ennusteesi perusteluineen.
- **Koejärjestely ja menetelmä:** mitä muutit, mitä mittasit ja mitä pidit vakiona, miten varmistit sen, sekä kytkentäkaavio.
- **Mittaustulokset:** alkuperäiset jännitteen ja sähkövirran lukemat omissa sarakkeissaan ja teho niiden oikealla puolella.
- **Tulos:** kuvaaja, teho epävarmuuksineen oikein pyöristettynä ja voimalan paras käyttöalue.
- **Luotettavuus:** energiahäviöt ja ne tekijät, jotka vaikuttivat mittaustulosten luotettavuuteen.

## Laajennus: tuulivoimalan hyötysuhde

Kuinka suuri osa tuulen tehosta muuttuu sähköksi? Roottorin läpi virtaavan tuulen teho on

```latex
P_\text{tuuli} = \tfrac{1}{2}\rho A v^3
```

missä $\rho$ on ilman tiheys (huoneilmassa noin $1{,}2\,\text{kg/m}^3$; tiheys riippuu lämpötilasta ja ilmanpaineesta), $A = \pi r^2$ roottorin pyyhkäisemä pinta-ala, $r$ roottorin säde eli etäisyys navan keskeltä lavan kärkeen ja $v$ tuulen nopeus. Malli olettaa, että tuuli puhaltaa kohtisuoraan roottoria kohti ja sen nopeus on sama koko pinta-alalla. Nopeus $v$ on tuulen nopeus ennen kuin roottori hidastaa ilmaa. [[apua:fy4-15|Tuulivoimalan teho]]

<svg data-fig="swept" viewBox="0 0 600 340" role="img" aria-label="Kaaviokuva. Vasemmalla roottori edestä: kolmen lavan kärjet piirtävät pyöriessään katkoviivalla merkityn ympyrän. Ympyrän säde r on etäisyys navan keskeltä lavan kärkeen, ja ympyrän pinta-ala on roottorin pyyhkäisemä pinta-ala A, joka on pii kertaa r toiseen. Oikealla sama roottori sivulta: kolme sinistä nopeusnuolta v osoittaa vasemmalta kohti roottoria, kohtisuoraan roottorin tasoa vastaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-tuulivoimala-swept.webp" x="1.2" y="0" width="597" height="345.8" preserveAspectRatio="none"/>
  <foreignObject x="230" y="118" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="130" y="295.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A = \pi r^2$</div></foreignObject>
  <foreignObject x="363.5" y="41.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
</svg>

Voimalan **hyötysuhde** on sen antaman sähkötehon $P$ ja tuulen tehon suhde: [[apua:fy2-4|Hyötysuhde]]

```latex
\eta = \frac{P}{P_\text{tuuli}}
```

Edes ihanteellinen roottori ei voi muuttaa käyttökelpoiseksi kuin noin $59\ \%$ läpi virtaavan tuulen tehosta, koska ilman on päästävä virtaamaan pois roottorin takaa. Tätä ylärajaa kutsutaan Betzin rajaksi. Todellisessa voimalassa osa energiasta menetetään lisäksi kitkaan ja generaattorissa, joten hyötysuhde jää rajan alle.

Määritä voimalan hyötysuhde epävarmuuksineen ainakin sillä tekijän arvolla, jolla voimala toimi parhaiten, ja selvitä, minkä suureen epävarmuus vaikuttaa tulokseen eniten. Onko tuloksesi uskottava, kun vertaat sitä Betzin rajaan? Miten tuulen epätasaisuus voi vaikuttaa tulokseen?

::: tuki OO
**Vihjeitä.** Mittaa tuulen nopeus useasta kohdasta tasaisesti roottorin alueelta voimala sivuun siirrettynä. Koska tuulen teho on verrannollinen nopeuden kuutioon, laske keskiarvo luvuista $v^3$, älä korota nopeuksien keskiarvoa kolmanteen potenssiin. Hyötysuhteen suhteellinen epävarmuus on suhteellisten epävarmuuksien summa, ja potenssi kertoo, kuinka monta kertaa suure lasketaan mukaan:

```latex
\begin{aligned}
\frac{\Delta \eta}{\eta} &= \frac{\Delta P}{P} + \frac{\Delta \rho}{\rho} \\
&\quad + 2\cdot\frac{\Delta r}{r} + 3\cdot\frac{\Delta v}{v}
\end{aligned}
```

Koska käytit nopeuksien kuutioiden keskiarvoa, $v$ tarkoittaa tässä lukua $\sqrt[3]{\overline{v^3}}$, missä $\overline{v^3}$ on lukujen $v^3$ keskiarvo. Voit myös arvioida kuutioiden keskiarvon suhteellisen epävarmuuden suoraan ja käyttää sitä termin $3\cdot\dfrac{\Delta v}{v}$ paikalla. Myös ilman tiheyden epävarmuuden $\Delta\rho$ voit arvioida. Tiheys riippuu huoneen lämpötilasta ja ilmanpaineesta: katso se taulukkokirjasta tai laske se niiden avulla. Arvioi sitten, kuinka paljon tiheys muuttuu, kun lämpötila ja paine vaihtelevat mittaustesi epävarmuuden verran.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Muutitko vain yhtä tekijää kerrallaan? Miten sen voi todeta mittauspöytäkirjastasi?
- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
