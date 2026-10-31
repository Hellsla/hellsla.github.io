Kulmakertoimesta määritetty tulos on vain niin luotettava kuin kulmakerroin. Tässä ohjeessa arvioit kulmakertoimen epävarmuuden, siirrät sen lopputulokseen ja ilmoitat tuloksen oikein pyöristettynä.

## Mihin tarvitset tätä

Tulos ilmoitetaan epävarmuuksineen kaikissa tutkimuksissa, joissa suure määritetään kuvaajasta, esimerkiksi tutkimuksissa *Jousivakion määrittäminen*, *Putoamiskiihtyvyyden määrittäminen heilurin avulla* ja *Liukukitkakertoimen määrittäminen*. Tarvitset ensin [[ohje:tvt-suoran-sovitus|sovitetun suoran]] ja [[ohje:tvt-kulmakerroin|sen kulmakertoimen]].

## Työvaiheet

Valitse kulmakertoimen epävarmuuden $\Delta k$ arvioimiseen jompikumpi tapa ja kerro raportissa, kumpaa käytit.

### Tapa 1: jyrkin ja loivin suora

1. **Näytä epävarmuusjanat.** Merkitse jokaiseen pisteeseen epävarmuusjana, joka näyttää mittauksen epävarmuuden ([[ohje:tvt-kuvaaja|Mittauspisteiden kuvaaja]]). Graphical Analysisissa epävarmuusjanat ovat virhepalkkeja: valitse sarakkeen nimen vieressä olevan kolmen pisteen painikkeen (•••) valikosta **Sarakkeen ominaisuudet** ja sieltä **Näytä virhepalkit**.

2. **Lisää kaksi käsin säädettävää suoraa.** Ota käyttöön käsin säädettävä suora (englanninkielisessä versiossa **Add Manual Fit**, Pro). Se voi löytyä kuvaajatyökalujen valikosta, joka avautuu kuvaajan vasemman alakulman kuvakkeesta; vieritä valikkoa tarvittaessa alas. Jos et löydä sitä, kysy opettajalta. Vedä suoraa sen kahvoista. Ohjelma näyttää suoran kulmakertoimen ja vakiotermin ja päivittää ne, kun siirrät suoraa. Käsin säädettäviä suoria voi olla enintään kolme, joten tee yhdestä jyrkin ja toisesta loivin.

3. **Säädä jyrkin ja loivin suora.** Käännä ensimmäinen suora mahdollisimman jyrkäksi niin, että se vielä kulkee kaikkien tai lähes kaikkien epävarmuusjanojen kautta, ja toinen samalla tavalla mahdollisimman loivaksi. Kirjaa niiden kulmakertoimet $k_\text{max}$ ja $k_\text{min}$ tulosruuduista.

    <svg data-fig="lines" viewBox="0 0 600 340" role="img" aria-label="Kaaviokuva ilman lukuarvoja: kuusi mittauspistettä, joissa kussakin on yhtä pitkä pystysuora epävarmuusjana. Pisteisiin on sovitettu suora, jonka kulmakerroin on k. Katkoviivoilla on piirretty jyrkin ja loivin suora, jotka vielä kulkevat jokaisen epävarmuusjanan kautta; niiden kulmakertoimet ovat k max ja k min. Suorat leikkaavat toisensa pisteiden keskivaiheilla ja erkanevat päitä kohti." style="max-width:100%;font-size:24px">
  <line x1="79" y1="300" x2="464" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M476,300 L463,306 L463,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="301" x2="80" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,44 L86,57 L74,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="50" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="482" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <foreignObject x="70" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y$</div></foreignObject>
  <polyline points="101,285 429,85" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="90.5,264 429,110.5" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="96,275 444.5,89" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="133" y1="265.5" x2="133" y2="237" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="126" y1="265.5" x2="140" y2="265.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="126" y1="237" x2="140" y2="237" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="133" cy="251" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="185.5" y1="249.5" x2="185.5" y2="221" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="178.5" y1="249.5" x2="192.5" y2="249.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="178.5" y1="221" x2="192.5" y2="221" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="185.5" cy="235.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="238.5" y1="209.5" x2="238.5" y2="180.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="231.5" y1="209.5" x2="245.5" y2="209.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="231.5" y1="180.5" x2="245.5" y2="180.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="238.5" cy="195" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="291.5" y1="188" x2="291.5" y2="159" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="284.5" y1="188" x2="298.5" y2="188" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="284.5" y1="159" x2="298.5" y2="159" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="291.5" cy="173.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="344.5" y1="149" x2="344.5" y2="120.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="337.5" y1="149" x2="351.5" y2="149" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="337.5" y1="120.5" x2="351.5" y2="120.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="344.5" cy="134.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="397" y1="133" x2="397" y2="104.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="390" y1="133" x2="404" y2="133" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="390" y1="104.5" x2="404" y2="104.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="397" cy="119" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="452.5" y="74.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$k$</div></foreignObject>
  <foreignObject x="244" y="84" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$k_\text{max}$</div></foreignObject>
  <line x1="306" y1="105" x2="374" y2="114.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="365.5" y="188" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$k_\text{min}$</div></foreignObject>
  <line x1="369.5" y1="186" x2="328.5" y2="160" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

4. **Laske epävarmuus.** Arvioi kulmakertoimen epävarmuus vaihteluvälin puolikkaana:

    $$\Delta k = \frac{k_\text{max} - k_\text{min}}{2}$$

    Jyrkin ja loivin suora rajaavat arvioidun vaihteluvälin. Ne eivät ole varmoja ylä- ja alarajoja.

### Tapa 2: sovitusparametrin epävarmuus

1. **Näytä parametrien epävarmuudet.** Sovita suora valinnoilla **Käyrän sovitus** ja **Lineaarinen** ([[ohje:tvt-suoran-sovitus|Suoran sovittaminen mittauspisteisiin]]). Parametrien epävarmuuksien näyttäminen (englanninkielisessä versiossa **Show uncertainty of curve fit parameters**, Pro) voi olla tulosruudun rattaan kuvakkeen takana; jos et löydä sitä, kysy opettajalta. Kun asetus on päällä, tulosruudussa näkyy kulmakertoimen eli ohjelman m:n vieressä sen epävarmuus. Käytä tätä parametrin epävarmuutta kulmakertoimen epävarmuutena $\Delta k$.

2. **Tiedä, mitä luku kertoo.** Luku perustuu pisteiden hajontaan suoran ympärillä, ei virhepalkkeihin. Jos pisteitä on vähän ja ne osuvat sattumalta lähes suoralle, epävarmuus voi olla epärealistisen pieni. Vertaa sitä silloin jyrkimmän ja loivimman suoran arvioon.

### Tuloksen epävarmuus ja ilmoittaminen

1. **Siirrä epävarmuus lopputulokseen.** Jos tulos saadaan kertomalla tai jakamalla kulmakerroin tarkasti tunnetulla vakiolla, tuloksen suhteellinen epävarmuus on sama kuin kulmakertoimen. Heilurin putoamiskiihtyvyydelle $g = \tfrac{4\pi^2}{k}$ pätee siis $\tfrac{\Delta g}{g} = \tfrac{\Delta k}{k}$. Jos tuloksen laskemiseen tarvitaan muitakin mitattuja suureita, tulon ja osamäärän suhteellinen epävarmuus on enintään suureiden suhteellisten epävarmuuksien summa.

2. **Laske välivaiheet pyöristämättä.** Keksityssä esimerkkiaineistossa $k_\text{max} = 4{,}21\,\text{s}^2/\text{m}$ ja $k_\text{min} = 3{,}89\,\text{s}^2/\text{m}$, joten $\Delta k = (4{,}21 - 3{,}89)\,\text{s}^2/\text{m} : 2 = 0{,}16\,\text{s}^2/\text{m}$. Kun $k = 4{,}05\,\text{s}^2/\text{m}$, suhteellinen epävarmuus on $0{,}16 : 4{,}05 \approx 0{,}040$ eli noin $4\,\%$. Putoamiskiihtyvyys on $g = 4\pi^2 : 4{,}05\,\text{s}^2/\text{m} \approx 9{,}748\,\text{m/s}^2$ ja sen epävarmuus $\Delta g \approx 0{,}040 \cdot 9{,}748\,\text{m/s}^2 \approx 0{,}39\,\text{m/s}^2$.

3. **Pyöristä ja ilmoita.** Pyöristä epävarmuus yhteen merkitsevään numeroon ja tulos samaan desimaaliin kuin epävarmuus. Esimerkin tulos on $g = (9{,}7 \pm 0{,}4)\,\text{m/s}^2$: lukuarvo, epävarmuus ja yksikkö.

4. **Pohdi systemaattiset virheet erikseen.** Kumpikaan tapa ei sisällä systemaattisia virheitä. Jos videoanalyysin mittakaava on asetettu väärin, kaikki paikat ovat samassa suhteessa liian suuria tai pieniä. Pisteet asettuvat silti siististi suoralle, ja epävarmuus näyttää pieneltä, vaikka kulmakerroin on väärä. Vertaa tulosta vertailuarvoon: jos vertailuarvo on epävarmuusvälin sisällä, tulos on sen kanssa sopusoinnussa, mutta se ei todista arvoja samoiksi.

## Tavallisimmat virheet

- **Jyrkin ja loivin suora eivät kulje epävarmuusjanojen kautta.** Huomaat sen, kun suora ohittaa useita janoja. Piirrä suorat niin, että ne vielä sopivat pisteisiin epävarmuuksien rajoissa.
- **Epävarmuudessa on liikaa numeroita**, esimerkiksi $g = (9{,}748 \pm 0{,}385)\,\text{m/s}^2$. Epävarmuuden toinen ja kolmas numero eivät ole luotettavia. Pyöristä epävarmuus yhteen merkitsevään numeroon.
- **Tulos ja epävarmuus on pyöristetty eri tarkkuuteen**, esimerkiksi $g = (9{,}748 \pm 0{,}4)\,\text{m/s}^2$. Pyöristä tulos samaan desimaaliin kuin epävarmuus.
- **Kulmakertoimen epävarmuus on ilmoitettu lopputuloksen epävarmuutena.** Yksikkö paljastaa virheen: $\Delta k$ on yksikössä $\text{s}^2/\text{m}$, mutta $\Delta g$ yksikössä $\text{m/s}^2$. Siirrä epävarmuus suhteellisena.
- **Pieni epävarmuus tulkitaan oikeaksi tulokseksi.** Sovituksen epävarmuus voi olla pieni, vaikka systemaattinen virhe tekee tuloksesta väärän. Pohdi systemaattiset virheet erikseen raportin luotettavuusosassa.

## Tarkista ennen kuin jatkat

- Tiedät, kummalla tavalla arvioit kulmakertoimen epävarmuuden.
- Epävarmuus on siirretty lopputulokseen, ja sillä on lopputuloksen yksikkö.
- Epävarmuus on pyöristetty yhteen merkitsevään numeroon ja tulos samaan desimaaliin.
- Systemaattiset virheet on pohdittu erikseen.
