# Umpinaisen sylinterin hitausmomentti

> **Tutkimuskysymys:** Kuinka suuri on umpinaisen sylinterin hitausmomentti, kun se määritetään kaltevaa tasoa alas vierivän sylinterin liikkeestä, ja vastaako tulos teoreettista mallia?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: työpöydällä on kirjapinon varaan nojaava lauta, joka muodostaa kaltevan tason. Tason yläpäässä on levossa umpinainen metallisylinteri päästä katsottuna, ja tason poikki pystytetty viivain pitää sitä paikallaan. Tason alapäässä on pehmeä pysäytin. Pöydällä on lisäksi ohutseinäinen putki ja oikealla pystyssä polkupyörän rengas akseleineen." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10hh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10hh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy10hh-board" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e0b878"/><stop offset="1" stop-color="#c99a55"/></linearGradient><radialGradient id="fy10hh-cyl" cx="0.4" cy="0.35" r="0.75"><stop offset="0" stop-color="#e9edf1"/><stop offset="1" stop-color="#c4ccd4"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10hh-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy10hh-desk)"/>
  <line x1="0" y1="492" x2="1200" y2="488" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="510" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="532" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="554" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="576" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="96" y="429" width="134" height="41" rx="4" fill="#4c6ef5" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="108" y1="449" x2="218" y2="449" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <rect x="100" y="387.5" width="134" height="41" rx="4" fill="#e8590c" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="112" y1="407.5" x2="222" y2="407.5" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <rect x="96" y="346" width="134" height="41" rx="4" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="108" y1="366" x2="218" y2="366" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <rect x="100" y="305" width="134" height="41" rx="4" fill="#f08c00" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="112" y1="325" x2="222" y2="325" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <path d="M110,254 L820,452 L815,469.5 L105,271.5 Z" fill="url(#fy10hh-board)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="830" y="420" width="46" height="50" rx="10" fill="#495057" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="239.5" cy="236" r="52" fill="url(#fy10hh-cyl)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="239.5" cy="236" r="3.5" fill="#1f2933"/>
  <path d="M275.5,300 L283.5,302.5 L318.5,177 L310.5,175 Z" fill="#ffe8a3" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="960" cy="426" r="40" fill="none" stroke="#8a96a3" stroke-width="5"/>
  <circle cx="960" cy="426" r="42.5" fill="none" stroke="#1f2933" stroke-width="2"/>
  <circle cx="960" cy="426" r="37.5" fill="none" stroke="#1f2933" stroke-width="2"/>
  <circle cx="960" cy="426" r="3.5" fill="#1f2933"/>
  <circle cx="1100" cy="378" r="88" fill="none" stroke="#1f2933" stroke-width="10.56"/>
  <circle cx="1100" cy="378" r="79.2" fill="none" stroke="#8a96a3" stroke-width="3"/>
  <line x1="1106.5" y1="380.5" x2="1177.5" y2="378" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1105" y1="383" x2="1173" y2="404.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1103" y1="384.5" x2="1159.5" y2="428" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1101" y1="385" x2="1138.5" y2="445" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1098.5" y1="385" x2="1113.5" y2="454.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1096" y1="384" x2="1086.5" y2="454.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1094.5" y1="382" x2="1061.5" y2="445" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1093.5" y1="380" x2="1040.5" y2="428" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1093" y1="377.5" x2="1027" y2="404.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1093.5" y1="375.5" x2="1022.5" y2="378" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1095" y1="373" x2="1027" y2="351.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1097" y1="371.5" x2="1040.5" y2="328" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1099" y1="371" x2="1061.5" y2="311" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1101.5" y1="371" x2="1086.5" y2="301.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1104" y1="372" x2="1113.5" y2="301.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1105.5" y1="374" x2="1138.5" y2="311" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1106.5" y1="376" x2="1159.5" y2="328" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1107" y1="378.5" x2="1173" y2="351.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="1100" cy="378" r="8.8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1094" y="372" width="12" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
</svg>

Pyörä, vauhtipyörä ja pyörivä taitoluistelija liikkuvat eri tavalla kuin suoraan liukuva kappale: pyörimisliikkeessä ei ratkaise pelkkä massa, vaan myös se, miten massa on jakautunut pyörimisakselin ympärille. Tätä kuvaa suure nimeltä **hitausmomentti**. Tässä tutkimuksessa selvität ensin, mitä hitausmomentti tarkoittaa, ja määrität sitten mittaamalla umpinaisen sylinterin hitausmomentin, kun sylinteri vierii kaltevaa tasoa alas. Pyörimisliikkeen energia ja hitausmomentti eivät kuulu lukion fysiikan moduuleihin, joten tarvittava teoria on tiivistetty tälle sivulle. Mittaa, analysoi ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** mitä hitausmomentti tarkoittaa ja mistä se riippuu, kuinka suuri umpinaisen sylinterin hitausmomentti on epävarmuuksineen, kun se määritetään vierimisliikkeestä energian säilymisen avulla, ja mahtuuko teoreettisen mallin antama arvo mittaustuloksen epävarmuusväliin.

**Päätät itse** (osittain ohjattu ja itsenäinen työtapa): tason kaltevuuden ja vierimismatkat, sen, miten mittaat sylinterin nopeuden, toistojen määrän, kuvaajan akselit tai laskutavan sekä tavan, jolla arvioit tuloksen epävarmuuden. Osittain ohjatussa työtavassa sivu ehdottaa näihin yhden toimivan tavan, jonka voit korvata perustellulla omallasi. Itsenäisessä työtavassa suunnittelet ja perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, pyörimismäärän säilymisen demonstraatio polkupyörän renkaalla, kuuluu työhösi.
:::

::: tuki OO
**Osittain ohjattu työtapa.** Laajennus, pyörimismäärän säilymisen demonstraatio polkupyörän renkaalla, on vapaaehtoinen. Opettaja kertoo, tehdäänkö se.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Umpinainen sylinteri ja ontto putki päästetään levosta yhtä aikaa samalta korkeudelta vierimään kaltevaa tasoa alas. Kumpi ehtii alas ensin, vai tulevatko ne yhtä aikaa? Miksi?
2. Onko vierivän sylinterin nopeus tason alapäässä suurempi, yhtä suuri vai pienempi kuin sellaisen kappaleen nopeus, joka liukuu kitkatta alas samalta korkeudelta? Mihin sylinterin potentiaalienergia muuttuu?
3. Jos osa sylinterin energiasta muuttuu matkalla lämmöksi, esimerkiksi vierimisvastuksen takia, tuleeko mittaamastasi hitausmomentista liian suuri vai liian pieni?
4. Mikä mittauksessasi on todennäköisesti suurin epävarmuuden lähde?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Selvitä: mitä hitausmomentti tarkoittaa?

Ennen mittausta ota selvää käsitteestä esimerkiksi oppikirjasta, luotettavista verkkolähteistä tai opettajalta, ja kirjoita omin sanoin:

1. Mistä kappaleen hitausmomentti riippuu?
2. Miten hitausmomentti liittyy kappaleen pyörimisliikkeeseen?
3. Miten massan jakautuminen pyörimisakselin suhteen vaikuttaa hitausmomenttiin?

Kokeile sitten: päästä umpinainen sylinteri ja vertailukappale, jonka massa on jakautunut toisin (esimerkiksi putki), levosta yhtä aikaa samalta korkeudelta vierimään tasoa alas. Kirjaa, kumpi ehti alas ensin, ja toista kokeilu muutaman kerran. Merkitse lähteesi muistiin.

## Teoriaa lyhyesti

Tarkista tästä selvityksesi ja täydennä sitä.

**Pyörimisliike.** Kun kappale pyörii akselin ympäri, sen pyörimisen nopeutta kuvaa **kulmanopeus** $\omega$: kuinka suuren kulman kappale kiertyy aikayksikössä. Kun kulma mitataan radiaaneina, kulmanopeuden yksikkö on $\text{rad/s}$, ja akselista etäisyydellä $r$ oleva kappaleen kohta liikkuu ratanopeudella $v = r\omega$.

**Hitausmomentti.** Kuvitellaan kappale jaetuksi pieniin osiin. Jos osan massa on $m_i$ ja sen etäisyys pyörimisakselista $r_i$, kappaleen hitausmomentti akselin suhteen on

```latex
I = \sum m_i r_i^2
```

Hitausmomentin yksikkö on $\text{kg}\cdot\text{m}^2$. Hitausmomentti on pyörimisliikkeessä samassa asemassa kuin massa etenemisliikkeessä: mitä suurempi hitausmomentti, sitä vaikeampi kappaleen pyörimistä on saada alkuun, muuttaa tai pysäyttää. Hitausmomentti riippuu kappaleen massasta, massan jakautumisesta ja pyörimisakselin paikasta. Koska etäisyys on yhtälössä toisessa potenssissa, kaukana akselista oleva massa kasvattaa hitausmomenttia paljon enemmän kuin akselin lähellä oleva.

Umpinaisen ja tasa-aineisen sylinterin, jonka massa on $m$ ja säde $r$, hitausmomentti symmetria-akselinsa suhteen on teoreettisen mallin mukaan $I = \tfrac{1}{2}\, m r^2$. Ohutseinäisen putken massa on lähes kokonaan etäisyydellä $r$ akselista, joten sen hitausmomentti on likimain $m r^2$. Malli olettaa, että sylinterin tiheys on joka kohdassa sama ja että se pyörii symmetria-akselinsa ympäri.

<svg data-fig="concept" viewBox="0 0 600 330" role="img" aria-label="Kaaviokuva: vasemmalla umpinainen tasa-aineinen sylinteri ja oikealla ohutseinäinen putki päästä katsottuna. Kummallakin on sama massa m ja sama säde r, ja pyörimisakseli kulkee keskipisteen kautta kohtisuoraan kuvan tasoa vastaan. Sylinterin massa on jakautunut koko poikkileikkaukselle, putken massa on lähes kokonaan etäisyydellä r akselista. Sylinterin hitausmomentti on puolet m r toiseen, putken likimain m r toiseen." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy10hc-160" cx="0.4" cy="0.35" r="0.75"><stop offset="0" stop-color="#e9edf1"/><stop offset="1" stop-color="#c4ccd4"/></radialGradient></defs>
  <circle cx="160" cy="125" r="80" fill="url(#fy10hc-160)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="160" cy="125" r="3.5" fill="#1f2933"/>
  <line x1="160" y1="125" x2="225.5" y2="79" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="186" y="77.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r$</div></foreignObject>
  <circle cx="440" cy="125" r="80" fill="none" stroke="#8a96a3" stroke-width="9.6"/>
  <circle cx="440" cy="125" r="84.8" fill="none" stroke="#1f2933" stroke-width="2"/>
  <circle cx="440" cy="125" r="75.2" fill="none" stroke="#1f2933" stroke-width="2"/>
  <circle cx="440" cy="125" r="3.5" fill="#1f2933"/>
  <line x1="440" y1="125" x2="505.5" y2="79" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="466" y="77.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="37.5" y="220.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{umpinainen sylinteri}$</div></foreignObject>
  <foreignObject x="323.5" y="220.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ohutseinäinen putki}$</div></foreignObject>
  <foreignObject x="112.5" y="270.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I = \tfrac{1}{2}\, m r^2$</div></foreignObject>
  <foreignObject x="405" y="270.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I \approx m r^2$</div></foreignObject>
</svg>

**Pyörimisliikkeen energia.** Pyörivällä kappaleella on liike-energiaa, vaikka sen keskipiste pysyisi paikallaan. Kulmanopeudella $\omega$ pyörivän kappaleen pyörimisenergia on

```latex
E_\text{r} = \tfrac{1}{2}\, I \omega^2
```

Vierivä sylinteri sekä etenee että pyörii, joten sen liike-energia on etenemisen ja pyörimisen liike-energioiden summa $\tfrac{1}{2}\, m v^2 + \tfrac{1}{2}\, I \omega^2$, missä $v$ on sylinterin keskipisteen nopeus.

**Vieriminen ilman liukumista.** Kun sylinteri vierii liukumatta, sen keskipisteen nopeus ja kulmanopeus liittyvät toisiinsa yhtälöllä $v = r\omega$. Sylinterin ja tason kosketuskohta on silloin joka hetki levossa tason suhteen, joten lepokitka ei tee työtä eikä muuta mekaanista energiaa lämmöksi. Jos lisäksi vierimisvastus ja ilmanvastus ovat merkityksettömän pieniä, sylinterin mekaaninen energia säilyy: kun sylinterin keskipiste laskee korkeuden $h$, potentiaalienergiaa $mgh$ muuttuu etenemisen ja pyörimisen liike-energiaksi. [[apua:fy4-8|Mekaanisen energian säilyminen]]

<svg data-fig="setup" viewBox="0 0 600 400" role="img" aria-label="Kaaviokuva. Umpinainen sylinteri lähtee levosta kaltevan tason yläosasta ja vierii alas. Matka tason suuntaisesti lähtökohdasta loppukohtaan on s. Sylinterin keskipisteen korkeus laskee matkalla h:n verran. Loppukohdassa sylinterin keskipisteen nopeus v osoittaa tason suuntaisesti alas, ja sylinteri pyörii myötäpäivään kulmanopeudella omega. Sylinterin säde on r." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy10hs-c0" cx="0.4" cy="0.35" r="0.75"><stop offset="0" stop-color="#e9edf1"/><stop offset="1" stop-color="#c4ccd4"/></radialGradient><radialGradient id="fy10hs-c1" cx="0.4" cy="0.35" r="0.75"><stop offset="0" stop-color="#e9edf1"/><stop offset="1" stop-color="#c4ccd4"/></radialGradient></defs>
  <path d="M40,120 L560,330 L554,345 L34,135 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="40" y1="347" x2="590" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="99" cy="107" r="34" fill="url(#fy10hs-c0)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="99" cy="107" r="3.5" fill="#1f2933"/>
  <circle cx="433" cy="242" r="34" fill="url(#fy10hs-c1)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="433" cy="242" r="3.5" fill="#1f2933"/>
  <foreignObject x="20" y="38.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lähtö levosta}$</div></foreignObject>
  <line x1="69" y1="181.5" x2="403" y2="316" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="66" y1="189.5" x2="72.5" y2="173" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="399.5" y1="324.5" x2="406.5" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="79.5" y1="155.5" x2="71.5" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="413.5" y1="290" x2="405" y2="310.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <foreignObject x="212" y="258.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s$</div></foreignObject>
  <line x1="139" y1="107" x2="593" y2="107" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="473" y1="242" x2="593" y2="242" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="585" y1="107" x2="585" y2="242" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="577" y1="107" x2="593" y2="107" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="577" y1="242" x2="593" y2="242" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="557" y="160" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$h$</div></foreignObject>
  <line x1="433" y1="242" x2="463.5" y2="227.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="473" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r$</div></foreignObject>
  <line x1="433" y1="242" x2="496" y2="267.5" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M509,272.5 L492.5,273.5 L497.5,261 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="517" y="254" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <path d="M389.5,217 A50,50 0 0 1 458,198.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M468.5,204.5 L455,204 L461,193.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="403" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\omega$</div></foreignObject>
</svg>

## Hitausmomentista mitattaviksi suureiksi

Hitausmomenttia ei voi lukea mittarista. Kirjaa ennen kuin luet eteenpäin:

1. Kirjoita energian säilyminen sylinterille, joka lähtee levosta ja jonka keskipiste laskee korkeuden $h$.
2. Ratkaise yhtälöstä hitausmomentti $I$.
3. Mitkä suureet sinun on mitattava, ja miten saat sylinterin nopeuden tason alapäässä selville?

::: tuki OO
**Tarkista kirjauksesi tästä.** Energian säilymisestä ja ehdosta $\omega = \dfrac{v}{r}$ saadaan

```latex
mgh = \tfrac{1}{2}\, m v^2 + \tfrac{1}{2}\, I \cdot \frac{v^2}{r^2}
```

ja siitä ratkaistuna

```latex
I = m r^2 \left( \frac{2gh}{v^2} - 1 \right)
```

Tarvitset siis sylinterin massan $m$, säteen $r$, keskipisteen korkeuden muutoksen $h$ ja nopeuden $v$ tason alapäässä. Massan saat vaa'alla ja säteen halkaisijasta työntömitalla. Nopeutta on vaikea mitata suoraan, mutta sen voi päätellä matkasta ja ajasta: sylinteriin vaikuttavat voimat pysyvät liikkeen aikana samoina, joten sen kiihtyvyys on vakio. Kun sylinteri lähtee levosta ja vierii matkan $s$ ajassa $t$, sen keskinopeus on $\dfrac{s}{t}$ ja loppunopeus kaksinkertainen:

```latex
v = \frac{2s}{t}
```

[[apua:fy4-2|Tasaisesti kiihtyvä liike]]
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona, ja miten varmistat, että sylinteri lähtee levosta ja vierii liukumatta. Kokeile vierimistä ensin muutaman kerran.

::: tuki OO
**Osittain ohjattu.** Pidä tason kaltevuus vakiona ja muuta vierimismatkaa $s$: päästä sylinteri levosta eri kohdista ja mittaa aika $t$, jonka se tarvitsee matkaan. Tee mittaukset ainakin viidellä eri matkalla ja jokaisella matkalla kolme toistoa. Laske jokaiselle matkalle keskipisteen korkeuden muutos $h$. Kun tason pinta on suora, $h$ on yhtä suuri kuin tason pinnan korkeuden muutos matkalla $s$: $h = s \cdot \dfrac{H}{L}$, missä $H$ on tason pinnan kahden pisteen korkeusero ja $L$ niiden välinen etäisyys tasoa pitkin. Kirjaa päätöksesi perusteluineen.

Mieti ainakin näitä:

- Kuinka jyrkäksi taso kannattaa asettaa, jotta sylinteri vierii liukumatta mutta lähtee varmasti liikkeelle ja aika on riittävän pitkä mitattavaksi?
- Miten päästät sylinterin liikkeelle levosta tönäisemättä, esimerkiksi viivaimen takaa, ja miten merkitset lähtö- ja loppukohdan?
- Miten mittaat ajan niin tarkasti kuin mahdollista: käsin ajanottovälineellä, videolta vai liikeanturilla?
- Pitääkö taso olla suorassa linjassa, ettei sylinteri ajaudu sivuun?
- Jos käytät kourua, vierikö sylinteri koko ulkopinnallaan tasaisella pohjalla? V-urassa tai kahden kiskon varassa sylinteri koskettaa alustaa pienemmällä säteellä kuin $r$, jolloin yhtälö $v = r\omega$ ei päde ja hitausmomentista tulee liian suuri.
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana: toistot omiin sarakkeisiinsa ja niistä lasketut suureet niiden oikealle puolelle. Mittaa ja kirjaa myös sylinterin massa ja säde.

::: tuki OO
Voit käyttää esimerkiksi tällaisia taulukoita. Mittaa halkaisija työntömitalla useasta kohdasta:

| $d_1\ (\text{m})$ | $d_2\ (\text{m})$ | $d_3\ (\text{m})$ | $\bar{d}\ (\text{m})$ | $r = \dfrac{\bar{d}}{2}\ (\text{m})$ | $m\ (\text{kg})$ |
|---|---|---|---|---|---|
| | | | | | |

| $s\ (\text{m})$ | $t_1\ (\text{s})$ | $t_2\ (\text{s})$ | $t_3\ (\text{s})$ | $\bar{t}\ (\text{s})$ | $h\ (\text{m})$ | $v = \dfrac{2s}{\bar{t}}\ (\text{m/s})$ | $v^2\ (\text{m}^2/\text{s}^2)$ |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Kirjaa lisäksi tason mitat $H$ ja $L$.
:::

Muista mittausepävarmuus: kirjaa jokaisen suureen kohdalla, kuinka tarkasti sen mittasit, ja miten arvioit tarkkuuden. Toistojen hajonta kertoo, kuinka paljon mittaamasi suure vaihtelee vierimisestä toiseen. [[apua:fy1-3|Toistomittausten keskiarvo ja epävarmuus]]

## Käsittele tulokset

Määritä mittaustuloksistasi sylinterin hitausmomentti energian säilymisen avulla ja perustele, miksi valitsit juuri tämän laskutavan tai nämä kuvaajan akselit. Laske lisäksi hitausmomentti teoreettisella mallilla $I = \tfrac{1}{2}\, m r^2$ mittaamistasi massasta ja säteestä. [[apua:fy1-4|Graafinen esitys]]

Vastaa lisäksi:

1. Vertaa sylinterin nopeutta tason alapäässä nopeuteen, jonka kitkatta liukuva kappale saisi samalta korkeudelta. Miten selität eron?
2. Selitä hitausmomentin avulla, miksi umpinainen sylinteri ja vertailukappale tulivat alas siinä järjestyksessä kuin tulivat. Riippuuko järjestys mielestäsi kappaleiden massasta tai koosta vai vain siitä, miten massa on jakautunut? Perustele energian säilymisen avulla.

::: tuki OO
**Kuvaajan avulla.** Edellisen kohdan yhtälöstä saadaan nopeuden neliö korkeuden funktiona:

```latex
v^2 = \frac{2g}{1 + \dfrac{I}{m r^2}} \cdot h
```

Kun pystyakselille valitaan $v^2$ ja vaaka-akselille $h$, mallin mukainen kuvaaja on origon kautta kulkeva suora. Sovita mittauspisteisiin suora ja merkitse sen kulmakerrointa $a$. Silloin

```latex
I = m r^2 \left( \frac{2g}{a} - 1 \right)
```

Kuvaaja on yksittäisiä laskuja parempi, koska se näyttää, sopivatko kaikki mittaukset samaan malliin, ja suora tasoittaa satunnaisia virheitä. Katkoviivalla oleva suora on vertailun vuoksi kitkatta liukuvan kappaleen malli $v^2 = 2gh$.

<svg data-fig="model" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja: nopeuden neliö v toiseen tason alapäässä korkeuden h funktiona mallin mukaan. Katkoviivalla on suora, jonka kulmakerroin on 2 g; se vastaisi kitkatta liukuvaa kappaletta. Yhtenäinen suora on vierivän kappaleen malli: suora origon kautta, jonka kulmakerroin a on pienempi kuin 2 g. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="310" x2="484" y2="310" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,310 L483,316 L483,304 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="311" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="80" y="3.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v^2$</div></foreignObject>
  <polyline points="90,310 417,72.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="90,310 455,135" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="150" y="73" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{kulmakerroin } 2g$</div></foreignObject>
  <foreignObject x="288.5" y="210.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kulmakerroin } a$</div></foreignObject>
</svg>

Jos suora ei kulje origon kautta, mieti, onko matkojen tai korkeuksien nollakohdassa systemaattinen virhe. Matkaan verrannollinen energiahäviö, esimerkiksi tasainen vierimisvastus, ei näy vakioterminä, koska kaltevuus on vakio: se muuttaa vain kulmakerrointa.
:::

Laskuihin ja kuvaajiin voit käyttää esimerkiksi Graphical Analysis -ohjelmaa tai taulukkolaskentaa. Ruukkilabran ohjeet: [[ohje:tvt-kuvaaja|Mittauspisteiden kuvaaja]] ja [[ohje:tvt-taulukkolaskenta|Taulukkolaskenta]].

## Epävarmuus ja luotettavuus

Ilmoita mittaamasi hitausmomentti muodossa $I = (I \pm \Delta I)\ \text{kg}\cdot\text{m}^2$ ja perustele, miten arvioit epävarmuuden $\Delta I$. Ilmoita samoin mallin antama arvo epävarmuuksineen. Mahtuvatko arvot toistensa epävarmuusväleihin? Päällekkäiset välit tarkoittavat, että tulos on sopusoinnussa mallin kanssa, eivät sitä, että arvot on todistettu samoiksi.

::: tuki OO
**Epävarmuuden arviointi.** Määritä ensin kulmakertoimen epävarmuus $\Delta a$ sovitusohjelman keskivirheestä tai jyrkimmän ja loivimman suoran avulla: $\Delta a = \dfrac{a_\text{max} - a_\text{min}}{2}$. Etene sitten vaihe kerrallaan:

- Suureen $\dfrac{2g}{a}$ suhteellinen epävarmuus on sama kuin kulmakertoimen, $\dfrac{\Delta a}{a}$.
- Kun suureesta $\dfrac{2g}{a}$ vähennetään luku $1$, absoluuttinen epävarmuus pysyy samana, mutta erotus on pienempi kuin $\dfrac{2g}{a}$. Erotuksen suhteellinen epävarmuus on siksi selvästi suurempi kuin kulmakertoimen suhteellinen epävarmuus. Tämä on tämän menetelmän heikkous: pienikin virhe nopeudessa näkyy hitausmomentissa suurena.
- Hitausmomentissa on lisäksi tekijä $m r^2$. Suhteelliset epävarmuudet lasketaan yhteen, ja koska säde on toisessa potenssissa, sen suhteellinen epävarmuus lasketaan kahdesti: $\dfrac{\Delta m}{m} + 2 \cdot \dfrac{\Delta r}{r}$.
- Mallin arvon $\tfrac{1}{2}\, m r^2$ suhteellinen epävarmuus on $\dfrac{\Delta m}{m} + 2 \cdot \dfrac{\Delta r}{r}$.

Koska sekä mittaustuloksessa että mallissa on sama tekijä $m r^2$, voit lisäksi verrata suoraan lukua $\dfrac{I}{m r^2} = \dfrac{2g}{a} - 1$ mallin arvoon $\tfrac{1}{2}$. Pyöristä epävarmuus yhteen merkitsevään numeroon ja tulos samaan desimaaliin.
:::

Laske myös mittaamasi suhde $\dfrac{I}{m r^2}$ ja vertaa sitä mallin arvoon $\tfrac{1}{2}$: onko se suurempi vai pienempi, ja sopiiko poikkeaman suunta ennusteeseesi 3?

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet hitausmomenttia? Pitivätkö mallin oletukset paikkansa: vierikö sylinteri liukumatta, olivatko energiahäviöt pieniä ja onko sylinterisi todella umpinainen ja tasa-aineinen? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Vastaako mittaamasi hitausmomentti teoreettista mallia epävarmuuksien rajoissa? Jos ei, mikä mallin oletus tai mittauksen virhelähde selittää eron parhaiten? Viittaa kuvaajaan tai taulukkoon, esimerkiksi "kuvaajasta 1 nähdään, että …". Kirjoita lopuksi omin sanoin, mitä hitausmomentti tarkoittaa ja miten massan jakautuminen vaikuttaa siihen, ja vertaa tuloksiasi ennusteisiisi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla (kuvaajista ja tuloksista ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]) ja käy läpi sen kaikki osat. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** hitausmomentin merkitys omin sanoin lähteineen, pyörimisenergia, vierimisen ehto ja energian säilymisen yhtälö, josta hitausmomentti ratkaistaan.
- **Koejärjestely ja menetelmä:** mitä muutit, mitä mittasit ja mitä pidit vakiona, miten määritit nopeuden ja miten varmistit, että sylinteri lähti levosta.
- **Mittaustulokset:** alkuperäiset mittaukset toistoineen omissa sarakkeissaan ja johdetut suureet niiden oikealla puolella.
- **Tulos:** mitattu ja mallin antama hitausmomentti epävarmuuksineen oikein pyöristettyinä.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet, niiden vaikutuksen suunta ja mallin oletusten pätevyys.

## Laajennus: pyörimismäärän säilyminen

Etenemisliikkeessä kappaleella on liikemäärä $\overline{p} = m\overline{v}$, ja eristetyn systeemin liikemäärä säilyy. [[apua:fy4-10|Liikemäärän säilyminen]] Pyörimisliikkeessä vastaava suure on **pyörimismäärä** eli liikemäärän momentti. Kun kappale pyörii symmetria-akselinsa ympäri, sen pyörimismäärän suuruus on

```latex
L = I\omega
```

Pyörimismäärä $\overline{L}$ on vektori, joka osoittaa pyörimisakselin suuntaan: kun oikean käden sormet kiertyvät pyörimisen suuntaan, peukalo osoittaa pyörimismäärän suunnan. Pyörimismäärä säilyy sekä suuruudeltaan että suunnaltaan, jos systeemiin ei vaikuta ulkoista momenttia eli vääntövaikutusta. Pyörimismäärän komponentti jossakin suunnassa säilyy, kun ulkoisella momentilla ei ole komponenttia siinä suunnassa, vaikka pyörimismäärä muissa suunnissa muuttuisi.

Selvitä ensin lähteistä, millaisissa tilanteissa pyörimismäärä säilyy, ja kirjaa esimerkkejä arkielämästä. Suunnittele sitten polkupyörän renkaan avulla koe tai demonstraatio, jolla voit havaita pyörimismäärän säilymiseen liittyvän ilmiön. Kuvaile:

1. mitä teet
2. mitä havaitset
3. miten havaintosi voidaan selittää pyörimismäärän avulla.

Arvioi lopuksi, kuinka hyvin koe tai demonstraatio havainnollistaa pyörimismäärän säilymistä ja mitkä tekijät, esimerkiksi kitka, häiritsevät sitä.

**Turvallisuus.** Pidä kädet, hiukset, korut ja löysät vaatteet poissa renkaan pinnoista. Pyörivää jakkaraa saa käyttää vain opettajan luvalla: pysy jakkaralla tukevasti, pidä ympärillä tilaa ja pyydä toista opiskelijaa varmistamaan vierestä.

::: tuki OO
**Ideoita.** Valitse yksi ja suunnittele se loppuun itse:

- Pidä rengasta akselin kahvoista ja pyöritä sitä. Yritä kääntää akselin suuntaa, ja vertaa tuntumaa siihen, kun rengas ei pyöri.
- Opettajan luvalla: istu pyörivällä jakkaralla jalat irti lattiasta ja pidä pyörivää rengasta akseli pystyssä. Käännä renkaan akseli toisin päin ja havainnoi jakkaraa.
- Ripusta pyörivä rengas narusta toisesta akselin päästä akseli vaakasuorassa ja havainnoi, mitä akseli tekee.

Mieti jokaisessa: mikä on systeemi, vaikuttaako siihen ulkoinen momentti ja minkä akselin suhteen, ja mikä pyörimismäärän osa säilyy?
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi mittaustuloksiin ja niiden epävarmuuksiin vai siihen, mitä odotit?
- Selitätkö hitausmomentin nyt omin sanoin paremmin kuin työn alussa?
- Mitä tekisit toisin, jos aloittaisit alusta?
