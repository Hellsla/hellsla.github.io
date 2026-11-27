# Sähköturvallisuus kotona ja työssä

> **Miksi** keittiön sulake laukeaa, kun monta laitetta on päällä yhtä aikaa, vaikka mikään niistä ei ole rikki?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: keittiö iltaisin. Työtasolla ovat vedenkeitin, josta nousee höyryä, kahvinkeitin, leivänpaahdin ja mikroaaltouuni, kaikki kytkettyinä seinän pistorasioihin. Vasemmalla seinällä on avattu sähkökeskus, jossa on rivi johdonsuojakatkaisijoita; yksi niistä on lauennut alas. Ikkunasta näkyy iltataivas ja kaukana voimajohtopylväitä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Sulake suojaa johtoa ylikuumenemiselta
Kodin sähköt jaetaan sähkökeskuksessa ryhmiin. Jokaisella ryhmällä on oma ryhmäjohto ja oma sulake, tavallisesti $10\,\text{A}$ tai $16\,\text{A}$. Saman ryhmän pistorasiat ja valaisimet on kytketty rinnan, joten jokaisen laitteen jännite on $230\,\text{V}$ ja laitteiden virrat summautuvat ryhmäjohdossa (luku *Vastusten sarja- ja rinnankytkennät*). Sulake on ryhmäjohdon alussa, joten sen läpi kulkee koko ryhmän virta. Yksittäinen laite voi olla kunnossa, mutta monta laitetta yhdessä ylittää sulakkeen nimellisvirran.

<svg data-fig="ryhma" viewBox="0 0 600 340" role="img" aria-label="Kytkentäkaavio, ei mittakaavassa: kodin yksi sähköryhmä. Vasemmalla vaihtojännitelähde 230 V. Ylempi johdin kulkee lähteestä sulakkeen kautta oikealle, ja siihen on kytketty rinnan kolme laitetta: kaksi vastusta, joiden tehot ovat P1 ja P2, ja lamppu, jonka teho on P3. Laitteiden alapäät on yhdistetty alempaan johtimeen, joka palaa lähteeseen. Violetit nuolet: sulakkeen läpi kulkee koko virta I, ja se jakautuu laitteiden virroiksi I1, I2 ja I3. Alla yhtälö I = I1 + I2 + I3." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-ryhma.webp" x="0" y="-1.2" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="25" y="21.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$230\,\text{V}$</div></foreignObject>
  <foreignObject x="120" y="41.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sulake}$</div></foreignObject>
  <foreignObject x="230" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="236" y="162.5" width="42" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P_1$</div></foreignObject>
  <foreignObject x="330" y="116.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <foreignObject x="346" y="162.5" width="42" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P_2$</div></foreignObject>
  <foreignObject x="440" y="116.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <foreignObject x="444" y="162.5" width="42" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P_3$</div></foreignObject>
  <foreignObject x="550" y="116.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_3$</div></foreignObject>
  <foreignObject x="190" y="301.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I = I_1 + I_2 + I_3$</div></foreignObject>
</svg>

Ryhmäjohdon johtimilla on pieni resistanssi, ja niissä kehittyy lämpöteho $P = RI^2$ (luku *Sähköteho ja vastuksen lämpeneminen*): kun virta kaksinkertaistuu, johdon lämpöteho nelinkertaistuu. Sulakkeen koko valitaan johdon mukaan: johto määrää, kuinka suuren virran sulake saa päästää läpi. Jos virta on pitkään suurempi, johto ja sen liitokset kuumenevat, eriste vaurioituu ja voi syttyä tulipalo. Sulake katkaisee virran ennen sitä. Pieni ylikuorma voi jatkua pitkäänkin, mutta mitä suurempi ylivirta on, sitä nopeammin sulake toimii; oikosulussa virta katkeaa sekunnin murto-osassa. Tulppasulakkeessa ohut lanka sulaa omasta lämpenemisestään, johdonsuojakatkaisija taas laukeaa ja käännetään takaisin päälle. Palanutta sulaketta ei koskaan korvata suuremmalla.

```pysahdy
Ryhmäjohdon virta kasvaa kolminkertaiseksi. Kuinka moninkertaiseksi johdon lämpöteho kasvaa?
---
Lämpöteho on $P = RI^2$, joten se on verrannollinen virran neliöön. Teho kasvaa $3^2 = 9$-kertaiseksi.
```

### Maadoitus ohjaa vikavirran pois ihmisestä
Pistorasian kahteen reikään tulevat vaihejohdin L ja nollajohdin N. Maadoitetussa pistorasiassa on lisäksi suojamaadoituskoskettimet PE, jotka on kytketty keltavihreään suojamaadoitusjohtimeen eli suojajohtimeen. Kiinteistön sähkökeskuksessa suojajohdin on yhdistetty maadoitukseen ja sähköverkosta tulevaan johtimeen, jota pitkin virta palaa sähkönsyöttöön. Johtimien eristeiden värit ovat Suomessa vakiintuneet: uusissa asennuksissa vaihejohdin on yleensä ruskea, nollajohdin sininen ja suojamaadoitusjohdin keltavihreä. Vanhoissa asennuksissa värit voivat poiketa, eikä johtimen väristä saa päätellä, onko se jännitteetön.

<svg data-fig="pistorasia" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva, ei mittakaavassa, kaksi osaa. Vasemmalla maadoitettu pistorasia edestä: pyöreässä syvennyksessä on kaksi reikää vaihe- ja nollajohtimelle sekä ylä- ja alareunassa metalliset suojamaadoituskoskettimet, merkitty PE. Oikealla sähköjohto, jonka kuoresta tulee kolme eristettyä johdinta: ruskea vaihejohdin L, sininen nollajohdin N ja keltavihreä suojamaadoitusjohdin PE." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-pistorasia.webp" x="1.2" y="1.2" width="597" height="338.3" preserveAspectRatio="none"/>
  <foreignObject x="66" y="11.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pistorasia}$</div></foreignObject>
  <foreignObject x="178" y="65.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{PE}$</div></foreignObject>
  <foreignObject x="178" y="237.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{PE}$</div></foreignObject>
  <foreignObject x="385" y="11.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{johto}$</div></foreignObject>
  <foreignObject x="418" y="85.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vaihe}\ \text{L}$</div></foreignObject>
  <foreignObject x="418" y="151.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{nolla}\ \text{N}$</div></foreignObject>
  <foreignObject x="418" y="217.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{maadoitus}\ \text{PE}$</div></foreignObject>
</svg>

Pesukoneen tai vedenkeittimen johtava metallirunko on kytketty pistotulpan kautta suojamaadoitukseen. Jos vaihejohtimen eristys rikkoutuu ja metallirunko tulee jännitteiseksi, vikavirralle muodostuu suojajohtimen kautta pienen resistanssin reitti takaisin sähkönsyöttöön. Suuri vikavirta saa sulakkeen tai johdonsuojakatkaisijan katkaisemaan virran nopeasti. Myös vikavirtasuoja voi katkaista syötön, kun sen havaitsema vikavirta ylittää toimintarajan. Ilman suojamaadoitusta runko jäisi jännitteiseksi, ja virta kulkisi runkoon koskevan ihmisen kautta maahan. Selitys koskee Suomessa tavallista TN-järjestelmää; muissa maadoitusjärjestelmissä vikavirran reitti voi olla erilainen. Siksi maadoituskosketinta ei saa ohittaa, eikä maadoitettua pistotulppaa kytketä maadoittamattomaan pistorasiaan jatkojohdon tai sovittimen avulla.

<svg data-fig="maadoitus" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa, kaksi paneelia. Kummassakin on laite, jonka metallirunko on piirretty auki: ruskea vaihejohdin tulee ylhäältä laitteen vastukselle, mutta sen kulunut kohta koskettaa runkoa, mikä on merkitty kipinällä ja sanalla vika. Ihminen seisoo maassa ja koskettaa kädellään laitteen runkoa. Vasemmalla, ilman maadoitusta, violetti katkoviiva ja nuoli näyttävät virran I kulkevan rungosta ihmisen käden ja kehon kautta jalkoihin ja maahan. Oikealla runkoon on kytketty keltavihreä suojamaadoitusjohdin, ja violetti nuoli näyttää vikavirran kulkevan sitä pitkin ylöspäin takaisin kohti sähkönsyöttöä; teksti: sulake laukeaa. Ihmisen kautta kulkee vain pieni virta, kunnes sulake katkaisee virran." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-maadoitus.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="50" y="9.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ei maadoitusta}$</div></foreignObject>
  <foreignObject x="340" y="9.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{suojamaadoitettu}$</div></foreignObject>
  <foreignObject x="162" y="211.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vika}$</div></foreignObject>
  <foreignObject x="13" y="233.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="462" y="211.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vika}$</div></foreignObject>
  <foreignObject x="526" y="95.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_\text{v}$</div></foreignObject>
  <foreignObject x="20" y="347.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{virta ihmisen kautta}$</div></foreignObject>
  <foreignObject x="350" y="347.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sulake laukeaa}$</div></foreignObject>
</svg>

### Suojausluokat kertovat, miten laite suojaa käyttäjää
Laitteen kilvessä on sen **suojausluokan** merkki. Suojausluokan I laitteessa on johtava runko, joka on suojamaadoitettu, ja sen pistotulpassa on maadoituskoskettimet. Suojausluokan II laitteessa ei ole maadoitusta: jännitteiset osat on erotettu käyttäjästä kaksinkertaisella tai vahvistetulla eristyksellä, ja pistotulppa on usein litteä. Suojausluokan III laite toimii pienellä suojajännitteellä, enintään $50\,\text{V}$ vaihtojännitteellä tai $120\,\text{V}$ tasajännitteellä, joka tulee turvamuuntajasta tai akusta. Tavallisissa oloissa sen kosketus ei aiheuta vaarallista virtaa.

<svg data-fig="luokat" viewBox="0 0 600 300" role="img" aria-label="Suojausluokkien merkit kolmessa sarakkeessa. Vasemmalla luokka I: maadoitusmerkki, eli pystyviiva ja kolme lyhenevää vaakaviivaa, ympyrän sisällä; suojamaadoitus, esimerkiksi pesukone. Keskellä luokka II: kaksi sisäkkäistä neliötä; kaksoiseristys, esimerkiksi hiustenkuivaaja. Oikealla luokka III: vinoneliö, jonka sisällä on roomalainen numero kolme; suojajännite, esimerkiksi akkuporakone." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-luokat.webp" x="15.6" y="6" width="576.9" height="299.3" preserveAspectRatio="none"/>
  <foreignObject x="30" y="165.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{luokka I}$</div></foreignObject>
  <foreignObject x="5" y="201.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maadoitus}$</div></foreignObject>
  <foreignObject x="5" y="241.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{pesukone}$</div></foreignObject>
  <foreignObject x="230" y="165.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{luokka II}$</div></foreignObject>
  <foreignObject x="205" y="201.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kaksoiseristys}$</div></foreignObject>
  <foreignObject x="205" y="241.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{hiustenkuivaaja}$</div></foreignObject>
  <foreignObject x="430" y="165.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{luokka III}$</div></foreignObject>
  <foreignObject x="405" y="201.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{suojajännite}$</div></foreignObject>
  <foreignObject x="405" y="241.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{akkuporakone}$</div></foreignObject>
  <foreignObject x="462" y="88.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{III}$</div></foreignObject>
</svg>

### Vikavirtasuoja suojaa ihmistä
Sulake ei huomaa ihmisen kautta kulkevaa virtaa: sen nimellisvirta on ampeereja, mutta jo kymmenien milliampeerien virta kehon läpi voi olla hengenvaarallinen. Ihmistä se suojaa vain yhdessä suojamaadoituksen kanssa, kun vika aiheuttaa maasulun. Ihmisen kautta kulkevan pienen virran katkaisee **vikavirtasuoja**. Se vertaa vaihejohtimessa laitteeseen menevää virtaa ja nollajohtimessa palaavaa virtaa. Ehjässä piirissä ne ovat yhtä suuret. Jos osa virrasta pääsee vian kautta maahan, esimerkiksi ihmisen kautta, palaava virta on pienempi. Kun ero ylittää laukaisuvirran, tavallisesti $30\,\text{mA}$, suoja katkaisee virran sekunnin murto-osassa. Uusissa asennuksissa pistorasiaryhmät suojataan vikavirtasuojalla, ja sen testipainiketta kannattaa painaa säännöllisesti.

<svg data-fig="vikavirtasuoja" viewBox="0 0 600 360" role="img" aria-label="Kytkentäkaavio, ei mittakaavassa. Vasemmalla vaihtojännitelähde 230 V. Ylempi johdin on vaihejohdin L ja alempi nollajohdin N. Molemmat kulkevat katkoviivalla rajatun vikavirtasuojan läpi, jossa ne kulkevat saman rautarenkaan läpi. Vaihejohtimessa on sen jälkeen sulake. Oikealla laite, jonka metallirungon sisällä on vastus vaihe- ja nollajohtimen välissä; vaihejohtimen ja rungon välissä on vika, merkitty kipinällä. Rungosta kulkee virtatie ihmisen resistanssin R keho kautta maahan. Violetit nuolet: vaihejohtimessa virta I L laitteeseen, nollajohtimessa virta I N takaisin ja ihmisen kautta maahan vikavirta I v. Ylhäällä oikealla yhtälö I L miinus I N on I v." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-vikavirtasuoja.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="16" y="25.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$230\,\text{V}$</div></foreignObject>
  <foreignObject x="71" y="77.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{L}$</div></foreignObject>
  <foreignObject x="71" y="273.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="55" y="311.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vikavirtasuoja}$</div></foreignObject>
  <foreignObject x="209" y="65.5" width="96" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sulake}$</div></foreignObject>
  <foreignObject x="313.5" y="49.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_\text{L}$</div></foreignObject>
  <foreignObject x="313.5" y="301.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_\text{N}$</div></foreignObject>
  <foreignObject x="365" y="175.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{laite}$</div></foreignObject>
  <foreignObject x="436" y="257.5" width="76" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_\text{keho}$</div></foreignObject>
  <foreignObject x="552" y="167.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_\text{v}$</div></foreignObject>
  <foreignObject x="420" y="17.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$I_\text{L} - I_\text{N} = I_\text{v}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/residual-current-device.webp" alt="Valkoinen nelinapainen vikavirtasuoja mustalla taustalla: keltainen TEST-painike, musta vipu ja ruuviliittimet ylä- ja alareunassa; kyljessä on merkinnät jännitteestä, laukaisuvirrasta ja nimellisvirrasta."><figcaption>Vikavirtasuoja. Merkintä $I_{\Delta n} = 0{,}03\,\text{A}$ kertoo, että suoja katkaisee virran, kun vaihe- ja nollajohtimen virtojen ero on $30\,\text{mA}$. Keltaisesta TEST-painikkeesta suojan toiminta kokeillaan säännöllisesti.</figcaption></figure>

Vikavirtasuoja ei estä kaikkia iskuja. Jos ihminen koskettaa yhtä aikaa vaihejohdinta ja nollajohdinta, virta palaa nollajohdinta pitkin, eikä vaihe- ja nollajohtimen virtojen välille synny eroa. Siksi jännitteisiin osiin ei kosketa, vaikka ryhmässä olisi vikavirtasuoja.

```pysahdy
Mitä kahta virtaa vikavirtasuoja vertaa, ja milloin se katkaisee virran?
---
Se vertaa vaihejohtimen ja nollajohtimen virtaa. Kun virtojen ero ylittää laukaisuvirran, tavallisesti $30\,\text{mA}$, se katkaisee virran.
```

### Eristeen läpilyöntilujuus
Johtojen muovikuori, pistotulpan runko ja suurjännitejohtojen eristimet erottavat jännitteiset osat ihmisestä. Jokainen eriste kestää kuitenkin vain tietyn suuruisen sähkökentän. Kun kenttä ylittää eristeen **läpilyöntilujuuden**, eriste alkaa johtaa ja sen läpi purkautuu kipinä (luku *Kondensaattori ja sen energia*). Tasaisessa kentässä eristekerros, jonka paksuus on $d$, kestää jännitteen $E_\text{max} d$. Siksi suurempi jännite vaatii paksumman eristeen tai pidemmän ilmavälin, ja eristeen pitää olla ehjä: halkeama, kosteus tai lika heikentää eristystä.

### Suurjännitejohdot ja askeljännite
Sähkö siirretään voimalaitoksilta suurella jännitteellä, kantaverkossa jopa $400\,\text{kV}$:lla, koska samalla teholla suuri jännite tarkoittaa pientä virtaa ja siten pieniä lämpöhäviöitä $RI^2$ johdoissa. Suurjännitejohtimet ovat paljaita, ja niitä eristää ympäröivä ilma. Ilman läpilyöntilujuus on noin $3\,\text{MV/m}$, joten johdinta ei tarvitse koskettaa saadakseen iskun: valokaari voi hypätä johtimesta lähelle tuotuun esineeseen, kuten nostokoneen puomiin, onkivapaan tai leijan naruun. Junien ajojohdossa jännite on $25\,\text{kV}$, joten vaunujen katolle ei kiivetä.

Lintu voi istua paljaalla johtimella, koska sen molemmat jalat ovat lähes samassa potentiaalissa: jalkojen välinen potentiaaliero on hyvin pieni, joten linnun kautta kulkee vain erittäin pieni virta. Vaara syntyy, kun keho yhdistää kaksi eri potentiaalissa olevaa kohtaa, esimerkiksi johtimen ja maan.

Jos johdin putoaa maahan, virta leviää maaperään. Maan potentiaali on suurin kosketuskohdassa ja pienenee etäisyyden kasvaessa, joten eri kohtien välillä on jännite. Ihmisen jalkojen välistä jännitettä kutsutaan **askeljännitteeksi**: se on sitä suurempi, mitä lähempänä kosketuskohtaa ollaan ja mitä pidempi askel on. Pudonneen johtimen luota poistutaan lyhyin askelin jalat yhdessä tai tasajalkaa hyppien, johdinta ei lähestytä, ja vahingosta ilmoitetaan hätänumeroon $112$.

<svg data-fig="askel" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, ei mittakaavassa: maahan pudonnut sähköjohto ja askeljännite. Vasemmalla puupylväs, jonka katkennut johdin on pudonnut maahan; putoamiskohdassa on kipinä. Maan sisällä putoamiskohdan ympärillä on sisäkkäisiä katkoviivakaaria, joilla potentiaali on sama; väri vaalenee punertavasta hiekanväriseksi kauemmas mentäessä, ja nuoli kertoo, että potentiaali pienenee. Keskellä ihminen ottaa pitkän askeleen: hänen jalkansa ovat eri kaarilla, ja jalkojen välillä on askeljännite U askel. Oikealla ihminen seisoo jalat yhdessä, ja hänen jalkojensa välinen jännite on lähes nolla." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-askel.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="255" y="227.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U_\text{askel}$</div></foreignObject>
  <foreignObject x="445" y="227.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U \approx 0$</div></foreignObject>
  <foreignObject x="255" y="267.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{potentiaali pienenee}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/high-voltage-sign.webp" alt="Keltainen kolmion muotoinen varoitusmerkki, jossa on musta reunus ja musta salamanuoli, valkoisella pinnalla."><figcaption>Salamanuolimerkki varoittaa vaarallisesta jännitteestä. Se on esimerkiksi sähkökeskuksen kannessa: kannen takana on jännitteisiä osia, joihin ei saa koskea.</figcaption></figure>

### Turvallinen toiminta kotona ja työssä
Suomessa varsinaisia sähköasennustöitä saavat tehdä vain sähköalan ammattilaiset, ja töitä tekevän yrityksen on oltava Turvallisuus- ja kemikaalivirasto Tukesin rekisterissä sähköurakoitsijana. Maallikko eli sähköalan koulutusta vailla oleva sähkönkäyttäjä saa tehdä vain erikseen sallittuja vähäisiä sähkötöitä, ja niitäkin ainoastaan silloin, kun hän varmasti osaa tehdä työn turvallisesti ja tuntee siihen liittyvät ohjeet. Tällaisia töitä ovat esimerkiksi sulakkeen ja lampun vaihtaminen, lauenneen johdonsuojakatkaisijan tai vikavirtasuojan palauttaminen, yksivaiheisen jatkojohdon korjaaminen, sähkölaitteen rikkoutuneen yksivaiheisen liitäntäjohdon ja pistotulpan vaihtaminen sekä sisustusvalaisimen liittäminen valaisinliittimellä. Työt tehdään aina jännitteettöminä. Ajantasainen luettelo sallituista töistä on Tukesin verkkosivuilla. Epävarmassa tilanteessa työ jätetään sähköalan ammattilaiselle.

Työpaikoilla, kuten rakennustyömailla, jatkojohdot ja laitteet tarkastetaan, kosteissa paikoissa käytetään vikavirtasuojaa tai suojajännitettä, ja vioittunut laite poistetaan käytöstä. Jos laite haisee palaneelta, kuumenee tavallista enemmän tai antaa pieniä sähköiskuja, sen pistotulppa irrotetaan ja laite viedään korjattavaksi. Jos joku jää kiinni jännitteiseen osaan, virta katkaistaan ensin, ennen kuin häneen kosketaan, ja soitetaan hätänumeroon $112$.

## Kaava: Ryhmäjohdon virta ja kosketusvirta
Ryhmän laitteet ovat rinnan samassa jännitteessä, joten jokaisen laitteen virta on $I_k = P_k : U$, ja ryhmäjohdossa ja sulakkeessa kulkee niiden summa:
```latex
I = \frac{P_1 + P_2 + P_3 + \dots}{U}
```
missä $I$ on ryhmäjohdon kokonaisvirta ($\text{A}$), $P_1, P_2, \dots$ samaan aikaan päällä olevien laitteiden tehot ($\text{W}$) ja $U$ verkkojännite $230\,\text{V}$. Verkkojännite on vaihtojännitteen tehollinen arvo. Tässä luvussa tarkastellaan laitteita, joiden virta ja jännite ovat samanvaiheiset, kuten lämmittäviä laitteita, tai joiden tehokerroin oletetaan likimain yhdeksi. Silloin teho lasketaan kaavalla $P = UI$ kuten tasajännitteellä. Yleisesti vaihtovirtapiirin pätöteho riippuu myös jännitteen ja virran vaihe-erosta. Ryhmä ei ole ylikuormitettu, kun $I$ on enintään sulakkeen nimellisvirta $I_\text{s}$. Laitteiden yhteisteho saa siis olla $10\,\text{A}$:n ryhmässä enintään $230\,\text{V} \cdot 10\,\text{A} = 2300\,\text{W}$ ja $16\,\text{A}$:n ryhmässä $230\,\text{V} \cdot 16\,\text{A} = 3680\,\text{W}$.

```pysahdy
Samassa ryhmässä ovat päällä silitysrauta ($1{,}1\,\text{kW}$) ja kahvinkeitin ($0{,}70\,\text{kW}$). Kuinka suuri on ryhmäjohdon virta?
---
$I = \tfrac{P_1 + P_2}{U}$. Sijoitus: $\tfrac{1100\,\text{W} + 700\,\text{W}}{230\,\text{V}} \approx 7{,}8\,\text{A}$.
```

### Kehon läpi kulkeva virta
Kun ihminen koskettaa jännitteistä osaa ja samalla maata, hänen kehonsa on osa virtapiiriä. Kehon läpi kulkeva virta saadaan Ohmin laista (luku *Resistanssi ja Ohmin laki*):
```latex
I = \frac{U}{R}
```
missä $I$ on kehon läpi kulkeva virta ($\text{A}$), $U$ kosketusjännite eli jännite kosketuskohtien välillä ($\text{V}$) ja $R$ koko virtatien resistanssi ($\Omega$): ihon, kehon sisäosien sekä kenkien ja lattian resistanssit sarjassa.

Kehon resistanssi ei ole vakio. Suurin osa siitä on ihossa, ja se riippuu ihon kosteudesta, kosketuspinnan koosta, virran reitistä ja jännitteestä. Kuivalla iholla ja eristävillä kengillä virtatien resistanssi voi olla satoja kilo-ohmeja. Märkä tai hikinen iho, suuri kosketuspinta ja paljaat jalat märällä lattialla pienentävät sen noin kilo-ohmiin, jolloin $230\,\text{V}$:n kosketusjännite antaa virran $230\,\text{V} : 1\,\text{k}\Omega \approx 230\,\text{mA}$. Kehon sisäosien resistanssi on vain satojen ohmien luokkaa.

Kengät pienentävät virtaa vain, jos ne ovat ehjät ja kuivat, lattia on kuiva eikä ihminen koske samalla mihinkään muuhun maadoitettuun, kuten hanaan tai maadoitettuun laitteeseen: silloin virta kulkee kenkien ohi. Kenkiä ei saa pitää sähköiskulta suojaavana varusteena.

| $I$ (noin) | vaikutus |
| --- | --- |
| $0{,}5\,\text{mA}$ | virta tuntuu |
| $10\,\text{mA}$ | ote ei irtoa |
| $30\,\text{mA}$ | hengitys vaikeutuu |
| yli $50\,\text{mA}$ | kammiovärinän vaara |

Noin $0{,}5\,\text{mA}$ on tuntokynnys. Noin $10\,\text{mA}$:n virta kouristaa lihakset niin, ettei otteesta välttämättä pääse irti: se on irrottamiskynnys. Yli $50\,\text{mA}$:n virta voi aiheuttaa sydämen kammiovärinän, jos se kestää noin sekunnin; lyhyempi isku vaatii suuremman virran.

Taulukko koskee kodin $50\,\text{Hz}$:n vaihtovirtaa. Vikavirtasuojan tavallinen laukaisuvirta $30\,\text{mA}$ on valittu niin, että suoja katkaisee virran yleensä ennen kuin se ehtii aiheuttaa kammiovärinää. Arvot ovat suuntaa antavia, ja ne perustuvat kansainvälisen standardin IEC 60479-1 kuvaamiin virran vaikutuksiin aikuiseen. Vaikutus riippuu myös virran kestosta ja reitistä sekä ihmisestä, eikä mitään virtaa voi pitää varmasti turvallisena.

<svg data-fig="vaikutukset" viewBox="0 0 600 360" role="img" aria-label="Asteikko, ei lineaarinen: kehon läpi kulkevan 50 hertsin vaihtovirran I suuruus milliampeereina logaritmisella pystyakselilla 0,1 mA:sta 1000 mA:iin, jokainen kymmenkertaistus yhtä pitkä väli. Akselin vieressä väripalkki: alle 0,5 mA vihreä, 0,5–10 mA vaaleanoranssi, 10–50 mA oranssi ja yli 50 mA punainen. Merkinnät: 0,5 mA virta tuntuu, 10 mA ote ei irtoa, 30 mA hengitys vaikeutuu, 50 mA kammiovärinän vaara. Suuntaa antavat arvot." style="max-width:100%;font-size:24px">
  <line x1="140" y1="334" x2="140" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M140,32 L133,48 L147,48 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="95" y="3.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I\ (\text{mA})$</div></foreignObject>
  <line x1="134" y1="330" x2="140" y2="330" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="315.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$0{,}1$</div></foreignObject>
  <line x1="134" y1="264" x2="140" y2="264" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="249.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <line x1="134" y1="198" x2="140" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="183.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$10$</div></foreignObject>
  <line x1="134" y1="132" x2="140" y2="132" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="117.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$100$</div></foreignObject>
  <line x1="134" y1="66" x2="140" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="51.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$1000$</div></foreignObject>
  <rect x="146" y="284" width="26" height="46" fill="#b2f2bb" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="146" y="198" width="26" height="86" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="146" y="152" width="26" height="46" fill="#e8590c" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="146" y="66" width="26" height="86" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="172" y1="284" x2="190" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="284" x2="202" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210" y="269.5" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0{,}5\,\text{mA}\ \ \text{virta tuntuu}$</div></foreignObject>
  <line x1="172" y1="198" x2="190" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="198" x2="202" y2="212" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210" y="197.5" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10\,\text{mA}\ \ \text{ote ei irtoa}$</div></foreignObject>
  <line x1="172" y1="166.5" x2="190" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="166.5" x2="202" y2="172.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210" y="158" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$30\,\text{mA}\ \ \text{hengitys vaikeutuu}$</div></foreignObject>
  <line x1="172" y1="152" x2="190" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="152" x2="202" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210" y="111.5" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$50\,\text{mA}\ \ \text{kammiovärinän vaara}$</div></foreignObject>
</svg>

## Esimerkki
Keittiön pistorasiaryhmä on suojattu $16\,\text{A}$:n sulakkeella. Aamulla päällä ovat yhtä aikaa vedenkeitin ($2{,}2\,\text{kW}$), kahvinkeitin ($1{,}0\,\text{kW}$) ja mikroaaltouuni, jonka ottoteho on $1{,}3\,\text{kW}$. Kuinka suuri virta ryhmäjohdossa kulkee, ja ylittyykö sulakkeen nimellisvirta?

<!-- vaihe -->

**Tunnetut ja kysytty.** $P_1 = 2{,}2\,\text{kW}$, $P_2 = 1{,}0\,\text{kW}$, $P_3 = 1{,}3\,\text{kW}$, $U = 230\,\text{V}$, sulakkeen nimellisvirta $I_\text{s} = 16\,\text{A}$.

Kysytään ryhmäjohdon virtaa $I$ ja sitä, onko $I > I_\text{s}$.

<!-- vaihe -->

**Periaate.** Laitteet on kytketty samaan ryhmään rinnan, joten jokaisen jännite on $230\,\text{V}$ ja niiden virrat summautuvat ryhmäjohdossa ja sulakkeessa. Siksi kokonaisvirta lasketaan laitteiden yhteistehosta.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
I = \frac{P_1 + P_2 + P_3}{U}
```

<!-- vaihe -->

**Yksikkömuunnokset.** $$\begin{aligned} &P_1 + P_2 + P_3 \\ &= 2{,}2\,\text{kW} + 1{,}0\,\text{kW} + 1{,}3\,\text{kW} \\ &= 4{,}5\,\text{kW} \\ &= 4{,}5 \cdot 1000\,\text{W} \\ &= 4500\,\text{W} \end{aligned}$$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
I &= \frac{P_1 + P_2 + P_3}{U} \\
&= \frac{4500\,\text{W}}{230\,\text{V}} \\
&= 19{,}6\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ryhmäjohdossa kulkee noin $20\,\text{A}$:n virta, kaksi merkitsevää numeroa kuten tehoissa. Se on suurempi kuin sulakkeen nimellisvirta $16\,\text{A}$, joten ryhmä on ylikuormitettu. Näin pieni ylivirta ei katkaise virtaa heti, mutta sulake laukeaa, jos kuormitus jatkuu riittävän kauan. Laitteita kannattaa käyttää vuorotellen.

<!-- vaihe -->

**Järkevyys.** Laitteiden omat virrat ovat $9{,}6\,\text{A}$, $4{,}3\,\text{A}$ ja $5{,}7\,\text{A}$, ja niiden summa on sama $19{,}6\,\text{A}$. Arvio $4500\,\text{W} : 200\,\text{V} \approx 22\,\text{A}$ on hieman suurempi, koska jakaja on pienempi. Yksikään laite ei yksin ylitä $16\,\text{A}$:ä; vain yhteinen virta ylittää.

## Yleinen virhekäsitys
Moni ajattelee, että sulake suojaa ihmistä sähköiskulta. Sulake suojaa johtoja: sen nimellisvirta on $10\,\text{A}$ tai $16\,\text{A}$, kun taas jo noin $50\,\text{mA}$:n virta kehon läpi voi aiheuttaa sydämen kammiovärinän. Sulake ei huomaa ihmisen kautta kulkevaa niin pientä virtaa lainkaan. Ihmistä se suojaa vain yhdessä suojamaadoituksen kanssa: runkoviassa suuri vikavirta kulkee suojajohdinta pitkin takaisin sähkönsyöttöön, ja sulake katkaisee sen. Ihmisen kautta kulkevan pienen virran katkaisee vikavirtasuoja, joka laukeaa noin $30\,\text{mA}$:n vikavirrasta.

Toinen virhe on ajatella, että suuri jännite yksin on vaarallinen tai pieni jännite aina turvallinen. Vahingon tekee kehon läpi kulkeva virta, joka riippuu sekä jännitteestä että virtatien resistanssista. Lintu istuu turvassa $20\,\text{kV}$:n johtimella, koska sen jalkojen välinen potentiaaliero on hyvin pieni, mutta märkä iho voi tehdä pienemmästäkin jännitteestä vaarallisen.

## Tiivistelmä
- Saman ryhmän laitteet ovat rinnan, joten sulakkeen läpi kulkee niiden yhteinen virta $I = (P_1 + P_2 + \dots) : U$. Sulake suojaa johtoa ylikuumenemiselta, koska johdon lämpöteho on $RI^2$.
- Suojamaadoitus yhdistää laitteen metallirungon suojajohtimeen. Runkovian vikavirta kulkee keltavihreää suojajohdinta pitkin takaisin sähkönsyöttöön, jolloin sulake tai johdonsuojakatkaisija katkaisee virran. Suojausluokat ovat I (maadoitus), II (kaksoiseristys) ja III (suojajännite).
- Vikavirtasuoja vertaa vaihe- ja nollajohtimen virtoja ja katkaisee virran, kun ero ylittää noin $30\,\text{mA}$.
- Kehon läpi kulkeva virta on $I = U : R$. Märkä iho pienentää resistanssia, ja jo kymmenien milliampeerien virta voi olla hengenvaarallinen.
- Eriste kestää kentän vain läpilyöntilujuuteen asti; suurjännitejohdosta valokaari voi hypätä ilman kosketusta. Maahan pudonneen johtimen lähellä askeljännite on vaarallinen.
- Suomessa varsinaiset sähköasennustyöt kuuluvat sähköalan ammattilaisille. Maallikko saa tehdä vain erikseen sallittuja vähäisiä töitä, kuten vaihtaa sulakkeen, ja vain jos hän osaa tehdä työn turvallisesti.
