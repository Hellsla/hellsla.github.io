# Homogeeninen sähkökenttä

> **Miksi** ilmanpuhdistimen pölyhiukkaset päätyvät laitteen levyjen pintaan, vaikka ilma virtaa levyjen ohi?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: aurinkoinen olohuone. Vasemmalla ikkunasta tulee vino auringonsäde, jossa leijuu pölyhiukkasia. Keskellä lattialla seisoo valkoinen pylvään muotoinen ilmanpuhdistin, jonka kyljessä on ritilä. Pölyhiukkaset kulkevat kaarevina jonoina säteestä puhdistimen ritilää kohti. Oikealla on sininen sohva ja ruukkukasvi." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Varaus muuttaa ympäröivää tilaa
Luvussa *Sähkövaraus ja Coulombin laki* kaksi varausta vaikuttivat toisiinsa voimalla, vaikka ne eivät koskettaneet toisiaan. Tätä kutsutaan etävuorovaikutukseksi. Sitä kuvataan **sähkökentän** avulla. Sähkökenttä on se alue varauksen ympärillä, jossa toiseen varaukseen kohdistuu sähköinen voima. Varaus muuttaa ympäröivää tilaa niin, että jokaiseen toiseen varaukseen kohdistuu siellä voima. Kenttä on olemassa jokaisessa kohdassa, vaikka siellä ei juuri nyt olisi varausta, johon kenttä voisi vaikuttaa. Kun kohtaan tuodaan varaus, kenttä vaikuttaa siihen. Ajatus on sama kuin painovoimassa: Maa vetää omenaa kentän välityksellä, vaikka omena ei kosketa Maata.

### Sähkökentän voimakkuus
Kenttää tutkitaan pienellä positiivisella **testivarauksella** $q$. Testivaraus on niin pieni, ettei se muuta kenttää aiheuttavien varausten paikkoja. Kun testivaraukseen kohdistuu voima $\overline{F}$, kohdan **sähkökentän voimakkuus** on voima jaettuna testivarauksella: $\overline{E} = \overline{F} : q$. Sähkökentän voimakkuus kertoo siis, kuinka suuri voima kohdistuu yhteen coulombiin. Sen yksikkö on $\text{N/C}$. Jos $2{,}0\,\text{nC}$:n varaukseen kohdistuu voima $100\,\mu\text{N}$, kentän voimakkuus on $5{,}0 \cdot 10^{4}\,\text{N/C}$. Suure ei riipu testivarauksesta. Kaksinkertainen varaus saa kaksinkertaisen voiman, mutta osamäärä pysyy samana. Symboli $E$ on sama kuin luvun *Lähdejännite ja sisäinen resistanssi* lähdejännitteellä. Siksi tässä luvussa $E$ tarkoittaa aina sähkökentän voimakkuutta.

Sähkökenttä on vektori eli suure, jolla on suuruus ja suunta. Kentän suunta on se suunta, johon kenttä työntää positiivista varausta. Negatiiviseen varaukseen, esimerkiksi elektroniin, kohdistuu voima kenttää vastaan. Kuvassa kohdan $P$ kenttä on sama molemmissa tilanteissa. Voiman suunta riippuu testivarauksen merkistä.

```pysahdy
Kentän voimakkuus mitataan testivarauksella. Testivaraus kaksinkertaistetaan samassa kohdassa. Muuttuuko kentän voimakkuus?
---
Ei muutu. Voima kaksinkertaistuu, mutta $E = F : q$ pysyy samana, koska varaus kasvaa yhtä paljon.
```

<svg data-fig="test" viewBox="0 0 600 330" role="img" aria-label="Kaksi kaavakuvaa vierekkäin, ei mittakaavassa. Kummassakin kuvassa vasemmalla on suuri positiivinen varaus Q. Sen oikealla puolella on kohta P, johon on tuotu pieni testivaraus. Kohdan P sähkökentän vihreä nuoli E osoittaa kummassakin kuvassa oikealle, poispäin varauksesta Q. Vasemmassa kuvassa testivaraus on positiivinen. Siihen kohdistuvan voiman punainen nuoli F osoittaa samaan suuntaan kuin kenttä. Oikeassa kuvassa testivaraus on negatiivinen. Voiman nuoli osoittaa vastakkaiseen suuntaan, kohti varausta Q." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-test.webp" x="0" y="-1.2" width="600" height="337.5" preserveAspectRatio="none"/>
  <foreignObject x="20" y="19.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{positiivinen } q$</div></foreignObject>
  <foreignObject x="47" y="207.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="165" y="191.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P$</div></foreignObject>
  <foreignObject x="210" y="69.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="224" y="127.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="65" y="265.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{F} = q\overline{E}$</div></foreignObject>
  <foreignObject x="320" y="19.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{negatiivinen } q$</div></foreignObject>
  <foreignObject x="347" y="207.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="465" y="191.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P$</div></foreignObject>
  <foreignObject x="510" y="69.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="400" y="127.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="365" y="265.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{F} = q\overline{E}$</div></foreignObject>
</svg>

### Kenttäviivat
Kenttää havainnollistetaan **kenttäviivoilla**. Kenttäviivan suunta kussakin kohdassa on kentän suunta. Nuoli näyttää, mihin suuntaan positiiviseen varaukseen kohdistuva voima osoittaa. Kenttäviivat lähtevät positiivisista varauksista ja päättyvät negatiivisiin varauksiin. Missä viivat ovat tiheässä, kenttä on voimakas. Missä viivat ovat harvassa, kenttä on heikko. Kaksi kenttäviivaa ei koskaan leikkaa toisiaan, koska kentällä on jokaisessa kohdassa vain yksi suunta. Kenttäviiva ei ole varauksen rata. Se näyttää voiman suunnan eikä sitä, mihin suuntaan varaus liikkuu.

Pistevarauksen kenttäviivat ovat säteittäisiä suoria eli lähtevät varauksesta joka suuntaan. Ne harvenevat kauempana varauksesta, koska kenttä heikkenee etäisyyden kasvaessa kuten Coulombin laki kertoo. Kahden erimerkkisen varauksen kenttäviivat kaartuvat positiivisesta varauksesta negatiiviseen.

<svg data-fig="lines" viewBox="0 0 600 340" role="img" aria-label="Kaksi kenttäviivakuvaa vierekkäin, kaavakuva. Vasemmalla on positiivinen pistevaraus. Siitä lähtee tasaisesti joka suuntaan kaksitoista vihreää suoraa kenttäviivaa, ja nuolet osoittavat ulospäin. Viivat harvenevat kauempana varauksesta. Oikealla on positiivinen ja yhtä suuri negatiivinen varaus vierekkäin. Kenttäviivat lähtevät positiivisesta varauksesta ja kaartuvat negatiiviseen varaukseen. Viivat ovat tiheimmillään varausten lähellä ja niiden välissä. Viivat eivät leikkaa toisiaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-lines.webp" x="0" y="0" width="600" height="347.5" preserveAspectRatio="none"/>
  <foreignObject x="95" y="297.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+Q$</div></foreignObject>
  <foreignObject x="345" y="297.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+Q \text{ ja } -Q$</div></foreignObject>
</svg>

### Homogeeninen kenttä levyjen välissä
Kaksi laajaa metallilevyä asetetaan yhdensuuntaisesti vastakkain, ja ne kytketään jännitelähteen napoihin. Silloin toiseen levyyn kertyy positiivista varausta ja toiseen yhtä paljon negatiivista varausta. Levyjen välissä kenttäviivat ovat suoria, yhdensuuntaisia ja tasavälein. Silloin kentän voimakkuus ja suunta ovat samat kaikkialla levyjen välissä. Tällainen kenttä on **homogeeninen** eli sama joka kohdassa. Pieneen varattuun palloon kohdistuu sama voima, olipa pallo lähellä positiivista levyä, lähellä negatiivista levyä tai niiden puolivälissä.

<svg data-fig="plates" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva: kaksi vaakasuoraa yhdensuuntaista metallilevyä. Ylemmässä levyssä on positiivista ja alemmassa negatiivista varausta. Vihreät kenttäviivat kulkevat ylemmästä levystä alempaan. Levyjen välissä viivat ovat suoria, yhdensuuntaisia ja tasavälein, joten kenttä on homogeeninen. Levyjen päissä viivat kaartuvat ulospäin ja harvenevat. Levyjen välissä on kaksi samanlaista positiivista palloa eri kohdissa. Kumpaankin palloon kohdistuu yhtä suuri punainen voimanuoli F alaspäin, kentän suuntaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-plates.webp" x="1.2" y="-1.2" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="62" y="91.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="62" y="223.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="224" y="161.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F}$</span></div></foreignObject>
  <foreignObject x="420" y="201.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F}$</span></div></foreignObject>
  <foreignObject x="540" y="157.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
</svg>

Miksi voima ei kasva, kun pallo siirretään lähemmäs levyä? Lähellä levyä lähimmät varaukset vaikuttavat palloon voimakkaasti. Useimmat levyn varaukset ovat silloin kuitenkin pallon sivuilla. Niiden voimat osoittavat lähes levyn suuntaisesti. Sivuttaiset osat kumoavat toisensa, eivätkä ne vie palloa levyä kohti. Kauempana levystä jokainen varaus vaikuttaa heikommin. Yhä useamman varauksen voima osoittaa kuitenkin lähes kohtisuoraan levyä kohti. Laajalla levyllä nämä kaksi vaikutusta tasapainottavat toisensa. Siksi levyn kenttä ei riipu etäisyydestä levyyn. Levyjen ulkopuolella positiivisen ja negatiivisen levyn kentät ovat vastakkaissuuntaiset ja lähes kumoavat toisensa. Levyjen välissä ne ovat samansuuntaiset ja summautuvat. Kenttä on homogeeninen vain levyjen välissä ja levyjen päistä kaukana. Levyjen päissä kenttäviivat kaartuvat ulospäin ja harvenevat.

### Ilmanpuhdistin
Sähköisessä ilmanpuhdistimessa ilma kulkee ensin varausosan läpi. Siellä pölyhiukkaset saavat sähkövarauksen. Sitten ilma virtaa yhdensuuntaisten levyjen välistä, ja levyjen välillä on usean kilovoltin jännite. Homogeeninen kenttä työntää jokaista varattua hiukkasta kohti levyä samalla voimalla koko matkan. Hiukkanen ajautuu levyn pintaan ja jää siihen, vaikka ilma jatkaa matkaansa. Sama periaate on voimalaitosten sähkösuodattimissa. Ne poistavat savukaasuista lähes kaiken pölyn.

## Kaava: Sähkökentän voimakkuus
Sähkökentän voimakkuus kohdassa, jossa pieneen testivaraukseen $q$ kohdistuu sähköinen voima $\overline{F}$, on
```kaavat
sähkökentän voimakkuus :: \overline{E} = \frac{\overline{F}}{q}
```
missä $\overline{E}$ on sähkökentän voimakkuus ($\text{N/C}$), $\overline{F}$ sähköinen voima ($\text{N}$) ja $q$ testivaraus ($\text{C}$). Kun kenttä tunnetaan, mihin tahansa varaukseen kohdistuva voima saadaan kertomalla: $\overline{F} = q\overline{E}$. Jos $q$ on negatiivinen, voima osoittaa kenttää vastaan.

### Kenttä levyjen jännitteestä
Homogeenisen kentän voimakkuuden voi laskea levyjen välisestä jännitteestä. Positiivinen varaus $q$ siirtyy positiiviselta levyltä negatiiviselle. Siihen kohdistuu koko matkan sama voima $F = qE$. Kenttä tekee silloin työn $W = Fd = qEd$. Luvun *Virtapiiri, sähkövirta ja jännite* mukaan jännite kertoo energian yhtä varausyksikköä kohti. Siksi sama työ on myös $W = qU$. Merkitään nämä yhtä suuriksi. Varaus supistuu eli häviää yhtälöstä, ja homogeenisen kentän voimakkuus on
```kaavat
jännite homogeenisessa sähkökentässä :: E = \frac{U}{d}
```
missä $E$ on sähkökentän voimakkuus ($\text{V/m}$), $U$ levyjen välinen jännite ($\text{V}$) ja $d$ levyjen välinen etäisyys ($\text{m}$). Yksiköt $\text{V/m}$ ja $\text{N/C}$ ovat sama yksikkö, sillä $1\,\text{V/m} = 1\,\tfrac{\text{J}}{\text{C} \cdot \text{m}} = 1\,\tfrac{\text{N} \cdot \text{m}}{\text{C} \cdot \text{m}} = 1\,\text{N/C}$. Esimerkiksi jännite $2{,}0\,\text{kV}$ levyjen välillä $4{,}0\,\text{cm}$ antaa kentän $2000\,\text{V} : 0{,}040\,\text{m} = 5{,}0 \cdot 10^{4}\,\text{V/m}$.

```pysahdy
Levyjen välinen jännite on $600\,\text{V}$ ja etäisyys $3{,}0\,\text{cm}$. Kuinka voimakas kenttä levyjen välissä on?
---
Kentän voimakkuus on $E = U : d$. Kun $d = 0{,}030\,\text{m}$, $E = 600\,\text{V} : 0{,}030\,\text{m}$, joten $E = 2{,}0 \cdot 10^{4}\,\text{V/m}$.
```

<svg data-fig="work" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, ei mittakaavassa: jännitelähde U on kytketty johtimilla kahteen vaakasuoraan levyyn. Plusnapa on ylemmässä ja miinusnapa alemmassa levyssä. Levyjen etäisyys on d. Levyjen välissä vihreät kenttäviivat osoittavat alas. Positiivinen varaus q lähtee ylemmän levyn luota ja kulkee katkoviivaa pitkin alemmalle levylle. Siihen kohdistuu koko matkan sama punainen voima F, joka on q kertaa E ja osoittaa alas. Kun varaus kulkee matkan d, kenttä tekee työn F kertaa d. Se on yhtä suuri kuin q kertaa U." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-work.webp" x="7.4" y="1.2" width="591.1" height="342.4" preserveAspectRatio="none"/>
  <foreignObject x="28" y="155.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="122" y="135.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="122" y="175.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="284" y="105.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$q$</div></foreignObject>
  <foreignObject x="342" y="157.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F} = q\overline{E}$</span></div></foreignObject>
  <foreignObject x="566" y="155.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="210" y="285.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = Fd = qEd = qU$</div></foreignObject>
</svg>

Yhtälö pätee vain homogeenisessa kentässä eli levyjen välissä, kun levyt ovat laajoja niiden väliseen etäisyyteen verrattuna. Kuvaaja näyttää simulaation levymallilla lasketun kentän levyjen puolivälin korkeudella. Levyjen keskeltä noin $7\,\text{cm}$:n päähän kenttä on $U : d = 50\,\text{kV/m}$. Levyjen päissä ja niiden ulkopuolella kenttä heikkenee. Ilmanpuhdistimessa jännite $5{,}0\,\text{kV}$ ja levyjen väli $1{,}0\,\text{cm}$ antavat kentän $5{,}0 \cdot 10^{5}\,\text{V/m}$. Maan pinnalla on selkeällä säällä noin $100\,\text{V/m}$:n kenttä. Ukkospilven alla kenttä voi olla jopa kymmeniä kilovoltteja metriä kohti.

<svg data-fig="profile" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa, laskettu simulaation levymallilla: sähkökentän voimakkuus E kilovoltteina metriä kohti levyjen puolivälin korkeudella kohdan x funktiona, kun jännite on 2,0 kV ja levyjen etäisyys 4,0 cm. Levyjen keskikohta on x = 0 ja levyn pää x = 10 cm. Välillä 0–7 cm kentän voimakkuus on vakio 50 kV/m, joka on U jaettuna d:llä. Lähellä levyn päätä se alkaa pienetä. Levyn päässä se on noin 38 kV/m ja levyjen ulkopuolella 14 cm:n kohdalla enää noin 9 kV/m." style="max-width:100%;font-size:24px">
  <line x1="151.5" y1="280" x2="151.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="207" y1="280" x2="207" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262.5" y1="280" x2="262.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="317.5" y1="280" x2="317.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="373" y1="280" x2="373" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428.5" y1="280" x2="428.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="484" y1="280" x2="484" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="243.5" x2="484" y2="243.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="206.5" x2="484" y2="206.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="170" x2="484" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="133.5" x2="484" y2="133.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="96.5" x2="484" y2="96.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="60" x2="484" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="280" x2="498" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M510,280 L497,286 L497,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="281" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="151.5" y1="280" x2="151.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="141.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="207" y1="280" x2="207" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="197" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="262.5" y1="280" x2="262.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="317.5" y1="280" x2="317.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="307.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="373" y1="280" x2="373" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="356.5" y="289.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="428.5" y1="280" x2="428.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="412" y="289.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="484" y1="280" x2="484" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="467.5" y="289.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$14$</div></foreignObject>
  <line x1="89" y1="243.5" x2="96" y2="243.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="229" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="206.5" x2="96" y2="206.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="192" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="170" x2="96" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="155.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="89" y1="133.5" x2="96" y2="133.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="119" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="96.5" x2="96" y2="96.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="82" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="60" x2="96" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="66" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="516" y="265.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{cm})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{kV/m})$</div></foreignObject>
  <line x1="373" y1="60" x2="373" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="381" y="60" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{levyn pää}$</span></div></foreignObject>
  <line x1="96" y1="96.5" x2="290" y2="96.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="96,96.5 123.5,96.5 151.5,96.5 179,96.5 207,96.5 234.5,96.5 262.5,97 290,97.5 304,98 317.5,100 331.5,103.5 345.5,110.5 359.5,123 373,141 387,162.5 401,183.5 414.5,201.5 428.5,215.5 456.5,235 484,247" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="106.5" y="60" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$E = \tfrac{U}{d}$</span></div></foreignObject>
</svg>

### Varattu hiukkanen homogeenisessa kentässä
Homogeenisessa kentässä varattuun hiukkaseen kohdistuu vakiovoima $F = qE$. Newtonin toisen lain mukaan sen kiihtyvyys $a = qE : m$ on silloin vakio tyhjiössä, kun muut voimat ovat pieniä. Levossa oleva hiukkanen kiihtyy tasaisesti kentän suuntaisesti. Positiivinen hiukkanen kiihtyy kentän suuntaan ja negatiivinen kenttää vastaan. Hiukkanen voi tulla levyjen väliin sivulta. Silloin sen rata kaartuu kohti toista levyä samaan tapaan kuin vaakasuoraan heitetyn pallon rata kaartuu alaspäin. Elektroniin kohdistuu kentässä $5{,}0 \cdot 10^{4}\,\text{V/m}$ voima $8{,}0 \cdot 10^{-15}\,\text{N}$. Elektronin paino on vain $8{,}9 \cdot 10^{-30}\,\text{N}$. Elektronin painovoima voidaan siksi jättää huomiotta. Raskaammille kappaleille, kuten öljypisaroille ja pölyhiukkasille, painovoima voi olla yhtä tärkeä kuin sähköinen voima.

```pysahdy
Hiukkasen varaus kaksinkertaistuu, mutta massa ja kenttä pysyvät samoina. Miten kiihtyvyys muuttuu?
---
Se kaksinkertaistuu. Kiihtyvyys $a = qE : m$ on suoraan verrannollinen varaukseen $q$.
```

<svg data-fig="electron" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, ei mittakaavassa: kaksi vaakasuoraa levyä, ylempi positiivinen ja alempi negatiivinen. Vihreät kenttäviivat osoittavat alas. Elektroni tulee vasemmalta levyjen väliin vaakasuorassa, ja sen sininen nopeusnuoli v osoittaa oikealle. Levyjen välissä elektronin rata kaartuu tasaisesti ylöspäin kohti positiivista levyä. Radan kohdassa on punainen voimanuoli F ja oranssi kiihtyvyysnuoli a. Molemmat osoittavat ylös, kenttää vastaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-electron.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="556" y="121.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="90" y="207.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="262" y="121.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F}$</span></div></foreignObject>
  <foreignObject x="340" y="127.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{a}$</span></div></foreignObject>
  <foreignObject x="40" y="215.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-e$</div></foreignObject>
</svg>

## Esimerkki
Pieni öljypisara, jonka massa on $4{,}9 \cdot 10^{-15}\,\text{kg}$, leijuu paikallaan kahden vaakasuoran levyn välissä. Levyjen etäisyys on $6{,}0\,\text{mm}$, jännite on $600\,\text{V}$, ja positiivinen levy on ylempänä. Kuinka suuri on pisaran varaus, ja kuinka monta alkeisvarausta $e = 1{,}602 \cdot 10^{-19}\,\text{C}$ se on?

<!-- vaihe -->

**Tunnetut ja kysytty.** Massa $m = 4{,}9 \cdot 10^{-15}\,\text{kg}$, levyjen etäisyys $d = 6{,}0\,\text{mm}$, jännite $U = 600\,\text{V}$, putoamiskiihtyvyys $g = 9{,}81\,\text{m/s}^2$ ja alkeisvaraus $e$.

Kysytään pisaran varauksen suuruutta $q$ ja alkeisvarausten lukumäärää $n$.

<!-- vaihe -->

**Periaate.** Levyjen välinen kenttä on homogeeninen, joten $E = U : d$. Pisara on levossa. Newtonin ensimmäisen lain mukaan siihen kohdistuvat voimat silloin kumoavat toisensa. Paino $mg$ osoittaa alas, joten sähköisen voiman $qE$ täytyy osoittaa ylös, kohti positiivista levyä. Pisara on siis negatiivinen. Varaus on alkeisvarauksen monikerta, joten lukumäärä saadaan jakamalla.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&E = \frac{U}{d} \\
&qE = mg \\
&q = \frac{mg}{E} \\
&n = \frac{q}{e}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** $d = 6{,}0\,\text{mm} = 6{,}0 \cdot 0{,}001\,\text{m} = 6{,}0 \cdot 10^{-3}\,\text{m}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
E &= \frac{U}{d} \\
&= \frac{600\,\text{V}}{6{,}0 \cdot 10^{-3}\,\text{m}} \\
&= 1{,}0 \cdot 10^{5}\,\text{V/m} \\
mg &= 4{,}9 \cdot 10^{-15}\,\text{kg} \\
&\quad \cdot 9{,}81\,\text{m/s}^2 \\
&= 4{,}807 \cdot 10^{-14}\,\text{N} \\
q &= \frac{mg}{E} \\
&= \frac{4{,}807 \cdot 10^{-14}\,\text{N}}{1{,}0 \cdot 10^{5}\,\text{V/m}} \\
&= 4{,}807 \cdot 10^{-19}\,\text{C} \\
n &= \frac{q}{e} \\
&= \frac{4{,}807 \cdot 10^{-19}\,\text{C}}{1{,}602 \cdot 10^{-19}\,\text{C}} \\
&= 3{,}0
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Pisaran varaus on $-4{,}8 \cdot 10^{-19}\,\text{C}$ eli kolme alkeisvarausta. Pisarassa on kolme ylimääräistä elektronia. Varaus ilmoitetaan kahdella merkitsevällä numerolla kuten massa ja etäisyys.

<!-- vaihe -->

**Järkevyys.** Kolmen alkeisvarauksen sähköinen voima kentässä $1{,}0 \cdot 10^{5}\,\text{V/m}$ on $3 \cdot 1{,}602 \cdot 10^{-19}\,\text{C} \cdot 1{,}0 \cdot 10^{5}\,\text{V/m} = 4{,}8 \cdot 10^{-14}\,\text{N}$. Se on yhtä suuri kuin pisaran paino $4{,}9 \cdot 10^{-15}\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 = 4{,}8 \cdot 10^{-14}\,\text{N}$. Lukumäärä on lähes tarkalleen kokonaisluku, kuten pitääkin, koska varaus koostuu alkeisvarauksista.

## Yleinen virhekäsitys
Moni ajattelee, että levyjen välissä varattuun palloon kohdistuva voima kasvaa, kun pallo siirretään lähemmäs levyä. Ajatus tulee Coulombin laista, jonka mukaan voima kasvaa etäisyyden pienentyessä. Coulombin laki koskee kuitenkin pistevarauksia. Laajojen levyjen kenttä on homogeeninen. Levyjen välissä voima on sama kaikkialla, eikä se riipu siitä, kuinka lähellä levyä pallo on. Voimakkuus riippuu vain levyjen jännitteestä ja etäisyydestä: $E = U : d$.

Toinen virhekäsitys on, että kenttäviiva on varauksen kulkema rata. Joku ajattelee myös, että kenttää on vain viivojen kohdalla. Kenttäviiva näyttää voiman suunnan kussakin kohdassa, ja kenttää on myös viivojen välissä. Kolmas virhe on luulla, että sähkökentän voimakkuus riippuu testivarauksesta. Suurempi varaus saa suuremman voiman, mutta voiman ja varauksen osamäärä $E = F : q$ on sama.

## Tiivistelmä
- Varaus muuttaa ympäröivää tilaa: sähkökenttä vaikuttaa jokaiseen siellä olevaan varaukseen sähköisellä voimalla.
- Sähkökentän voimakkuus on testivaraukseen kohdistuva voima jaettuna varauksella, $\overline{E} = \overline{F} : q$. Yksikkö on $\text{N/C} = \text{V/m}$. Varaukseen kohdistuva voima on $\overline{F} = q\overline{E}$: positiiviseen kentän suuntaan, negatiiviseen kenttää vastaan.
- Kenttäviivat lähtevät positiivisista ja päättyvät negatiivisiin varauksiin. Ne eivät leikkaa toisiaan, ja niiden tiheys kertoo kentän voimakkuuden.
- Yhdensuuntaisten levyjen välissä kenttä on homogeeninen: sama voimakkuus ja suunta kaikkialla levyjen välissä, kun levyjen päistä ollaan kaukana.
- Homogeenisen kentän voimakkuus on $E = U : d$. Varattuun hiukkaseen kohdistuu siinä vakiovoima, joten sen kiihtyvyys on vakio tyhjiössä, kun muut voimat ovat pieniä.
