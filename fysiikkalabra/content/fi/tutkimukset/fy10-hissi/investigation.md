# Hissin kulkema matka kiihtyvyydestä

> **Tutkimuskysymys:** Kuinka pitkän matkan hissi kulkee, kun matka päätellään pelkästä kiihtyvyysmittauksesta, ja kuinka hyvin tulos vastaa todellista matkaa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: läpileikkaus nelikerroksisesta koulurakennuksesta. Keskellä on hissikuilu, jossa hissikori on kahden kerroksen välissä matkalla. Korissa seisoo opiskelija, ja korin lattialla on puhelin. Kuilussa kulkee kori köysissä, ja vastapaino on alempana kuilun reunalla. Vasemmalla portaat nousevat toisesta kerroksesta välipohjan aukon kautta kolmanteen kerrokseen. Portaiden alapäässä toinen opiskelija mittaa viivaimella yhden askelman nousua: askelmien määrä kertaa nousu on kerroskorkeus lattiasta seuraavan kerroksen lattiaan. Oikealla kerroksissa on ikkunat." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10hh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10hh-win800436" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe8fb"/><stop offset="1" stop-color="#ffffff"/></linearGradient><linearGradient id="fy10hh-win990436" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe8fb"/><stop offset="1" stop-color="#ffffff"/></linearGradient><linearGradient id="fy10hh-win800304" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe8fb"/><stop offset="1" stop-color="#ffffff"/></linearGradient><linearGradient id="fy10hh-win990304" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe8fb"/><stop offset="1" stop-color="#ffffff"/></linearGradient><linearGradient id="fy10hh-win800172" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe8fb"/><stop offset="1" stop-color="#ffffff"/></linearGradient><linearGradient id="fy10hh-win990172" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe8fb"/><stop offset="1" stop-color="#ffffff"/></linearGradient><linearGradient id="fy10hh-win80040" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe8fb"/><stop offset="1" stop-color="#ffffff"/></linearGradient><linearGradient id="fy10hh-win99040" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe8fb"/><stop offset="1" stop-color="#ffffff"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10hh-wall)"/>
  <rect x="480" y="0" width="240" height="600" fill="#d5dde4"/>
  <line x1="506" y1="0" x2="506" y2="600" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="694" y1="0" x2="694" y2="600" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <rect x="0" y="568" width="480" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="720" y="568" width="480" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="0" y="436" width="480" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="720" y="436" width="480" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="0" y="304" width="150" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="420" y="304" width="60" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="720" y="304" width="480" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="0" y="172" width="480" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="720" y="172" width="480" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="0" y="40" width="480" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="720" y="40" width="480" height="16" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="0" y="562" width="480" height="6" fill="#d9b26a"/>
  <rect x="720" y="562" width="480" height="6" fill="#d9b26a"/>
  <rect x="466" y="472" width="14" height="96" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="0" y="430" width="480" height="6" fill="#d9b26a"/>
  <rect x="720" y="430" width="480" height="6" fill="#d9b26a"/>
  <rect x="466" y="340" width="14" height="96" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="0" y="298" width="150" height="6" fill="#d9b26a"/>
  <rect x="420" y="298" width="60" height="6" fill="#d9b26a"/>
  <rect x="720" y="298" width="480" height="6" fill="#d9b26a"/>
  <rect x="466" y="208" width="14" height="96" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="0" y="166" width="480" height="6" fill="#d9b26a"/>
  <rect x="720" y="166" width="480" height="6" fill="#d9b26a"/>
  <rect x="466" y="76" width="14" height="96" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="477" y="0" width="3" height="600" fill="#1f2933"/>
  <rect x="720" y="0" width="3" height="600" fill="#1f2933"/>
  <rect x="800" y="478" width="130" height="62" rx="3" fill="url(#fy10hh-win800436)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="865" y1="478" x2="865" y2="540" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="990" y="478" width="130" height="62" rx="3" fill="url(#fy10hh-win990436)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="1055" y1="478" x2="1055" y2="540" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="800" y="346" width="130" height="62" rx="3" fill="url(#fy10hh-win800304)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="865" y1="346" x2="865" y2="408" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="990" y="346" width="130" height="62" rx="3" fill="url(#fy10hh-win990304)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="1055" y1="346" x2="1055" y2="408" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="800" y="214" width="130" height="62" rx="3" fill="url(#fy10hh-win800172)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="865" y1="214" x2="865" y2="276" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="990" y="214" width="130" height="62" rx="3" fill="url(#fy10hh-win990172)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="1055" y1="214" x2="1055" y2="276" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="800" y="82" width="130" height="62" rx="3" fill="url(#fy10hh-win80040)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="865" y1="82" x2="865" y2="144" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="990" y="82" width="130" height="62" rx="3" fill="url(#fy10hh-win99040)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="1055" y1="82" x2="1055" y2="144" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="640" cy="22" r="14" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="585" y1="24" x2="585" y2="214" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="593" y1="24" x2="593" y2="214" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="591" y1="10" x2="640" y2="10" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="690" y1="22" x2="690" y2="420" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="678" y="420" width="24" height="110" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="508" y="214" width="156" height="142" rx="4" fill="#eef2f5" stroke="#1f2933" stroke-width="3"/>
  <rect x="508" y="344" width="156" height="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="650" y1="268" x2="650" y2="296" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <path d="M551.5,344 L553.5,294.5 H566.5 L568.5,344 H562 L560,311 L558,344 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M549,298 Q547.5,261.5 560,259.5 Q572.5,261.5 571,298 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M550,266 L547,298" fill="none" stroke="#1971c2" stroke-width="7.26" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="547" cy="300.5" r="3.63" fill="#f1dfb5"/>
  <path d="M570,266 L573,298" fill="none" stroke="#1971c2" stroke-width="7.26" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="573" cy="300.5" r="3.63" fill="#f1dfb5"/>
  <rect x="557" y="253" width="6" height="8" fill="#f1dfb5"/>
  <circle cx="560" cy="246.5" r="9.9" fill="#f1dfb5"/>
  <path d="M550,246.5 Q550,234.5 560,235 Q570.5,235 570,245 Q562,241 550,246.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="603" y="337" width="34" height="7" rx="2" fill="#1f2933"/>
  <rect x="606" y="338.5" width="28" height="2" fill="#8a96a3"/>
  <path d="M170,430 v-11 h21 v-11 h21 v-11 h21 v-11 h21 v-11 h21 v-11 h21 v-11 h21 v-11 h21 v-11 h21 v-11 h21 v-11 h21 v-11 h21 L420,320 L200,430 Z" fill="#b9c0c7" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="158" y="408" width="8" height="22" rx="1" fill="#ffe8a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="158" y1="426" x2="163" y2="426" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="158" y1="422" x2="161" y2="422" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="158" y1="418" x2="163" y2="418" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="158" y1="414" x2="161" y2="414" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="158" y1="410" x2="163" y2="410" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <path d="M124,390 L119,428.5" fill="none" stroke="#1f2933" stroke-width="7.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M114,430 h11" fill="none" stroke="#6c757d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M124.5,356 L158,412" fill="none" stroke="#2b8a3e" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M115.5,350 Q134,342.5 131.5,365 L130,392.5 H115 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M124,390 L129,428.5" fill="none" stroke="#1f2933" stroke-width="7.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M133,430 h11" fill="none" stroke="#6c757d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M126,355 L158,412" fill="none" stroke="#2b8a3e" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="158" cy="412" r="3.25" fill="#f1dfb5"/>
  <rect x="123" y="340" width="5" height="7.5" fill="#f1dfb5"/>
  <circle cx="125.5" cy="333.5" r="8.5" fill="#f1dfb5"/>
  <path d="M117,335 Q116.5,324 126,324.5 Q134,325 134,331 Q125.5,329 117,335 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="120" y="526" width="160" height="10" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <line x1="136" y1="536" x2="136" y2="562" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="264" y1="536" x2="264" y2="562" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="390" y="522" width="30" height="40" rx="4" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <circle cx="393" cy="498" r="16" fill="#2b8a3e"/>
  <circle cx="407" cy="484" r="16" fill="#2b8a3e"/>
  <circle cx="421" cy="502" r="16" fill="#2b8a3e"/>
  <rect x="140" y="122" width="180" height="10" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <line x1="154" y1="132" x2="154" y2="166" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="306" y1="132" x2="306" y2="166" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="780" y="498" width="60" height="64" rx="4" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
</svg>

Puhelimen kiihtyvyysanturi ei näe, missä kerroksessa hissi on, eikä se mittaa nopeutta tai matkaa. Se tuntee vain, miten hissin liike muuttuu. Tässä tutkimuksessa selvität, voiko pelkästä kiihtyvyysdatasta päätellä, kuinka pitkän matkan hissi kulki, ja vertaat tulosta matkaan, jonka saat rakennuksesta muulla tavalla. Mittaa, laske ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** hissin liikkeen vaiheet kiihtyvyysdatasta, hissin nopeus ajan funktiona, hissin kulkema matka epävarmuuksineen sekä se, kuinka hyvin tulos vastaa todellista matkaa.

**Päätät itse:** puhelimen paikan ja asennon, hissimatkan pituuden ja mittausten määrän, sen, miten määrität anturin lukeman levossa, miten selvität todellisen matkan, sekä tavan, jolla arvioit tuloksen epävarmuuden. Osittain ohjatussa työtavassa sivu antaa näihin tukea ja näyttää laskentatavan. Itsenäisessä työtavassa valitset myös tavan, jolla lasket nopeuden ja matkan, ja perustelet kaikki valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus kuuluu työhösi: korjaa laskennasta nollakohdan virhe ja tutki, miten korjaus muuttaa tulosta.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Hissi lähtee levosta, kulkee muutaman kerroksen ylöspäin ja pysähtyy. Hahmottele allekkain samalle aika-akselille hissin kiihtyvyyden, nopeuden ja kuljetun matkan kuvaajat.
2. Mitä puhelimen kiihtyvyysanturi näyttää pystysuunnassa, kun hissi seisoo paikallaan?
3. Oletetaan, että jokaiseen kiihtyvyyslukemaan on jäänyt sama pieni virhe. Miten virhe näkyy lasketussa nopeudessa ja matkassa: pysyykö se samana vai kasvaako se matkan aikana?
4. Kuinka pitkä on mielestäsi yhden kerroksen korkeus, ja kuinka lähelle sitä uskot kiihtyvyydestä lasketun matkan osuvan?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

**Nopeus kiihtyvyydestä.** Kiihtyvyys kertoo, kuinka nopeasti nopeus muuttuu. Hyvin lyhyellä aikavälillä $\Delta t$ kiihtyvyys on lähes vakio, joten nopeus muuttuu tällä välillä likimain määrän $\Delta v = a \cdot \Delta t$. Se on $(t,a)$-kuvaajan kapean suikaleen pinta-ala. Kun suikaleet lasketaan yhteen alusta alkaen, saadaan nopeuden muutos koko ajalta: **nopeuden muutos on $(t,a)$-kuvaajan ja aika-akselin välinen pinta-ala**, ja aika-akselin alapuolinen osa lasketaan negatiivisena. Jos hissi on alussa levossa, nopeuden muutos on sama kuin nopeus.

**Matka nopeudesta.** Samalla tavalla **siirtymä on $(t,v)$-kuvaajan ja aika-akselin välinen pinta-ala**. Kun hissi kulkee koko ajan samaan suuntaan, siirtymä on sama kuin kuljettu matka. [[apua:fy4-2|Siirtymä (t,v)-kuvaajan pinta-alana]]

**Mitä anturi mittaa.** Puhelimen kiihtyvyysanturi mittaa kolmen toisiaan vastaan kohtisuoran akselin suuntaisia lukemia. Levossakaan pystysuoran akselin lukema ei yleensä ole nolla. Sovelluksesta riippuen se on noin putoamiskiihtyvyyden $g$ suuruinen tai lähellä nollaa, mutta ei tarkalleen nolla. Anturi reagoi samaan kuin vaaka hississä: kun hissin kiihtyvyys muuttuu, lukema muuttuu. Hissin oma kiihtyvyys on siksi lukeman **muutos** levossa mitatusta lukemasta, ja tätä levossa mitattua lukemaa kutsutaan tässä anturin nollakohdaksi. [[apua:fy4-16|Hissi, tukivoima ja näennäinen paino]]

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, miten mittaat kiihtyvyyden, miten määrität anturin nollakohdan ja miten selvität hissin todellisen matkan.

::: tuki OO
**Osittain ohjattu.** Mittaat hissin kiihtyvyyttä koko matkan ajan, levosta lepoon. Muut päätökset teet itse, mutta mieti ainakin näitä:

- Missä asennossa puhelin on, ja mikä sen akseleista osoittaa pystysuoraan? Puhelin pysyy parhaiten samassa asennossa, kun se on hissin lattialla näyttö ylöspäin.
- Mistä anturin nollakohta saadaan? Mittaus kannattaa aloittaa muutama sekunti ennen kuin hissi lähtee ja lopettaa vasta, kun hissi on taas pysähtynyt kokonaan. Silloin datassa on lepojaksot sekä alussa että lopussa.
- Kuinka monta kerrosta hissi kulkee? Pitkä matka antaa pitkän tasaisen vaiheen, mutta pitkällä matkalla pienikin virhe ehtii kasvaa. Kirjaa lähtö- ja tulokerros.
- Kuinka monta kertaa toistat mittauksen? Voit tehdä useita matkoja samalla hissikäynnillä, esimerkiksi ylös ja takaisin alas.
- Miten saat todellisen matkan? Kerroskorkeus on matka yhden kerroksen lattiasta seuraavan kerroksen lattiaan. Sen voi mitata esimerkiksi portaikosta: porrasaskelmien määrä kertaa yhden askelman nousu. Joskus kerroskorkeus löytyy myös rakennuksen piirustuksista.
:::

## Mittaa

Tallenna jokaisesta hissimatkasta kiihtyvyysdata tiedostoksi, jonka voit avata taulukkolaskennassa. Kirjaa jokaisesta matkasta ylös lähtö- ja tulokerros, suunta ja puhelimen asento. Mittaa todellinen matka ja kirjaa myös, kuinka tarkasti sen sait selville. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

::: tuki OO
**Vihjeitä mittaukseen.** Selvitä ennen hissimatkaa, kumpaan suuntaan anturin pystysuora akseli osoittaa: nosta puhelinta pöydältä nopeasti ylöspäin ja katso, kasvaako vai pieneneekö pystyakselin etumerkillinen lukema (ei pelkkä lukeman suuruus). Tarkista myös lukemien yksikkö: jos lukema on levossa noin $1{,}00$, sovellus näyttää kiihtyvyyden putoamiskiihtyvyyden $g$ kerrannaisina, ja lukemat muutetaan yksikköön $\text{m/s}^2$ kertomalla ne luvulla $9{,}81\ \text{m/s}^2$. Pidä puhelin koko mittauksen ajan samassa asennossa, koska kallistuminen muuttaa lukemaa. Seiso paikallasi, äläkä koske puhelimeen matkan aikana. Jos sovellus antaa valita, mittaa kaikki akselit: pystyakselin lisäksi niistä näkee, onko puhelin kallistunut.
:::

## Käsittele tulokset

Piirrä kiihtyvyys ajan funktiona ja tunnista kuvaajasta hissin liikkeen vaiheet: liikkeellelähtö, mahdollinen tasaisen nopeuden vaihe, hidastuminen ja pysähtyminen. Merkitse vaiheiden alku- ja loppuhetket kuvaajaan.

Määritä sitten anturin nollakohta ja hissin kiihtyvyys, ja laske kiihtyvyysdatasta hissin nopeus ja edelleen hissin kulkema matka. Piirrä kiihtyvyys, nopeus ja matka allekkain samalle aika-akselille. Merkitse akseleille suureet ja yksiköt. [[apua:fy1-4|Kuvaajan laatiminen]]

Vastaa:

1. Vastaavatko kuvaajasi ennustettasi? Missä kohdin ne poikkeavat?
2. Mikä on laskemasi nopeus lopussa, kun hissi on taas pysähtynyt? Mitä se kertoo laskennan luotettavuudesta?
3. Kuinka pitkän matkan hissi kulki laskentasi mukaan?

::: tuki OO
**Laskenta taulukkolaskennassa.** Mittausdata ei ole jatkuva käyrä vaan satoja tai tuhansia lukemia tasaisin aikavälein. Siksi pinta-alat lasketaan **numeerisesti**: jokaisen kahden peräkkäisen lukeman väliin tulee kapea suikale, ja suikaleiden alat lasketaan yhteen taulukkolaskennassa. Tee jokaiselle suureelle oma sarakkeensa, alkuperäiset lukemat vasemmalle ja lasketut niiden oikealle puolelle:

| $t\ (\text{s})$ | $a_\text{mitattu}\ (\text{m/s}^2)$ | $a = a_\text{mitattu} - a_0\ (\text{m/s}^2)$ | $v\ (\text{m/s})$ | $s\ (\text{m})$ |
|---|---|---|---|---|
| | | | $0$ | $0$ |
| | | | | |

**Nollakohta.** Laske alun lepojakson lukemien keskiarvo $a_0$. Ota mukaan vain lukemat ajalta, jolloin hissi varmasti seisoi.

**Hissin kiihtyvyys.** Vähennä nollakohta jokaisesta lukemasta: $a = a_\text{mitattu} - a_0$. Jos anturin akseli osoitti alaspäin, vaihda merkki niin, että ylöspäin on positiivinen suunta.

**Nopeus.** Aloita arvosta $v = 0$, koska hissi on alussa levossa. Jokainen seuraava nopeus on edellinen nopeus plus kahden peräkkäisen kiihtyvyyslukeman välisen suikaleen pinta-ala. Kun suikaleen korkeudeksi otetaan lukemien keskiarvo, rivin $i$ nopeus on

```latex
v_i = v_{i-1} + \frac{a_{i-1} + a_i}{2} \cdot (t_i - t_{i-1})
```

**Matka.** Laske matka samalla tavalla nopeuksista, alkaen arvosta $s = 0$:

```latex
s_i = s_{i-1} + \frac{v_{i-1} + v_i}{2} \cdot (t_i - t_{i-1})
```

Kirjoita kaava kerran ja kopioi se koko sarakkeeseen. Matkasarakkeen viimeinen arvo on hissin kulkema matka. Säilytä alkuperäiset lukemat muuttamattomina omassa sarakkeessaan.

**Vertaa omiin kuvaajiisi ja ennusteeseesi.** Kun hissi kulkee ylöspäin, sen liikkeen vaiheet näyttävät tältä:

<svg data-fig="vaiheet" viewBox="0 0 600 330" role="img" aria-label="Kaaviokuva hissin ylöspäin suuntautuvan matkan kolmesta vaiheesta. Kussakin vaiheessa on hissikori köysissä, ja korin lattialla on puhelin. Vasemmalla hissi lähtee liikkeelle: sininen nopeusnuoli v osoittaa ylöspäin ja oranssi kiihtyvyysnuoli a ylöspäin. Keskellä hissi liikkuu tasaisella nopeudella: nopeusnuoli osoittaa ylöspäin ja on pisin, ja kiihtyvyys on nolla. Oikealla hissi hidastuu: nopeusnuoli osoittaa yhä ylöspäin, mutta kiihtyvyysnuoli osoittaa alaspäin." style="max-width:100%;font-size:24px">
  <foreignObject x="23" y="10" width="164" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{liikkeellelähtö}$</div></foreignObject>
  <line x1="105" y1="44" x2="105" y2="96" stroke="#6c757d" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="65" y="96" width="80" height="130" rx="4" fill="#eef2f5" stroke="#1f2933" stroke-width="3"/>
  <rect x="65" y="214" width="80" height="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="88" y="207" width="34" height="7" rx="2" fill="#1f2933"/>
  <rect x="91" y="208.5" width="28" height="2" fill="#8a96a3"/>
  <line x1="51" y1="196" x2="51" y2="163" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M51,150 L57.5,164 L44.5,164 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="12" y="152.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="159" y1="160" x2="159" y2="123" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M159,110 L165.5,124 L152.5,124 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="165" y="120.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="223" y="10" width="154" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{tasainen nopeus}$</div></foreignObject>
  <line x1="300" y1="44" x2="300" y2="96" stroke="#6c757d" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="260" y="96" width="80" height="130" rx="4" fill="#eef2f5" stroke="#1f2933" stroke-width="3"/>
  <rect x="260" y="214" width="80" height="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="283" y="207" width="34" height="7" rx="2" fill="#1f2933"/>
  <rect x="286" y="208.5" width="28" height="2" fill="#8a96a3"/>
  <line x1="246" y1="196" x2="246" y2="119" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M246,106 L252.5,120 L239.5,120 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="207" y="130.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="277.5" y="235.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$a = 0$</div></foreignObject>
  <foreignObject x="428.5" y="10" width="133" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{hidastuminen}$</div></foreignObject>
  <line x1="495" y1="44" x2="495" y2="96" stroke="#6c757d" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="455" y="96" width="80" height="130" rx="4" fill="#eef2f5" stroke="#1f2933" stroke-width="3"/>
  <rect x="455" y="214" width="80" height="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="478" y="207" width="34" height="7" rx="2" fill="#1f2933"/>
  <rect x="481" y="208.5" width="28" height="2" fill="#8a96a3"/>
  <line x1="441" y1="196" x2="441" y2="163" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M441,150 L447.5,164 L434.5,164 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="402" y="152.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="549" y1="120" x2="549" y2="157" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M549,170 L542.5,156 L555.5,156 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="555" y="130.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="197" y="288" width="206" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{hissi kulkee ylöspäin}$</div></foreignObject>
</svg>

Mallin mukaiset kuvaajat ovat tämän muotoisia. Kiihtyvyyskuvaajan kummun pinta-ala on nopeuden kasvu, ja nopeuskuvaajan koko pinta-ala on kuljettu matka. Kuvaajissa ei ole mittaustuloksia, vain mallin muodot. Todellisessa datassa on lisäksi kohinaa: lukema heiluu pienesti myös levossa.

<svg data-fig="malli" viewBox="0 0 600 600" role="img" aria-label="Kolme mallikuvaajaa allekkain samalla aika-akselilla, ilman lukuarvoja ja mittauspisteitä. Ylimpänä kiihtyvyys a ajan funktiona: alussa ja lopussa nolla, liikkeellelähdössä positiivinen pyöristetty kumpu, tasaisen nopeuden aikana nolla ja hidastuessa yhtä suuri negatiivinen kuoppa. Keskellä nopeus v: nollasta kasvaa tasaiseen arvoon, pysyy vakiona ja pienenee takaisin nollaan. Alimpana kuljettu matka s: kasvaa ensin kiihtyen, sitten tasaisesti suorana ja lopuksi hidastuen, kunnes pysyy vakiona. Katkoviivat erottavat liikkeen vaiheet. Nopeuden muutos on kiihtyvyyskuvaajan pinta-ala, ja matka on nopeuskuvaajan pinta-ala." style="max-width:100%;font-size:24px">
  <line x1="123" y1="30" x2="123" y2="580" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <line x1="196.5" y1="30" x2="196.5" y2="580" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <line x1="385" y1="30" x2="385" y2="580" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <line x1="459" y1="30" x2="459" y2="580" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <line x1="90" y1="170" x2="90" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,32 L96,45 L84,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="105" x2="508" y2="105" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M520,105 L507,111 L507,99 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="102" y="21.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a$</div></foreignObject>
  <foreignObject x="526" y="90.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <line x1="90" y1="380" x2="90" y2="234" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,222 L96,235 L84,235 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="380" x2="508" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M520,380 L507,386 L507,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="102" y="211.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <foreignObject x="526" y="365.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <line x1="90" y1="580" x2="90" y2="434" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,422 L96,435 L84,435 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="580" x2="508" y2="580" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M520,580 L507,586 L507,574 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="102" y="411.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s$</div></foreignObject>
  <foreignObject x="526" y="565.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <polyline points="90,105 91.5,105 93.5,105 95,105 96.5,105 98,105 100,105 101.5,105 103,105 105,105 106.5,105 108,105 109.5,105 111.5,105 113,105 114.5,105 116,105 118,105 119.5,105 121,105 123,105 124.5,104 126,102 127.5,98 129.5,93.5 131,87.5 132.5,81.5 134.5,75.5 136,69.5 137.5,64 139,60 141,57 142.5,55 144,55 146,55 147.5,55 149,55 150.5,55 152.5,55 154,55 155.5,55 157,55 159,55 160.5,55 162,55 164,55 165.5,55 167,55 168.5,55 170.5,55 172,55 173.5,55 175.5,55 177,55 178.5,57 180,60 182,64 183.5,69.5 185,75.5 187,81.5 188.5,87.5 190,93.5 191.5,98 193.5,102 195,104 196.5,105 198,105 200,105 201.5,105 203,105 205,105 206.5,105 208,105 209.5,105 211.5,105 213,105 214.5,105 216.5,105 218,105 219.5,105 221,105 223,105 224.5,105 226,105 228,105 229.5,105 231,105 232.5,105 234.5,105 236,105 237.5,105 239,105 241,105 242.5,105 244,105 246,105 247.5,105 249,105 250.5,105 252.5,105 254,105 255.5,105 257.5,105 259,105 260.5,105 262,105 264,105 265.5,105 267,105 269,105 270.5,105 272,105 273.5,105 275.5,105 277,105 278.5,105 280,105 282,105 283.5,105 285,105 287,105 288.5,105 290,105 291.5,105 293.5,105 295,105 296.5,105 298.5,105 300,105 301.5,105 303,105 305,105 306.5,105 308,105 310,105 311.5,105 313,105 314.5,105 316.5,105 318,105 319.5,105 321,105 323,105 324.5,105 326,105 328,105 329.5,105 331,105 332.5,105 334.5,105 336,105 337.5,105 339.5,105 341,105 342.5,105 344,105 346,105 347.5,105 349,105 351,105 352.5,105 354,105 355.5,105 357.5,105 359,105 360.5,105 362,105 364,105 365.5,105 367,105 369,105 370.5,105 372,105 373.5,105 375.5,105 377,105 378.5,105 380.5,105 382,105 383.5,105 385,105 387,106 388.5,108 390,112 392,116.5 393.5,122.5 395,128.5 396.5,134.5 398.5,140.5 400,146 401.5,150 403,153 405,155 406.5,155 408,155 410,155 411.5,155 413,155 414.5,155 416.5,155 418,155 419.5,155 421.5,155 423,155 424.5,155 426,155 428,155 429.5,155 431,155 433,155 434.5,155 436,155 437.5,155 439.5,155 441,153 442.5,150 444,146 446,140.5 447.5,134.5 449,128.5 451,122.5 452.5,116.5 454,112 455.5,108 457.5,106 459,105 460.5,105 462.5,105 464,105 465.5,105 467,105 469,105 470.5,105 472,105 474,105 475.5,105 477,105 478.5,105 480.5,105 482,105 483.5,105 485,105 487,105 488.5,105 490,105 492,105 493.5,105 495,105 496.5,105 498.5,105 500,105 500,105" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90,380 91.5,380 93.5,380 95,380 96.5,380 98,380 100,380 101.5,380 103,380 105,380 106.5,380 108,380 109.5,380 111.5,380 113,380 114.5,380 116,380 118,380 119.5,380 121,380 123,380 124.5,380 126,380 127.5,379.5 129.5,379 131,377.5 132.5,376 134.5,374 136,371.5 137.5,368.5 139,365.5 141,361.5 142.5,358 144,354 146,350 147.5,346.5 149,342.5 150.5,338.5 152.5,335 154,331 155.5,327 157,323.5 159,319.5 160.5,315.5 162,311.5 164,308 165.5,304 167,300 168.5,296.5 170.5,292.5 172,288.5 173.5,285 175.5,281 177,277 178.5,273.5 180,269.5 182,266.5 183.5,263.5 185,261 187,259 188.5,257.5 190,256 191.5,255.5 193.5,255 195,255 196.5,255 198,255 200,255 201.5,255 203,255 205,255 206.5,255 208,255 209.5,255 211.5,255 213,255 214.5,255 216.5,255 218,255 219.5,255 221,255 223,255 224.5,255 226,255 228,255 229.5,255 231,255 232.5,255 234.5,255 236,255 237.5,255 239,255 241,255 242.5,255 244,255 246,255 247.5,255 249,255 250.5,255 252.5,255 254,255 255.5,255 257.5,255 259,255 260.5,255 262,255 264,255 265.5,255 267,255 269,255 270.5,255 272,255 273.5,255 275.5,255 277,255 278.5,255 280,255 282,255 283.5,255 285,255 287,255 288.5,255 290,255 291.5,255 293.5,255 295,255 296.5,255 298.5,255 300,255 301.5,255 303,255 305,255 306.5,255 308,255 310,255 311.5,255 313,255 314.5,255 316.5,255 318,255 319.5,255 321,255 323,255 324.5,255 326,255 328,255 329.5,255 331,255 332.5,255 334.5,255 336,255 337.5,255 339.5,255 341,255 342.5,255 344,255 346,255 347.5,255 349,255 351,255 352.5,255 354,255 355.5,255 357.5,255 359,255 360.5,255 362,255 364,255 365.5,255 367,255 369,255 370.5,255 372,255 373.5,255 375.5,255 377,255 378.5,255 380.5,255 382,255 383.5,255 385,255 387,255 388.5,255 390,255.5 392,256 393.5,257.5 395,259 396.5,261 398.5,263.5 400,266.5 401.5,269.5 403,273.5 405,277 406.5,281 408,285 410,288.5 411.5,292.5 413,296.5 414.5,300 416.5,304 418,308 419.5,311.5 421.5,315.5 423,319.5 424.5,323.5 426,327 428,331 429.5,335 431,338.5 433,342.5 434.5,346.5 436,350 437.5,354 439.5,358 441,361.5 442.5,365.5 444,368.5 446,371.5 447.5,374 449,376 451,377.5 452.5,379 454,379.5 455.5,380 457.5,380 459,380 460.5,380 462.5,380 464,380 465.5,380 467,380 469,380 470.5,380 472,380 474,380 475.5,380 477,380 478.5,380 480.5,380 482,380 483.5,380 485,380 487,380 488.5,380 490,380 492,380 493.5,380 495,380 496.5,380 498.5,380 500,380 500,380" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90,580 91.5,580 93.5,580 95,580 96.5,580 98,580 100,580 101.5,580 103,580 105,580 106.5,580 108,580 109.5,580 111.5,580 113,580 114.5,580 116,580 118,580 119.5,580 121,580 123,580 124.5,580 126,580 127.5,580 129.5,580 131,580 132.5,580 134.5,580 136,580 137.5,580 139,579.5 141,579.5 142.5,579.5 144,579.5 146,579 147.5,579 149,579 150.5,578.5 152.5,578.5 154,578 155.5,577.5 157,577.5 159,577 160.5,576.5 162,576 164,575.5 165.5,575 167,574.5 168.5,574 170.5,573.5 172,573 173.5,572.5 175.5,572 177,571.5 178.5,570.5 180,570 182,569.5 183.5,568.5 185,568 187,567 188.5,566.5 190,565.5 191.5,565 193.5,564 195,563 196.5,562.5 198,561.5 200,561 201.5,560 203,559.5 205,558.5 206.5,557.5 208,557 209.5,556 211.5,555.5 213,554.5 214.5,554 216.5,553 218,552.5 219.5,551.5 221,550.5 223,550 224.5,549 226,548.5 228,547.5 229.5,547 231,546 232.5,545 234.5,544.5 236,543.5 237.5,543 239,542 241,541.5 242.5,540.5 244,540 246,539 247.5,538 249,537.5 250.5,536.5 252.5,536 254,535 255.5,534.5 257.5,533.5 259,532.5 260.5,532 262,531 264,530.5 265.5,529.5 267,529 269,528 270.5,527.5 272,526.5 273.5,525.5 275.5,525 277,524 278.5,523.5 280,522.5 282,522 283.5,521 285,520 287,519.5 288.5,518.5 290,518 291.5,517 293.5,516.5 295,515.5 296.5,515 298.5,514 300,513 301.5,512.5 303,511.5 305,511 306.5,510 308,509.5 310,508.5 311.5,507.5 313,507 314.5,506 316.5,505.5 318,504.5 319.5,504 321,503 323,502.5 324.5,501.5 326,500.5 328,500 329.5,499 331,498.5 332.5,497.5 334.5,497 336,496 337.5,495 339.5,494.5 341,493.5 342.5,493 344,492 346,491.5 347.5,490.5 349,490 351,489 352.5,488 354,487.5 355.5,486.5 357.5,486 359,485 360.5,484.5 362,483.5 364,482.5 365.5,482 367,481 369,480.5 370.5,479.5 372,479 373.5,478 375.5,477.5 377,476.5 378.5,475.5 380.5,475 382,474 383.5,473.5 385,472.5 387,472 388.5,471 390,470 392,469.5 393.5,468.5 395,468 396.5,467 398.5,466.5 400,465.5 401.5,465 403,464.5 405,463.5 406.5,463 408,462.5 410,462 411.5,461.5 413,461 414.5,460.5 416.5,460 418,459.5 419.5,459 421.5,458.5 423,458 424.5,457.5 426,457.5 428,457 429.5,456.5 431,456.5 433,456 434.5,456 436,456 437.5,455.5 439.5,455.5 441,455.5 442.5,455.5 444,455 446,455 447.5,455 449,455 451,455 452.5,455 454,455 455.5,455 457.5,455 459,455 460.5,455 462.5,455 464,455 465.5,455 467,455 469,455 470.5,455 472,455 474,455 475.5,455 477,455 478.5,455 480.5,455 482,455 483.5,455 485,455 487,455 488.5,455 490,455 492,455 493.5,455 495,455 496.5,455 498.5,455 500,455 500,455" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polygon points="90,105 90,105 90.5,105 90.5,105 91,105 91,105 91,105 91.5,105 91.5,105 92,105 92,105 92.5,105 92.5,105 92.5,105 93,105 93,105 93.5,105 93.5,105 93.5,105 94,105 94,105 94.5,105 94.5,105 94.5,105 95,105 95,105 95.5,105 95.5,105 95.5,105 96,105 96,105 96.5,105 96.5,105 97,105 97,105 97,105 97.5,105 97.5,105 98,105 98,105 98,105 98.5,105 98.5,105 99,105 99,105 99,105 99.5,105 99.5,105 100,105 100,105 100,105 100.5,105 100.5,105 101,105 101,105 101.5,105 101.5,105 101.5,105 102,105 102,105 102.5,105 102.5,105 102.5,105 103,105 103,105 103.5,105 103.5,105 103.5,105 104,105 104,105 104.5,105 104.5,105 105,105 105,105 105,105 105.5,105 105.5,105 106,105 106,105 106,105 106.5,105 106.5,105 107,105 107,105 107,105 107.5,105 107.5,105 108,105 108,105 108,105 108.5,105 108.5,105 109,105 109,105 109.5,105 109.5,105 109.5,105 110,105 110,105 110.5,105 110.5,105 110.5,105 111,105 111,105 111.5,105 111.5,105 111.5,105 112,105 112,105 112.5,105 112.5,105 113,105 113,105 113,105 113.5,105 113.5,105 114,105 114,105 114,105 114.5,105 114.5,105 115,105 115,105 115,105 115.5,105 115.5,105 116,105 116,105 116,105 116.5,105 116.5,105 117,105 117,105 117.5,105 117.5,105 117.5,105 118,105 118,105 118.5,105 118.5,105 118.5,105 119,105 119,105 119.5,105 119.5,105 119.5,105 120,105 120,105 120.5,105 120.5,105 121,105 121,105 121,105 121.5,105 121.5,105 122,105 122,105 122,105 122.5,105 122.5,105 123,105 123,105 123,105 123.5,105 123.5,105 124,104.5 124,104.5 124,104.5 124.5,104 124.5,104 125,104 125,103.5 125.5,103 125.5,103 125.5,102.5 126,102.5 126,102 126.5,101.5 126.5,101 126.5,100.5 127,100 127,100 127.5,99.5 127.5,99 127.5,98 128,97.5 128,97 128.5,96.5 128.5,96 128.5,95.5 129,94.5 129,94 129.5,93.5 129.5,92.5 130,92 130,91.5 130,90.5 130.5,90 130.5,89 131,88.5 131,87.5 131,87 131.5,86 131.5,85.5 132,84.5 132,84 132,83 132.5,82.5 132.5,81.5 133,81 133,80 133.5,79 133.5,78.5 133.5,77.5 134,77 134,76 134.5,75.5 134.5,74.5 134.5,74 135,73 135,72.5 135.5,71.5 135.5,71 135.5,70 136,69.5 136,68.5 136.5,68 136.5,67.5 136.5,66.5 137,66 137,65.5 137.5,64.5 137.5,64 138,63.5 138,63 138,62.5 138.5,62 138.5,61 139,60.5 139,60 139,60 139.5,59.5 139.5,59 140,58.5 140,58 140,57.5 140.5,57.5 140.5,57 141,57 141,56.5 141,56 141.5,56 141.5,56 142,55.5 142,55.5 142.5,55.5 142.5,55 142.5,55 143,55 143,55 143.5,55 143.5,55 143.5,55 144,55 144,55 144.5,55 144.5,55 144.5,55 145,55 145,55 145.5,55 145.5,55 146,55 146,55 146,55 146.5,55 146.5,55 147,55 147,55 147,55 147.5,55 147.5,55 148,55 148,55 148,55 148.5,55 148.5,55 149,55 149,55 149,55 149.5,55 149.5,55 150,55 150,55 150.5,55 150.5,55 150.5,55 151,55 151,55 151.5,55 151.5,55 151.5,55 152,55 152,55 152.5,55 152.5,55 152.5,55 153,55 153,55 153.5,55 153.5,55 154,55 154,55 154,55 154.5,55 154.5,55 155,55 155,55 155,55 155.5,55 155.5,55 156,55 156,55 156,55 156.5,55 156.5,55 157,55 157,55 157,55 157.5,55 157.5,55 158,55 158,55 158.5,55 158.5,55 158.5,55 159,55 159,55 159.5,55 159.5,55 159.5,55 160,55 160,55 160.5,55 160.5,55 160.5,55 161,55 161,55 161.5,55 161.5,55 162,55 162,55 162,55 162.5,55 162.5,55 163,55 163,55 163,55 163.5,55 163.5,55 164,55 164,55 164,55 164.5,55 164.5,55 165,55 165,55 165,55 165.5,55 165.5,55 166,55 166,55 166.5,55 166.5,55 166.5,55 167,55 167,55 167.5,55 167.5,55 167.5,55 168,55 168,55 168.5,55 168.5,55 168.5,55 169,55 169,55 169.5,55 169.5,55 169.5,55 170,55 170,55 170.5,55 170.5,55 171,55 171,55 171,55 171.5,55 171.5,55 172,55 172,55 172,55 172.5,55 172.5,55 173,55 173,55 173,55 173.5,55 173.5,55 174,55 174,55 174.5,55 174.5,55 174.5,55 175,55 175,55 175.5,55 175.5,55 175.5,55 176,55 176,55 176.5,55 176.5,55 176.5,55 177,55 177,55.5 177.5,55.5 177.5,55.5 177.5,56 178,56 178,56 178.5,56.5 178.5,57 179,57 179,57.5 179,57.5 179.5,58 179.5,58.5 180,59 180,59.5 180,60 180.5,60 180.5,60.5 181,61 181,62 181,62.5 181.5,63 181.5,63.5 182,64 182,64.5 182,65.5 182.5,66 182.5,66.5 183,67.5 183,68 183.5,68.5 183.5,69.5 183.5,70 184,71 184,71.5 184.5,72.5 184.5,73 184.5,74 185,74.5 185,75.5 185.5,76 185.5,77 185.5,77.5 186,78.5 186,79 186.5,80 186.5,81 187,81.5 187,82.5 187,83 187.5,84 187.5,84.5 188,85.5 188,86 188,87 188.5,87.5 188.5,88.5 189,89 189,90 189,90.5 189.5,91.5 189.5,92 190,92.5 190,93.5 190,94 190.5,94.5 190.5,95.5 191,96 191,96.5 191.5,97 191.5,97.5 191.5,98 192,99 192,99.5 192.5,100 192.5,100 192.5,100.5 193,101 193,101.5 193.5,102 193.5,102.5 193.5,102.5 194,103 194,103 194.5,103.5 194.5,104 195,104 195,104 195,104.5 195.5,104.5 195.5,104.5 196,105 196,105 196,105 196.5,105 196.5,105 197,105 197,105 196.5,105" fill="#e8590c" fill-opacity="0.18"/>
  <foreignObject x="145" y="72" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\Delta v$</div></foreignObject>
  <polygon points="90,380 90,380 92,380 94,380 96,380 98,380 100,380 102.5,380 104.5,380 106.5,380 108.5,380 110.5,380 112.5,380 114.5,380 116.5,380 118.5,380 121,380 123,380 125,380 127,379.5 129,379 131,377.5 133,375.5 135,373 137,369.5 139,365.5 141,360.5 143.5,356 145.5,351 147.5,346.5 149.5,341.5 151.5,336.5 153.5,332 155.5,327 157.5,322.5 159.5,317.5 162,312.5 164,308 166,303 168,298.5 170,293.5 172,288.5 174,284 176,279 178,274.5 180,269.5 182,265.5 184.5,262 186.5,259.5 188.5,257.5 190.5,256 192.5,255.5 194.5,255 196.5,255 198.5,255 200.5,255 203,255 205,255 207,255 209,255 211,255 213,255 215,255 217,255 219,255 221,255 223,255 225.5,255 227.5,255 229.5,255 231.5,255 233.5,255 235.5,255 237.5,255 239.5,255 241.5,255 244,255 246,255 248,255 250,255 252,255 254,255 256,255 258,255 260,255 262,255 264,255 266.5,255 268.5,255 270.5,255 272.5,255 274.5,255 276.5,255 278.5,255 280.5,255 282.5,255 285,255 287,255 289,255 291,255 293,255 295,255 297,255 299,255 301,255 303,255 305,255 307.5,255 309.5,255 311.5,255 313.5,255 315.5,255 317.5,255 319.5,255 321.5,255 323.5,255 326,255 328,255 330,255 332,255 334,255 336,255 338,255 340,255 342,255 344,255 346,255 348.5,255 350.5,255 352.5,255 354.5,255 356.5,255 358.5,255 360.5,255 362.5,255 364.5,255 367,255 369,255 371,255 373,255 375,255 377,255 379,255 381,255 383,255 385,255 387,255 389.5,255.5 391.5,256 393.5,257.5 395.5,259.5 397.5,262 399.5,265.5 401.5,269.5 403.5,274.5 405.5,279 408,284 410,288.5 412,293.5 414,298.5 416,303 418,308 420,312.5 422,317.5 424,322.5 426,327 428,332 430.5,336.5 432.5,341.5 434.5,346.5 436.5,351 438.5,356 440.5,360.5 442.5,365.5 444.5,369.5 446.5,373 449,375.5 451,377.5 453,379 455,379.5 457,380 459,380 461,380 463,380 465,380 467,380 469,380 471.5,380 473.5,380 475.5,380 477.5,380 479.5,380 481.5,380 483.5,380 485.5,380 487.5,380 490,380 492,380 494,380 496,380 498,380 500,380 500,380" fill="#1971c2" fill-opacity="0.12"/>
  <foreignObject x="230" y="328" width="122" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{pinta-ala} = s$</div></foreignObject>
</svg>
:::

Laskentaan voit käyttää taulukkolaskentaa tai muuta ohjelmaa, joka laskee sarakkeiden arvoja riveittäin. Ruukkilabran ohje ohjelman käyttöön on tekeillä.

## Epävarmuus ja luotettavuus

Ilmoita hissin kulkema matka muodossa $s = (s \pm \Delta s)\ \text{m}$ ja perustele, miten arvioit epävarmuuden $\Delta s$. Ilmoita myös todellinen matka epävarmuuksineen ja vertaa tuloksia: mahtuvatko ne toistensa epävarmuusväleihin?

Pohdi lisäksi, miksi pieni virhe kiihtyvyydessä voi kasvaa suureksi virheeksi matkassa.

::: tuki OO
**Miksi pieni virhe kasvaa.** Oletetaan, että nollakohta $a_0$ on määritetty hieman väärin, niin että jokaiseen kiihtyvyyteen jää sama pieni virhe $\delta a$. Laskettuun nopeuteen kertyy silloin virhettä tasaisesti, $\delta a \cdot t$, joten nopeus ei palaa lopussa nollaan. Matkaan kertyy virhettä vielä nopeammin, $\tfrac{1}{2} \cdot \delta a \cdot t^2$, aivan kuten tasaisesti kiihtyvässä liikkeessä. Virhe kasvaa siis ajan neliössä: mitä pidempään laskenta kestää, sitä enemmän se korostuu.

<svg data-fig="ryominta" viewBox="0 0 600 470" role="img" aria-label="Kaksi mallikuvaajaa allekkain, ilman lukuarvoja. Ylempänä nopeus v ajan funktiona: yhtenäinen viiva on laskettu oikeasta kiihtyvyydestä ja palaa lopussa nollaan. Katkoviiva on laskettu kiihtyvyydestä, jossa on pieni vakiovirhe: se kulkee aluksi lähes yhtenäisen viivan päällä, mutta erkanee siitä tasaisesti, eikä nopeus palaa lopussa nollaan. Jäljelle jäävä nopeus on merkitty v loppu. Alempana matka s: katkoviivan ja yhtenäisen viivan ero kasvaa yhä nopeammin ajan kuluessa." style="max-width:100%;font-size:24px">
  <line x1="90" y1="210" x2="90" y2="34" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,22 L96,35 L84,35 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="210" x2="478" y2="210" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M490,210 L477,216 L477,204 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="102" y="11.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <foreignObject x="496" y="195.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <line x1="90" y1="440" x2="90" y2="254" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,242 L96,255 L84,255 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="440" x2="478" y2="440" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M490,440 L477,446 L477,434 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="102" y="231.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s$</div></foreignObject>
  <foreignObject x="496" y="425.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <polyline points="90,210 91.5,210 93,210 94.5,210 96,210 97.5,210 99,210 100.5,210 102,210 103.5,210 105,210 106.5,210 108,210 110,210 111.5,210 113,210 114.5,210 116,210 117.5,210 119,210 120.5,210 122,210 123.5,210 125,209.5 126.5,209 128,207.5 129.5,206 131,204 132.5,201.5 134,199 135.5,195.5 137,192 138.5,188.5 140,184.5 141.5,180.5 143,177 144.5,173 146,169.5 148,165.5 149.5,162 151,158 152.5,154.5 154,150.5 155.5,147 157,143 158.5,139 160,135.5 161.5,131.5 163,128 164.5,124 166,120.5 167.5,116.5 169,113 170.5,109 172,105.5 173.5,102 175,98.5 176.5,95.5 178,93 179.5,91 181,89.5 182.5,88.5 184,88 186,87.5 187.5,87.5 189,87.5 190.5,87.5 192,87.5 193.5,87.5 195,87.5 196.5,87.5 198,87.5 199.5,87.5 201,87.5 202.5,87.5 204,87.5 205.5,87.5 207,87.5 208.5,87.5 210,87.5 211.5,87.5 213,87.5 214.5,87.5 216,87.5 217.5,87.5 219,87.5 220.5,87.5 222,87.5 224,87.5 225.5,87.5 227,87.5 228.5,87.5 230,87.5 231.5,87.5 233,87.5 234.5,87.5 236,87.5 237.5,87.5 239,87.5 240.5,87.5 242,87.5 243.5,87.5 245,87.5 246.5,87.5 248,87.5 249.5,87.5 251,87.5 252.5,87.5 254,87.5 255.5,87.5 257,87.5 258.5,87.5 260,87.5 262,87.5 263.5,87.5 265,87.5 266.5,87.5 268,87.5 269.5,87.5 271,87.5 272.5,87.5 274,87.5 275.5,87.5 277,87.5 278.5,87.5 280,87.5 281.5,87.5 283,87.5 284.5,87.5 286,87.5 287.5,87.5 289,87.5 290.5,87.5 292,87.5 293.5,87.5 295,87.5 296.5,87.5 298,87.5 300,87.5 301.5,87.5 303,87.5 304.5,87.5 306,87.5 307.5,87.5 309,87.5 310.5,87.5 312,87.5 313.5,87.5 315,87.5 316.5,87.5 318,87.5 319.5,87.5 321,87.5 322.5,87.5 324,87.5 325.5,87.5 327,87.5 328.5,87.5 330,87.5 331.5,87.5 333,87.5 334.5,87.5 336,87.5 338,87.5 339.5,87.5 341,87.5 342.5,87.5 344,87.5 345.5,87.5 347,87.5 348.5,87.5 350,87.5 351.5,87.5 353,87.5 354.5,87.5 356,87.5 357.5,87.5 359,87.5 360.5,87.5 362,87.5 363.5,87.5 365,87.5 366.5,87.5 368,88 369.5,88.5 371,89.5 372.5,91 374,93 376,95.5 377.5,98.5 379,102 380.5,105.5 382,109 383.5,113 385,116.5 386.5,120.5 388,124 389.5,128 391,131.5 392.5,135.5 394,139 395.5,143 397,147 398.5,150.5 400,154.5 401.5,158 403,162 404.5,165.5 406,169.5 407.5,173 409,177 410.5,180.5 412,184.5 414,188.5 415.5,192 417,195.5 418.5,199 420,201.5 421.5,204 423,206 424.5,207.5 426,209 427.5,209.5 429,210 430.5,210 432,210 433.5,210 435,210 436.5,210 438,210 439.5,210 441,210 442.5,210 444,210 445.5,210 447,210 448.5,210 450,210 452,210 453.5,210 455,210 456.5,210 458,210 459.5,210 461,210 462.5,210 464,210 465.5,210 467,210 468.5,210 470,210 470,210" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90,210 91.5,210 93,209.5 94.5,209.5 96,209.5 97.5,209 99,209 100.5,209 102,209 103.5,208.5 105,208.5 106.5,208.5 108,208 110,208 111.5,208 113,207.5 114.5,207.5 116,207.5 117.5,207.5 119,207 120.5,207 122,207 123.5,206.5 125,206 126.5,205 128,204 129.5,202 131,200 132.5,197.5 134,194.5 135.5,191 137,187.5 138.5,183.5 140,179.5 141.5,175.5 143,171.5 144.5,168 146,164 148,160 149.5,156 151,152 152.5,148 154,144 155.5,140.5 157,136.5 158.5,132.5 160,128.5 161.5,124.5 163,120.5 164.5,116.5 166,113 167.5,109 169,105 170.5,101 172,97 173.5,93.5 175,90 176.5,87 178,84.5 179.5,82.5 181,80.5 182.5,79.5 184,78.5 186,78 187.5,77.5 189,77.5 190.5,77.5 192,77 193.5,77 195,77 196.5,77 198,76.5 199.5,76.5 201,76.5 202.5,76 204,76 205.5,76 207,75.5 208.5,75.5 210,75.5 211.5,75.5 213,75 214.5,75 216,75 217.5,74.5 219,74.5 220.5,74.5 222,74 224,74 225.5,74 227,73.5 228.5,73.5 230,73.5 231.5,73.5 233,73 234.5,73 236,73 237.5,72.5 239,72.5 240.5,72.5 242,72 243.5,72 245,72 246.5,72 248,71.5 249.5,71.5 251,71.5 252.5,71 254,71 255.5,71 257,70.5 258.5,70.5 260,70.5 262,70.5 263.5,70 265,70 266.5,70 268,69.5 269.5,69.5 271,69.5 272.5,69 274,69 275.5,69 277,69 278.5,68.5 280,68.5 281.5,68.5 283,68 284.5,68 286,68 287.5,67.5 289,67.5 290.5,67.5 292,67.5 293.5,67 295,67 296.5,67 298,66.5 300,66.5 301.5,66.5 303,66 304.5,66 306,66 307.5,65.5 309,65.5 310.5,65.5 312,65.5 313.5,65 315,65 316.5,65 318,64.5 319.5,64.5 321,64.5 322.5,64 324,64 325.5,64 327,64 328.5,63.5 330,63.5 331.5,63.5 333,63 334.5,63 336,63 338,62.5 339.5,62.5 341,62.5 342.5,62.5 344,62 345.5,62 347,62 348.5,61.5 350,61.5 351.5,61.5 353,61 354.5,61 356,61 357.5,61 359,60.5 360.5,60.5 362,60.5 363.5,60 365,60 366.5,60 368,60 369.5,61 371,61.5 372.5,63 374,65 376,67.5 377.5,70 379,73 380.5,76.5 382,80 383.5,83.5 385,87.5 386.5,91 388,94.5 389.5,98 391,102 392.5,105.5 394,109 395.5,112.5 397,116.5 398.5,120 400,123.5 401.5,127 403,131 404.5,134.5 406,138 407.5,141.5 409,145.5 410.5,149 412,152.5 414,156 415.5,159.5 417,163 418.5,166 420,169 421.5,171.5 423,173 424.5,174.5 426,175.5 427.5,176 429,176 430.5,176 432,176 433.5,176 435,175.5 436.5,175.5 438,175.5 439.5,175.5 441,175 442.5,175 444,175 445.5,174.5 447,174.5 448.5,174.5 450,174 452,174 453.5,174 455,174 456.5,173.5 458,173.5 459.5,173.5 461,173 462.5,173 464,173 465.5,172.5 467,172.5 468.5,172.5 470,172.5 470,172.5" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="90,440 91.5,440 93,440 94.5,440 96,440 97.5,440 99,440 100.5,440 102,440 103.5,440 105,440 106.5,440 108,440 110,440 111.5,440 113,440 114.5,440 116,440 117.5,440 119,440 120.5,440 122,440 123.5,440 125,440 126.5,440 128,440 129.5,440 131,440 132.5,440 134,440 135.5,439.5 137,439.5 138.5,439.5 140,439.5 141.5,439 143,439 144.5,438.5 146,438.5 148,438 149.5,438 151,437.5 152.5,437 154,437 155.5,436.5 157,436 158.5,435.5 160,435 161.5,434.5 163,434 164.5,433.5 166,433 167.5,432.5 169,431.5 170.5,431 172,430.5 173.5,429.5 175,429 176.5,428 178,427.5 179.5,426.5 181,426 182.5,425 184,424.5 186,423.5 187.5,422.5 189,422 190.5,421 192,420 193.5,419.5 195,418.5 196.5,418 198,417 199.5,416 201,415.5 202.5,414.5 204,414 205.5,413 207,412 208.5,411.5 210,410.5 211.5,410 213,409 214.5,408 216,407.5 217.5,406.5 219,405.5 220.5,405 222,404 224,403.5 225.5,402.5 227,401.5 228.5,401 230,400 231.5,399.5 233,398.5 234.5,397.5 236,397 237.5,396 239,395.5 240.5,394.5 242,393.5 243.5,393 245,392 246.5,391 248,390.5 249.5,389.5 251,389 252.5,388 254,387 255.5,386.5 257,385.5 258.5,385 260,384 262,383 263.5,382.5 265,381.5 266.5,380.5 268,380 269.5,379 271,378.5 272.5,377.5 274,376.5 275.5,376 277,375 278.5,374.5 280,373.5 281.5,372.5 283,372 284.5,371 286,370.5 287.5,369.5 289,368.5 290.5,368 292,367 293.5,366 295,365.5 296.5,364.5 298,364 300,363 301.5,362 303,361.5 304.5,360.5 306,360 307.5,359 309,358 310.5,357.5 312,356.5 313.5,356 315,355 316.5,354 318,353.5 319.5,352.5 321,351.5 322.5,351 324,350 325.5,349.5 327,348.5 328.5,347.5 330,347 331.5,346 333,345.5 334.5,344.5 336,343.5 338,343 339.5,342 341,341 342.5,340.5 344,339.5 345.5,339 347,338 348.5,337 350,336.5 351.5,335.5 353,335 354.5,334 356,333 357.5,332.5 359,331.5 360.5,331 362,330 363.5,329 365,328.5 366.5,327.5 368,326.5 369.5,326 371,325 372.5,324.5 374,323.5 376,323 377.5,322 379,321.5 380.5,320.5 382,320 383.5,319.5 385,318.5 386.5,318 388,317.5 389.5,317 391,316.5 392.5,316 394,315.5 395.5,315 397,314.5 398.5,314 400,314 401.5,313.5 403,313 404.5,313 406,312.5 407.5,312.5 409,312 410.5,312 412,311.5 414,311.5 415.5,311.5 417,311.5 418.5,311 420,311 421.5,311 423,311 424.5,311 426,311 427.5,311 429,311 430.5,311 432,311 433.5,311 435,311 436.5,311 438,311 439.5,311 441,311 442.5,311 444,311 445.5,311 447,311 448.5,311 450,311 452,311 453.5,311 455,311 456.5,311 458,311 459.5,311 461,311 462.5,311 464,311 465.5,311 467,311 468.5,311 470,311 470,311" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90,440 91.5,440 93,440 94.5,440 96,440 97.5,440 99,440 100.5,440 102,440 103.5,440 105,440 106.5,440 108,440 110,440 111.5,440 113,440 114.5,440 116,440 117.5,440 119,440 120.5,440 122,440 123.5,440 125,439.5 126.5,439.5 128,439.5 129.5,439.5 131,439.5 132.5,439.5 134,439.5 135.5,439.5 137,439 138.5,439 140,439 141.5,438.5 143,438.5 144.5,438 146,438 148,437.5 149.5,437 151,437 152.5,436.5 154,436 155.5,435.5 157,435 158.5,434.5 160,434 161.5,433.5 163,433 164.5,432.5 166,431.5 167.5,431 169,430.5 170.5,429.5 172,429 173.5,428 175,427.5 176.5,426.5 178,426 179.5,425 181,424 182.5,423 184,422.5 186,421.5 187.5,420.5 189,420 190.5,419 192,418 193.5,417 195,416.5 196.5,415.5 198,414.5 199.5,413.5 201,413 202.5,412 204,411 205.5,410 207,409 208.5,408.5 210,407.5 211.5,406.5 213,405.5 214.5,405 216,404 217.5,403 219,402 220.5,401.5 222,400.5 224,399.5 225.5,398.5 227,397.5 228.5,397 230,396 231.5,395 233,394 234.5,393 236,392.5 237.5,391.5 239,390.5 240.5,389.5 242,388.5 243.5,388 245,387 246.5,386 248,385 249.5,384 251,383 252.5,382.5 254,381.5 255.5,380.5 257,379.5 258.5,378.5 260,377.5 262,377 263.5,376 265,375 266.5,374 268,373 269.5,372 271,371.5 272.5,370.5 274,369.5 275.5,368.5 277,367.5 278.5,366.5 280,365.5 281.5,365 283,364 284.5,363 286,362 287.5,361 289,360 290.5,359 292,358.5 293.5,357.5 295,356.5 296.5,355.5 298,354.5 300,353.5 301.5,352.5 303,351.5 304.5,350.5 306,350 307.5,349 309,348 310.5,347 312,346 313.5,345 315,344 316.5,343 318,342 319.5,341 321,340.5 322.5,339.5 324,338.5 325.5,337.5 327,336.5 328.5,335.5 330,334.5 331.5,333.5 333,332.5 334.5,331.5 336,330.5 338,329.5 339.5,328.5 341,327.5 342.5,327 344,326 345.5,325 347,324 348.5,323 350,322 351.5,321 353,320 354.5,319 356,318 357.5,317 359,316 360.5,315 362,314 363.5,313 365,312 366.5,311 368,310 369.5,309 371,308 372.5,307 374,306 376,305.5 377.5,304.5 379,303.5 380.5,302.5 382,301.5 383.5,301 385,300 386.5,299 388,298.5 389.5,297.5 391,297 392.5,296.5 394,295.5 395.5,295 397,294.5 398.5,293.5 400,293 401.5,292.5 403,292 404.5,291.5 406,291 407.5,290.5 409,290 410.5,290 412,289.5 414,289 415.5,288.5 417,288.5 418.5,288 420,288 421.5,287.5 423,287.5 424.5,287 426,287 427.5,286.5 429,286.5 430.5,286 432,286 433.5,285.5 435,285.5 436.5,285 438,285 439.5,285 441,284.5 442.5,284.5 444,284 445.5,284 447,283.5 448.5,283.5 450,283 452,283 453.5,282.5 455,282.5 456.5,282 458,282 459.5,281.5 461,281.5 462.5,281 464,281 465.5,280.5 467,280.5 468.5,280 470,280 470,280" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <line x1="474" y1="172.5" x2="474" y2="210" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="466" y1="172.5" x2="482" y2="172.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="430.5" y="140" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$v_\text{loppu}$</div></foreignObject>
  <line x1="110" y1="282" x2="148" y2="282" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="156" y="270" width="143" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{ilman virhettä}$</div></foreignObject>
  <line x1="110" y1="312" x2="148" y2="312" stroke="#6b7480" stroke-width="3" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="156" y="300" width="174" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{nollakohdan virhe}$</div></foreignObject>
</svg>

Matkan epävarmuuden voit arvioida esimerkiksi näillä tavoilla:

- **Toistot.** Laske matka usealta samanpituiselta hissimatkalta. Ilmoita tulos keskiarvona ja arvioi epävarmuus esimerkiksi vaihteluvälin puolikkaana: $\Delta s = \dfrac{s_\text{max} - s_\text{min}}{2}$.
- **Loppunopeus.** Jos virhe on vakio, se näkyy loppunopeutena $v_\text{loppu}$, vaikka hissi on pysähtynyt. Kun laskennan kesto on $t_\text{loppu}$, virhe on $\delta a = \dfrac{v_\text{loppu}}{t_\text{loppu}}$, ja matkaan sen aiheuttama virhe on $\tfrac{1}{2} \cdot \delta a \cdot t_\text{loppu}^2 = \tfrac{1}{2} \cdot v_\text{loppu} \cdot t_\text{loppu}$. Sitä voi käyttää arviona matkan epävarmuudelle.

Pyöristä $\Delta s$ yhteen merkitsevään numeroon ja $s$ samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, esimerkiksi nollakohta, puhelimen asento, anturin kohina tai todellisen matkan mittaus? Olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tulosta? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Kuinka pitkän matkan hissi kulki, ja kuinka hyvin kiihtyvyydestä laskettu matka vastasi todellista matkaa? Mistä erot johtuivat? Viittaa kuvaajiin, esimerkiksi "kuvaajasta 2 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** miten nopeus ja matka saadaan kuvaajien pinta-aloina ja mitä anturi näyttää levossa.
- **Työn suunnitelma:** puhelimen asento ja akseli, miten määritit anturin nollakohdan ja miten selvitit todellisen matkan.
- **Mittaustulokset ja käsittely:** kiihtyvyys, nopeus ja matka allekkain samalla aika-akselilla ja liikkeen vaiheet merkittyinä, sekä laskennan periaate.
- **Tulos:** $s = (s \pm \Delta s)\ \text{m}$ oikein pyöristettynä ja vertailu todelliseen matkaan.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet, loppunopeuden merkitys ja virheiden vaikutuksen suunta.

## Laajennus: nollakohdan virheen korjaus

Jos laskettu nopeus ei palaa lopussa nollaan, vaikka hissi on pysähtynyt, tiedetään, että laskennassa on virhe. Tätä tietoa voi käyttää virheen korjaamiseen. Jos oletetaan, että virhe $\delta a$ on koko matkan ajan sama, se saadaan loppunopeudesta, ja sen voi vähentää jokaisesta kiihtyvyydestä ennen kuin nopeus ja matka lasketaan uudelleen. Korjattu nopeus palaa lopussa nollaan.

Korjaa laskentasi tällä tavalla ja vertaa korjattua matkaa korjaamattomaan ja todelliseen matkaan. Muuttuiko tulos paljon? Missä tilanteessa oletus vakiovirheestä ei pätisi, esimerkiksi jos puhelin kallistui kesken matkan?

Mittaa lisäksi eripituisia matkoja, esimerkiksi yhden, kahden ja kolmen kerroksen matkat, ja piirrä laskettu matka kerrosten lukumäärän funktiona. Mitä kuvaajan kulmakerroin kertoo? Vertaa sitä mittaamaasi kerroskorkeuteen epävarmuuksineen. Päällekkäiset epävarmuusvälit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi.

::: tuki OO
**Vihjeitä.** Korjauksessa vähennetään jokaisesta kiihtyvyydestä $\delta a = \dfrac{v_\text{loppu}}{t_\text{loppu}}$, missä $v_\text{loppu}$ on korjaamaton loppunopeus ja $t_\text{loppu}$ laskennan kesto. Tee korjaus omiin sarakkeisiinsa, niin alkuperäinen laskenta säilyy vertailua varten. Jos alun ja lopun lepojaksojen keskimääräiset lukemat poikkeavat selvästi toisistaan, nollakohta on muuttunut kesken mittauksen, eikä vakiovirheen oletus pidä.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi ja laskentasi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajiin ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
