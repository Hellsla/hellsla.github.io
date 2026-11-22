# Soveltava luku: langaton lataus, induktioliesi ja kuituyhteys

> **Miksi** puhelin latautuu ilman johtoa, kattila kuumenee ilman liekkiä ja nettiyhteys kulkee valona lasikuidussa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: keittiön työtaso. Keskellä on musta induktioliesi. Sen keittoalueella on teräskattila, ja kattilasta nousee höyryä. Oikealla puhelin lepää pyöreän langattoman laturin päällä. Vasemmalla seinällä on kuitureititin. Siihen tulee ohut valokaapeli, ja kaapelin pää hehkuu." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-16-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Kolme laitetta, kaksi ilmiötä
Keittiön kolme arkista laitetta toimivat tämän kurssin ilmiöillä. Langaton laturi ja induktioliesi perustuvat **sähkömagneettiseen induktioon**. Siinä muuttuva magneettivuo synnyttää jännitteen johdinsilmukkaan tai pyörrevirtoja metalliin (luvut *Sähkömagneettinen induktio* ja *Lenzin laki ja pyörrevirrat*). Pyörrevirta on sähkövirta, joka kiertää metallikappaleen sisällä.

Kuituyhteys perustuu **kokonaisheijastumiseen**. Valo pysyy kuidun ytimessä, koska se osuu ytimen ja kuoren rajapintaan rajakulmaa suuremmalla tulokulmalla (luku *Kokonaisheijastuminen ja valokuitu*). Tässä luvussa ideat yhdistetään. Kysymme kolmea asiaa: missä laitteessa energiaa siirtyy, mihin energiaa häviää ja mikä rajoittaa laitteen toimintaa.

### Langaton lataus: muuntaja ilman rautasydäntä
Langattoman laturin alustassa on litteä **lähetinkäämi**. Puhelimen takakuoren alla on samanlainen **vastaanotinkäämi**. Lähetinkäämissä kulkee vaihtovirta. Qi-standardin latureissa sen taajuus on noin $100$–$200\,\text{kHz}$. Virta synnyttää vaihtuvan magneettikentän, ja osa kentän vuosta kulkee vastaanotinkäämin läpi.

Kun vuo muuttuu, vastaanotinkäämiin indusoituu vaihtojännite. Jännite noudattaa induktiolakia: jännitteen hetkellinen arvo riippuu siitä, kuinka nopeasti vuo muuttuu kullakin hetkellä. Puhelimen elektroniikka tasasuuntaa jännitteen eli muuttaa sen tasajännitteeksi, ja sillä ladataan akkua. Laite on kuin muuntaja (luku *Muuntaja ja sähköenergian siirto*), mutta käämejä ei yhdistä rautasydän. Niiden välissä on vain ilmaa ja muovia.

### Miksi etäisyys ratkaisee
Muuntajassa rautasydän ohjaa lähes koko vuon toisiokäämin läpi. Ilman sydäntä lähetinkäämin kenttäviivat kiertävät käämin johtimien ympäri ja kääntyvät takaisin jo lähellä käämiä. Kun puhelin on aivan alustan päällä, suuri osa vuosta kulkee vastaanottimen läpi. Kun puhelinta nostetaan, yhä harvempi kenttäviiva yltää vastaanottimeen asti. Silloin vuo ja jännite pienenevät jyrkästi.

Kuvassa vihreät viivat ovat lähetinkäämin kenttäviivoja. Vihreä kolmio näyttää kentän suunnan käämin keskellä. Vastaanotinkäämin läpi kulkevat viivat on piirretty tummemmin. Siksi laturin ja puhelimen väli on vain muutamia millimetrejä.

Käämien taakse asetetaan ohut ferriittilevy. Ferriitti on aine, joka magnetoituu ferromagneettisen aineen tavoin, mutta se johtaa sähköä huonosti. Siksi siihen ei synny suuria pyörrevirtoja. Levy kokoaa kenttää käämien väliin ja estää kenttää kuumentamasta puhelimen metalliosia.

<svg data-fig="charger" viewBox="0 0 600 380" role="img" aria-label="Periaatekuva langattomasta laturista sivulta leikattuna. Kentän muoto on laskettu. Kuvassa on kaksi paneelia. Kummassakin alhaalla on latausalusta, jonka sisällä on lähetinkäämi. Sen yläpuolella on puhelin, jonka pohjassa on samankokoinen vastaanotinkäämi. Lähetinkäämin vaihtovirta synnyttää magneettikentän. Kentän vihreät kenttäviivat kiertävät käämin johtimien ympäri ja kulkevat käämin keskeltä ylöspäin. Vihreä kolmio käämin keskellä näyttää kentän suunnan. Vasemmalla puhelin on 3 millimetrin päässä, ja kuusi kenttäviivaa kulkee vastaanotinkäämin läpi. Oikealla puhelin on 20 millimetrin päässä, ja vastaanottimen läpi kulkee vain yksi viiva. Muut viivat kääntyvät takaisin jo ennen puhelinta. Vastaanottimen läpi kulkevat viivat on piirretty tummemmin." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-16-charger.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="102.5" y="214.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{puhelin}$</span></div></foreignObject>
  <foreignObject x="402.5" y="146.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{puhelin}$</span></div></foreignObject>
  <foreignObject x="75" y="17.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$z = 3\,\text{mm}$</div></foreignObject>
  <foreignObject x="370" y="17.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$z = 20\,\text{mm}$</div></foreignObject>
  <foreignObject x="100" y="303.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{laturi}$</div></foreignObject>
  <foreignObject x="400" y="303.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{laturi}$</div></foreignObject>
  <foreignObject x="8" y="337.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lähetinkäämi}$</div></foreignObject>
  <foreignObject x="306" y="85.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vastaanotinkäämi}$</div></foreignObject>
</svg>

```pysahdy
Puhelin nostetaan langattoman laturin päältä $3\,\text{mm}$:n korkeudelta $20\,\text{mm}$:n korkeudelle. Miksi vastaanotinkäämin jännite pienenee, vaikka lähetinkäämin virta pysyy samana?
---
Vastaanottimen läpi kulkee vähemmän kenttäviivoja, joten vuo pienenee. Silloin myös indusoitunut jännite pienenee.
```

### Hukka langattomassa latauksessa
Vastaanottimeen saadaan riittävä jännite, vaikka vain osa vuosta osuu siihen. Silloin lähetinkäämissä on kuitenkin kuljettava suurempi virta. Virta muuttaa käämien resistanssissa sähköenergiaa sisäenergiaksi teholla $P = RI^2$, joten laturi ja puhelin lämpenevät.

Eräässä vuonna 2020 tehdyssä laitevertailussa (Ravenscraft, OneZero, 2020) puhelimen lataaminen tyhjästä täyteen otti pistorasiasta johdolla $14{,}26\,\text{Wh}$. Kohdalleen asetetulla latausalustalla se vei keskimäärin $21{,}01\,\text{Wh}$ eli noin $47\,\%$ enemmän energiaa. Kun käämit olivat vähän sivussa toisistaan, lataus vei $25{,}62\,\text{Wh}$. Ero riippuu kuitenkin laturista, puhelimesta, lataustavasta ja käämien kohdistuksesta. Siksi luvut eivät päde kaikkiin langattomiin latureihin.

Jos laturin ja puhelimen välissä on kolikko tai avain, siihen syntyy pyörrevirtoja ja se kuumenee. Siksi laturi tunnistaa vieraan metalliesineen ja keskeyttää latauksen.

### Induktioliesi: kattilan pohja toisiopuolena
Induktiolieden lasilevyn alla on litteä kuparikela. Kelassa kulkee vaihtovirta, jonka taajuus on kymmeniä kilohertsejä. Kelan vaihtuva magneettikenttä kulkee lasin läpi kattilan pohjaan. Pohjan läpi kulkeva vuo muuttuu jatkuvasti, joten pohjaan indusoituu pyörrevirtoja. Lenzin lain mukaan ne kiertävät niin, että niiden oma kenttä vastustaa vuon muutosta.

Pohjan resistanssissa pyörrevirtojen sähköenergia muuttuu pohjan sisäenergiaksi, ja kuuma pohja lämmittää ruoan. Induktioliesi toimii siis samaan tapaan kuin muuntaja. Kattilan metallipohja on muuntajan toisiopuoli. Pohjaan ei kuitenkaan synny yhtä tavallisen käämin kierrosta. Muuttuva magneettikenttä synnyttää pohjaan monta pyörrevirtojen reittiä.

Lasi ei johda sähköä, joten siihen ei synny virtoja. Lasi lämpenee vain siksi, että kuuma kattila lämmittää sen.

<svg data-fig="hob" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva induktioliedestä sivulta leikattuna, ei mittakaavassa. Ylhäällä on teräskattila, jossa on vettä. Kattila seisoo lieden lasilevyllä, ja lasin alla on litteä kuparikela. Kelan vaihtovirta synnyttää vaihtuvan magneettikentän. Kentän vihreät kenttäviivat kiertävät kelan johtimien ympäri, ja uloimmat kulkevat lasin läpi kattilan pohjaan. Kattilan pohjassa kiertää pyörrevirta vastakkaiseen suuntaan kuin kelan virta. Kelan virran suunta on merkitty kuparinvärisiin johtimiin valkoisilla pisteillä ja risteillä. Pyörrevirran suunta on merkitty violetteihin merkkeihin. Oranssit nuolet näyttävät, että energia siirtyy kuumenevasta pohjasta veteen. Lasilevyssä ei kulje virtaa." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-16-hob.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="470" y="85.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vesi}$</div></foreignObject>
  <foreignObject x="12" y="105.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{teräskattila}$</div></foreignObject>
  <foreignObject x="20" y="285.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lasi}$</div></foreignObject>
  <foreignObject x="522" y="285.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kela}$</div></foreignObject>
  <foreignObject x="443" y="125.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{pyörrevirta}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/induction-hob.webp" alt="Musta keittotaso, jossa on neljä keittoaluetta. Takana on kattila."><figcaption>Induktioliesi. Lasin alla on käämi, jossa kulkee vaihtovirta. Sen magneettikenttä tekee kattilan pohjaan pyörrevirtoja. Kattila lämpenee itse. Taso lämpenee vain kattilan takia.</figcaption></figure>

```pysahdy
Induktioliedellä lasilevy ei ole kuuma ennen kuin kattila on kuumentunut sen päällä. Miksi lasiin ei tule pyörrevirtoja?
---
Lasi ei johda sähköä, joten muuttuva magneettikenttä ei saa siinä aikaan virtaa. Lasi lämpenee vasta, kun kuuma kattila lämmittää sitä.
```

### Miksi kattilan on oltava terästä tai valurautaa
Tavalliset kotien induktioliedet on suunniteltu kattiloille, joiden pohjassa on ferromagneettista ainetta, kuten terästä tai valurautaa. Induktiolämmitys ei kuitenkaan aina vaadi ferromagneettista ainetta. Myös muut johteet lämpenevät, jos laite on suunniteltu niille. Ferromagneettinen pohja vahvistaa kelan kenttää ja kokoaa vuon itseensä (luku *Magneetit, magneettinen dipoli ja magneettikenttä*).

Lisäksi teräs johtaa sähköä huonommin kuin alumiini. Pyörrevirrat kulkevat teräksessä vain ohuessa pintakerroksessa, jonka resistanssi on suuri. Siksi pohjan sisäenergia kasvaa nopeasti samalla kelan virralla.

Alumiini ja kupari eivät ole ferromagneettisia, ja ne johtavat sähköä erittäin hyvin. Niissä pyörrevirrat leviävät paksummalle alueelle ja resistanssi jää pieneksi. Siksi lämpenemistä tulee vähän. Tavallinen induktioliesi tunnistaa sopimattoman kattilan eikä yleensä käynnisty alumiinikattilalla. Monessa kattilassa on pohjan alla teräslevy juuri tätä varten.

### Kuituyhteys: valo kulkee lasissa
Kuituyhteydessä lähetin muuttaa tiedon infrapunavalon pulsseiksi. Pulssit etenevät hiuksen paksuisen kuidun ytimessä kokonaisheijastuen. Ytimen taitekerroin on hieman suurempi kuin kuoren, ja lähes akselin suuntainen valo osuu ytimen seinään rajakulmaa suuremmalla tulokulmalla.

Lasissa, jonka taitekerroin on $1{,}47$, valo etenee nopeudella $v = c : n$. Siksi jokainen kilometri viivästyttää signaalia noin $4{,}9\,\mu\text{s}$.

Kokonaisheijastuminen ei hukkaa valoa, mutta lasi itse vaimentaa sitä. Osa valosta absorboituu eli jää lasiin. Osa siroaa sivuille lasin pienistä tiheysvaihteluista. Kvartsilasin vaimennus on pienin noin $1550\,\text{nm}$:n aallonpituudella, joten pitkät yhteydet käyttävät sitä.

### Vaimennus rajoittaa yhteyden pituutta
Yleisen tietoliikennekuidun vaimennus on valmistajan mukaan enintään $0{,}18\,\text{dB/km}$ aallonpituudella $1550\,\text{nm}$ ja $0{,}32\,\text{dB/km}$ aallonpituudella $1310\,\text{nm}$ (Corning, SMF-28 Ultra -kuidun tuotetiedote, 2016). Vaimennus kertoo, kuinka paljon valon teho pienenee.

Desibeli on tuttu luvusta *Intensiteetti ja desibeliasteikko* (FY5). Jokainen $10\,\text{dB}$ tarkoittaa, että teho pienenee kymmenesosaan. Noin $3\,\text{dB}$ puolittaa tehon. Aallonpituudella $1550\,\text{nm}$ teho siis puolittuu noin $17\,\text{km}$:n matkalla. Matkan $100\,\text{km}$ jälkeen tehosta on jäljellä alle $2\,\%$.

Vastaanotin tunnistaa pulssit vielä hyvin heikostakin valosta. Pitkillä yhteyksillä valo on silti vahvistettava optisella vahvistimella noin $50$–$100\,\text{km}$:n välein.

## Kaava: Vaimennus desibeleinä
Kun valon teho kuidun alussa on $P_0$ ja lopussa $P$, kuidun **vaimennus** desibeleinä on
```latex
\begin{aligned}
&A = 10\,\text{dB} \cdot \lg \frac{P_0}{P} \\[6pt]
&A = aL
\end{aligned}
```
missä $A$ on vaimennus ($\text{dB}$), $\lg$ kymmenkantainen logaritmi, $a$ kuidun vaimennuskerroin ($\text{dB/km}$) ja $L$ kuidun pituus ($\text{km}$). Vaimennuskerroin kertoo, kuinka monta desibeliä yksi kilometri vaimentaa. Kaava $A = aL$ pätee, kun kuitu on koko matkalta samanlaista.

Peräkkäisten osuuksien vaimennukset desibeleinä lasketaan yhteen. Niiden tehojen suhteet kerrotaan keskenään. Kaksi peräkkäistä $10\,\text{dB}$:n osuutta vaimentavat yhteensä $20\,\text{dB}$. Teho pienenee ensin kymmenesosaan ja sitten siitä vielä kymmenesosaan, eli sadasosaan. Liitokset ja jyrkät mutkat lisäävät vaimennusta, ja ne lisätään samalla tavalla.

Kuvaajasta näkyy, että teho pienenee joka kilometrillä samassa suhteessa. Siksi käyrät eivät ole suoria vaan loivenevat.

<svg data-fig="graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa. Se näyttää valokuidun läpi kulkevan valon tehon prosentteina lähetetystä tehosta kuidun pituuden funktiona matkalla 0–25 kilometriä. Yhtenäinen käyrä on aallonpituudelle 1550 nm, vaimennus on 0,18 dB/km. Teho laskee 25 kilometrissä 35 prosenttiin. Katkoviivakäyrä on aallonpituudelle 1310 nm, vaimennus on 0,32 dB/km. Teho laskee 16 prosenttiin. Katkoviivoilla on merkitty, että 1550 nanometrin valon teho puolittuu 16,7 kilometrin matkalla." style="max-width:100%;font-size:24px">
  <line x1="163" y1="286" x2="163" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="229.5" y1="286" x2="229.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296.5" y1="286" x2="296.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="363" y1="286" x2="363" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="286" x2="430" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="242" x2="430" y2="242" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="198" x2="430" y2="198" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="154" x2="430" y2="154" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="110" x2="430" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="66" x2="430" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="444" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,286 L443,292 L443,280 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,40 L102,53 L90,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="163" y1="286" x2="163" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="153" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="229.5" y1="286" x2="229.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="213" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="296.5" y1="286" x2="296.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="280" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="363" y1="286" x2="363" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="346.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="430" y1="286" x2="430" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="413.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="89" y1="242" x2="96" y2="242" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="227.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="198" x2="96" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="183.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="154" x2="96" y2="154" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="139.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="89" y1="110" x2="96" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="95.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="89" y1="66" x2="96" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="51.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="66" y="291.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="462" y="271.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L\ (\text{km})$</div></foreignObject>
  <foreignObject x="86" y="9.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P : P_0\ (\%)$</div></foreignObject>
  <polyline points="96,66 99,68 101.5,70 104.5,71.5 107,73.5 110,75.5 112.5,77 115.5,79 118.5,80.5 121,82.5 124,84 126.5,86 129.5,87.5 132,89.5 135,91 138,92.5 140.5,94.5 143.5,96 146,97.5 149,99.5 151.5,101 154.5,102.5 157,104 160,105.5 163,107 165.5,108.5 168.5,110 171,112 174,113 176.5,114.5 179.5,116 182.5,117.5 185,119 188,120.5 190.5,122 193.5,123.5 196,125 199,126 202,127.5 204.5,129 207.5,130.5 210,131.5 213,133 215.5,134 218.5,135.5 221,137 224,138 227,139.5 229.5,140.5 232.5,142 235,143 238,144.5 240.5,145.5 243.5,147 246.5,148 249,149 252,150.5 254.5,151.5 257.5,152.5 260,154 263,155 266,156 268.5,157 271.5,158.5 274,159.5 277,160.5 279.5,161.5 282.5,162.5 285.5,163.5 288,165 291,166 293.5,167 296.5,168 299,169 302,170 305,171 307.5,172 310.5,173 313,174 316,175 318.5,175.5 321.5,176.5 324,177.5 327,178.5 330,179.5 332.5,180.5 335.5,181.5 338,182 341,183 343.5,184 346.5,185 349.5,185.5 352,186.5 355,187.5 357.5,188.5 360.5,189 363,190 366,191 369,191.5 371.5,192.5 374.5,193 377,194 380,195 382.5,195.5 385.5,196.5 388,197 391,198 394,198.5 396.5,199.5 399.5,200 402,201 405,201.5 407.5,202.5 410.5,203 413.5,204 416,204.5 419,205 421.5,206 424.5,206.5 427,207.5 430,208" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,66 99,69.5 101.5,72.5 104.5,76 107,79 110,82.5 112.5,85.5 115.5,88.5 118.5,91.5 121,94.5 124,97.5 126.5,100 129.5,103 132,106 135,108.5 138,111 140.5,114 143.5,116.5 146,119 149,121.5 151.5,124 154.5,126.5 157,129 160,131.5 163,134 165.5,136 168.5,138.5 171,140.5 174,143 176.5,145 179.5,147 182.5,149.5 185,151.5 188,153.5 190.5,155.5 193.5,157.5 196,159.5 199,161.5 202,163 204.5,165 207.5,167 210,169 213,170.5 215.5,172.5 218.5,174 221,175.5 224,177.5 227,179 229.5,180.5 232.5,182.5 235,184 238,185.5 240.5,187 243.5,188.5 246.5,190 249,191.5 252,193 254.5,194.5 257.5,195.5 260,197 263,198.5 266,200 268.5,201 271.5,202.5 274,203.5 277,205 279.5,206 282.5,207.5 285.5,208.5 288,209.5 291,211 293.5,212 296.5,213 299,214.5 302,215.5 305,216.5 307.5,217.5 310.5,218.5 313,219.5 316,220.5 318.5,221.5 321.5,222.5 324,223.5 327,224.5 330,225.5 332.5,226.5 335.5,227 338,228 341,229 343.5,230 346.5,230.5 349.5,231.5 352,232.5 355,233 357.5,234 360.5,235 363,235.5 366,236.5 369,237 371.5,238 374.5,238.5 377,239.5 380,240 382.5,240.5 385.5,241.5 388,242 391,243 394,243.5 396.5,244 399.5,244.5 402,245.5 405,246 407.5,246.5 410.5,247 413.5,248 416,248.5 419,249 421.5,249.5 424.5,250 427,250.5 430,251" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 6"/>
  <line x1="319.5" y1="176" x2="319.5" y2="286" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="176" x2="319.5" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="319.5" cy="176" r="6.5" fill="#e64980" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="329.5" y="139.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$16{,}7\,\text{km}$</span></div></foreignObject>
  <foreignObject x="440" y="193.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e64980">$1550\,\text{nm}$</div></foreignObject>
  <foreignObject x="440" y="230.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e64980">$1310\,\text{nm}$</div></foreignObject>
</svg>

```pysahdy
Kuidun vaimennuskerroin on $0{,}18\,\text{dB/km}$ ja kuidun pituus on $50\,\text{km}$. Kuinka suuri on vaimennus desibeleinä ja kuinka suuri osa tehosta on jäljellä?
---
Vaimennus on $A = aL = 0{,}18\,\text{dB/km}\cdot 50\,\text{km} = 9{,}0\,\text{dB}$. Vaimennuksen määritelmästä $\lg (P_0 : P) = A : 10\,\text{dB} = 0{,}90$, joten $P_0 : P = 10^{0{,}90} \approx 7{,}9$. Tehosuhde on siis $P/P_0 \approx 0{,}13$ eli noin $13\,\%$.
```

### Langattoman laturin jännite
Vastaanotinkäämin yhden kierroksen läpi kulkeva vuo vaihtelee sinimuotoisesti. Vuon huippuarvo on $\Phi_0$ ja taajuus $f$. Silloin käämiin syntyy vaihtojännite, jonka huippuarvo saadaan samoin kuin generaattorissa (luku *Generaattori ja vaihtovirta*). Huippuarvo on jännitteen suurin arvo.
```latex
e_0 = N \cdot 2\pi f \cdot \Phi_0
```
missä $e_0$ on jännitteen huippuarvo ($\text{V}$), $N$ vastaanotinkäämin kierrosten lukumäärä, $f$ taajuus ($\text{Hz}$) ja $\Phi_0$ vuon huippuarvo yhden kierroksen läpi ($\text{Wb}$). Suuri taajuus tekee vuon muutoksesta nopean, joten jo pieni vuo riittää. Kun etäisyys kasvaa, $\Phi_0$ pienenee jyrkästi. Sen mukana myös $e_0$ pienenee.

## Esimerkki
Kuituyhteyden pituus on $80\,\text{km}$, ja kuidun vaimennuskerroin on $0{,}20\,\text{dB/km}$. Lähetin syöttää kuituun valoa teholla $2{,}0\,\text{mW}$. Liitosten vaimennusta ei oteta huomioon. Kuinka suuri teho saapuu vastaanottimeen?

<!-- vaihe -->

**Tunnetut ja kysytty.** Kuidun pituus $L = 80\,\text{km}$, vaimennuskerroin $a = 0{,}20\,\text{dB/km}$ ja lähetetty teho $P_0 = 2{,}0\,\text{mW}$.

Kysytään vastaanottimeen saapuvaa tehoa $P$.

<!-- vaihe -->

**Periaate.** Kuitu on koko matkalta samanlaista, joten vaimennus on vaimennuskerroin kertaa pituus. Vaimennuksen määritelmästä ratkaistaan ensin tehojen suhde ja sitten saapuva teho.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&A = aL \\[6pt]
&\lg \frac{P_0}{P} = \frac{A}{10\,\text{dB}} \\[6pt]
&P = P_0 \cdot 10^{-\frac{A}{10\,\text{dB}}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kilometrit supistuvat tulossa $aL$, ja teho saadaan samassa yksikössä kuin $P_0$. Lopuksi $1\,\text{mW} = 1000\,\mu\text{W}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&A = aL \\
&= 0{,}20\,\tfrac{\text{dB}}{\text{km}} \cdot 80\,\text{km} \\
&= 16\,\text{dB} \\[6pt]
&P = P_0 \cdot 10^{-\frac{A}{10\,\text{dB}}} \\
&= 2{,}0\,\text{mW} \cdot 10^{-\frac{16\,\text{dB}}{10\,\text{dB}}} \\
&= 2{,}0\,\text{mW} \cdot 10^{-1{,}6} \\
&= 0{,}0502\,\text{mW}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Vastaanottimeen saapuu teho $P \approx 0{,}050\,\text{mW} = 50\,\mu\text{W}$. Vastauksessa on kaksi merkitsevää numeroa, koska lähetetyssä tehossa $2{,}0\,\text{mW}$ ja vaimennuskertoimessa on kaksi.

<!-- vaihe -->

**Järkevyys.** Kymmenen desibeliä pienentää tehon kymmenesosaan ja kaksikymmentä desibeliä sadasosaan. Siksi $16\,\text{dB}$:n jälkeen tehoa on jäljellä jotain niiden väliltä, noin $2{,}5\,\%$. Tehosta $2{,}0\,\text{mW}$ on $2{,}5\,\%$ eli $0{,}050\,\text{mW}$, kuten tuloksessa.

## Yleinen virhekäsitys
Moni ajattelee, että langaton laturi lähettää energiaa radioaaltojen tapaan kauas huoneeseen. Silloin puhelimen voisi ladata mistä tahansa laturin läheltä. Laturin magneettikenttä kuitenkin heikkenee jyrkästi jo muutamien senttimetrien matkalla. Energiaa siirtyy vain silloin, kun vastaanotinkäämi on kentässä aivan lähettimen vieressä.

Toinen yleinen virhe on luulla, että induktioliesi kuumentaa lasilevyä ja lasi lämmittää kattilan. Pyörrevirrat muuttavat sähköenergiaa kattilan pohjan sisäenergiaksi. Lasi lämpenee vain siksi, että kuumasta kattilasta siirtyy siihen lämpöä.

Kolmas virhe koskee desibelejä. Kun vaimennus desibeleinä kaksinkertaistuu, teho ei puolitu. Tehojen suhde korotetaan toiseen potenssiin. Esimerkiksi $20\,\text{dB}$ jättää tehosta $1\,\%$, ei $5\,\%$.

## Tiivistelmä
- Langaton laturi on muuntaja ilman rautasydäntä. Lähetinkäämin vaihtovirran vuo indusoi vastaanotinkäämiin jännitteen $e_0 = N \cdot 2\pi f \cdot \Phi_0$. Vuo ja jännite pienenevät jyrkästi, kun käämien väli kasvaa tai käämit siirtyvät sivuun.
- Langattomassa latauksessa osa energiasta muuttuu käämien sisäenergiaksi. Eräässä laitevertailussa lataus vei noin $47\,\%$ enemmän energiaa kuin johdolla. Ero riippuu laitteista ja käämien kohdistuksesta.
- Induktioliedessä kelan vaihtuva kenttä synnyttää kattilan pohjaan pyörrevirtoja, jotka lämmittävät pohjaa. Ferromagneettinen teräspohja kuumenee hyvin ja alumiini ja kupari huonosti. Sähköä johtamaton lasi ei kuumene itsestään lainkaan.
- Valokuidussa valo pysyy ytimessä kokonaisheijastumalla, mutta lasi vaimentaa sitä. Vaimennukselle pätee $A = aL$ ja $A = 10\,\text{dB} \cdot \lg (P_0 : P)$. Jokainen $10\,\text{dB}$ pienentää tehon kymmenesosaan.
