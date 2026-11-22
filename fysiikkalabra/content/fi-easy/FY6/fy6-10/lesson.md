# Sähkövaraus ja Coulombin laki

> **Miksi** villapaitaan hierottu ilmapallo jää kiinni seinään, vaikka seinässä ei ole sähkövarausta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: huoneen vaalea seinä, jossa sininen ilmapallo pysyy kiinni seinässä ilman teippiä, ja sen naru roikkuu alas. Vasemmalla pöydällä on muovikampa, jota kohti pienet paperisilpun palat nousevat pöydältä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Sähkövaraus ja alkeisvaraus
Aineen atomeissa on positiivisesti varattuja protoneja ja negatiivisesti varattuja elektroneja (luku *Virtapiiri, sähkövirta ja jännite*). **Sähkövaraus** on hiukkasten ominaisuus. Sen vuoksi hiukkaset vaikuttavat toisiinsa sähköisellä vuorovaikutuksella. Samanmerkkiset varaukset hylkivät toisiaan, ja erimerkkiset varaukset vetävät toisiaan puoleensa. Varauksen tunnus on $Q$ tai $q$. Sen yksikkö on coulombi $\text{C}$. Protonin varaus on $+e$ ja elektronin varaus on $-e$. Tässä $e$ on **alkeisvaraus**, joka on pienin vapaana esiintyvä varaus. Neutronilla ei ole varausta.

Tavallisessa kappaleessa on yhtä monta protonia ja elektronia. Siksi sen kokonaisvaraus on nolla, ja kappale on sähköisesti neutraali. Kappale on varautunut, kun siinä on elektroneja enemmän tai vähemmän kuin protoneja. Varaus koostuu aina kokonaisista alkeisvarauksista. Varausta ei voi olla esimerkiksi puolta alkeisvarausta:
```latex
Q = n e
```
Tässä $Q$ on kappaleen varauksen suuruus ($\text{C}$). Luku $n$ on ylimääräisten tai puuttuvien elektronien lukumäärä. Vakio $e = 1{,}602 \cdot 10^{-19}\,\text{C}$ on alkeisvaraus. Coulombi on suuri varaus, sillä siihen tarvitaan $6{,}24 \cdot 10^{18}$ alkeisvarausta. Hankauksen jälkeen ilmapallon varaus on tyypillisesti kymmeniä nanocoulombeja. Esimerkiksi varaus $-50\,\text{nC}$ tarkoittaa noin $3{,}1 \cdot 10^{11}$ ylimääräistä elektronia.

```pysahdy
Voiko kappaleen varaus olla $0{,}5e$ eli puolet alkeisvarauksesta?
---
Ei voi. Varaus on aina kokonaisluku kertaa alkeisvaraus, $Q = ne$. Elektroneja siirtyy vain kokonaisia.
```

### Varauksen säilyminen
Varausta ei synny eikä häviä. Eristetyn systeemin kokonaisvaraus pysyy samana, vaikka varausta siirtyy kappaleesta toiseen. Kokonaisvaraus on kaikkien varausten summa. Tämä on **varauksen säilymislaki**. Kun ilmapalloa hierotaan villaan, osa villan elektroneista siirtyy ilmapallon pintaan. Ilmapallo saa negatiivisen varauksen. Villalle jää yhtä suuri positiivinen varaus, koska siltä puuttuu yhtä monta elektronia. Kiinteissä aineissa siirtyvät elektronit. Protonit pysyvät atomien ytimissä.

<svg data-fig="hankaus" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa, kaksi paneelia. Vasemmalla ennen hankausta: ilmapallossa ja villakankaassa on kummassakin neljä positiivista ja neljä negatiivista varausta. Siksi kumpikin on neutraali, Q = 0. Oikealla hankauksen jälkeen: kolme elektronia on siirtynyt villasta ilmapalloon, mitä näyttää sininen nuoli villasta palloon. Ilmapallossa on neljä positiivista ja seitsemän negatiivista varausta, Q = −3e, ja villassa neljä positiivista ja yksi negatiivinen, Q = +3e. Varausten summa on edelleen nolla." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-10-hankaus.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="58.5" y="11.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ennen hankausta}$</div></foreignObject>
  <foreignObject x="61.5" y="243.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = 0$</div></foreignObject>
  <foreignObject x="203.5" y="243.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = 0$</div></foreignObject>
  <foreignObject x="24" y="281.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ilmapallo}$</div></foreignObject>
  <foreignObject x="191" y="281.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{villa}$</div></foreignObject>
  <foreignObject x="340" y="11.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hankauksen jälkeen}$</div></foreignObject>
  <foreignObject x="377.5" y="315.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{elektroneja}$</div></foreignObject>
  <foreignObject x="349" y="243.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = -3e$</div></foreignObject>
  <foreignObject x="491" y="243.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = +3e$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/balloon-hair.webp" alt="Käsi pitää punaista ilmapalloa hiusten yläpuolella. Hiukset nousevat kohti palloa."><figcaption>Ilmapalloa on hangattu hiuksiin. Elektroneja siirtyi hiuksista palloon. Pallossa on nyt negatiivinen varaus ja hiuksissa positiivinen varaus. Erimerkkiset varaukset vetävät toisiaan.</figcaption></figure>

### Kappaleiden varautuminen
Kappale voidaan varata kolmella tavalla.

- **Hankaus.** Kaksi eri ainetta hangataan toisiaan vasten. Elektroneja siirtyy aineesta, joka pitää niistä heikommin kiinni, toiseen aineeseen. Kappaleet varautuvat yhtä suuresti ja vastakkaismerkkisesti.
- **Kosketus.** Varattu kappale koskettaa johdetta, ja osa varauksesta siirtyy johteeseen. Johde on aine, jossa varaukset pääsevät liikkumaan. Kaksi samanlaista metallipalloa jakaa kosketuksessa yhteisen varauksensa tasan. Jos varaukset ovat ensin $+12\,\text{nC}$ ja $0\,\text{nC}$, kummankin varaus on kosketuksen jälkeen $+6\,\text{nC}$.
- **Influenssi.** Varattu kappale tuodaan johteen lähelle koskematta siihen. Johteen vapaat elektronit siirtyvät. Siksi johteen lähipuolelle syntyy vastakkaismerkkinen varaus ja kaukaiselle puolelle samanmerkkinen varaus. Johteen kokonaisvaraus ei muutu. Jos johde yhdistetään hetkeksi maahan johtimella, osa elektroneista siirtyy maahan tai maasta johteeseen. Silloin johde jää varatuksi.

### Miksi varattu kappale vetää neutraalia kappaletta
Influenssi selittää, miksi varattu kappale vetää puoleensa myös neutraalia kappaletta. Metallipallon vastakkaismerkkinen varaus on lähempänä varattua sauvaa kuin samanmerkkinen varaus. Sähköinen voima heikkenee etäisyyden kasvaessa. Siksi vetovoima on suurempi kuin hylkimisvoima, ja pallo vetäytyy sauvaa kohti.

Eriste on aine, jossa varaukset eivät pääse liikkumaan vapaasti. Eristeessä elektronit eivät pääse liikkumaan kappaleesta toiseen. Jokaisen molekyylin varaukset kuitenkin siirtyvät hieman. Silloin molekyyli **polarisoituu**. Negatiivisesti varatun ilmapallon vieressä seinän molekyylien positiiviset päät kääntyvät palloa kohti. Seinä pysyy neutraalina. Lähellä olevat positiiviset päät vetävät palloa kuitenkin enemmän kuin kauempana olevat negatiiviset päät hylkivät sitä. Siksi ilmapallo pysyy seinässä ja kampa nostaa paperisilppua.

<svg data-fig="influenssi" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa, kaksi paneelia. Vasemmalla johde: negatiivisesti varattu muovisauva on eristetangon päässä olevan metallipallon vasemmalla puolella. Pallon vapaat elektronit ovat siirtyneet kauemmas sauvasta. Siksi pallon sauvan puoleisella pinnalla on kolme positiivista ja vastakkaisella pinnalla kolme negatiivista varausta. Pallo on kokonaisuutena neutraali. Punainen voimanuoli osoittaa pallosta sauvaa kohti. Oikealla eriste: negatiivisesti varattu ilmapallo seinän vieressä. Seinän molekyylien varaukset ovat siirtyneet hieman niin, että jokaisen molekyylin positiivinen pää on palloa kohti. Punainen voimanuoli osoittaa ilmapallosta seinää kohti." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-10-influenssi.webp" x="1.2" y="1.2" width="597" height="368.2" preserveAspectRatio="none"/>
  <foreignObject x="115" y="11.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{johde}$</div></foreignObject>
  <foreignObject x="408.5" y="11.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{eriste}$</div></foreignObject>
  <foreignObject x="12" y="179.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{muovisauva}$</div></foreignObject>
  <foreignObject x="109" y="61.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="135" y="311.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{metallipallo}$</div></foreignObject>
  <foreignObject x="333" y="67.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="334" y="275.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ilmapallo}$</div></foreignObject>
  <foreignObject x="493" y="311.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{seinä}$</div></foreignObject>
</svg>

### Sähkövirta on varauksen siirtymistä
Kun varausta siirtyy paikasta toiseen, kulkee sähkövirta. Johtimessa virta on poikkileikkauksen läpi aikayksikössä kulkeva varaus, $I = Q : t$ (luku *Virtapiiri, sähkövirta ja jännite*). Sama pätee kipinään ja salamaan. Kun kosketat kuivana talvipäivänä ovenkahvaa, kehostasi purkautuu kipinässä varaus. Se on tyypillisesti alle mikrocoulombin. Purkaus kestää vain noin mikrosekunnin. Siksi virta on hetken ampeerin luokkaa, vaikka siirtynyt varaus on pieni.

### Varauksen ympärillä on sähkökenttä
Varattu kappale vaikuttaa toiseen varattuun kappaleeseen koskematta siihen. Tämä kuvataan sähkökentällä. Varaus muuttaa ympäröivää tilaa niin, että toiseen varaukseen kohdistuu siinä paikassa sähköinen voima. Kenttää havainnollistetaan kenttäviivoilla. Kenttäviivan suunta on suunta, johon pieneen positiiviseen testivaraukseen kohdistuva voima osoittaa. Negatiiviseen varaukseen voima osoittaa kenttäviivaa vastaan.

**Pistevaraus** on varattu kappale, jonka koko on pieni verrattuna tarkasteltaviin etäisyyksiin. Positiivisesta pistevarauksesta kenttäviivat lähtevät säteittäin ulospäin. Negatiiviseen pistevaraukseen ne tulevat säteittäin sisäänpäin. Lähellä varausta viivat ovat tiheässä ja kenttä on voimakas. Kauempana viivat harvenevat ja kenttä heikkenee. Kentän voimakkuutta käsitellään laskemalla luvussa *Homogeeninen sähkökenttä*.

<svg data-fig="kentta" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, ei mittakaavassa, kaksi paneelia. Vasemmalla positiivinen pistevaraus, jonka ympärillä on kahdeksan säteittäistä kenttäviivaa, nuolet varauksesta poispäin. Oikealla negatiivinen pistevaraus, jonka kenttäviivojen nuolet osoittavat varausta kohti. Kummankin oikealla puolella on pieni positiivinen testivaraus, ja punainen voimanuoli osoittaa kenttäviivan suuntaan: positiivisesta varauksesta poispäin ja negatiivista varausta kohti. Kenttäviivat ovat vihreitä, voimanuoli punainen. Viivat ovat lähellä varausta tiheässä ja harvenevat kauempana." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-10-kentta.webp" x="-1.3" y="-1.3" width="603" height="353" preserveAspectRatio="none"/>
  <foreignObject x="219.5" y="81.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="103.5" y="281.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+Q$</div></foreignObject>
  <foreignObject x="519.5" y="81.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="403.5" y="281.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-Q$</div></foreignObject>
  <foreignObject x="12" y="11.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{kenttäviiva}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/balloons-repel.webp" alt="Kaksi keltaista ilmapalloa roikkuu langoissa liitutaulun edessä. Pallot ovat erillään."><figcaption>Molemmissa ilmapalloissa on samanmerkkinen varaus. Pallot työntävät toisiaan poispäin, ja langat menevät vinoon. Palloon vaikuttavat painovoima, langan voima ja toisen pallon sähköinen voima.</figcaption></figure>

## Kaava: Coulombin laki
Kahden pistevarauksen välisen sähköisen voiman suuruus on suoraan verrannollinen varausten tuloon. Se on myös kääntäen verrannollinen niiden välisen etäisyyden neliöön. Suora verrannollisuus tarkoittaa, että kun varausten tulo kaksinkertaistuu, voimakin kaksinkertaistuu. Kääntäen verrannollinen tarkoittaa, että kun etäisyyden neliö kasvaa, voima pienenee samassa suhteessa. Tämä on **Coulombin laki**:
```kaavat
Coulombin voiman suuruus :: F = k\,\frac{\lvert q_1 q_2 \rvert}{r^2}
```
Tässä $F$ on voiman suuruus ($\text{N}$), $q_1$ ja $q_2$ ovat varaukset ($\text{C}$) ja $r$ on varausten välinen etäisyys ($\text{m}$). Vakio $$k = 8{,}988 \cdot 10^{9}\,\tfrac{\text{N} \cdot \text{m}^2}{\text{C}^2}$$ on Coulombin lain vakio. Coulombin laki pätee täsmällisesti eli tarkasti pistevarauksille. Ajatellaan palloa, jonka varaus on jakautunut pallosymmetrisesti eli tasaisesti joka suuntaan. Sen ulkopuolella kenttä on sama kuin pistevarauksen kenttä, joka on sijoitettu pallon keskipisteeseen. Siksi tällaisten pallojen etäisyys mitataan keskipisteiden välillä. Varatut johtavat pallot voivat olla lähellä toisiaan. Silloin varaukset niiden pinnalla voivat siirtyä eli jakautua uudella tavalla. Silloin malli, jossa pistevaraukset ovat keskipisteissä, ei ole enää tarkka. Vakion arvo pätee tyhjiössä. Ilmassa voima on lähes sama.

```pysahdy
Kaksi pistevarausta, kumpikin $1{,}0\,\mu\text{C}$, on $0{,}30\,\text{m}$:n päässä toisistaan. Kuinka suuri sähköinen voima niiden välillä on?
---
Voima on $F = k\,\lvert q_1 q_2 \rvert : r^2$. Lukuarvoilla $F = 9{,}0 \cdot 10^{9} \cdot 1{,}0 \cdot 10^{-12} : 0{,}30^2$ (yksikkö $\text{N}$), joten $F \approx 0{,}10\,\text{N}$.
```

### Voima ja vastavoima
Coulombin laki antaa voiman suuruuden. Voiman suunta päätellään varausten merkeistä. Voimat ovat varausten välisellä suoralla. Samanmerkkiset varaukset hylkivät toisiaan, ja erimerkkiset varaukset vetävät toisiaan puoleensa. Varaus $q_1$ vaikuttaa varaukseen $q_2$ voimalla $\overline{F}_{12}$. Varaus $q_2$ vaikuttaa varaukseen $q_1$ voimalla $\overline{F}_{21}$. Ne ovat voima ja vastavoima, $\overline{F}_{12} = -\overline{F}_{21}$ (luku *Vuorovaikutus ja voima: Newtonin ensimmäinen ja kolmas laki*). Ne ovat yhtä suuret ja vastakkaissuuntaiset myös silloin, kun varaukset ovat eri suuret. Lain kaavassa varaukset esiintyvät symmetrisesti. Siksi sama $F$ vaikuttaa kumpaankin varaukseen.

<svg data-fig="coulomb" viewBox="0 0 600 364" role="img" aria-label="Kaavakuva, ei mittakaavassa. Ylhäällä samanmerkkiset varaukset q1 ja q2, molemmat positiivisia: varaukseen q1 vaikuttava voima F21 osoittaa vasemmalle poispäin q2:sta. Varaukseen q2 vaikuttava voima F12 osoittaa oikealle poispäin q1:stä. Siksi varaukset hylkivät toisiaan. Alhaalla erimerkkiset varaukset, q1 positiivinen ja q2 negatiivinen: voimat osoittavat toisiaan kohti. Siksi varaukset vetävät toisiaan puoleensa. Kaikki neljä voimanuolta ovat yhtä pitkiä. Alimpana varausten keskipisteiden välinen etäisyys r." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-10-coulomb.webp" x="0" y="0" width="600" height="373.8" preserveAspectRatio="none"/>
  <foreignObject x="102.5" y="7.5" width="395" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{samanmerkkiset varaukset hylkivät}$</div></foreignObject>
  <foreignObject x="121.5" y="177.5" width="357" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{erimerkkiset varaukset vetävät}$</div></foreignObject>
  <foreignObject x="109" y="43.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{21}$</div></foreignObject>
  <foreignObject x="433" y="43.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{12}$</div></foreignObject>
  <foreignObject x="183.5" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$q_1$</div></foreignObject>
  <foreignObject x="383.5" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$q_2$</div></foreignObject>
  <foreignObject x="225" y="213.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{21}$</div></foreignObject>
  <foreignObject x="317" y="213.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{12}$</div></foreignObject>
  <foreignObject x="183.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$q_1$</div></foreignObject>
  <foreignObject x="383.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$q_2$</div></foreignObject>
  <foreignObject x="287" y="327.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
</svg>

### Etäisyyden neliö
Voima riippuu etäisyydestä voimakkaasti. Kun etäisyys kaksinkertaistuu, nimittäjä $r^2$ nelinkertaistuu. Silloin voima pienenee neljäsosaan. Kolminkertaisella etäisyydellä voima on yhdeksäsosa ja nelinkertaisella kuudestoistaosa. Varauksiin voima on sen sijaan suoraan verrannollinen: se kasvaa samassa suhteessa. Kun toinen varaus kaksinkertaistuu, voima kaksinkertaistuu. Kuvaajassa kumpikin varaus on $20\,\text{nC}$. Etäisyydellä $3\,\text{cm}$ voima on $4{,}0\,\text{mN}$. Etäisyydellä $6\,\text{cm}$ voima on enää $1{,}0\,\text{mN}$.

<svg data-fig="kuvaaja" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa: kahden pistevarauksen, q1 = q2 = 20 nC, välinen voima F millinewtoneina etäisyyden r funktiona senttimetreinä. Käyrä laskee jyrkästi. Etäisyydellä 3 cm voima on 4,0 mN. Kaksinkertaisella etäisyydellä 6 cm voima on neljäsosa eli 1,0 mN. Kolminkertaisella etäisyydellä 9 cm se on yhdeksäsosa eli 0,44 mN. Nelinkertaisella etäisyydellä 12 cm se on kuudestoistaosa eli 0,25 mN. Pisteiden viereen on merkitty F, F/4, F/9 ja F/16." style="max-width:100%;font-size:24px">
  <line x1="166.5" y1="310" x2="166.5" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="249.5" y1="310" x2="249.5" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="332" y1="310" x2="332" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="415" y1="310" x2="415" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="257" x2="470" y2="257" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="204" x2="470" y2="204" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="151.5" x2="470" y2="151.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="98.5" x2="470" y2="98.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="310" x2="484" y2="310" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,310 L483,316 L483,304 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="311" x2="84" y2="58" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,46 L90,59 L78,59 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="166.5" y1="310" x2="166.5" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="156.5" y="319.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="249.5" y1="310" x2="249.5" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="239.5" y="319.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="332" y1="310" x2="332" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="322" y="319.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$9$</div></foreignObject>
  <line x1="415" y1="310" x2="415" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="398.5" y="319.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="77" y1="257" x2="84" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="242.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="77" y1="204" x2="84" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="189.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="77" y1="151.5" x2="84" y2="151.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="137" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="77" y1="98.5" x2="84" y2="98.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="84" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="54" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="295.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (\text{cm})$</div></foreignObject>
  <foreignObject x="74" y="15.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{mN})$</div></foreignObject>
  <polyline points="164,84 166.5,97 169,109.5 171.5,120.5 174,130.5 176,140 178.5,149 181,157 183.5,164.5 186,171.5 188.5,177.5 191,183.5 193.5,189.5 196,194.5 198.5,199.5 201,204 203.5,208.5 206,212.5 208,216.5 210.5,220 213,223.5 215.5,226.5 218,229.5 220.5,232.5 223,235 225.5,237.5 228,240 230.5,242.5 233,244.5 235.5,247 237.5,249 240,250.5 242.5,252.5 245,254.5 247.5,256 250,257.5 252.5,259 255,260.5 257.5,262 260,263 262.5,264.5 265,266 267,267 269.5,268 272,269 274.5,270 277,271 279.5,272 282,273 284.5,274 287,275 289.5,275.5 292,276.5 294.5,277.5 296.5,278 299,279 301.5,279.5 304,280 306.5,281 309,281.5 311.5,282 314,282.5 316.5,283 319,284 321.5,284.5 324,285 326,285.5 328.5,286 331,286.5 333.5,287 336,287 338.5,287.5 341,288 343.5,288.5 346,289 348.5,289.5 351,289.5 353.5,290 355.5,290.5 358,291 360.5,291 363,291.5 365.5,292 368,292 370.5,292.5 373,292.5 375.5,293 378,293.5 380.5,293.5 383,294 385,294 387.5,294.5 390,294.5 392.5,295 395,295 397.5,295.5 400,295.5 402.5,295.5 405,296 407.5,296 410,296.5 412.5,296.5 414.5,297 417,297 419.5,297 422,297.5 424.5,297.5 427,297.5 429.5,298 432,298 434.5,298 437,298.5 439.5,298.5 442,298.5 444,299 446.5,299 449,299 451.5,299.5 454,299.5 456.5,299.5 459,299.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="166.5" cy="98.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="180.5" y="54" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F$</div></foreignObject>
  <circle cx="249.5" cy="257" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="263.5" y="212.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\tfrac{F}{4}$</div></foreignObject>
  <circle cx="332" cy="286.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="346" y="242" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\tfrac{F}{9}$</div></foreignObject>
  <circle cx="415" cy="297" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="429" y="252.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\tfrac{F}{16}$</div></foreignObject>
  <foreignObject x="230.5" y="88" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$4{,}0\,\text{mN}$</div></foreignObject>
  <line x1="166.5" y1="98.5" x2="166.5" y2="310" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="84" y1="98.5" x2="166.5" y2="98.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
</svg>

### Usean varauksen voimat
Kun varaukseen vaikuttaa useampi muu varaus, jokaisen varauksen voima lasketaan Coulombin lailla erikseen, ikään kuin muita ei olisi. Varaukseen vaikuttava kokonaisvoima on näiden voimien vektorisumma. Vektorisumma tarkoittaa, että voimien suunnat otetaan huomioon:
```latex
\overline{F} = \overline{F}_1 + \overline{F}_2
```
Tässä $\overline{F}$ on kokonaisvoima ($\text{N}$). Voimat $\overline{F}_1$ ja $\overline{F}_2$ ovat kahden muun varauksen siihen kohdistamat voimat ($\text{N}$). Kun kaikki varaukset ovat samalla suoralla, samansuuntaiset voimat lasketaan yhteen. Vastakkaissuuntaiset voimat vähennetään toisistaan.

```pysahdy
Kolme varausta on samalla suoralla. Keskimmäiseen varaukseen vaikuttavat kaksi yhtä suurta samanmerkkistä varausta, kumpikin yhtä kaukana. Mikä on kokonaisvoima?
---
Nolla. Kumpikin varaus vaikuttaa keskimmäiseen vastakkaiselta puolelta, ja molemmat joko hylkivät tai vetävät sitä. Voimat ovat yhtä suuret ja vastakkaiset, joten ne kumoavat toisensa: $\overline{F} = \overline{0}$.
```

## Esimerkki
Kaksi pientä metallipalloa on eristetangoilla. Pallojen keskipisteiden etäisyys on $6{,}0\,\text{cm}$. Toisen pallon varaus on $+12\,\text{nC}$ ja toisen pallon varaus on $-8{,}0\,\text{nC}$. Kuinka suuri on pallojen välinen sähköinen voima? Vetävätkö pallot toisiaan puoleensa vai hylkivätkö ne toisiaan?

<!-- vaihe -->

**Tunnetut ja kysytty.** $q_1 = +12\,\text{nC}$, $q_2 = -8{,}0\,\text{nC}$ ja $r = 6{,}0\,\text{cm}$.

Kysytään voiman suuruutta $F$.

Kysytään myös sitä, vetävätkö vai hylkivätkö pallot toisiaan.

<!-- vaihe -->

**Periaate.** Pallot ovat pieniä verrattuna niiden etäisyyteen. Siksi niitä voi käsitellä pistevarauksina, ja Coulombin laki antaa voiman suuruuden. Voiman suunta päätellään merkeistä: erimerkkiset varaukset vetävät toisiaan puoleensa. Kumpaankin palloon vaikuttaa yhtä suuri voima.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
F = k\,\frac{\lvert q_1 q_2 \rvert}{r^2}
```

<!-- vaihe -->

**Yksikkömuunnokset.** $q_1 = 12\,\text{nC} = 12 \cdot 10^{-9}\,\text{C}$, $\lvert q_2 \rvert = 8{,}0\,\text{nC} = 8{,}0 \cdot 10^{-9}\,\text{C}$ ja $r = 6{,}0\,\text{cm} = 6{,}0 \cdot 0{,}01\,\text{m} = 0{,}060\,\text{m}$. Varausten tulon itseisarvo on $\lvert q_1 q_2 \rvert = 12 \cdot 10^{-9}\,\text{C} \cdot 8{,}0 \cdot 10^{-9}\,\text{C} = 9{,}6 \cdot 10^{-17}\,\text{C}^2$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&F = k\,\frac{\lvert q_1 q_2 \rvert}{r^2} \\
&= 8{,}988 \cdot 10^{9}\,\tfrac{\text{N} \cdot \text{m}^2}{\text{C}^2} \\
&\quad \cdot \frac{9{,}6 \cdot 10^{-17}\,\text{C}^2}{(0{,}060\,\text{m})^2} \\
&= 2{,}397 \cdot 10^{-4}\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Voima on $2{,}4 \cdot 10^{-4}\,\text{N} = 0{,}24\,\text{mN}$. Vastauksessa on kaksi merkitsevää numeroa kuten varauksessa $8{,}0\,\text{nC}$ ja etäisyydessä $6{,}0\,\text{cm}$. Pallot vetävät toisiaan puoleensa, koska niiden varaukset ovat erimerkkiset.

<!-- vaihe -->

**Järkevyys.** Pyöristetyillä luvuilla $10^{10} \cdot 10^{-16} : 0{,}004 \approx 2{,}5 \cdot 10^{-4}$. Suuruusluokka on siis oikea. Suuruusluokka kertoo luvun koon suunnilleen. Voima on yhtä suuri kuin noin $24\,\text{mg}$:n massan paino. Se on pieni, mutta se riittää liikuttamaan kevyitä kappaleita. Puolet lyhyemmällä etäisyydellä voima olisi nelinkertainen, $0{,}96\,\text{mN}$.

## Yleinen virhekäsitys
Moni ajattelee, että suurempi varaus vaikuttaa pienempään suuremmalla voimalla kuin pienempi suurempaan. Varausten väliset voimat ovat kuitenkin voima ja vastavoima. Ne ovat aina yhtä suuret ja vastakkaissuuntaiset. Coulombin laissa on varausten tulo. Siksi kummankin varauksen kaksinkertaistaminen kaksinkertaistaa saman voiman, joka vaikuttaa molempiin.

Toinen virhe on ajatella, että neutraaliin kappaleeseen ei vaikuta sähköinen voima. Varattu kappale vetää neutraalia kappaletta puoleensa. Influenssi tai polarisoituminen tuo vastakkaismerkkisen varauksen lähemmäs kuin samanmerkkisen. Kolmas virhe on luulla, että hankaus synnyttää varausta. Hankaus vain siirtää elektroneja kappaleesta toiseen. Kokonaisvaraus säilyy.

## Tiivistelmä
- Varaus on alkeisvarauksen monikerta, $Q = ne$, $e = 1{,}602 \cdot 10^{-19}\,\text{C}$. Samanmerkkiset varaukset hylkivät ja erimerkkiset vetävät toisiaan puoleensa.
- Varaus säilyy. Hankauksessa ja kosketuksessa elektroneja vain siirtyy kappaleesta toiseen. Kaksi samanlaista metallipalloa jakaa kosketuksessa yhteisen varauksensa tasan.
- Influenssissa varattu kappale siirtää johteen varauksia. Eristeessä se polarisoi molekyylit. Siksi varattu kappale vetää neutraalia kappaletta puoleensa.
- Sähkövirta on varauksen siirtymistä, $I = Q : t$.
- Pistevarauksen kenttäviivat ovat säteittäisiä: positiivisesta ulospäin ja negatiiviseen sisäänpäin. Kenttä heikkenee etäisyyden kasvaessa.
- Coulombin laki $F = k\,\tfrac{\lvert q_1 q_2 \rvert}{r^2}$: kaksinkertainen etäisyys antaa neljäsosan voimasta. Voima ja vastavoima ovat yhtä suuret. Usean varauksen voimat lasketaan yhteen vektoreina.
