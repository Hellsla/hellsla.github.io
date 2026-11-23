# Vesivoimalaitoksen pienoismallin hyötysuhde

> **Tutkimuskysymys:** Kuinka suuri osa putoavan veden energiasta muuttuu pienoisvoimalaitoksessa sähköksi, ja miten hyötysuhde riippuu käyttötilanteesta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydän vieressä on korkea teline, jonka päällä on vesisäiliö. Säiliön pohjasta lähtee letku alas pienen vesiturbiinin luo. Turbiinin akselilla on generaattori, josta johdot kulkevat kuormavastukselle ja kahdelle yleismittarille, joiden näytöt ovat tyhjät. Turbiinin läpi kulkenut vesi valuu ämpäriin, joka on vaa&#x27;an päällä. Pöydällä on sekuntikello ja kuivausliina." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-vesivoima-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Suomessa vesivoimalaitokset muuttavat putoavan veden energiaa sähköksi. Pienoismallissa periaate on sama: vesi putoaa, pyörittää turbiinia, ja turbiinin akselilla oleva generaattori tuottaa sähköä. Tässä tutkimuksessa selvität mittaamalla, kuinka suuri osa veden energiasta päätyy pienoismallissa sähköksi ja muuttuuko osuus, kun voimalaitosta käytetään eri tavoin. Mittaa, laske ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** mikä on pienoisvoimalaitoksen hyötysuhde epävarmuuksineen ja miten se muuttuu, kun veden virtaamaa tai putouskorkeutta muutetaan. Selvitä myös, mitä energiaa tai tehoa järjestelmään syötetään, mitä siitä saadaan hyödyksi ja mitä suureita näiden määrittämiseksi on mitattava.

**Päätät itse:** mitä järjestelmään luet kuuluvaksi ja mistä mihin putouskorkeus mitataan, muutatko virtaamaa vai putouskorkeutta ja millä arvoilla, miten mittaat veden määrän ja ajan, mittauspisteiden ja toistojen määrän, kuvaajan, jolla esität tulokset, sekä tavan, jolla arvioit tuloksen epävarmuuden. Osittain ohjatussa työtavassa sivu antaa näihin tukea, itsenäisessä työtavassa perustelet valintasi itse.

Opettajan pienoismalli voi poiketa tämän sivun kuvista: sovella suunnitelmasi siihen laitteeseen, joka teillä on käytössä.

::: tuki I
**Itsenäinen työtapa.** Laajennus, kuorman vaikutus sähkötehoon ja hyötysuhteeseen, kuuluu työhösi, jos pienoismallin kuormaa voi vaihtaa.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Kuinka suuri osa veden energiasta arvelet päätyvän pienoismallissa sähköksi: lähes kaikki, noin puolet vai pieni osa? Miksi?
2. Mihin se osa veden energiasta joutuu, joka ei muutu sähköksi? Luettele ainakin kolme kohdetta.
3. Jos veden teho kaksinkertaistuu, kaksinkertaistuuko myös sähköteho? Pysyykö hyötysuhde samana?
4. Minkä suureen mittaaminen on todennäköisesti vaikeinta, ja miten voisit helpottaa sitä?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Energiaa tai tehoa ei voi lukea suoraan mistään mittarista. Ennen kuin luet eteenpäin, kirjaa:

1. Mitä energiaa järjestelmään syötetään, ja mistä suureista sen teho saadaan?
2. Mitä energiaa järjestelmästä saadaan hyödyksi, ja mistä suureista sen teho saadaan?
3. Missä järjestelmä alkaa ja mihin se päättyy? Esimerkiksi: kuuluuko veden putoaminen turbiinin alapuolella keräysastiaan järjestelmään?

## Teoriaa lyhyesti

**Hyötysuhde** $\eta$ on laitteen antaman hyötytehon ja laitteeseen otetun tehon suhde [[apua:fy2-4|Hyötysuhde]]:

```latex
\eta = \frac{P_\text{s}}{P_\text{o}}
```

missä $P_\text{s}$ on tässä työssä generaattorin kuormalle antama sähköteho ja $P_\text{o}$ veden voimalaitokselle tuoma teho. Energia säilyy, joten hyötysuhde on enintään $100\,\%$.

**Teho** on energian muutos jaettuna ajalla, jossa muutos tapahtuu: $P = \dfrac{\Delta E}{\Delta t}$ [[apua:fy2-3|Teho]]. Kun vesi laskeutuu korkeuden $h$ verran, sen **potentiaalienergia** pienenee määrällä $mgh$ [[apua:fy4-7|Potentiaalienergia]]. Oikea vesivoimala käyttää juuri tätä energiaa [[apua:fy4-15|Vesi- ja tuulivoima]].

**Sähköteho.** Kun generaattori syöttää sähkövirtaa kuormaan, esimerkiksi vastukseen, kuorman saama sähköteho on

```latex
P_\text{s} = UI
```

missä $U$ on kuorman napojen välinen jännite (yksikkö voltti, $\text{V}$) ja $I$ kuorman läpi kulkeva sähkövirta (yksikkö ampeeri, $\text{A}$). Teho saadaan watteina, koska $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$. Jännite mitataan jännitemittarilla, joka kytketään kuorman rinnalle, ja sähkövirta virtamittarilla, joka kytketään sarjaan kuorman kanssa, niin että sama virta kulkee molempien läpi. Sähkötehoa käsitellään tarkemmin moduulissa FY6.

Kysy opettajalta, antaako pienoismallin generaattori tasa- vai vaihtojännitettä, ja aseta molemmat mittarit sen mukaan. Vaihtojännitteellä $P_\text{s} = UI$ lasketaan mittarien näyttämistä tehollisarvoista, ja se pätee, kun kuormana on vastus.

::: tuki OO
Tarkista kirjauksesi tästä. Rajataan järjestelmäksi vesi, turbiini ja generaattori siitä, kun vesi lähtee ylemmän astian vedenpinnalta, siihen, kun se on kulkenut turbiinin läpi. **Putouskorkeus** $h$ mitataan ylemmän astian vedenpinnasta turbiinin tasolle, esimerkiksi turbiinin akselin tasolle, sama kohta jokaisessa mittauksessa. Turbiinin alapuolinen putoaminen keräysastiaan ei pyöritä turbiinia, joten se jää järjestelmän ulkopuolelle.

<svg data-fig="setup" viewBox="0 0 600 470" role="img" aria-label="Kaaviokuva. Vasemmalla ylhäällä on vesiastia. Sen pohjasta letku vie veden alas turbiinille. Putouskorkeus h on merkitty astian vedenpinnasta turbiinin akselin tasolle. Turbiinin läpi kulkenut vesi valuu keräysastiaan, joka on vaa&#x27;an päällä. Turbiinin akselilla on generaattori G. Generaattorin virtapiirissä on kuormavastus R, sen kanssa sarjassa virtamittari A ja sen rinnalla jännitemittari V." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-vesivoima-setup.webp" x="0" y="-1.2" width="600" height="475" preserveAspectRatio="none"/>
  <foreignObject x="90" y="337.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{turbiini}$</div></foreignObject>
  <foreignObject x="322" y="423.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{vaaka}$</div></foreignObject>
  <foreignObject x="58" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="450" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="362" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{G}$</div></foreignObject>
  <foreignObject x="426" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="556" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
</svg>

Kun ajassa $\Delta t$ turbiinin läpi virtaa veden massa $\Delta m$, veden potentiaalienergia pienenee määrällä $\Delta m \cdot g h$. Veden voimalaitokselle tuoma teho on siis

```latex
P_\text{o} = \frac{\Delta m}{\Delta t} \cdot g h
```

missä $\dfrac{\Delta m}{\Delta t}$ on massavirta eli sekunnissa turbiinin läpi kulkeva veden massa ($\text{kg/s}$), $g$ putoamiskiihtyvyys ja $h$ putouskorkeus. Malli edellyttää, että

- vesi on ylemmän astian pinnalla lähes levossa ja virtaa alas pelkän painovoiman vaikutuksesta. Jos pienoismalliin tulee vettä vesijohdosta tai pumpulta, putouskorkeus ei yksin kerro veden energiaa: kysy opettajalta, miten järjestely tehdään.
- putouskorkeus pysyy mittauksen ajan lähes samana. Jos ylemmän astian pinta laskee mittauksen aikana selvästi, käytä pinnan korkeuden keskiarvoa ja ota pinnan lasku huomioon epävarmuudessa.

Turbiinista lähtevällä vedellä on vielä liike-energiaa. Se ei muutu sähköksi, joten tässä rajauksessa se on yksi häviöistä.

Hyötysuhde on tällöin

```latex
\eta = \frac{P_\text{s}}{P_\text{o}} = \frac{UI}{\dfrac{\Delta m}{\Delta t} \cdot g h}
```
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona. Kirjaa järjestelmän rajaus perusteluineen.

::: tuki OO
**Osittain ohjattu.** Valitse, muutatko virtaamaa, esimerkiksi letkun hanalla tai suuttimen koolla, vai putouskorkeutta, eli ylemmän astian korkeutta. Pidä toinen niistä ja kuorma vakiona. Tee mittaus ainakin viidellä eri arvolla. Jokaisessa mittauksessa mittaat veden massan $\Delta m$, joka kulkee turbiinin läpi ajassa $\Delta t$, putouskorkeuden $h$ sekä kuorman jännitteen $U$ ja sähkövirran $I$ samana aikana. Kirjaa päätöksesi perusteluineen.

Mieti ainakin näitä:

- Miten mittaat massan $\Delta m$? Punnitsetko keräysastian ennen ja jälkeen vai mittaatko veden tilavuuden ja käytät veden tiheyttä? Jos osa turbiinin läpi kulkeneesta vedestä roiskuu keräysastian ohi, $\Delta m$ jää liian pieneksi ja hyötysuhde liian suureksi.
- Kuinka pitkä keräysaika $\Delta t$ tarvitaan, jotta ajanoton aloitus ja lopetus eivät vaikuta paljon tulokseen?
- Pysyykö ylemmän astian vedenpinta paikallaan, vai pitääkö sitä täyttää mittauksen aikana tai seurata pinnan laskua?
- Heilahtelevatko jännite ja virta? Miten luet niistä edustavan arvon samalta ajalta kuin veden keräys?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle. Kirjaa myös, kuinka tarkasti luit kunkin suureen, ja huolehdi, että jokainen mittaus tehdään mahdollisimman samalla tavalla. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

::: tuki OO
Voit käyttää esimerkiksi tällaista taulukkoa:

| $h\ (\text{m})$ | $\Delta m\ (\text{kg})$ | $\Delta t\ (\text{s})$ | $U\ (\text{V})$ | $I\ (\text{A})$ | $P_\text{o}\ (\text{W})$ | $P_\text{s}\ (\text{W})$ | $\eta$ |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Jos punnitset keräysastian ennen ja jälkeen, kirjaa molemmat lukemat omiin sarakkeisiinsa ja laske $\Delta m$ niiden erotuksena. Aloita veden keräys vasta, kun turbiinin pyörimisnopeus ja mittarien lukemat ovat asettuneet. Toista ainakin yksi mittaus, niin näet, kuinka hyvin tulos toistuu.
:::

## Käsittele tulokset

Laske jokaisesta mittauksesta veden teho, sähköteho ja hyötysuhde. Esitä tulokset kuvaajana, josta näkyy, miten hyötysuhde tai sähköteho muuttuu käyttötilanteen mukana. Merkitse akseleille suureet ja yksiköt. [[apua:fy1-4|Graafinen esitys]]

Vastaa:

1. Onko hyötysuhde sama kaikissa mittauksissa? Jos ei, millä tavalla se muuttuu?
2. Onko sähköteho suoraan verrannollinen veden tehoon?
3. Millä käyttötavalla pienoismalli toimii parhaiten, ja mistä arvelet sen johtuvan?

::: tuki OO
**Kuvaajan valinta.** Kaksi luontevaa kuvaajaa ovat hyötysuhde $\eta$ muutetun suureen funktiona sekä sähköteho $P_\text{s}$ veden tehon $P_\text{o}$ funktiona. Jälkimmäisessä kuvaajassa hyötysuhde on origosta mittauspisteeseen piirretyn suoran kulmakerroin. Jos kaikki pisteet ovat samalla origon kautta kulkevalla suoralla, hyötysuhde on sama kaikissa mittauksissa. Jos pisteet eivät ole sellaisella suoralla, hyötysuhde muuttuu. Mieti, mitä kuvaajan muoto kertoo häviöistä.

<svg data-fig="eta" viewBox="0 0 600 380" role="img" aria-label="Mallikuvaaja: vaaka-akselilla veden teho P o ja pystyakselilla sähköteho P s, samassa mittakaavassa. Katkoviiva origosta on suora, jolla hyötysuhde on yksi eli sata prosenttia; sen yläpuolelle ei voi päätyä, koska energia säilyy. Toinen origon kautta kulkeva suora näyttää, että kaikilla saman origon kautta kulkevan suoran pisteillä on sama hyötysuhde. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="149" y1="330" x2="424" y2="330" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M436,330 L423,336 L423,324 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="150" y1="331" x2="150" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M150,44 L156,57 L144,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="120" y="335.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="442" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{o}$</div></foreignObject>
  <foreignObject x="140" y="13.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{s}$</div></foreignObject>
  <polygon points="150,330 410,70 150,70" fill="#c9c2b2" fill-opacity="0.35"/>
  <polyline points="150,330 410,70" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <foreignObject x="165.5" y="92" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{mahdoton alue}$</div></foreignObject>
  <foreignObject x="332" y="162" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\eta = 1$</div></foreignObject>
  <polyline points="150,330 410,200" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="418" y="185.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sama } \eta$</div></foreignObject>
</svg>
:::

Tee laskut ja kuvaajat Graphical Analysis Pro -ohjelmalla. Ruukkilabran ohjeet: [[ohje:tvt-kuvaaja|Mittauspisteiden kuvaaja]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita hyötysuhde epävarmuuksineen ainakin yhdessä käyttötilanteessa ja perustele, miten arvioit epävarmuuden. Pohdi myös, mitkä mitatuista suureista vaikuttavat tulokseen eniten.

::: tuki OO
Hyötysuhde lasketaan viiden mitatun suureen tuloista ja osamääristä. Silloin tuloksen suhteellinen epävarmuus on likimain mitattujen suureiden suhteellisten epävarmuuksien summa:

```latex
\begin{aligned}
\frac{\Delta \eta}{\eta} \approx {} & \frac{\Delta U}{U} + \frac{\Delta I}{I} \\
& + \frac{\Delta (\Delta m)}{\Delta m} + \frac{\Delta (\Delta t)}{\Delta t} \\
& + \frac{\Delta h}{h}
\end{aligned}
```

Jos $\Delta m$ on kahden punnituksen erotus, sen epävarmuus on punnitusten epävarmuuksien summa. Jos jännite ja virta heilahtelevat, käytä epävarmuutena heilahtelun puolikasta. Jos vedenpinta laskee mittauksen aikana, käytä putouskorkeutena keskiarvoa ja epävarmuutena puolta pinnan laskusta. Laske jokaisen termin osuus erikseen: suurin termi kertoo, mitä mittausta kannattaa parantaa ensimmäisenä.

Pyöristä $\Delta \eta$ yhteen merkitsevään numeroon ja $\eta$ samaan tarkkuuteen.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet hyötysuhdetta? Muuttaisiko toisenlainen järjestelmän rajaus tulosta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Kuinka suuri on pienoismallin hyötysuhde, ja miten se riippuu käyttötilanteesta? Mitkä ovat tärkeimmät energiahäviöt, ja mihin energia niissä muuttuu? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

Halutessasi arvioi yhden häviön suuruus, esimerkiksi turbiinista lähtevän veden liike-energia sekunnissa: mitä sinun pitäisi mitata, ja kuinka suuren osan veden tehosta se vie?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tutkimuskysymys ja tausta:** mitä energiaa järjestelmään syötetään, mitä siitä saadaan hyödyksi ja miten tehot lasketaan mitatuista suureista.
- **Koejärjestely ja menetelmä:** kuva järjestelystä, järjestelmän rajaus, mistä mihin putouskorkeus mitattiin, miten virtapiiri kytkettiin ja miten työturvallisuus huomioitiin.
- **Mittaustulokset:** alkuperäiset lukemat omissa sarakkeissaan ja lasketut tehot ja hyötysuhde niiden oikealla puolella.
- **Tulos:** hyötysuhde epävarmuuksineen oikein pyöristettynä ja kuvaaja sen riippuvuudesta käyttötilanteesta.
- **Luotettavuus:** suurimmat epävarmuuden lähteet ja tärkeimmät energiahäviöt.

## Laajennus: kuorman vaikutus

Generaattorin antama sähköteho ei riipu pelkästään vedestä vaan myös siitä, mihin generaattori on kytketty. Mitä suurempi virta generaattorin läpi kulkee, sitä enemmän generaattori jarruttaa turbiinia.

Pidä veden virtaama ja putouskorkeus vakiona ja vaihda kuormaa, esimerkiksi eri suuruisiin vastuksiin. Ennen kuin mittaat, pohdi lausekkeen $P_\text{s} = UI$ avulla: mitä sähköteholle tapahtuu, jos kuorman resistanssi on hyvin suuri, jolloin virta on lähes nolla? Entä jos kuorma on lähes oikosulku, jolloin jännite on lähes nolla? Mittaa sitten sähköteho usealla kuormalla, esitä tulos kuvaajana ja päättele, millä kuormalla pienoismalli antaa suurimman sähkötehon ja suurimman hyötysuhteen. Vertaa tulosta päämittauksen tulokseen: kumpi vaikuttaa hyötysuhteeseen enemmän, päämittauksessa muuttamasi suure vai kuorma?

::: tuki OO
**Vihjeitä.** Kirjaa jokaisesta kuormasta, mikä se oli, esimerkiksi vastuksen resistanssi. Aloita suurimmasta resistanssista: kun resistanssi pienenee, virta kasvaa, joten tarkista ennen jokaista mittausta, että virtamittarin mittausalue riittää. Laske hyötysuhde jokaisella kuormalla samalla tavalla kuin päämittauksessa. Pohdi myös: miksi kuorma, jolla sähköteho on suurin, antaa myös suurimman hyötysuhteen, kun veden teho pysyy vakiona?
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
