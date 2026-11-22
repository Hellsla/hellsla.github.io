# Dispersio: prisma ja sateenkaari

> **Miksi** pääsateenkaaren ulkoreunalla on punaista ja sisäreunalla violettia, ja miksi sateenkaaren näkee vain, kun aurinko on selän takana?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kesäsateen jälkeen pellon ja metsän yllä on kirkas sateenkaari, jonka ulkoreunalla on punainen ja sisäreunalla violetti. Sen ulkopuolella näkyy himmeämpi toinen sateenkaari, jossa värit ovat päinvastaisessa järjestyksessä, ja kaarten välissä taivas on tummempi. Taustalla on harmaita sadepilviä. Etualalla ihminen seisoo selin katsojaan ja katsoo kaarta." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Taitekerroin riippuu aallonpituudesta
Luvussa *Valon heijastuminen ja taittuminen* taitekerroin $n$ kertoi, kuinka monta kertaa hitaammin valo kulkee aineessa kuin tyhjiössä. Tarkat mittaukset osoittavat, että taitekerroin riippuu myös valon aallonpituudesta. Vedessä ja lasissa taitekerroin on violetille valolle suurempi kuin punaiselle, joten violetti valo kulkee niissä hitaammin. Kruunulasissa punainen valo etenee noin $198\,000\,\text{km/s}$:n ja violetti noin $196\,000\,\text{km/s}$:n nopeudella. Taitekertoimen riippuvuutta aallonpituudesta sanotaan **dispersioksi**. Taulukon aallonpituudet ovat tyhjiössä. Rajapinnassa valon taajuus ei muutu, ja väri määräytyy taajuudesta, joten väri säilyy, vaikka nopeus ja aallonpituus muuttuvat.

| väri | $\lambda\ (\text{nm})$ | vesi | kruunulasi |
|---|---|---|---|
| punainen | $656$ | $1{,}3315$ | $1{,}5143$ |
| keltainen | $589$ | $1{,}3334$ | $1{,}5167$ |
| sininen | $486$ | $1{,}3375$ | $1{,}5224$ |
| violetti | $405$ | $1{,}3431$ | $1{,}5302$ |

Veden taitekertoimet lämpötilassa $20\,{}^\circ\text{C}$: M. Daimon ja A. Masumura, *Applied Optics* 46, 2007. Kruunulasin N-BK7 taitekertoimet: SCHOTT AG, optisten lasien luettelo, 2017.

<figure class="unit-photo"><img src="pics/fy7/prism-dispersion.webp" alt="Harmaalla seinällä pystysuora valojuova, jossa värit vaihtuvat vasemmalta oikealle punaisesta keltaisen ja vihreän kautta siniseen."><figcaption>Prisman läpi kulkenut valkoinen valo seinällä. Prisma taittaa violettia ja sinistä valoa enemmän kuin punaista, joten värit erkanevat spektriksi.</figcaption></figure>

```pysahdy
Valkoinen valo tulee ilmasta kruunulasiin. Kumpi väri hidastuu lasissa enemmän, punainen vai violetti, ja miksi?
---
Violetti hidastuu enemmän, koska sen taitekerroin ($1{,}5302$) on suurempi kuin punaisen ($1{,}5143$).
```

### Miksi violetti hidastuu enemmän
Valon sähkökenttä saa aineen elektronit värähtelemään valon taajuudella. Värähtelevät elektronit lähettävät itse valoa, joka yhdistyy tulevaan valoon, ja yhdistynyt aalto etenee hitaammin kuin valo tyhjiössä. Elektronien vaste riippuu taajuudesta. Vedessä ja lasissa se voimistuu, kun taajuus kasvaa kohti ultraviolettia, jota aine voimakkaasti absorboi. Siksi suurtaajuinen violetti valo hidastuu enemmän kuin pientaajuinen punainen, ja sen taitekerroin on suurempi.

### Prisma hajottaa valkoisen valon
Valkoinen valo, kuten auringonvalo, on eri aallonpituuksien eli värien seos. Kun se tulee vinosti lasiin, jokainen väri taittuu taittumislain mukaan mutta eri verran: violetin taitekerroin on suurin, joten se taittuu eniten normaalia kohti. Tasapaksun ikkunalasin toisesta pinnasta värit tulevat ulos taas alkuperäisen säteen suuntaisina, joten värejä ei huomaa. Prisman pinnat ovat vinossa toisiinsa nähden, joten toisessa pinnassa värit taittuvat vielä lisää erilleen. Prismasta tulee ulos värien viuhka eli **spektri**: punainen poikkeaa alkuperäisestä suunnastaan vähiten ja violetti eniten.

<svg data-fig="prism" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva, ei mittakaavassa: valkoisen valon kapea kimppu tulee vasemmalta alhaalta lasiprisman vasempaan sivuun. Prismassa valo hajoaa väreiksi, ja toisesta sivusta lähtee viuhka: punainen poikkeaa alkuperäisestä suunnastaan vähiten ja violetti eniten, ja niiden välissä ovat oranssi, keltainen, vihreä ja sininen. Värit osuvat oikealla olevaan valkoiseen varjostimeen allekkain, punainen ylimpänä. Värien erkaantuminen on piirretty todellista suuremmaksi." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-prism.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="16" y="113.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{valkoinen valo}$</div></foreignObject>
  <foreignObject x="473" y="137" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\text{punainen}$</div></foreignObject>
  <foreignObject x="473" y="283.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\text{violetti}$</div></foreignObject>
  <foreignObject x="223.5" y="276.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lasiprisma}$</div></foreignObject>
</svg>

Prisma ei värjää valoa. Isaac Newton osoitti 1660-luvulla, että kun spektristä erotetaan yksi väri ja se ohjataan toisen prisman läpi, se taittuu mutta ei enää hajoa uusiksi väreiksi. Toinen, toisin päin käännetty prisma taas kokoaa spektrin takaisin valkoiseksi valoksi. Värit olivat siis valmiina valkoisessa valossa, ja prisma vain erottaa ne toisistaan.

### Sateenkaari syntyy vesipisaroissa
Pieni sadepisara on lähes pallon muotoinen. Auringonvalo taittuu pisaraan, heijastuu pisaran takapinnasta ja taittuu ulos pisaran alaosasta. Valo palaa siis takaisin aurinkoa kohti, mutta kääntyneenä. Molemmissa taittumisissa violetti taittuu enemmän kuin punainen, joten värit erkanevat. Lähtösuunta riippuu myös siitä, mihin kohtaan pisaraa säde osuu. Valo kuitenkin kasautuu yhteen suuntaan, koska laajalta osumakohtien väliltä säteet lähtevät lähes samaan suuntaan: punainen noin $42^\circ$:n ja violetti noin $40{,}6^\circ$:n kulmassa siihen suuntaan nähden, josta auringonvalo tuli. Tähän suuntaan pisara loistaa kirkkaimmin.

<svg data-fig="drop" viewBox="0 0 600 372" role="img" aria-label="Periaatekuva, ei mittakaavassa: suuri vesipisara. Vasemmalta tulee vaakasuora valkoisen auringonvalon säde pisaran yläosaan. Tulokohdassa on katkoviivalla piirretty normaali, ja tulokulma alfa ja taitekulma beeta on merkitty. Pisarassa valo hajoaa: punainen ja violetti säde kulkevat pisaran takaseinään, heijastuvat siitä ja taittuvat ulos pisaran alaosasta vasemmalle alaspäin. Violetti lähtee loivemmassa kulmassa kuin punainen. Värien ero on piirretty todellista suuremmaksi." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-drop.webp" x="0" y="0" width="600" height="380" preserveAspectRatio="none"/>
  <foreignObject x="252" y="20" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="380" y="78" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\beta$</div></foreignObject>
  <foreignObject x="20" y="12" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{auringonvalo}$</div></foreignObject>
  <foreignObject x="468" y="43.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{heijastuu}$</div></foreignObject>
  <foreignObject x="349.5" y="330" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{punainen}$</div></foreignObject>
  <foreignObject x="172.5" y="310.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$\text{violetti}$</div></foreignObject>
</svg>

### Miksi punainen on pääsateenkaaren ulkoreunalla
Kun aurinko on selän takana, auringonsäteet kulkevat pään ohi kohti **vastapistettä**, joka on oman pään varjon kohdalla horisontin alapuolella. Silmään tulee punaista valoa niistä pisaroista, jotka näkyvät $42^\circ$:n kulmassa vastapisteen suunnasta, ja violettia niistä, jotka näkyvät $40{,}6^\circ$:n kulmassa. Samassa kulmassa olevat pisarat muodostavat ympyrän, jonka keskipiste on vastapiste. Punaisen ympyrä on suurempi, joten punainen on kaaren ulkoreunalla. Eri värit lähtevät pisarasta voimakkaimpina hieman eri suuntiin. Siksi katsojan silmään tulee kustakin pisarasta erityisen voimakkaasti tietyn väristä valoa, ja pisaran muiden värien voimakkaimmat suunnat kulkevat silmän ohi. Siksi jokainen katsoja näkee oman sateenkaarensa.

<svg data-fig="observer" viewBox="0 0 600 380" role="img" aria-label="Periaatekuva sivulta, kulmat eivät ole mittakaavassa: katsoja seisoo oikealla selkä aurinkoon päin, ja auringonsäteet tulevat oikealta ylhäältä vinosti alas vasemmalla olevaan sadekuuroon. Silmästä lähtee katkoviiva auringonsäteiden suuntaan alas vasemmalle kohti vastapistettä, joka on katsojan pään varjon kohdalla horisontin alapuolella. Ylempi pisara on 42 asteen kulmassa tästä suunnasta, ja siitä silmään tulee punainen valo; sen violetti valo kulkee silmän yläpuolelta ohi. Alempi pisara on noin 40,6 asteen kulmassa, ja siitä silmään tulee violetti valo; sen punainen valo osuu maahan katsojan eteen." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-observer.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="430" y="89.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$\text{auringonvalo}$</div></foreignObject>
  <foreignObject x="212" y="232.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$42^\circ$</span></div></foreignObject>
  <foreignObject x="281" y="224" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$40{,}6^\circ$</span></div></foreignObject>
  <foreignObject x="69.5" y="84" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{punainen}$</span></div></foreignObject>
  <foreignObject x="55.5" y="142" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{violetti}$</span></div></foreignObject>
  <foreignObject x="187.5" y="347.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{vastapiste}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/rainbow-glen-coe.webp" alt="Vihreä vuoristolaakso, jossa virtaa puro; laakson yllä näkyy sateenkaari pilvisen taivaan alla."><figcaption>Sateenkaari Glen Coen laaksossa Skotlannissa. Aurinko paistaa katsojan selän takaa, ja valo taittuu ja heijastuu vesipisaroissa, jotka hajottavat sen väreiksi.</figcaption></figure>

Sateenkaari näkyy siis vain, kun aurinko paistaa selän takaa ja edessä on pisaroita. Tasaisella maalla kaaresta näkyy vain horisontin yläpuolinen osa. Jos aurinko on korkeudella $h$ horisontista, vastapiste on yhtä paljon horisontin alapuolella, ja punaisen kaaren huippu on korkeudella $42^\circ - h$. Kun aurinko on yli $42^\circ$:n korkeudella, koko kaari jää horisontin alapuolelle, eikä sitä näe maan pinnalta. Siksi sateenkaaria näkyy keskikesällä aamuin ja illoin, kun aurinko on matalalla.

```pysahdy
Aurinko on $30^\circ$:n korkeudella horisontista. Kuinka korkealla horisontista pääsateenkaaren punaisen kaaren huippu on?
---
Huippu on korkeudella $42^\circ - 30^\circ = 12^\circ$, koska vastapiste on $30^\circ$ horisontin alapuolella.
```

### Sivukaari
Pääkaaren ulkopuolella näkyy joskus himmeämpi **sivukaari**. Siinä valo heijastuu pisaran sisällä kahdesti, ja värien järjestys on päinvastainen: punainen on sisäreunalla noin $50^\circ$:n ja violetti ulkoreunalla noin $54^\circ$:n kulmassa vastapisteen suunnasta. Jokaisessa heijastuksessa osa valosta pääsee pisarasta ulos, joten sivukaari on himmeämpi. Kaarten välissä taivas on tummempi, koska pääkaaren pisarat valaisevat vain kaaren sisäpuolta ja sivukaaren pisarat vain kaaren ulkopuolta.

## Kaava: Taittumislaki eri aallonpituuksille
Kun valo tulee ilmasta aineeseen, jokainen aallonpituus taittuu oman taitekertoimensa mukaan:
```latex
\sin \alpha_1 = n(\lambda) \sin \alpha_2
```
missä $\alpha_1$ on tulokulma ja $\alpha_2$ taitekulma, molemmat normaalista mitattuina, ja $n(\lambda)$ aineen taitekerroin aallonpituudella $\lambda$. Ilman taitekerroin on $1{,}0003$, joten se on pyöristetty ykköseksi; yleinen muoto on $n_1 \sin\alpha_1 = n_2 \sin\alpha_2$ (luku *Valon heijastuminen ja taittuminen*). Valon nopeus aineessa on $v = c : n(\lambda)$, missä $c = 3{,}00 \cdot 10^8\,\text{m/s}$. Kuvaajassa kruunulasin taitekerroin pienenee aallonpituuden kasvaessa, jyrkimmin violetin päässä.

<svg data-fig="n-graph" viewBox="0 0 600 372" role="img" aria-label="Kuvaaja mittakaavassa: kruunulasin N-BK7 taitekerroin n tyhjiöaallonpituuden lambda funktiona välillä 400–700 nm. Kuusi mittauspistettä valmistajan taulukosta: 405 nm 1,5302; 436 nm 1,5267; 486 nm 1,5224; 546 nm 1,5187; 589 nm 1,5167 ja 656 nm 1,5143. Käyrä laskee: lyhyillä aallonpituuksilla taitekerroin on suurin, ja käyrä loivenee punaista kohti. Vaaka-akselin alla on näkyvän valon värijana violetista punaiseen." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy711-band1" gradientUnits="userSpaceOnUse" x1="137.69230769230768" y1="0" x2="470.0" y2="0"><stop offset="0.000" stop-color="#7048e8"/><stop offset="0.200" stop-color="#1971c2"/><stop offset="0.400" stop-color="#2b8a3e"/><stop offset="0.583" stop-color="#f59f00"/><stop offset="0.700" stop-color="#e8590c"/><stop offset="0.867" stop-color="#c92a2a"/></linearGradient></defs>
  <line x1="137.5" y1="290" x2="137.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="193" y1="290" x2="193" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248.5" y1="290" x2="248.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="304" y1="290" x2="304" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="290" x2="359" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414.5" y1="290" x2="414.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="242" x2="470" y2="242" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="194" x2="470" y2="194" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="146" x2="470" y2="146" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="98" x2="470" y2="98" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="50" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="109" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="291" x2="110" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,24 L116,37 L104,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="137.5" y1="290" x2="137.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="115" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="193" y1="290" x2="193" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="248.5" y1="290" x2="248.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="226" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="304" y1="290" x2="304" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="359" y1="290" x2="359" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="336.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="414.5" y1="290" x2="414.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$700$</div></foreignObject>
  <line x1="103" y1="242" x2="110" y2="242" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="227.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}515$</div></foreignObject>
  <line x1="103" y1="194" x2="110" y2="194" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="179.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}520$</div></foreignObject>
  <line x1="103" y1="146" x2="110" y2="146" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}525$</div></foreignObject>
  <line x1="103" y1="98" x2="110" y2="98" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="83.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}530$</div></foreignObject>
  <line x1="103" y1="50" x2="110" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="35.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}535$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <foreignObject x="124" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$n$</span></div></foreignObject>
  <polyline points="137.5,90.5 140.5,93.5 143,96.5 146,99.5 149,102 151.5,105 154.5,108 157,110.5 160,113 162.5,116 165.5,118.5 168,121 171,123.5 173.5,126 176.5,128.5 179,131 182,133 185,135.5 187.5,138 190.5,140 193,142 196,144.5 198.5,146.5 201.5,148.5 204,150.5 207,153 209.5,155 212.5,156.5 215,158.5 218,160.5 221,162.5 223.5,164.5 226.5,166 229,168 232,170 234.5,171.5 237.5,173.5 240,175 243,176.5 245.5,178.5 248.5,180 251,181.5 254,183 257,184.5 259.5,186 262.5,187.5 265,189 268,190.5 270.5,192 273.5,193.5 276,195 279,196.5 281.5,198 284.5,199 287,200.5 290,202 293,203 295.5,204.5 298.5,205.5 301,207 304,208 306.5,209.5 309.5,210.5 312,212 315,213 317.5,214 320.5,215.5 323,216.5 326,217.5 329,218.5 331.5,219.5 334.5,221 337,222 340,223 342.5,224 345.5,225 348,226 351,227 353.5,228 356.5,229 359,230 362,231 365,231.5 367.5,232.5 370.5,233.5 373,234.5 376,235.5 378.5,236 381.5,237 384,238 387,239 389.5,239.5 392.5,240.5 395,241.5 398,242 401,243 403.5,243.5 406.5,244.5 409,245.5 412,246 414.5,247 417.5,247.5 420,248.5 423,249 425.5,250 428.5,250.5 431,251 434,252 437,252.5 439.5,253.5 442.5,254 445,254.5 448,255.5 450.5,256 453.5,256.5 456,257 459,258 461.5,258.5 464.5,259 467,259.5 470,260.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="143" cy="95.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="177.5" cy="130" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="233" cy="171" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="299.5" cy="206.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="347.5" cy="225.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="421.5" cy="248.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <rect x="137.5" y="336" width="332.5" height="12" rx="2" fill="url(#fy711-band1)" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="159" y="81" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{violetti}$</span></div></foreignObject>
  <foreignObject x="367.5" y="204" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{punainen}$</span></div></foreignObject>
</svg>

```pysahdy
Punaisen valon taitekerroin vedessä on $1{,}3315$. Kuinka nopeasti punainen valo etenee vedessä?
---
Nopeus on $v = c : n = 3{,}00 \cdot 10^8\,\text{m/s} : 1{,}3315 \approx 2{,}25 \cdot 10^8\,\text{m/s}$.
```

### Prisman poikkeamakulma
Prismassa säde taittuu kahdesti, ja kulmat riippuvat toisistaan:
```latex
\begin{aligned}
&\alpha_2 + \alpha_3 = A \\[6pt]
&\delta = \alpha_1 + \alpha_4 - A
\end{aligned}
```
missä $\alpha_1$ on tulokulma ja $\alpha_2$ taitekulma ensimmäisessä pinnassa, $\alpha_3$ tulokulma lasin sisältä toiseen pintaan ja $\alpha_4$ taitekulma ulos tullessa, kaikki normaaleista mitattuina. $A$ on prisman huippukulma ja $\delta$ **poikkeamakulma**, jonka verran säde kääntyy alkuperäisestä suunnastaan. Ensimmäinen yhtälö seuraa kolmion kulmien summasta, koska pintojen normaalit leikkaavat toisensa kulmassa $180^\circ - A$. Toinen seuraa siitä, että säde kääntyy ensimmäisessä pinnassa kulman $\alpha_1 - \alpha_2$ ja toisessa kulman $\alpha_4 - \alpha_3$. Violetille $\alpha_4$ on suurempi kuin punaiselle, joten sen poikkeamakulma on suurempi. Yhtälöt pätevät, kun säde pääsee ulos prisman toisesta pinnasta.

<svg data-fig="prism-angles" viewBox="0 0 600 336" role="img" aria-label="Kaavakuva prismasta: yksivärinen säde tulee vasemmalta prisman vasempaan sivuun tulokulmassa alfa 1 normaaliin nähden ja taittuu lasissa kulmaan alfa 2. Säde osuu oikeaan sivuun tulokulmassa alfa 3 ja lähtee prismasta taitekulmassa alfa 4. Molempien pintojen normaalit on piirretty katkoviivoin. Prisman huipussa on huippukulma A. Tulevan säteen jatke on piirretty katkoviivana, ja sen ja lähtevän säteen välinen kulma on poikkeamakulma delta." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-prism-angles.webp" x="0" y="1.2" width="600" height="346.2" preserveAspectRatio="none"/>
  <foreignObject x="99.5" y="183" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_1$</div></foreignObject>
  <foreignObject x="245" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_2$</div></foreignObject>
  <foreignObject x="298.5" y="204" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_3$</div></foreignObject>
  <foreignObject x="443" y="170" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_4$</div></foreignObject>
  <foreignObject x="280" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="455.5" y="130.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\delta$</div></foreignObject>
</svg>

### Sateenkaaren kulma
Pisarassa säde kääntyy tulokohdassa kulman $\alpha - \beta$, heijastuksessa kulman $180^\circ - 2\beta$ ja lähtökohdassa taas kulman $\alpha - \beta$. Kokonaiskääntymä on siis $180^\circ + 2\alpha - 4\beta$. Pisarasta lähtevän valon ja auringon suunnan välinen kulma on $180^\circ$ miinus kokonaiskääntymä eli
```latex
\theta = 4\beta - 2\alpha
```
missä $\alpha$ on tulokulma pisaran pinnalla, $\beta$ taitekulma, $\sin\alpha = n \sin\beta$, ja $\theta$ on kulma, jossa valo näkyy vastapisteen suunnasta. Kuvaaja näyttää, että $\theta$ riippuu tulokulmasta mutta ei kasva yli $42{,}3^\circ$:n, kun $n = 1{,}3315$. Huipun lähellä käyrä on lähes vaakasuora, joten laajalta tulokulmien väliltä säteet lähtevät lähes samaan suuntaan, ja siihen suuntaan näkyy kirkas kaari. Muu valo lähtee pienempiin kulmiin, joten taivas on kaaren sisäpuolella vaaleampi. Violetille ($n = 1{,}3431$) suurin kulma on $40{,}6^\circ$.

<svg data-fig="theta-graph" viewBox="0 0 600 350" role="img" aria-label="Kuvaaja mittakaavassa: punaisen valon (n = 1,332) säde lähtee vesipisarasta kulmassa theeta vastapisteen suuntaan nähden. Vaaka-akselilla on tulokulma alfa 0–90 astetta ja pystyakselilla theeta 0–45 astetta. Käyrä nousee origosta, saavuttaa suurimman arvonsa 42,3 astetta, kun tulokulma on noin 59,5 astetta, ja laskee sitten noin 15 asteeseen. Huipun lähellä käyrä on lähes vaakasuora: laajalta tulokulmien väliltä säteet lähtevät lähes samaan suuntaan." style="max-width:100%;font-size:24px">
  <line x1="137.5" y1="290" x2="137.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="179" y1="290" x2="179" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220.5" y1="290" x2="220.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262" y1="290" x2="262" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="304" y1="290" x2="304" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345.5" y1="290" x2="345.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="387" y1="290" x2="387" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428.5" y1="290" x2="428.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="263.5" x2="470" y2="263.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="236.5" x2="470" y2="236.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="210" x2="470" y2="210" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="183.5" x2="470" y2="183.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="156.5" x2="470" y2="156.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="130" x2="470" y2="130" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="103.5" x2="470" y2="103.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76.5" x2="470" y2="76.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="50" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,24 L102,37 L90,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="137.5" y1="290" x2="137.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="179" y1="290" x2="179" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220.5" y1="290" x2="220.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="204" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="262" y1="290" x2="262" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="304" y1="290" x2="304" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="345.5" y1="290" x2="345.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="329" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="387" y1="290" x2="387" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="428.5" y1="290" x2="428.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$90$</div></foreignObject>
  <line x1="89" y1="263.5" x2="96" y2="263.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="236.5" x2="96" y2="236.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="222" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="210" x2="96" y2="210" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="183.5" x2="96" y2="183.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="169" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="156.5" x2="96" y2="156.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="130" x2="96" y2="130" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="89" y1="103.5" x2="96" y2="103.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="76.5" x2="96" y2="76.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="62" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="50" x2="96" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha\ (^\circ)$</div></foreignObject>
  <foreignObject x="110" y="15.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\theta\ (^\circ)$</span></div></foreignObject>
  <polygon points="304,290 304,50 387,50 387,290" fill="#b2f2bb" fill-opacity="0.45"/>
  <polyline points="96,290 99,286 102,282 105.5,278 108.5,274 111.5,270 114.5,266 118,262 121,258 124,254 127,250 130.5,246 133.5,242 136.5,238 139.5,234 143,230.5 146,226.5 149,222.5 152,218.5 155,214.5 158.5,211 161.5,207 164.5,203.5 167.5,199.5 171,195.5 174,192 177,188.5 180,184.5 183.5,181 186.5,177.5 189.5,173.5 192.5,170 195.5,166.5 199,163 202,159.5 205,156 208,152.5 211.5,149.5 214.5,146 217.5,142.5 220.5,139.5 224,136.5 227,133 230,130 233,127 236,124 239.5,121 242.5,118 245.5,115 248.5,112.5 252,109.5 255,107 258,104.5 261,101.5 264.5,99 267.5,97 270.5,94.5 273.5,92 277,90 280,88 283,85.5 286,83.5 289,82 292.5,80 295.5,78 298.5,76.5 301.5,75 305,73.5 308,72 311,71 314,70 317.5,68.5 320.5,68 323.5,67 326.5,66 330,65.5 333,65 336,65 339,64.5 342,64.5 345.5,64.5 348.5,64.5 351.5,65 354.5,65.5 358,66 361,66.5 364,67.5 367,68.5 370.5,70 373.5,71 376.5,72.5 379.5,74.5 382.5,76.5 386,78.5 389,80.5 392,83 395,85.5 398.5,88.5 401.5,91.5 404.5,94.5 407.5,98 411,101.5 414,105.5 417,109.5 420,113.5 423,118 426.5,122.5 429.5,127.5 432.5,132.5 435.5,138 439,143.5 442,149 445,155 448,161.5 451.5,168 454.5,174.5 457.5,181.5 460.5,188.5 464,196 467,203.5 470,211.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="343" y1="64.5" x2="343" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="64.5" x2="343" y2="64.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="343" cy="64.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="308" y="24" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$42{,}3^\circ$</span></div></foreignObject>
  <foreignObject x="273" y="233" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{kirkas kaari}$</span></div></foreignObject>
</svg>

## Esimerkki
Valkoisen valon kapea kimppu tulee ilmasta kruunulasilevyn pintaan tulokulmassa $60{,}0^\circ$. Kuinka suuret ovat punaisen ($656\,\text{nm}$) ja violetin ($405\,\text{nm}$) valon taitekulmat lasissa, ja kuinka suuri kulma niiden välille syntyy? Käytä taulukon taitekertoimia.

<!-- vaihe -->

**Tunnetut ja kysytty.** Tulokulma $\alpha_1 = 60{,}0^\circ$, taulukosta punaisen valon taitekerroin $n_\text{p} = 1{,}5143$ ja violetin $n_\text{v} = 1{,}5302$.

Kysytään taitekulmia $\alpha_\text{p}$ ja $\alpha_\text{v}$ sekä niiden erotusta $\Delta\alpha = \alpha_\text{p} - \alpha_\text{v}$.

<!-- vaihe -->

**Periaate.** Kumpikin väri noudattaa taittumislakia omalla taitekertoimellaan. Valo tulee ilmasta, jonka taitekerroin on pyöristettynä $1$, joten $\sin \alpha_1 = n \sin \alpha_2$. Kummankin värin tulokulma on sama, koska ne kulkevat samassa valkoisen valon kimpussa.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&\sin \alpha_1 = n \sin \alpha_2 \\[6pt]
&\sin \alpha_2 = \frac{\sin \alpha_1}{n}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: taitekerroin on yksikötön, ja kulmat ovat asteina.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\sin \alpha_\text{p} = \frac{\sin \alpha_1}{n_\text{p}} \\
&= \frac{\sin 60{,}0^\circ}{1{,}5143} \\
&= 0{,}57190 \\
&\alpha_\text{p} = 34{,}88^\circ \\[6pt]
&\sin \alpha_\text{v} = \frac{\sin \alpha_1}{n_\text{v}} \\
&= \frac{\sin 60{,}0^\circ}{1{,}5302} \\
&= 0{,}56596 \\
&\alpha_\text{v} = 34{,}47^\circ
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Punaisen valon taitekulma on $34{,}9^\circ$ ja violetin $34{,}5^\circ$, kolmen merkitsevän numeron tarkkuudella kuten tulokulma $60{,}0^\circ$. Säteiden välinen kulma lasketaan pyöristämättömistä kulmista: $\Delta\alpha = 34{,}88^\circ - 34{,}47^\circ = 0{,}41^\circ$.

<!-- vaihe -->

**Järkevyys.** Molemmat taitekulmat ovat pienempiä kuin tulokulma, koska valo taittuu optisesti tiheämpään aineeseen tullessaan normaalia kohti. Violetin taitekulma on pienempi, koska sen taitekerroin on suurempi. Ero on alle puoli astetta, joten tasapaksussa lasissa värit erottuvat vain vähän; prisman vino toinen pinta kasvattaa eroa.

## Yleinen virhekäsitys
Moni ajattelee, että prisma värjää valon tai että värit syntyvät prisman lasissa. Värit ovat valmiina valkoisessa valossa, ja prisma erottaa ne, koska taitekerroin riippuu aallonpituudesta. Toinen yleinen virhe on päätellä, että punainen taittuu eniten, koska sen aallonpituus on pisin. Vedessä ja lasissa asia on päinvastoin: violetin taitekerroin on suurin, joten violetti taittuu ja poikkeaa eniten. Kolmas virhe on ajatella sateenkaarta esineeksi, joka on tietyssä paikassa. Kaari on suunta: se näkyy aina $42^\circ$:n kulmassa vastapisteestä, joten se siirtyy katsojan mukana, eikä sen päätä voi saavuttaa.

## Tiivistelmä
- Taitekerroin riippuu aallonpituudesta. Tätä sanotaan dispersioksi. Vedessä ja lasissa violetin taitekerroin on suurin ja punaisen pienin, joten violetti taittuu eniten.
- Prismassa valkoinen valo taittuu kahdesti vinoissa pinnoissa, ja värit erkanevat spektriksi. Poikkeamakulma on $\delta = \alpha_1 + \alpha_4 - A$, ja violetti poikkeaa eniten.
- Sateenkaaressa valo taittuu pisaraan, heijastuu sen takapinnasta ja taittuu ulos. Punainen näkyy noin $42^\circ$:n ja violetti noin $40{,}6^\circ$:n kulmassa vastapisteestä, joten punainen on ulkoreunalla.
- Sateenkaari näkyy, kun aurinko on selän takana ja alle $42^\circ$:n korkeudella. Sivukaaressa valo heijastuu kahdesti, ja värit ovat päinvastaisessa järjestyksessä.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: puutarhassa nurmikkoa kastellaan letkulla. Vesisuihkun pisaroissa näkyy pieni sateenkaari, kun aurinko paistaa kastelijan selän takaa." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
