# Säteilyannos ja säteilyturvallisuus Suomessa

> **Miksi** ydinvoimalaitokset antavat suomalaiselle vain hyvin pienen osan hänen säteilyannoksestaan, ja mistä loput tulevat?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvinen suomalainen maisema. Punainen omakotitalo on piirretty poikkileikkauksena. Katolla on lunta, ja savupiipusta nousee savua. Talon alla on kellari. Maan alla on hiekkaa, ja syvemmällä on harmaa graniittikallio. Taivaalla lentää matkustajakone. Kaukana metsän takana näkyy ydinvoimalaitoksen reaktorirakennus." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-13-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Annos mittaa kudokseen jäänyttä energiaa
Ionisoiva säteily vahingoittaa soluja, koska se irrottaa elektroneja atomeista ja molekyyleistä ja luovuttaa niille energiaansa (luku *Ionisoiva säteily ja elimistö*). Säteilyn haittaa arvioidaan siksi sen mukaan, kuinka paljon energiaa kudokseen jää. **Absorboitunut annos** $D$ on säteilyenergia, jonka kudos tai muu aine imee itseensä eli absorboi, jaettuna sen massalla. Sen yksikkö on gray: $1\,\text{Gy} = 1\,\tfrac{\text{J}}{\text{kg}}$. Energia jaetaan massalla, koska sama energia vaurioittaa jokaista solua enemmän, jos se keskittyy pieneen kudosmäärään. Jos energia leviää suureen kudosmäärään, jokainen solu saa vähemmän.

Energiat ovat lämmön mittakaavassa pieniä. Annos $1\,\text{Gy}$ lämmittäisi vettä vain noin $0{,}0002\,\text{K}$. Silti saman annoksen saaminen kerralla koko keholle aiheuttaa jo säteilysairauden. Haitta ei siis johdu lämpenemisestä. Energia tulee suurina paloina, jotka rikkovat yksittäisiä molekyylejä, kuten DNA:ta.

```pysahdy
Kaksi kudospalaa saa saman säteilyenergian. Toisen massa on kaksinkertainen. Kumpi saa suuremman absorboituneen annoksen?
---
Kevyempi, ja annos on kaksinkertainen. Annos on energia jaettuna massalla. Kevyemmän palan jokainen kilogramma saa siis kaksinkertaisen energian.
```

### Sama energia, eri haitta: painotetut annokset
Alfahiukkanen jättää lyhyelle matkalle tiheän ionisaatiojäljen. Gammafotoni sen sijaan ionisoi harvakseltaan pitkällä matkalla. Siksi sama absorboitunut annos alfasäteilystä vaurioittaa solujen DNA:ta enemmän kuin gammasäteilystä. Myös kudokset ovat erilaisia: punainen luuydin ja keuhkot ovat herkempiä säteilyn aiheuttamalle syövälle kuin iho. Säteilysuojelussa nämä erot otetaan huomioon painotuskertoimilla. Painotetun annoksen yksikkö on sievert $\text{Sv}$. Koko kehon **efektiivisen annoksen** avulla arvioidaan pienten annosten aiheuttamaa syöpäriskiä pitkällä aikavälillä. Se kuvaa keskimääräisen ihmisen riskiä, ei kenenkään oman riskin tarkkaa suuruutta. Sen avulla voidaan verrata hyvin erilaisia altistuksia, kuten radonia, röntgenkuvausta ja lentomatkaa.

<figure class="unit-photo"><img src="pics/fy8/radiacode-dosimeter.webp" alt="Musta säteilymittari vihreällä pohjalla. Näytöllä on lukema."><figcaption>Pieni säteilymittari. Näytöllä on pulssien määrä sekunnissa: $4{,}45$. Taustasäteily antaa mittariin pulsseja koko ajan, vaikka lähellä ei ole säteilylähdettä.</figcaption></figure>

### Mistä suomalaisen säteilyannos tulee
Säteilyturvakeskuksen (STUK) arvion mukaan suomalainen saa keskimäärin noin $5{,}9\,\text{mSv}$ efektiivisen annoksen vuodessa. Suurin osa tulee luonnosta: noin $5{,}1\,\text{mSv}$ eli noin $85\,\%$. Ydinvoimalaitosten, Tšernobylin laskeuman ja ydinasekokeiden yhteinen osuus on alle $0{,}1\,\text{mSv}$. Taulukossa ja sen alla olevassa pylväskuviossa ovat samat luvut.

| Lähde | Annos vuodessa |
| --- | --- |
| sisäilman radon | noin $4\,\text{mSv}$ |
| muu luonnon säteily | noin $1{,}1\,\text{mSv}$ |
| terveydenhuolto | noin $0{,}8\,\text{mSv}$ |
| ydinvoima, laskeuma ja muut | $< 0{,}1\,\text{mSv}$ |
| yhteensä | noin $5{,}9\,\text{mSv}$ |

Lähde: STUK-A263 (2020), arvio vuoden 2018 tilanteesta, pyöristetty. Terveydenhuollon osuus on raportissa $0{,}76\,\text{mSv}$. Se tulee röntgen- ja isotooppitutkimuksista. Muu luonnon säteily koostuu maaperän ja rakennusmateriaalien gammasäteilystä, avaruudesta tulevasta säteilystä ja kehon omista radioaktiivisista aineista, kuten kalium-40:stä. Luvut ovat keskiarvoja. Yksittäisen ihmisen annos riippuu ennen kaikkea kodin radonpitoisuudesta, ja se voi olla moninkertainen.

<svg data-fig="lahteet" viewBox="0 0 600 360" role="img" aria-label="Vaakapylväskuvio mittakaavassa: suomalaisen keskimääräinen efektiivinen annos vuodessa eri lähteistä. Luvut ovat STUKin arvio vuoden 2018 tilanteesta, ja yhteensä annos on noin 5,9 millisievertiä. Sisäilman radon antaa noin 4 millisievertiä. Muu luonnon säteily eli maaperä, rakennukset, avaruus ja elimistön omat aineet antavat yhteensä noin 1,1 millisievertiä. Terveydenhuolto antaa noin 0,8 millisievertiä vuodessa. Radonin pylväs on selvästi pisin: se on yli kolme kertaa niin pitkä kuin seuraava pylväs." style="max-width:100%;font-size:24px">
  <line x1="325.5" y1="34" x2="325.5" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="325.5" y1="286" x2="325.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="315.5" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="389" y1="34" x2="389" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="389" y1="286" x2="389" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="379" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="452.5" y1="34" x2="452.5" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="452.5" y1="286" x2="452.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="442.5" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="516" y1="34" x2="516" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="516" y1="286" x2="516" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="506" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="232" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <rect x="262" y="56" width="254" height="36" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="67" y="59.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{sisäilman radon}$</div></foreignObject>
  <foreignObject x="526" y="59.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4{,}0$</div></foreignObject>
  <rect x="262" y="132" width="70" height="36" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="30" y="135.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{muu luonnon säteily}$</div></foreignObject>
  <foreignObject x="342" y="135.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1{,}1$</div></foreignObject>
  <rect x="262" y="208" width="51" height="36" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="55" y="211.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{terveydenhuolto}$</div></foreignObject>
  <foreignObject x="323" y="211.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0{,}8$</div></foreignObject>
  <line x1="262" y1="287" x2="562" y2="287" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M574,287 L561,293 L561,281 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="262" y1="287" x2="262" y2="32" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="213" y="325.5" width="174" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$H_\text{E}\ (\text{mSv/vuosi})$</div></foreignObject>
</svg>

**Taustasäteily** on säteilyä, joka tulee luonnon säteilylähteistä jatkuvasti ympäristössämme. Lähteitä ovat maaperän ja kallion radioaktiiviset aineet, avaruudesta tuleva säteily ja ilman radon. Ulkona Suomessa ulkoisen taustasäteilyn annosnopeus on tavallisesti $0{,}05$–$0{,}30\,\mu\text{Sv/h}$. STUKin valvontaverkko mittaa sitä jatkuvasti eri puolilla maata. Lentokoneessa annosnopeus on moninkertainen: tyypillisellä kaukolennolla se on noin $3\,\mu\text{Sv/h}$. Ilmakehä suojaa avaruuden säteilyltä sitä vähemmän, mitä korkeammalla ollaan.

### Radon: näkymätön kaasu kallioperästä
**Radon** on radioaktiivinen jalokaasu. Sen yleisin isotooppi radon-222 syntyy radiumista maaperän ja kallion uraani-238:n hajoamissarjassa. Sen puoliintumisaika on $3{,}82\,\text{d}$ (luku *Hajoamislaki ja puoliintumisaika*). Suomen graniittisessa kallioperässä on paljon uraania, ja harjujen sora päästää maaperän ilmaa hyvin läpi. Talvella lämmin sisäilma nousee ylös ja vuotaa ulos talon yläosista. Silloin talon alaosaan syntyy alipaine eli ulkoilmaa pienempi paine. Alipaine imee radonpitoista maaperän ilmaa sisään perustusten raoista ja halkeamista.

Suurin osa radonista hengitetään ulos. Radonin lyhytikäiset hajoamistuotteet ovat kuitenkin kiinteitä aineita: ne ovat poloniumin, lyijyn ja vismutin isotooppeja. Ne tarttuvat ilman pölyhiukkasiin ja jäävät hengitysteiden pinnalle. Siellä polonium-218 ja polonium-214 lähettävät alfasäteilyä suoraan keuhkojen soluihin. Tupakoinnin jälkeen radon on merkittävin keuhkosyövän aiheuttaja. STUKin mukaan se aiheuttaa Suomessa noin 300 keuhkosyöpää vuodessa.

Radonpitoisuus ilmoitetaan becquereleinä kuutiometrissä. Yksikkö $1\,\tfrac{\text{Bq}}{\text{m}^3}$ tarkoittaa yhtä hajoamista sekunnissa yhdessä kuutiometrissä ilmaa. Suomalaisten asuntojen keskimääräinen pitoisuus on STUKin valtakunnallisten otantatutkimusten mukaan noin $94\,\tfrac{\text{Bq}}{\text{m}^3}$. Asuntojen viitearvo eli enimmäisarvo, jonka alle pitoisuuden tulisi jäädä, on $300\,\tfrac{\text{Bq}}{\text{m}^3}$. Uusissa rakennuksissa se on $200\,\tfrac{\text{Bq}}{\text{m}^3}$ (sosiaali- ja terveysministeriön asetus 1044/2018). Pitoisuus mitataan radonmittauspurkilla, joka on asunnossa kaksi kuukautta lämmityskaudella. Pitoisuutta voi pienentää kolmella tavalla: tehostamalla ilmanvaihtoa, tiivistämällä perustusten rakoja tai imemällä radonpitoista ilmaa pois talon alta radonimurilla tai radonkaivolla.

<figure class="unit-photo"><img src="pics/fy8/dosimeter-japan.webp" alt="Ulkona on laite, jossa on punaiset numerot ja japaninkielistä tekstiä."><figcaption>Säteilymittari ulkona Japanissa. Näytössä on annosnopeus. Se kertoo, kuinka paljon säteilyä alueella saa tunnissa. Mitä kauemmin alueella on, sitä suuremman annoksen saa.</figcaption></figure>

```pysahdy
Radon-222:n puoliintumisaika on $3{,}82\,\text{d}$. Yksi sisäänhengitys on keuhkoissa noin $5\,\text{s}$. Arvioi suuruusluokka sille osuudelle radonatomeista, jotka hajoavat yhden hengityksen aikana. Mitä tämä kertoo keuhkojen annoksen lähteestä?
---
$3{,}82\,\text{d} \approx 3{,}3 \cdot 10^{5}\,\text{s}$, joten osuus on suuruusluokkaa $\tfrac{5\,\text{s}}{3{,}3 \cdot 10^{5}\,\text{s}} \approx 10^{-5}$. Lähes kaikki radon hengitetään ulos hajoamatta, joten keuhkojen annos tulee pääosin hengitysteihin jäävistä kiinteistä hajoamistuotteista.
```

### Suojautuminen: aika, etäisyys ja suoja
Ulkoiselta säteilylähteeltä suojaudutaan kolmella tavalla. **Aika:** annos kasvaa suoraan verrannollisesti oleskeluaikaan. Siksi säteilylähteen lähellä tehdään vain välttämätön ja tehdään se nopeasti. **Etäisyys:** pistemäisestä lähteestä säteily leviää kaikkiin suuntiin yhä suuremmalle pinta-alalle. Siksi annosnopeus pienenee nopeasti, kun etäisyys kasvaa. **Suoja:** lähteen ja ihmisen välissä oleva aine absorboi säteilyä. Alfasäteilyn pysäyttää paperi tai ihon kuollut pintakerros. Beetasäteilyn pysäyttää muutaman millimetrin paksuinen muovi- tai alumiinilevy. Gammasäteilyä vaimentavat parhaiten tiheät aineet, kuten lyijy ja betoni. Mikään kerros ei kuitenkaan pysäytä gammasäteilyä kokonaan.

Sisäisiltä säteilylähteiltä suojaudutaan toisin. Sisäisiä lähteitä ovat esimerkiksi radonin hajoamistuotteet ja ravinnon radioaktiiviset aineet. Niiltä suojaudutaan estämällä aineiden pääsy elimistöön. Radon poistetaan sisäilmasta. Ruoaksi ei käytetä suuria määriä esimerkiksi sieniä, jotka keräävät paljon cesium-137:ää.

Annosrajat rajoittavat säteilyn käyttöä. Säteilytyötä tekevän efektiivinen annos saa olla enintään $20\,\text{mSv}$ vuodessa. Väestön annos säteilyn käytöstä saa olla enintään $1\,\text{mSv}$ vuodessa (säteilylaki 859/2018). Väestön raja ei koske luonnon säteilyä eikä potilaan omia lääketieteellisiä tutkimuksia. Niiden hyöty arvioidaan erikseen.

## Kaava: Absorboitunut ja efektiivinen annos

### Absorboitunut annos
Kudoksen massa on $m$, ja se absorboi säteilystä energian $E$. Silloin absorboitunut annos on
```latex
D = \frac{E}{m}
```
missä $D$ on absorboitunut annos ($\text{Gy}$), $E$ absorboitunut energia ($\text{J}$) ja $m$ kudoksen massa ($\text{kg}$). Absorboitunut annos on fysikaalinen suure: se ei kerro, millaista säteily oli.

### Ekvivalenttiannos ja säteilyn painotuskerroin
Elimen tai kudoksen $\text{T}$ ekvivalenttiannos ottaa huomioon säteilylajin:
```kaavat
ekvivalenttiannos :: H_\text{T} = w_\text{R} D_\text{T}
```
missä $H_\text{T}$ on kudoksen ekvivalenttiannos ($\text{Sv}$), $w_\text{R}$ säteilyn painotuskerroin (paljas luku eli luku ilman yksikköä) ja $D_\text{T}$ kudoksen absorboitunut annos ($\text{Gy}$). Painotuskerroin on säteilysuojelussa sovittu pyöristetty arvo. Se kuvaa, kuinka paljon haitallisempi säteilylaji on gammasäteilyyn verrattuna, kun absorboitunut annos on sama. Se ei kuitenkaan ole tarkka mitattu vaurioiden suhde jokaisessa solussa. Neutronien kerroin riippuu niiden energiasta.

| Säteilylaji | $w_\text{R}$ |
| --- | --- |
| gamma- ja röntgensäteily | $1$ |
| beetasäteily (elektronit) | $1$ |
| alfasäteily | $20$ |
| neutronit | $2{,}5$–$20$ |

<svg data-fig="painotus" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa: kaksi samanlaista kudospalaa. Vasempaan tulee gammasäteilyä. Aaltoviiva kulkee palan läpi, ja sen varrella on harvassa muutama ionisaatiokohta. Oikeaan osuu alfahiukkanen. Sen lyhyt paksu jälki pysähtyy palan sisään, ja jäljen varrella ionisaatiokohtia on tiheässä. Molemmissa absorboitunut annos on D = 1 milligray. Gammasäteilyn painotuskerroin on 1, joten ekvivalenttiannos on 1 millisievert. Alfasäteilyn painotuskerroin on 20, joten ekvivalenttiannos on 20 millisievertiä." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-13-painotus.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="76" y="11.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gammasäteily}$</div></foreignObject>
  <foreignObject x="107.5" y="207.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$D = 1\,\text{mGy}$</div></foreignObject>
  <foreignObject x="126" y="247.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$w_\text{R} = 1$</div></foreignObject>
  <foreignObject x="101" y="315.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$H_\text{T} = 1\,\text{mSv}$</div></foreignObject>
  <foreignObject x="372.5" y="11.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alfasäteily}$</div></foreignObject>
  <foreignObject x="397.5" y="207.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$D = 1\,\text{mGy}$</div></foreignObject>
  <foreignObject x="410" y="247.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$w_\text{R} = 20$</div></foreignObject>
  <foreignObject x="385" y="315.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$H_\text{T} = 20\,\text{mSv}$</div></foreignObject>
</svg>

### Efektiivinen annos ja kudoksen painotuskerroin
Joskus säteilytetään vain osa kehosta. Silloin kunkin kudoksen ekvivalenttiannos kerrotaan kudoksen painotuskertoimella $w_\text{T}$, joka kuvaa kudoksen herkkyyttä. Tulot lasketaan yhteen:
```latex
H_\text{E} = w_{\text{T}1} H_{\text{T}1} + w_{\text{T}2} H_{\text{T}2} + \ldots
```
missä $H_\text{E}$ on efektiivinen annos ($\text{Sv}$) ja $w_{\text{T}1}, w_{\text{T}2}, \ldots$ säteilytettyjen kudosten painotuskertoimet. Efektiivisen annoksen kansainvälinen tunnus on $E$. Tässä luvussa käytetään tunnusta $H_\text{E}$, jottei sitä sekoiteta energiaan $E$.

Kudosten painotuskertoimet ovat:

- $0{,}12$ kukin: punainen luuydin, paksusuoli, keuhkot, mahalaukku ja rinnat sekä muut kudokset yhteensä
- $0{,}08$: sukurauhaset
- $0{,}04$ kukin: virtsarakko, ruokatorvi, maksa ja kilpirauhanen
- $0{,}01$ kukin: luun pinta, aivot, sylkirauhaset ja iho

Painotuskertoimet ovat Kansainvälisen säteilysuojelutoimikunnan ICRP:n suosituksesta vuodelta 2007. Ne ovat myös Suomen säteilylainsäädännön perusta. Kudosten kertoimien summa on $1$. Kun koko keho saa saman ekvivalenttiannoksen, efektiivinen annos on siis yhtä suuri kuin se. Efektiivinen annos on säteilysuojelun suure. Se on laskettu sovitulle keskimääräiselle ihmiselle, ja se on tarkoitettu pienille annoksille. Sillä verrataan altistuksia ja valvotaan annosrajoja. Se ei ole yksittäisen ihmisen tarkka riskiarvio, eikä sillä suunnitella sädehoitoa. Suurten kerta-annosten välittömiä vaikutuksia, kuten säteilysairautta, arvioidaan absorboituneella annoksella grayna.

### Annosnopeus ja aika
Säteilymittari näyttää yleensä **annosnopeuden** $\dot{H}$. Se on annos aikayksikössä, esimerkiksi yksikössä $\mu\text{Sv/h}$. Kun annosnopeus pysyy vakiona, ajassa $t$ kertyy annos
```latex
H = \dot{H} t
```
missä $H$ on annos ($\text{Sv}$), $\dot{H}$ annosnopeus ($\tfrac{\text{Sv}}{\text{h}}$) ja $t$ oleskeluaika ($\text{h}$). Kun oleskeluaika puolittuu, myös annos puolittuu.

### Etäisyyden neliölaki
Pistemäisestä lähteestä lähtee säteilyä kaikkiin suuntiin. Etäisyydellä $r$ säteily jakautuu pallon pinnalle, jonka ala on $4\pi r^2$. Kun etäisyys kaksinkertaistuu, sama säteily jakautuu nelinkertaiselle alalle. Mittarin ikkunaan osuu silloin neljäsosa entisestä. Etäisyyksillä $r_1$ ja $r_2$ annosnopeuksien yhteys on
```latex
\dot{H}_2 = \dot{H}_1 \left(\frac{r_1}{r_2}\right)^2
```
missä $\dot{H}_1$ on annosnopeus etäisyydellä $r_1$ ja $\dot{H}_2$ etäisyydellä $r_2$. Laki pätee, kun lähde on pieni etäisyyteen verrattuna ja ilma vaimentaa säteilyä vain vähän. Näin on esimerkiksi gammasäteilylle muutaman metrin matkalla.

<svg data-fig="etaisyys" viewBox="0 0 600 384" role="img" aria-label="Kaavakuva etäisyyden neliölaista. Vasemmalla on pieni säteilylähde. Siitä leviää neljä sädettä oikealle. Etäisyydellä r säteet kulkevat yhden ruudun läpi. Etäisyydellä 2 r sama säteily jakautuu 2 kertaa 2 eli neljälle samankokoiselle ruudulle. Etäisyydellä 3 r se jakautuu 3 kertaa 3 eli yhdeksälle ruudulle. Yhden ruudun läpi kulkee siis etäisyydellä 2 r neljäsosa säteilystä ja etäisyydellä 3 r yhdeksäsosa. Suhteellinen annosnopeus on näillä etäisyyksillä 1, neljäsosa ja yhdeksäsosa." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-13-etaisyys.webp" x="1.2" y="2.5" width="597" height="388.1" preserveAspectRatio="none"/>
  <foreignObject x="162" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="162" y="329.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$1$</div></foreignObject>
  <foreignObject x="285.5" y="271.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2r$</div></foreignObject>
  <foreignObject x="292" y="315" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\dfrac{1}{4}$</div></foreignObject>
  <foreignObject x="415.5" y="271.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3r$</div></foreignObject>
  <foreignObject x="422" y="315" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\dfrac{1}{9}$</div></foreignObject>
  <foreignObject x="65.5" y="317.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\dot{H}$</div></foreignObject>
  <foreignObject x="3" y="349.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{suhteellinen}$</div></foreignObject>
  <foreignObject x="32" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="11" y="199.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lähde}$</div></foreignObject>
</svg>

```pysahdy
Pienen gammalähteen annosnopeus on $8\,\mu\text{Sv/h}$ etäisyydellä $1\,\text{m}$. Mikä se on etäisyydellä $4\,\text{m}$?
---
Etäisyys on nelinkertainen, joten annosnopeus on $\left(\tfrac{1}{4}\right)^2 = \tfrac{1}{16}$ entisestä. Siis $8\,\mu\text{Sv/h} \cdot \tfrac{1}{16} = 0{,}5\,\mu\text{Sv/h}$.
```

### Puoliintumispaksuus
Gammasäteilyn fotonit eivät pysähdy suojassa tietylle syvyydelle. Jokainen fotoni absorboituu tai siroaa satunnaisesti. Siksi jokainen samanpaksuinen kerros vaimentaa saman osuuden siihen tulevasta säteilystä. Se on samanlaista kuin puoliintumisajassa: jokainen puoliintumisaika puolittaa ytimien määrän. **Puoliintumispaksuus** $d_{1/2}$ on aineen paksuus, joka puolittaa annosnopeuden (luku *Ionisoiva säteily ja elimistö*). Kun suojan paksuus on $d$, annosnopeus on
```latex
\dot{H} = \dot{H}_0 \left(\frac{1}{2}\right)^{d/d_{1/2}}
```
missä $\dot{H}_0$ on annosnopeus ilman suojaa ja $\dot{H}$ suojan takana. Puoliintumispaksuus riippuu aineesta ja gammasäteilyn energiasta. Cesium-137:n gammasäteilylle se on lyijyssä noin $5{,}5\,\text{mm}$ ja betonissa noin $4\,\text{cm}$. Tämän luvun mallissa lyijyn puoliintumispaksuus on pyöristetty arvoon $6{,}0\,\text{mm}$. Kaava on yksinkertaistettu malli. Todellisessa suojassa osa sironneista fotoneista pääsee silti läpi, joten suoja mitoitetaan varmuusvaralla.

<svg data-fig="suoja" viewBox="0 0 600 380" role="img" aria-label="Kuvaaja mittakaavassa: annosnopeus mikrosieverteinä tunnissa lyijylevyn paksuuden funktiona. Paksuus on nollasta 30 millimetriin. Ilman lyijyä annosnopeus on 40. Jokainen 6 millimetrin kerros puolittaa sen. Kohdassa 6 millimetriä arvo on 20, kohdassa 12 millimetriä 10 ja kohdassa 18 millimetriä 5. Käyrä laskee yhä loivemmin eikä saavuta nollaa. Puoliintumispaksuus on merkitty vaakasuoralla hakasulkeella ensimmäisen kerroksen kohdalle." style="max-width:100%;font-size:24px">
  <line x1="177" y1="312" x2="177" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="253.5" y1="312" x2="253.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330.5" y1="312" x2="330.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="407" y1="312" x2="407" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="484" y1="312" x2="484" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="254.5" x2="484" y2="254.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="196.5" x2="484" y2="196.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="139" x2="484" y2="139" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="81" x2="484" y2="81" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="312" x2="498" y2="312" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M510,312 L497,318 L497,306 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="313" x2="100" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,32 L106,45 L94,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="177" y1="312" x2="177" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="167" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="253.5" y1="312" x2="253.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="237" y="321.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="330.5" y1="312" x2="330.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="314" y="321.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$18$</div></foreignObject>
  <line x1="407" y1="312" x2="407" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="390.5" y="321.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$24$</div></foreignObject>
  <line x1="484" y1="312" x2="484" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="467.5" y="321.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="93" y1="254.5" x2="100" y2="254.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="240" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="93" y1="196.5" x2="100" y2="196.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="182" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="93" y1="139" x2="100" y2="139" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="124.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="93" y1="81" x2="100" y2="81" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="66.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="516" y="297.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d\ (\text{mm})$</div></foreignObject>
  <foreignObject x="90" y="1.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\dot{H}\ (\mu\text{Sv/h})$</div></foreignObject>
  <polyline points="100,81 103,87.5 106.5,94 109.5,100.5 113,106.5 116,112 119,118 122.5,123.5 125.5,128.5 129,134 132,139 135,144 138.5,148.5 141.5,153.5 145,158 148,162.5 151,166.5 154.5,170.5 157.5,174.5 161,178.5 164,182.5 167,186 170.5,189.5 173.5,193 177,196.5 180,200 183,203 186.5,206 189.5,209 193,212 196,215 199,217.5 202.5,220.5 205.5,223 209,225.5 212,228 215,230.5 218.5,232.5 221.5,235 225,237 228,239.5 231,241.5 234.5,243.5 237.5,245.5 241,247 244,249 247,251 250.5,252.5 253.5,254.5 257,256 260,257.5 263,259 266.5,260.5 269.5,262 273,263.5 276,265 279,266 282.5,267.5 285.5,269 289,270 292,271 295,272.5 298.5,273.5 301.5,274.5 305,275.5 308,276.5 311,277.5 314.5,278.5 317.5,279.5 321,280.5 324,281.5 327,282.5 330.5,283 333.5,284 337,285 340,285.5 343,286.5 346.5,287 349.5,287.5 353,288.5 356,289 359,289.5 362.5,290.5 365.5,291 369,291.5 372,292 375,292.5 378.5,293.5 381.5,294 385,294.5 388,295 391,295.5 394.5,296 397.5,296.5 401,296.5 404,297 407,297.5 410.5,298 413.5,298.5 417,299 420,299 423,299.5 426.5,300 429.5,300 433,300.5 436,301 439,301 442.5,301.5 445.5,302 449,302 452,302.5 455,302.5 458.5,303 461.5,303 465,303.5 468,303.5 471,304 474.5,304 477.5,304.5 481,304.5 484,305" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="177" y1="196.5" x2="177" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="196.5" x2="177" y2="196.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="177" cy="196.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="253.5" y1="254.5" x2="253.5" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="254.5" x2="253.5" y2="254.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="253.5" cy="254.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="330.5" y1="283" x2="330.5" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="283" x2="330.5" y2="283" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="330.5" cy="283" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="100" cy="81" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="100" y1="61" x2="177" y2="61" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="100" y1="61" x2="100" y2="69" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="177" y1="61" x2="177" y2="69" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="189" y="46.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$d_{1/2} = 6{,}0\,\text{mm}$</span></div></foreignObject>
  <foreignObject x="279" y="159" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\dot{H} = \dot{H}_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$</span></div></foreignObject>
</svg>

## Esimerkki
Asunnon sisäilman radonin hajoamistuotteet lähettävät alfasäteilyä keuhkoihin. Oletetaan yksinkertaisesti, että säteily jakautuu tasaisesti koko keuhkoihin. Keuhkojen massa on $1{,}2\,\text{kg}$, ja ne absorboivat vuoden aikana alfasäteilystä energiaa $2{,}0\,\text{mJ}$. Keuhkojen kudoksen painotuskerroin on $0{,}12$. Kuinka suuri efektiivinen annos tästä aiheutuu?

<!-- vaihe -->

**Tunnetut ja kysytty.** Absorboitunut energia on $E = 2{,}0\,\text{mJ}$, keuhkojen massa $m = 1{,}2\,\text{kg}$, alfasäteilyn painotuskerroin $w_\text{R} = 20$ ja keuhkojen painotuskerroin $w_\text{T} = 0{,}12$.

Kysytään efektiivistä annosta $H_\text{E}$.

<!-- vaihe -->

**Periaate.** Absorboitunut annos on energia massaa kohti. Alfasäteily vaurioittaa soluja samalla annoksella moninkertaisesti gammasäteilyyn verrattuna. Siksi keuhkojen ekvivalenttiannos saadaan kertoimella $w_\text{R}$. Vain keuhkot säteilytetään. Efektiivinen annos on siis keuhkojen ekvivalenttiannos kerrottuna keuhkojen painotuskertoimella $w_\text{T}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Yhtälöt $D = \tfrac{E}{m}$, $H_\text{T} = w_\text{R} D$ ja $H_\text{E} = w_\text{T} H_\text{T}$ yhdistetään:
```latex
H_\text{E} = w_\text{T} w_\text{R} \frac{E}{m}
```

<!-- vaihe -->

**Yksikkömuunnokset.** $E = 2{,}0\,\text{mJ} = 2{,}0 \cdot 0{,}001\,\text{J} = 0{,}0020\,\text{J}$. Lisäksi $1\,\tfrac{\text{J}}{\text{kg}} = 1\,\text{Gy}$, ja painotettuna sama yksikkö on $1\,\text{Sv}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&H_\text{E} = w_\text{T} w_\text{R} \frac{E}{m} \\
&= 0{,}12 \cdot 20 \cdot \frac{0{,}0020\,\text{J}}{1{,}2\,\text{kg}} \\
&= 2{,}4 \cdot 0{,}0016667\,\text{Sv} \\
&= 0{,}0040\,\text{Sv}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Efektiivinen annos on noin $0{,}0040\,\text{Sv} = 4{,}0\,\text{mSv}$ vuodessa. Tuloksessa on kaksi merkitsevää numeroa, kuten energiassa $2{,}0\,\text{mJ}$ ja massassa $1{,}2\,\text{kg}$.

<!-- vaihe -->

**Järkevyys.** Absorboitunut annos on vain noin $1{,}7\,\text{mGy}$. Alfasäteilyn kerroin $20$ kasvattaa keuhkojen ekvivalenttiannoksen noin $33\,\text{mSv}$:iin, ja kerroin $0{,}12$ pienentää sen efektiiviseksi annokseksi, joka kuvaa koko kehon säteilyhaittaa. Tasainen jakautuminen on karkea mallioletus. Todellisuudessa alfahiukkaset absorboituvat hengitysteiden pinnan ohueen solukerrokseen. Tulos on samaa suuruusluokkaa kuin suomalaisen keskimääräinen radonannos, noin $4\,\text{mSv}$ vuodessa. Suuruusluokka tarkoittaa luvun kokoa suunnilleen.

Esimerkki käsitteli annoksen painotusta. Seuraavassa tehtävässä annosta pienennetään ajalla, etäisyydellä ja suojalla.

## Yleinen virhekäsitys
Moni ajattelee, että luonnon säteily on vaaratonta ja vain ihmisen tuottama säteily on vaarallista. Elimistö ei kuitenkaan erota, tuleeko alfahiukkanen kellarin radonista vai laboratorion lähteestä. Säteilyn alkuperä ei siis sinänsä määrää sen vaarallisuutta. Efektiivisen annoksen avulla voidaan vertailla altistuksia ja arvioida säteilyhaittoja. Sama efektiivinen annos ei silti takaa täsmälleen samaa riskiä jokaiselle ihmiselle. Suomalaisen suurin annos tulee luonnon radonista. Siksi radonin mittaaminen ja korjaaminen on tehokkain tapa pienentää omaa säteilyannosta.

Toinen yleinen virhe on ajatella, että etäisyyden kaksinkertaistaminen puolittaa annosnopeuden. Pistemäisen lähteen säteily leviää pinta-alalle, joka kasvaa etäisyyden neliönä. Kaksinkertainen etäisyys pienentää siis annosnopeuden neljäsosaan. Samoin kaksi puoliintumispaksuutta ei pysäytä gammasäteilyä kokonaan, vaan päästää läpi neljäsosan.

## Tiivistelmä
- Absorboitunut annos on absorboitunut energia massaa kohti, $D = \tfrac{E}{m}$. Sen yksikkö on gray $1\,\text{Gy} = 1\,\tfrac{\text{J}}{\text{kg}}$.
- Ekvivalenttiannos $H_\text{T} = w_\text{R} D_\text{T}$ ottaa huomioon säteilylajin (alfa $20$, gamma ja beeta $1$). Efektiivinen annos

    $$H_\text{E} = w_{\text{T}1} H_{\text{T}1} + w_{\text{T}2} H_{\text{T}2} + \ldots$$

    ottaa huomioon kudosten herkkyyden. Molempien yksikkö on sievert $\text{Sv}$.

- Suomalaisen keskimääräinen efektiivinen annos on noin $5{,}9\,\text{mSv}$ vuodessa (STUK-A263, 2020). Siitä sisäilman radon on noin $4\,\text{mSv}$ eli noin kaksi kolmasosaa.
- Radonin hajoamistuotteet lähettävät alfasäteilyä keuhkoihin. Asuntojen viitearvo on $300\,\tfrac{\text{Bq}}{\text{m}^3}$.
- Ulkoiselta säteilyltä suojaudutaan ajalla ($H = \dot{H} t$), etäisyydellä ($\dot{H} \propto \tfrac{1}{r^2}$) ja suojalla. Jokainen puoliintumispaksuus puolittaa gammasäteilyn annosnopeuden.
